import plotly.express as px


def create_pollution_chart(data):

    fig = px.line(
        data,
        x="Date",
        y=["PM2.5", "PM10"],
        title="Air Pollution Evolution",
        markers=True,
        labels={
            "value": "Concentration (µg/m³)",
            "Date": "Date",
            "variable": "Pollutant"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        hovermode="x unified",
        legend_title_text="Pollutant"
    )

    return fig