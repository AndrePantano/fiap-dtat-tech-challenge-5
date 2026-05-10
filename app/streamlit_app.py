from typing import Dict, List, Optional, Tuple
#from src.models.predict import predict_risk
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from app.components.hero import render_hero
from app.components.sidebar import render_sidebar
from app.components.metrics import render_metrics
from app.services.analytics import get_benchmarks, get_year_summary, get_sample_size, get_feature_importances
from app.pages.tab_triagem import render_tab_triagem
from src.config import MODEL_FILE
from utils.loaders import load_css, load_model, load_analytics_base

st.set_page_config(
    page_title="Passos Mágicos | Painel Preditivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()
render_sidebar()

try:
    model = load_model()
except Exception as exc:
    st.error(f"Não foi possível carregar o modelo treinado em `{MODEL_FILE.name}`. Detalhe técnico: {exc}")
    st.stop()

analytics_base = load_analytics_base()
importances = get_feature_importances(model)
benchmarks = get_benchmarks(analytics_base)
year_summary = get_year_summary(analytics_base)
#correlations = get_correlations(analytics_base)
sample_size = get_sample_size(analytics_base)


render_hero(sample_size)

render_metrics(analytics_base)

tab_triagem, tab_insights, tab_modelo = st.tabs(
    ["Triagem individual", "Insights da base", "Modelo e governança"]
)


# aqui vai a tab_triagem 
render_tab_triagem(tab_triagem, benchmarks, model, importances)

# aqui vai a tab_insights
# aqui vai a tab_modelo