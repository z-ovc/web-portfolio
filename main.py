import streamlit as st

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg",width=300)

with col2:
    st.title("zahra oveisi")
    content = """zahra is a fast learner who love new challanges.
    the most interesting thing about her is being happy always, even when she fails..."""
    st.info(content)