def transform_air_quality(df):
    df = df[(df["date"] >= "2018-11-05") & (df["date"] <= "2019-06-05")]

    return df


def transform_sensor_history(df):
    df["date"] = df["date"].values.astype("<M8[D]")
    df = df[(df["date"] >= "2018-11-06")]
    grouped_df = df.groupby("date")
    mean_df = grouped_df.mean()
    mean_df = mean_df.reset_index()
    mean_df = mean_df.round(1)
    final_df = mean_df.fillna(method="backfill")

    return final_df
