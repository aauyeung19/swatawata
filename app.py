import streamlit as st
import requests
import json

country_code = "us"
API_key = "98ec6864b86b42efec56dc8a1b9abcef"


if __name__ == "__main__":
    st.title("Sweater Weather Commitee")
    zip_code = st.text_input("What is your zipcode?", "")
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={API_key}&units=imperial')

    if response.status_code != 200:
        st.stop()
    data = response.json()
    desc = data["weather"][0]["description"]
    swatawata = st.button("Is it Sweater Weather?")
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    if swatawata:
        st.write(f"Right now there is/are {desc}")
        st.write(f"Current temperature is {temp} degrees farenheit")
        st.write(f"Feels like: {feels_like}")

        if temp > 60:
            st.image("no.gif")
        else:
            st.image("yes.gif")
    