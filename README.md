Weather Now app

This project is a weather-checking app built with Python, Poetry, GitHub and Streamlit.

Project Description:
The app lets users enter any city name and get current weather information, including:
- Temperature
- Humidity
- Wind speed and cloudiness
- Weather icon and description
- Local time in the selected city
- A map showing the city location

Setup Instructions:
1. Clone this repository  
2. Install dependencies using: poetry install
3. Create a `.env` file in the root folder and add your OpenWeatherMap API key:
API_KEY=your_api_key_here

How to Run:
The main file to run is: `main.py`

To start the app, run:
poetry run streamlit run main.py
