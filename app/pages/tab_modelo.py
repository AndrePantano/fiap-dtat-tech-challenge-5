import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from components.charts import plot_importance_chart
from components.cards import render_soft_card
from services.analytics import get_feature_importances
from src.constants import FEATURES, FEATURES_RESUMIDAS, FEATURE_LABELS, FEATURE_DESCRIPTIONS, NOTEBOOK_METRICS

def render_tab_modelo(tab_modelo, model):

    importances = get_feature_importances(model)

    with tab_modelo:
        st.subheader("Como o modelo apoia a operação")
        st.caption("Explicação de negócio, leitura das variáveis e recomendações de governança para uso contínuo.")

        model_cols = st.columns(3, gap="medium")
        model_cols[0].metric("Algoritmo", NOTEBOOK_METRICS["Modelo Treinado"])
        model_cols[1].metric("Variável-alvo", "INDE abaixo da mediana")
        model_cols[2].metric("Features", str(len(FEATURES)))

        governance_left, governance_right = st.columns([1.0, 1.0], gap="large")

        with governance_left:
            st.markdown("#### Importância dos indicadores no modelo")
            importance_fig = plot_importance_chart(importances[FEATURES_RESUMIDAS])
            st.pyplot(importance_fig, use_container_width=True)
            plt.close(importance_fig)
            
        with governance_right:
            st.markdown("#### Dicionário operacional das features")
            dictionary_rows = [
                {
                    "Indicador": feature.upper(),
                    "Leitura de negócio": FEATURE_LABELS[feature],
                    "Como interpretar": FEATURE_DESCRIPTIONS[feature],
                }
                for feature in FEATURES_RESUMIDAS
            ]
            st.dataframe(pd.DataFrame(dictionary_rows), use_container_width=True, hide_index=True)

        st.markdown(
            f"""
            <div class="outras_features">
                    <p>A <span>Idade</span> e a <span>Fase atual</span> do aluno foram utilizadas como features para o treinamento do modelo.
                    Isso porque, no ecossistema da Passos Mágicos, a relação entre essas duas features é o maior incicativo oculto de defasagem.
                    Um aluno mais velho preso em uma fase inicial carrega uma probabilidade de evasão ou risco muito diferente de um aluno com a idade ideal para aquela fase.
                    O algoritmo capturou exatamente essa nuance.</p>                
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("#### Governança recomendada")
        render_soft_card(
            "Usar como triagem e priorização",
            "O modelo é ideal para ordenar casos, apoiar reuniões pedagógicas e concentrar esforço onde a chance de risco é maior.",
        )
        render_soft_card(
            "Recalibrar periodicamente",
            "A base deve ser atualizada a cada novo ciclo e o modelo precisa ser reavaliado para capturar mudanças no perfil dos alunos e no programa.",
        )
        render_soft_card(
            "Combinar previsão com contexto humano",
            "A decisão final deve considerar histórico individual, contexto familiar, escola e evidências qualitativas trazidas pela equipe da Passos Mágicos.",
        )
