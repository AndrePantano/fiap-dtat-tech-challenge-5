from typing import Dict, List, Optional, Tuple
#from src.models.predict import predict_risk
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from app.components.hero import render_hero
from app.components.sidebar import render_sidebar
from app.components.metrics import render_metrics_summary
from app.services.analytics import get_benchmarks, get_sample_size, get_feature_importances
from app.pages.tab_triagem import render_tab_triagem
from app.pages.tab_insights import render_tab_insight
from app.pages.tab_modelo import render_tab_modelo
from src.config import MODEL_FILE
from utils.loaders import load_css, load_model, load_analytics_base

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
sample_size = get_sample_size(analytics_base)


render_hero(sample_size)

render_metrics_summary(analytics_base)

tab_triagem, tab_insights, tab_modelo = st.tabs(
    ["Predição Individual", "Insights da base", "Modelo e governança"]
)

# tab_triagem 
render_tab_triagem(tab_triagem, benchmarks, model, importances)

# tab_insights
render_tab_insight(tab_insights, analytics_base)

# tab_modelo
render_tab_modelo(tab_modelo, importances)