import streamlit as st


def pollution_category(pm25):

    if pm25 <= 15:
        return "Good"

    elif pm25 <= 35:
        return "Moderate"

    else:
        return "Poor"


def show_pollution_alert(pm25):

    category = pollution_category(pm25)

    if category == "Good":
        st.success("Good air quality!")

    elif category == "Moderate":
        st.warning("Moderate air pollution!")

    else:
        st.error("Poor air quality! Take precautions.")

    return category