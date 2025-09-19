import streamlit as st
from scrapper import scrapper
#from file_name import function_name1,function_name2
import asyncio
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

st.set_page_config(page_title="kaggle_scrapper",layout="wide")
st.title("Kaggle Dataset Scrapper")

user_email = st.text_input("Enter the email")
user_password = st.text_input("Enter the password",type="password")
topic = st.text_input("Enter the topic")
if st.button(label="Submit"):
    path = scrapper(user_email,user_password,topic)
    if path:
        st.write("✅ File has been successfully downloaded ")
        st.download_button(data=path,label="Click here to download",file_name =f"{topic}.zip")
    else:
        st.error("❌ Try another Topic")
        