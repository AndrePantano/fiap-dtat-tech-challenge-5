import streamlit as st

def render_soft_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="soft-card">
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
