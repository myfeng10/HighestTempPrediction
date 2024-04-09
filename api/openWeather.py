import requests
from datetime import datetime, timedelta 
from save import save_to_csv
import pandas as pd

api_key = 'ea921f6e1981bbd3c9c28b47207eb2de'

def getOpenWeather(lat,lon,city,date):
    units = 'metric'
    # Construct the URL with the parameters
    url = f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={date}&units={units}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize([data])
        filename = f"{city}_openWeather.csv"
        save_to_csv(df, filename, path="data/openWeather")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def getAllHistory(lat,lon,city):
    start_date = datetime(2023, 4, 1)
    end_date = datetime(2024, 3, 17)
    current_date = start_date

    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        getOpenWeather(lat,lon,city,date_str) 
        current_date += timedelta(days=1)


def openWeather_getDailyUpdate(date):
    getOpenWeather(40.77373,-73.98007,"ny",date)
    getOpenWeather(30.14440,-97.66876,"austin",date)
    getOpenWeather(25.81253,-80.24044,"miami",date)
    getOpenWeather(41.78701,-87.77166,"chicago",date)
if __name__ == "__main__": 
    # getAllHistory(40.77373,-73.98007,"ny")
    # getAllHistory(30.14440,-97.66876,"austin")
    # getAllHistory(25.81253,-80.24044,"miami")
    # getAllHistory(41.78701,-87.77166,"chicago")

    openWeather_getDailyUpdate("2024-03-24")



    pass