
import plotly.express as px

def create_pollution_chart(data):
    fig = px.line(
        data,
        x="Day",
        y=["PM2.5", "PM10"],
        title="Air Pollution Evolution",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Day",
        yaxis_title="Concentration (µg/m³)"
    )

    return fig
