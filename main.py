import requests as rq
import json
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


response = rq.get(url)


if response.status_code == 200:
    data = response.json()
    with open("data.json", "w") as f:
        json.dump(data, f)


with open("data.json", "r") as f:
    data = json.load(f)


st.title(data["title"])


st.image(data["url"], width=700)


st.caption(data["explanation"], unsafe_allow_html=True)


st.write("Date: " + data["date"])


st.write("Source: " + data["url"])