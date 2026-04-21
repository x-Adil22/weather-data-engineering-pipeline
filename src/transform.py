import json 
import os 
import pandas as pd 

def read_latest_file():
    files = os.listdir("/opt/airflow/data/raw")
    files.sort(reverse=True)

    latest_file = files[0]

    with open(f"/opt/airflow/data/raw/{latest_file}", "r") as f:
        data = json.load(f)

    return data

def transform_weather_data(data):
    current = data.get("current_weather",{})

    cleaned_data = {
        "temperature" : current.get("temperature"),
        "windspeed" : current.get("windspeed"),
        "winddirection" : current.get("winddirection"),
        "time" : current.get("time") 
    }

    df = pd.DataFrame([cleaned_data])
    
    return df

def clean_data(df):
    df = df.dropna()

    df["temperature"] = df["temperature"].astype(float)

    df["time"] = pd.to_datetime(df["time"])

    return df

def run_transformation():
    raw_data = read_latest_file()
    df = transform_weather_data(raw_data)
    df = clean_data(df)

    return df

if __name__ == "__main__":
    df = run_transformation()
    print(df)



