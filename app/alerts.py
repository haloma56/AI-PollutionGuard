
import streamlit as st

def show_pollution_alert(pm25):

    if pm25 <= 15:
        st.success("Good air quality")

    elif pm25 <= 35:
        st.warning("Moderate air pollution")

    else:
        st.error("High air pollution! Take precautions.")
