import os
import pandas as pd


def get_embassy_air_quality(csv_path):
    air_quality_path = os.path.join(csv_path, "embassy_air_quality.csv")
    df = pd.read_csv(air_quality_path, delimiter=";")
    df["date"] = pd.to_datetime(df["date"])
    df= df.rename(columns={"pm25": "pm25_embassy"})
    df["pm25_embassy"] = df["pm25_embassy"].astype("float64")

    return df


def get_sensor_history(csv_path):
    sensor_history_path = os.path.join(csv_path, "sensor_history.csv")
    df = pd.read_csv(sensor_history_path)
    df["date"] = pd.to_datetime(df["created_at"])
    df = df.rename(columns={"PM2.5": "pm25_sergek"})
    df = df[["date", "pm25_sergek"]]

    return df
