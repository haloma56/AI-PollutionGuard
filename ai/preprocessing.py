
import pandas as pd
from pathlib import Path

# Chemin du dataset
DATA_PATH = Path("data/AirQualityUCI.csv")

FEATURES = [
    "PT08.S1(CO)",
    "PT08.S2(NMHC)",
    "PT08.S3(NOx)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
    "T",
    "RH",
    "AH"
]

TARGET = "CO(GT)"


def load_and_clean_data():
    # Lecture du fichier CSV
    df = pd.read_csv(
        DATA_PATH,
        sep=";",
        decimal=",",
        encoding="utf-8"
    )

    # Supprimer les colonnes vides
    df = df.dropna(axis=1, how="all")

    # Remplacer la valeur -200 par NaN
    df = df.replace(-200, float("nan"))

    # Garder les features et la cible
    df = df[FEATURES + [TARGET]]

    # Supprimer les lignes avec valeurs manquantes
    df = df.dropna()

    X = df[FEATURES]
    y = df[TARGET]

    return X, y
