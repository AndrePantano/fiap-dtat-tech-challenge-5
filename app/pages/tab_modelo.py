import pandas as pd
import matplotlib.pyplot as plt
from app.components.charts import plot_importance_chart
from app.components.cards import render_soft_card
from app.services.analytics import get_feature_importances
from src.constants import FEATURES, FEATURES_RESUMIDAS, FEATURE_LABELS, FEATURE_DESCRIPTIONS

def render_tab_modelo(st, tab_modelo, model, metrics):

    importances = get_feature_importances(model)

    with tab_modelo:
        st.subheader("Como o modelo apoia a operação")
        st.caption("Explicação de negócio, leitura das variáveis e recomendações de governança para uso contínuo.")

        model_cols = st.columns(3, gap="medium")
        model_cols[0].metric("Algoritmo", metrics["model_name"])
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
