from app.components.cards import render_soft_card
from app.components.charts import plot_year_summary, plot_correlation_chart
from app.services.analytics import get_year_summary, get_year_summary_all_indicators, get_correlations
from app.utils.formatters import format_decimal

def render_tab_insight(st, plt, tab_insights, analytics_base):
    year_summary = get_year_summary(analytics_base)
    year_summary_all_indicators = get_year_summary_all_indicators(analytics_base)
    correlations = get_correlations(analytics_base)

    with tab_insights:
        st.subheader("Leitura executiva da base")
        st.caption("Resumo do que o notebook aponta sobre evolução, correlação e prioridades de atuação.")

        overview_cols = st.columns(3, gap="medium")
        overview_cols[0].metric(
            "INDE 2022 -> 2024",
            format_decimal(float(year_summary.loc[2024, 'inde'])),
            f"{format_decimal(float(year_summary.loc[2024, 'inde'] - year_summary.loc[2022, 'inde']))} no período",
        )
        overview_cols[1].metric(
            "IDA 2024",
            format_decimal(float(year_summary.loc[2024, 'ida'])),
            f"{format_decimal(float(year_summary.loc[2024, 'ida'] - year_summary.loc[2023, 'ida']))} vs 2023",
        )
        overview_cols[2].metric(
            "IEG 2024",
            format_decimal(float(year_summary.loc[2024, 'ieg'])),
            f"{format_decimal(float(year_summary.loc[2024, 'ieg'] - year_summary.loc[2023, 'ieg']))} vs 2023",
        )

        chart_left, chart_right = st.columns([1.05, 0.95], gap="large")

        with chart_left:
            st.markdown("<h4>Evolução dos indicadores-chave</h4>",unsafe_allow_html=True)
            trend_fig = plot_year_summary(year_summary_all_indicators)
            st.pyplot(trend_fig, use_container_width=True)
            plt.close(trend_fig)

        with chart_right:            
            st.markdown("<h4>O que mais move o INDE</h4>",unsafe_allow_html=True)
            corr_fig = plot_correlation_chart(correlations)
            st.pyplot(corr_fig, use_container_width=True)
            plt.close(corr_fig)

        insight_cols = st.columns(3, gap="medium")
        with insight_cols[0]:
            render_soft_card(
                "Evolução positiva do programa",
                f"O INDE sobe de {format_decimal(float(year_summary.loc[2022, 'inde']))} em 2022 para {format_decimal(float(year_summary.loc[2024, 'inde']))} em 2024, reforçando a efetividade global da jornada.",
            )
        with insight_cols[1]:
            render_soft_card(
                "Engajamento explica desempenho",
                f"O notebook mostra que IEG e IDA andam juntos. Em 2024, a queda do IEG ajuda a explicar a perda de consistência no desempenho acadêmico.",
            )
        with insight_cols[2]:
            render_soft_card(
                "IPV como ponte de evolução",
                f"O IPV se conecta fortemente a INDE ({format_decimal(float(correlations['ipv']), 2)}) e responde bem a desempenho, engajamento e apoio psicopedagógico.",
            )

        st.markdown("<h4>Tabela-resumo dos ciclos</h4>",unsafe_allow_html=True)
        year_display = year_summary_all_indicators.copy().rename(
            columns={
                'inde':'INDE',
                'ida':'IDA',
                'ieg':'IEG',
                "ips":"IPS",
                "ipp":"IPP",
                "ian":"IAN",
                "ipv":"IPV",
            }
        )
        st.dataframe(year_display.round(2), use_container_width=True)

        st.markdown("<h4>Direcionadores estratégicos</h4>",unsafe_allow_html=True)
        render_soft_card(
            "Priorizar IDA, IEG e IPV",
            "Esses três pilares concentram a maior parte da explicação do risco. Quando eles melhoram, o INDE tende a responder mais rápido.",
        )
        render_soft_card(
            "Usar IPP como alavanca de recuperação",
            "O suporte psicopedagógico não aparece como fator dominante do risco isolado, mas funciona como acelerador de evolução, especialmente via IPV.",
        )
        render_soft_card(
            "Tratar IPS como radar preventivo",
            "O psicossocial mostra baixa correlação direta com o INDE. Isso sugere uso como radar de prevenção e não como gatilho único de decisão.",
        )