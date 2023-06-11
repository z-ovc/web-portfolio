import streamlit as st
from send_email import send_mail

st.header("contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("enter your email:")
    mesage = st.text_area("enter your message...")
    button = st.form_submit_button()
    if button:
        print("hello")
        send_mail(msg=mesage)