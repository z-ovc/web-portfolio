import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 200px;
        margin-left: 500px;
    }
    """,
    unsafe_allow_html=True,
)
df = pd.read_csv("data.csv", sep= ";")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("zahra oveisi")
    content = """zahra is a fast learner who love new challanges.
    the most interesting thing about her is being happy always, even when she fails..."""
    st.info(content)

content2 = "if you need help feel free to contact me...!"
st.write(content2)

col3, emptycol, col4 = st.columns([3,1,3])

with col3:
    for index, row in df[:11].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"[SourceCode]({row['url']})")

with col4:
    for index, row in df[11:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"[SourceCode]({row['url']})")



