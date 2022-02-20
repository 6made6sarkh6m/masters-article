import pandas as pd
import matplotlib.pyplot as plt


def join_dataframes(quality_df, sensor_df):
    df = pd.merge(quality_df, sensor_df, on="date", how="left")
    df = df.fillna(method="backfill")
    df["diff"] = abs(df["pm25_embassy"] - df["pm25_sergek"])
    df = df.sort_values(by="date", ascending=True)

    return df


def plot_graph(df):
    fig, axs = plt.subplots(figsize=(12, 4))
    df.plot(kind="bar", rot=0, ax=axs)

    plt.xlabel("Date")
    plt.ylabel("PM2.5")

    # df.plot.bar(x="date", y="pm25", color="blue")
