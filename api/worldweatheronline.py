import requests
from datetime import datetime, timedelta 
from save import save_to_csv
import pandas as pd

# Your API key from World Weather Online
api_key = 'c47269f84f30466bb8e230346241803'

def wordWeatherApi(q,date,city):
    base_url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"

    params = {
        "q": q,  
        "date": date,   
        "tp": "1",  
        "format": "json",  
        "key": api_key, 
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize([data['data']['weather'][0]])
        
        filename = f"{city}_worldWeatherOnline.csv"
        save_to_csv(df, filename,path="data/worldWeatherOnline")
    else:
        print("Failed to retrieve data:", response.status_code)


def saveAllHistory(q,city):
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2024, 3, 17)
    current_date = start_date

    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        wordWeatherApi(q,city,date_str) 
        current_date += timedelta(days=1)

def worldweatheronline_getDailyUpdate(date):
    wordWeatherApi(10023,date,"ny")
    wordWeatherApi(78719,date,"austin")
    wordWeatherApi(33142,date,"miami")
    wordWeatherApi(60638,date,"chicago")

if __name__ == "__main__":
    # saveAllHistory("10023","ny") 
    # saveAllHistory(60638,"chicago")
    # saveAllHistory(78719,"austin")
    # saveAllHistory(33142,"miami")


    getDailyUpdate("2024-03-20")
    pass