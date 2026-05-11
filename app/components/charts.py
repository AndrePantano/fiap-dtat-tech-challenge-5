import matplotlib.pyplot as plt
import pandas as pd
from app.utils.formatters import format_decimal
from src.constants import FEATURES_RESUMIDAS, FEATURE_LABELS

def plot_profile_comparison(input_series: pd.Series, benchmarks: pd.DataFrame):
        
    labels = [FEATURE_LABELS[feature] for feature in FEATURES_RESUMIDAS]
    base = benchmarks
    current = input_series
    colors = ["#0f766e" if current[feature] >= base[feature] else "#e76f51" for feature in FEATURES_RESUMIDAS]

    fig, ax = plt.subplots(figsize=(7.6, 3))    
    ax.barh(labels, current.values, color=colors, height=0.34, label="Avaliação")

    for idx, value in enumerate(current.values):
        ax.text(min(value + 0.08, 10.1), idx, format_decimal(value, 1), va="center", fontsize=9, color="#14324a")

    ax.set_xlim(0, 10)
    ax.set_xlabel("Escala dos indicadores")
    ax.set_ylabel("")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)
    fig.tight_layout()
    return fig


def plot_year_summary(year_summary: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7.7, 4.6))
    colors = {        
        "inde": "#14324A",  # azul petróleo institucional
        "ida": "#E76F51",   # coral
        "ieg": "#2A9D8F",   # verde água
        "ips": "#457B9D",   # azul médio
        "ipp": "#8D99AE",   # cinza azulado
        "ian": "#E9C46A",   # amarelo queimado
        "ipv": "#9B5DE5",   # roxo equilibrado
        "iaa": "#EF476F",   # rosa/vermelho moderno
    }

    columns = ["inde", "ida","ieg", "ips", "ipp", "ian", "ipv", "iaa"]

    for column in columns:
        ax.plot(
            year_summary.index,
            year_summary[column],
            marker="o",
            linewidth=2.2,
            markersize=7,
            label=column,
            color=colors[column],
        )

    ax.set_xticks(year_summary.index.tolist())
    ax.set_ylim(5, 9)
    ax.set_ylabel("Média do indicador")
    ax.set_xlabel("Ano")
    ax.grid(alpha=0.18)
    ax.spines[["top", "right"]].set_visible(False)    
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.18),
        ncol=len(columns),
        frameon=False
    )
    fig.tight_layout()
    return fig


def plot_correlation_chart(correlations: pd.Series):
    ordered = correlations.sort_values()
    fig, ax = plt.subplots(figsize=(6.6, 4.3))
    colors = ["#d9e2ec" if value < 0.5 else "#0f766e" for value in ordered.values]
    ax.barh([FEATURE_LABELS[idx] for idx in ordered.index], ordered.values, color=colors)
    ax.set_xlim(0, 0.85)
    ax.set_xlabel("Correlação com INDE")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)

    for idx, value in enumerate(ordered.values):
        ax.text(value + 0.01, idx, format_decimal(value, 2), va="center", fontsize=9, color="#14324a")

    fig.tight_layout()
    return fig


def plot_importance_chart(importances: pd.Series):
    ordered = importances.sort_values()
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.barh([FEATURE_LABELS[idx] for idx in ordered.index], ordered.values, color="#f08a5d")
    ax.set_xlabel("Importância relativa")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)

    for idx, value in enumerate(ordered.values):
        ax.text(value + 0.006, idx, format_decimal(value, 2), va="center", fontsize=9, color="#14324a")

    fig.tight_layout()
    return fig
