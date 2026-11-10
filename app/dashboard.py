from pathlib import Path
import sys

import streamlit as st
import pandas as pd

# Project paths
APP_DIR = Path(__file__).resolve().parent
PROJECT_DIR = APP_DIR.parent

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from charts import create_pollution_chart
from alerts import show_pollution_alert


# Page configuration
st.set_page_config(
    page_title="AI-PollutionGuard",
    page_icon="🌍",
    layout="wide"
)


# Load dataset
DATA_FILE = PROJECT_DIR / "data" / "pollution.csv"


@st.cache_data
def load_data():

    data = pd.read_csv(DATA_FILE)

    data["Date"] = pd.to_datetime(data["Date"])

    return data


try:
    data = load_data()

except Exception as error:
    st.error(f"Error loading dataset: {error}")
    st.stop()


# Main title
st.title("🌍 AI-PollutionGuard")

st.subheader(
    "Intelligent Air Pollution Monitoring System"
)

st.write(
    "Monitor air quality and pollution levels "
    "using Artificial Intelligence."
)


# Sidebar
st.sidebar.title("Navigation")

cities = sorted(data["City"].unique())

city = st.sidebar.selectbox(
    "Select City",
    cities
)


# Filter data according to selected city
city_data = data[data["City"] == city].copy()

city_data = city_data.sort_values("Date")


# Latest measurements
latest = city_data.iloc[-1]

pm25 = latest["PM2.5"]
pm10 = latest["PM10"]
co = latest["CO"]
temperature = latest["Temperature"]
humidity = latest["Humidity"]


st.caption(f"Selected city: {city}")

st.header("Air Quality Measurements")


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "PM2.5",
    f"{pm25} µg/m³"
)

col2.metric(
    "PM10",
    f"{pm10} µg/m³"
)

col3.metric(
    "CO",
    f"{co} mg/m³"
)

col4.metric(
    "Temperature",
    f"{temperature} °C"
)

col5.metric(
    "Humidity",
    f"{humidity} %"
)


st.divider()


# Air quality alert
st.header("Air Quality Status")

show_pollution_alert(pm25)


# AI Prediction
st.header("AI Pollution Prediction")

st.info(
    "AI prediction will be connected "
    "after integrating the Machine Learning model."
)


# Pollution chart
st.header("Pollution Monitoring")

fig = create_pollution_chart(city_data)

st.plotly_chart(
    fig,
    width="stretch"
)


# Measurement history
st.header("Measurement History")

st.dataframe(
    city_data,
    width="stretch",
    hide_index=True
)


# Footer
st.caption(
    "AI-PollutionGuard | Environmental AI Project"
)

st.caption(
    "Note: The dataset contains simulated values "
    "for educational demonstration only."
)