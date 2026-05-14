import streamlit as st
from app.services.analytics import get_sample_size
from app.utils.formatters import format_int

def render_hero(analytics_base, metrics):

    sample_size = get_sample_size(analytics_base)

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-grid">
                <div id="hero-title">
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
                            {round(metrics["accuracy"] * 100,2)}% de acurácia
                        </strong>                        
                    </div>
                    <div class="hero-mini-card">
                        <span>Pilares centrais</span>
                        <strong>IDA, IEG e IPV</strong>
                        <span>Combinação que mais eleva a nota global.</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )