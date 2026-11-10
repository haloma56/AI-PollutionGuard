from pathlib import Path

import joblib
import pandas as pd

from ai.preprocessing import FEATURES


MODEL_PATH = Path(__file__).resolve().parent / "pollution_model.pkl"


def predict_pollution(pm25, pm10, temperature, humidity):

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Train the model first."
        )

    model = joblib.load(MODEL_PATH)

    input_data = pd.DataFrame([{
        "PM2.5": pm25,
        "PM10": pm10,
        "Temperature": temperature,
        "Humidity": humidity
    }], columns=FEATURES)

    prediction = model.predict(input_data)[0]

    return round(float(prediction), 3)