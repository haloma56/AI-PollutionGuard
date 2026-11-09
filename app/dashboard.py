
import streamlit as st
import pandas as pd

from charts import create_pollution_chart
from alerts import show_pollution_alert

st.set_page_config(
    page_title="AI-PollutionGuard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI-PollutionGuard")
st.subheader("Intelligent Air Pollution Monitoring System")

st.markdown("""
Monitor air quality and predict pollution levels
using Artificial Intelligence.
""")

# Sidebar
st.sidebar.title("Navigation")

city = st.sidebar.selectbox(
    "Select City",
    ["Algiers", "Oran", "Constantine", "El Oued"]
)

# Demo data
pm25 = 25
pm10 = 48
temperature = 29

col1, col2, col3 = st.columns(3)

col1.metric("PM2.5", f"{pm25} µg/m³")
col2.metric("PM10", f"{pm10} µg/m³")
col3.metric("Temperature", f"{temperature} °C")

st.divider()

# Air quality alert
st.subheader("Air Quality Status")
show_pollution_alert(pm25)

# AI Prediction
st.subheader("Pollution Prediction")
st.info("AI prediction will be connected after ML integration.")

# Pollution chart
st.subheader("Pollution Monitoring")

data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "PM2.5": [20, 25, 18, 35, 28],
    "PM10": [40, 45, 38, 55, 48]
})

fig = create_pollution_chart(data)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "AI-PollutionGuard | Environmental AI Project"
)
