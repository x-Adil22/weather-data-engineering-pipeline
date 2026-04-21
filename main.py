from src.extract import fetch_weather_data, save_raw_data
from src.transform import run_transformation
from src.load import load_data


def run_pipeline():
    print(" Running pipeline locally...")

    data = fetch_weather_data()
    save_raw_data(data)

    df = run_transformation()
    load_data(df)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()