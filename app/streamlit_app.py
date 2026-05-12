import streamlit as st
from components.hero import render_hero
from components.sidebar import render_sidebar
from components.metrics import render_metrics_summary
from pages.tab_triagem import render_tab_triagem
from pages.tab_insights import render_tab_insight
from pages.tab_modelo import render_tab_modelo
from utils.loaders import load_css, load_model, load_analytics_base
from src.config import MODEL_FILE

try:
    model = load_model()
except Exception as exc:
    st.error(f"Não foi possível carregar o modelo treinado em `{MODEL_FILE.name}`. Detalhe técnico: {exc}")
    st.stop()

load_css()
render_sidebar()

analytics_base = load_analytics_base()

render_hero(analytics_base)

render_metrics_summary(analytics_base)

tab_triagem, tab_insights, tab_modelo = st.tabs([
    "Predição Individual",
    "Insights da base",
    "Modelo e governança"
])

render_tab_triagem(tab_triagem, analytics_base, model)

render_tab_insight(tab_insights, analytics_base)

render_tab_modelo(tab_modelo, model)

st.caption("""Datathon - Passos Mágicos | Fonte: Base de dados da PEDE 2022, 2023 e 2024""")