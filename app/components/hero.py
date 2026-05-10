import streamlit as st
from app.utils.formatters import format_int
from src.constants import NOTEBOOK_METRICS

def render_hero(sample_size):

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-grid">
                <div>
                    <span class="eyebrow">
                        Datathon • Passos Mágicos
                    </span>
                    <h1>
                        Painel preditivo para triagem,
                        priorização e ação pedagógica
                    </h1>
                    <p>
                        Aplicação desenhada para apoiar
                        a Passos Mágicos na identificação
                        precoce de risco.
                    </p>
                </div>
                <div class="hero-mini">
                    <div class="hero-mini-card">
                        <span>Base analisada</span>
                        <strong>
                            {format_int(sample_size)} registros úteis
                        </strong>
                    </div>
                    <div class="hero-mini-card">
                        <span>Desempenho do modelo</span>
                        <strong>
                            {NOTEBOOK_METRICS["Acurácia"]} de acurácia
                        </strong>
                    </div>
                    <div class="hero-mini-card">
                        <span>Pilares centrais</span>
                        <strong>IDA, IEG e IPV</strong>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )