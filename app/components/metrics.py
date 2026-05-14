import streamlit as st
from app.services.analytics import get_year_summary, get_institution_count
from app.utils.formatters import format_decimal, format_pct, format_int

def render_metrics_summary(analytics_base, metrics):

    year_summary = get_year_summary(analytics_base)
    institution_count = get_institution_count(analytics_base)

    metric_columns = st.columns(4)

    metric_columns[0].metric("Recall da classe de risco", f"{round(metrics["1"]["recall"] * 100, 2)}%")

    metric_columns[1].metric(
        "INDE médio em 2024",
        format_decimal(float(year_summary.loc[2024, "inde"])),
        f"{format_decimal(float(year_summary.loc[2024, 'inde'] - year_summary.loc[2022, 'inde']))} vs 2022",
    )

    metric_columns[2].metric(
        "IEG em 2024",
        format_decimal(float(year_summary.loc[2024, "ieg"])),
        f"{format_decimal(float(year_summary.loc[2024, 'ieg'] - year_summary.loc[2023, 'ieg']))} vs 2023",
    )

    metric_columns[3].metric("Instituições mapeadas", format_int(institution_count))

def render_metrics_predict(prediction, below_median, scenario_df, combined_probability, probability):
    
    result_cols = st.columns(4)
    result_cols[0].metric("Classe prevista", "Risco" if prediction == 1 else "Baixo risco")
    result_cols[1].metric("Abaixo da mediana", f"{below_median}/6")
    result_cols[2].metric(
        "Melhor cenário projetado",
        format_pct(float(scenario_df.iloc[0]["Risco projetado"])),
        f"-{format_pct(float(scenario_df.iloc[0]['Redução potencial']))}",
    )
    result_cols[3].metric(
        "Plano conjunto",
        format_pct(combined_probability),
        f"-{format_pct(max(probability - combined_probability, 0.0))}",
    )