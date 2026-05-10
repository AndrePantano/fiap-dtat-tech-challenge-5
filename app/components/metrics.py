import streamlit as st
from utils.formatters import format_decimal, format_pct, format_int, join_labels
from src.constants import NOTEBOOK_METRICS
from app.services.analytics import get_year_summary, get_institution_count

def render_metrics(analytics_base):

    year_summary = get_year_summary(analytics_base)
    institution_count = get_institution_count(analytics_base)

    metric_columns = st.columns(4)

    metric_columns[0].metric("Recall da classe de risco", NOTEBOOK_METRICS["Recall risco"])

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

    metric_columns[3].metric(
        "Instituições mapeadas",
        format_int(institution_count),
        "na base consolidada"
    )