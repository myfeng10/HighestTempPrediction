import requests
import pandas as pd
import datetime
import os

from save import save_to_csv

def weatherApi_history(zipcode,date,city):
    url = "http://api.weatherapi.com/v1/history.json"
    parameters = {
        "key": "placeholder",   # please change to your own key
        "q": zipcode, 
        "dt": date,  
    }
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        data = response.json()
        print(data)
        forecast_df = pd.json_normalize(data['forecast']['forecastday'], sep='_')
        filename = f"{city}_weatherApi.csv"
        save_to_csv(forecast_df, filename,path="data/weatherApi")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def getAllHistory(zipcode,city):
    start_date = datetime.date(2023, 4, 1)
    end_date = datetime.date(2024, 3, 17)
    current_date = start_date

    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        weatherApi_history(zipcode, date_str, city)
        current_date += datetime.timedelta(days=1) 

def weatherapi_getDailyUpdate(date):
    weatherApi_history(10023,date,"ny")
    weatherApi_history(78719,date,"austin")
    weatherApi_history(33142,date,"miami")
    weatherApi_history(60638,date,"chicago")

if __name__ == "__main__":
    # getAllHistory(10023,"ny") 
    # getAllHistory(60638,"chicago")
    # getAllHistory(78719,"austin")
    # getAllHistory(33142,"miami")
    # start_date = datetime.date(2023, 3, 19)
    # end_date = datetime.date(2024, 3, 24)
    # current_date = start_date

    # while current_date <= end_date:
    #     date_str = current_date.strftime('%Y-%m-%d')
    #     getDailyUpdate(date_str)
    #     current_date += datetime.timedelta(days=1) 
    weatherapi_getDailyUpdate("2024-03-24") 
