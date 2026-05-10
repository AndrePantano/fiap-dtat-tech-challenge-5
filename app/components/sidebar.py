import streamlit as st

def render_sidebar():

    with st.sidebar:
        st.markdown("### Como usar")
        st.write("1. Ajuste os seis indicadores do aluno.")
        st.write("2. Leia o risco previsto e os fatores que mais puxam o caso.")
        st.write("3. Use as simulações para priorizar a intervenção pedagógica.")
        st.write("4. Navegue pelas abas para ver o contexto analítico da base.")
        st.markdown("### Faixas operacionais")
        st.write("Até 39%: monitoramento.")
        st.write("40% a 69%: atenção dirigida.")
        st.write("70% ou mais: prioridade imediata.")
        st.caption("Os resultados apoiam a decisão pedagógica, mas não substituem avaliação humana.")