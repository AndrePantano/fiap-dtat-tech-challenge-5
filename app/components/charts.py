import matplotlib.pyplot as plt
import pandas as pd
from app.utils.formatters import format_decimal
from src.constants import FEATURES, FEATURE_LABELS

def plot_profile_comparison(input_series: pd.Series, benchmarks: pd.DataFrame):
    labels = [FEATURE_LABELS[feature] for feature in FEATURES]
    base = benchmarks.loc[FEATURES, "mediana"].astype(float)
    current = input_series.loc[FEATURES].astype(float)
    colors = ["#0f766e" if current[feature] >= base[feature] else "#e76f51" for feature in FEATURES]

    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.barh(labels, base.values, color="#d9e2ec", height=0.58, label="Mediana da base")
    ax.barh(labels, current.values, color=colors, height=0.34, label="Aluno avaliado")

    for idx, value in enumerate(current.values):
        ax.text(min(value + 0.08, 10.1), idx, format_decimal(value, 1), va="center", fontsize=9, color="#14324a")

    ax.set_xlim(0, 10)
    ax.set_xlabel("Escala dos indicadores")
    ax.set_ylabel("")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    return fig


def plot_year_summary(year_summary: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(7.7, 4.6))
    colors = {
        "INDE": "#14324a",
        "IDA": "#f08a5d",
        "IEG": "#0f766e",
        "IPV": "#2f5d8a",
        "IAN": "#7b8da6",
    }

    for column in ["INDE", "IDA", "IEG", "IPV", "IAN"]:
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
    ax.legend(frameon=False, ncol=3)
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
    fig, ax = plt.subplots(figsize=(6.6, 4.3))
    ax.barh([FEATURE_LABELS[idx] for idx in ordered.index], ordered.values, color="#f08a5d")
    ax.set_xlabel("Importância relativa")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)

    for idx, value in enumerate(ordered.values):
        ax.text(value + 0.006, idx, format_decimal(value, 2), va="center", fontsize=9, color="#14324a")

    fig.tight_layout()
    return fig
