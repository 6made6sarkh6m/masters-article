import os
from preprocessing import get_embassy_air_quality, get_sensor_history
from transformation import transform_air_quality, transform_sensor_history
from analytics import join_dataframes, plot_graph


if __name__ == "__main__":
    csv_dir = os.path.join(os.getcwd(), "csv")

    quality_df = get_embassy_air_quality(csv_dir)
    sensor_df = get_sensor_history(csv_dir)

    quality_df = transform_air_quality(quality_df)
    sensor_df = transform_sensor_history(sensor_df)

    final_df = join_dataframes(quality_df, sensor_df)
    print(final_df.head(60))

