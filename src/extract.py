import requests
import json 
from datetime import datetime

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request Failed")
    
    return response.json()

def save_raw_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/opt/airflow/data/raw/weather_{timestamp}.json"

    with open(filename,"w") as f:
        json.dump(data,f)

if __name__ == "__main__":
    data = fetch_weather_data()
    save_raw_data(data)



