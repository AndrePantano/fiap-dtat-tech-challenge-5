import pandas as pd
from app.components.charts import plot_profile_comparison
from app.components.cards import render_soft_card
from app.components.metrics import render_metrics_predict
from app.utils.formatters import format_decimal, format_pct
from app.services.analytics import get_benchmarks, get_feature_importances
from app.services.risk_analysis import predict_risk, classify_risk, build_priority_table, build_strengths_table, build_scenarios, build_recommendations, build_case_summary
from src.constants import FEATURES, FEATURES_RESUMIDAS, FEATURE_HELP


def render_tab_triagem(st, plt, tab_triagem, analytics_base, model):

    importances = get_feature_importances(model)
    benchmarks = get_benchmarks(analytics_base)

    with tab_triagem:
        st.subheader("Leitura da Predição")
        st.caption(
            "Os controles abaixo atualizam a leitura automaticamente. Use a análise para triagem, reunião de caso ou monitoramento recorrente."
        )

        col_form, col_preview = st.columns([1.05, 0.95], gap="large")

        with col_form:
            
            defaults = {
                feature: benchmarks.loc[feature, "exemplo"] for feature in FEATURES
            }
                        
            left, right = st.columns(2, gap="medium")

            with left:
                fase = st.text_input("Fase Atual", placeholder="Digite a fase atual", key="fase_estudante", value=int(defaults['fase']))
                ida = st.slider("IDA", 0.0, 10.0, defaults["ida"], 0.1, help=FEATURE_HELP["ida"])
                ieg = st.slider("IEG", 0.0, 10.0, defaults["ieg"], 0.1, help=FEATURE_HELP["ieg"])

            with right:
                ipv = st.slider("IPV", 0.0, 10.0, defaults["ipv"], 0.1, help=FEATURE_HELP["ipv"])
                ips = st.slider("IPS", 0.0, 10.0, defaults["ips"], 0.1, help=FEATURE_HELP["ips"])
                ipp = st.slider("IPP", 0.0, 10.0, defaults["ipp"], 0.1, help=FEATURE_HELP["ipp"])
                
            st.caption("Escala de referência dos indicadores: 0 a 10.")

        input_series = pd.Series({
            "ida": ida,
            "ieg": ieg,
            "ips": ips,
            "ipp": ipp,
            "fase": fase,
            "ipv": ipv,            
        })
        
        input_series_resumida = input_series[FEATURES_RESUMIDAS]
        
        prediction, probability = predict_risk(model, input_series)   
        band = classify_risk(probability)
        priority_df = build_priority_table(input_series, benchmarks, importances)
        strengths_df = build_strengths_table(input_series, benchmarks)
        scenario_df, combined_probability = build_scenarios(model, input_series, benchmarks, probability, importances)
        recommendations = build_recommendations(priority_df)
        case_summary = build_case_summary(band, priority_df, strengths_df, probability, combined_probability)

        with col_preview:
            benchmark_fig = plot_profile_comparison(input_series_resumida, benchmarks.loc[FEATURES_RESUMIDAS, "exemplo_resumido"])
            st.pyplot(benchmark_fig, use_container_width=True)
            plt.close(benchmark_fig)

            below_median = int((priority_df["Gap"] > 0).sum())
            top_gap = priority_df.iloc[0]
            
            st.markdown(
                f"""
                <div class="soft-card">
                    <h4>Resumo instantâneo</h4>
                    <p>
                        {below_median} de {priority_df.shape[0]} indicadores estão abaixo da mediana da base.
                        O maior desvio atual aparece em <strong>{top_gap["Indicador"]}</strong>.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="risk-panel {band["tone"]}">
                <div>
                    <span class="eyebrow" style="background: rgba(20,50,74,0.08); color: #14324a;">Leitura preditiva</span>
                    <h3>{band["label"]}</h3>
                    <p>{band["message"]}</p>
                </div>
                <div class="risk-score">{format_pct(probability)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(int(probability * 100))

        render_metrics_predict(prediction, below_median, scenario_df, combined_probability, probability)

        st.info(case_summary)

        analysis_left, analysis_right = st.columns([1.05, 0.95], gap="large")

        with analysis_left:
            st.markdown("#### Prioridades de intervenção")
            priority_display = priority_df.copy()
            priority_display["Valor atual"] = priority_display["Valor atual"].map(lambda x: format_decimal(x, 1))
            priority_display["Mediana da base"] = priority_display["Mediana da base"].map(lambda x: format_decimal(x, 1))
            priority_display["Gap"] = priority_display["Gap"].map(lambda x: format_decimal(x, 2))
            priority_display["Importância"] = priority_display["Importância"].map(lambda x: format_decimal(x, 2))
            st.dataframe(
                priority_display[["Indicador", "Status", "Valor atual", "Mediana da base", "Gap", "Importância"]].sort_values('Indicador'),
                use_container_width=True,
                hide_index=True,
            )

            st.markdown("#### Recomendações acionáveis")
            for title, description in recommendations:
                render_soft_card(title, description)

        with analysis_right:
            st.markdown("#### Simulações de melhoria")
            scenario_display = scenario_df.copy()
            scenario_display["Valor alvo"] = scenario_display["Valor alvo"].map(lambda x: format_decimal(x, 1))
            scenario_display["Risco projetado"] = scenario_display["Risco projetado"].map(lambda x: format_pct(x))
            scenario_display["Redução potencial"] = scenario_display["Redução potencial"].map(lambda x: format_pct(x))
            st.dataframe(
                scenario_display[["Indicador", "Valor alvo", "Risco projetado", "Redução potencial"]].sort_values('Indicador'),
                use_container_width=True,
                hide_index=True,
            )

            st.markdown("#### Fortalezas do perfil")
            if strengths_df.empty:
                render_soft_card(
                    "Sem fortalezas evidentes acima da mediana",
                    "O caso pede foco em recuperação dos pilares centrais antes de ampliar outras frentes.",
                )
            else:
                for _, row in strengths_df.head(3).iterrows():
                    render_soft_card(
                        row["Indicador"],
                        f"Indicador acima da mediana da base em {format_decimal(row['Ganho'], 2)} ponto(s), o que ajuda a amortecer o risco atual.",
                    )

