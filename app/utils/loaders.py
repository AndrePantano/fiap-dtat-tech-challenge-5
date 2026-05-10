from typing import Optional

import joblib
import pandas as pd
import streamlit as st

from src.config import MODEL_FILE, DATA_PATH, STYLE_DIR

from src.constants import FEATURES

def load_css():
    css_path = STYLE_DIR / "main.css"

    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


@st.cache_resource(show_spinner=False)
def load_model():
    return joblib.load(MODEL_FILE)


@st.cache_data(show_spinner=False)
def load_analytics_base() -> Optional[pd.DataFrame]:

    if not DATA_PATH.exists():        
        return None

    df = pd.read_csv(DATA_PATH, sep=";")

    inde_mapping = {2022: "inde_22", 2023: "inde_23", 2024: "inde_24"}

    for year, column in inde_mapping.items():
        if column in df.columns:
            mask = df["ano_base"] == year
            df.loc[mask, "inde"] = pd.to_numeric(df.loc[mask, column], errors="coerce")

    df["inde"] = pd.to_numeric(df["inde"], errors="coerce")

    return df