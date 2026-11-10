import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "pollution.csv"

FEATURES = [
    "PM2.5",
    "PM10",
    "Temperature",
    "Humidity"
]

TARGET = "CO"


def load_and_clean_data():

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    required_columns = ["City", "Date"] + FEATURES + [TARGET]

    missing = set(required_columns) - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )

    for column in FEATURES + [TARGET]:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df = df.replace(
        [float("inf"), float("-inf")],
        float("nan")
    )

    df = df.dropna(
        subset=FEATURES + [TARGET]
    )

    if len(df) < 5:
        raise ValueError(
            "Not enough valid data for training."
        )

    X = df[FEATURES]
    y = df[TARGET]

    return X, y