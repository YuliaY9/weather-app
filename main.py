import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import folium
from streamlit_folium import folium_static

load_dotenv()
api_key=os.getenv("API_KEY")

st.title ("Weather Now")

city= st.text_input ("Enter city name")
city = city.strip()   
clicked= st.button("Get weather")

if city or (clicked or city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response= requests.get(url)

    if response.status_code== 200:
        data=response.json()
        #st.json(data)
        temp=data["main"]["temp"]
        hum=data ["main"]["humidity"]
        desc=data["weather"][0]["description"]
        desc_emoji_dict = {
            "clear sky": "☀️",
            "few clouds": "🌤️",
            "scattered clouds": "⛅",
            "overcast clouds": "☁️",
            "rain": "🌧️",
            "light rain": "🌦️",
            "thunderstorm": "⛈️",
            "snow": "❄️",
            "mist": "🌫️"
        }
        emoji= desc_emoji_dict.get(desc.lower(), "")
        wind=data["wind"]["speed"]
        clouds=data["clouds"]["all"]
        country=data["sys"]["country"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        timezone_delta_sec = data["timezone"]
        utc_time = datetime.now(timezone.utc)
        local_time = utc_time + timedelta(seconds=timezone_delta_sec)
        map_object = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat,lon],popup=city.title()).add_to(map_object)

        st.subheader (f"Weather in {city.title()},{country}")
        st.write(f"🌡️Temperature {temp}°C")
        st.write(f"💧Humidity {hum}%")
        st.write(f"🌬️Wind Speed {wind}m/s")
        st.write(f"☁️Cloudiness {clouds}")
        st.write(f"{emoji}{desc.capitalize()}")
        st.write(f"Local time: {local_time.strftime('%d-%m-%Y %H:%M')}")
        folium_static(map_object)

    elif response.status_code==404:
            st.error("City not found. Please try again")

    else:
        st.error(f"Unexpected error occurred. Status code {response.status_code}")

else:print("Please enter a city name and press ENTER or click a button")
