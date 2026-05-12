import pandas as pd
from typing import Tuple, Dict, List
from src.constants import FEATURES, FEATURES_RESUMIDAS, FEATURE_LABELS, ACTION_LIBRARY
from utils.formatters import format_pct, join_labels

def predict_risk(model, input_series: pd.Series) -> Tuple[int, float]:
    payload = pd.DataFrame([[input_series[feature] for feature in FEATURES]], columns=FEATURES)
    prediction = int(model.predict(payload)[0])
    probability = float(model.predict_proba(payload)[0][1])
    return prediction, probability


def classify_risk(probability: float) -> Dict[str, str]:
    if probability >= 0.70:
        return {
            "label": "Prioridade imediata",
            "tone": "risk-high",
            "message": "O aluno apresenta combinação de sinais que pedem atuação rápida da equipe pedagógica e monitoramento próximo.",
        }
    if probability >= 0.40:
        return {
            "label": "Atenção dirigida",
            "tone": "risk-mid",
            "message": "Há sinais relevantes de atenção. O caso pede plano de acompanhamento com foco nos pilares que mais deslocam o risco.",
        }
    return {
        "label": "Estável com monitoramento",
        "tone": "risk-low",
        "message": "O perfil está mais protegido no cenário atual, mas vale acompanhar a consistência dos indicadores ao longo dos próximos ciclos.",
    }


def build_priority_table(input_series: pd.Series, benchmarks: pd.DataFrame, importances: pd.Series) -> pd.DataFrame:
    rows = []

    for feature in FEATURES_RESUMIDAS:
        current = float(input_series[feature])
        median = float(benchmarks.loc[feature, "exemplo_resumido"])
        q25 = float(benchmarks.loc[feature, "q25"])
        importance = float(importances.get(feature))
        gap = max(median - current, 0.0)
        status = "Crítico" if current < q25 else "Abaixo da mediana" if current < median else "Acima da mediana"

        rows.append(
            {
                "Feature": feature,
                "Indicador": FEATURE_LABELS[feature],
                "Valor atual": current,
                "Mediana da base": median,
                "Gap": gap,
                "Importância": importance,
                "Prioridade": gap * importance,
                "Status": status,
            }
        )

    priority_df = pd.DataFrame(rows).sort_values(["Prioridade", "Gap"], ascending=False)
    return priority_df


def build_strengths_table(input_series: pd.Series, benchmarks: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for feature in FEATURES:
        current = float(input_series[feature])
        median = float(benchmarks.loc[feature, "mediana"])
        if current >= median:
            rows.append(
                {
                    "Indicador": FEATURE_LABELS[feature],
                    "Valor atual": current,
                    "Mediana da base": median,
                    "Ganho": current - median,
                }
            )

    strengths = pd.DataFrame(rows)
    if strengths.empty:
        return strengths
    return strengths.sort_values("Ganho", ascending=False)


def build_scenarios(model, input_series: pd.Series, benchmarks: pd.DataFrame, base_probability: float, importances: pd.Series) -> Tuple[pd.DataFrame, float]:
    rows = []

    for feature in FEATURES_RESUMIDAS:
        scenario = input_series.copy()
        target = max(float(input_series[feature]), float(benchmarks.loc[feature, "exemplo_resumido"]))
        scenario[feature] = min(target, 10.0)
        _, new_probability = predict_risk(model, scenario)
        rows.append(
            {
                "Feature": feature,
                "Indicador": FEATURE_LABELS[feature],
                "Valor alvo": scenario[feature],
                "Risco projetado": new_probability,
                "Redução potencial": max(base_probability - new_probability, 0.0),
            }
        )

    scenario_df = pd.DataFrame(rows).sort_values(
        ["Redução potencial", "Risco projetado"], ascending=[False, True]
    )

    priority_features = [
        row["Feature"]
        for _, row in build_priority_table(input_series, benchmarks, importances).iterrows()
        if row["Gap"] > 0
    ][:3]

    combined = input_series.copy()
    for feature in priority_features:
        combined[feature] = max(float(combined[feature]), float(benchmarks.loc[feature, "exemplo_resumido"]))

    _, combined_probability = predict_risk(model, combined)
    return scenario_df, combined_probability


def build_recommendations(priority_df: pd.DataFrame) -> List[Tuple[str, str]]:
    relevant = priority_df[priority_df["Gap"] > 0.10].head(3)
    if relevant.empty:
        return [
            (
                "Manter o ritmo e prevenir regressão",
                "O perfil está alinhado ou acima da mediana da base nos principais pilares. O foco deve ser preservar consistência e monitorar pequenas oscilações de engajamento e desempenho.",
            )
        ]

    recommendations = []
    for _, row in relevant.iterrows():
        recommendations.append(ACTION_LIBRARY[row["Feature"]])
    return recommendations


def build_case_summary(
    band: Dict[str, str],
    priority_df: pd.DataFrame,
    strengths_df: pd.DataFrame,
    base_probability: float,
    combined_probability: float,
) -> str:
    main_alerts = priority_df[priority_df["Gap"] > 0.10]["Indicador"].head(2).tolist()
    main_strengths = strengths_df["Indicador"].head(2).tolist() if not strengths_df.empty else []

    sentences = [f"A leitura atual enquadra o caso como {band['label'].lower()}."]

    if main_alerts:
        sentences.append(f"Os maiores desvios aparecem em {join_labels(main_alerts)}.")
    else:
        sentences.append("Os indicadores centrais estão acima da mediana da base, o que reduz a pressão de risco no curto prazo.")

    if main_strengths:
        sentences.append(f"As fortalezas mais claras estão em {join_labels(main_strengths)}.")

    if combined_probability < base_probability:
        sentences.append(
            f"No cenário combinado, o risco projetado cai para {format_pct(combined_probability)}."
        )
    elif combined_probability > base_probability:
        sentences.append(
            f"No cenário combinado, o risco projetado fica em {format_pct(combined_probability)}, indicando que a equipe deve validar a intervenção com contexto pedagógico."
        )
    else:
        sentences.append(
            f"No cenário combinado, o risco projetado permanece em {format_pct(combined_probability)}."
        )
    return " ".join(sentences)