
import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path("ai/pollution_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_pollution(
    sensor_co,
    sensor_nmhc,
    sensor_nox,
    sensor_no2,
    sensor_o3,
    temperature,
    humidity,
    absolute_humidity
):
    input_data = pd.DataFrame([{
        "PT08.S1(CO)": sensor_co,
        "PT08.S2(NMHC)": sensor_nmhc,
        "PT08.S3(NOx)": sensor_nox,
        "PT08.S4(NO2)": sensor_no2,
        "PT08.S5(O3)": sensor_o3,
        "T": temperature,
        "RH": humidity,
        "AH": absolute_humidity
    }])

    prediction = model.predict(input_data)[0]

    return round(float(prediction), 3)
