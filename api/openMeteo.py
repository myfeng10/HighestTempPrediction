# pip install openmeteo-requests
# pip install requests-cache retry-requests numpy pandas
"""
code from 
https://open-meteo.com/en/docs/#hourly=&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,uv_index_clear_sky_max,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&timezone=America%2FNew_York&past_days=92&forecast_days=1&start_date=2023-04-01&end_date=2024-03-17&time_mode=time_interval
"""

import openmeteo_requests
from save import save_to_csv

import requests_cache
import pandas as pd
from retry_requests import retry
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

def getOpenMeteo(lat,lon,city,startDate,endDate):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max", "uv_index_clear_sky_max", "precipitation_sum", "rain_sum", "showers_sum", "snowfall_sum", "precipitation_hours", "precipitation_probability_max", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant", "shortwave_radiation_sum", "et0_fao_evapotranspiration"],
        "timezone": "America/New_York",
        "start_date": startDate,
        "end_date": endDate
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
  
    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
    daily_apparent_temperature_max = daily.Variables(3).ValuesAsNumpy()
    daily_apparent_temperature_min = daily.Variables(4).ValuesAsNumpy()
    daily_sunrise = daily.Variables(5).ValuesAsNumpy()
    daily_sunset = daily.Variables(6).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(7).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(8).ValuesAsNumpy()
    daily_uv_index_max = daily.Variables(9).ValuesAsNumpy()
    daily_uv_index_clear_sky_max = daily.Variables(10).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(11).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(12).ValuesAsNumpy()
    daily_showers_sum = daily.Variables(13).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(14).ValuesAsNumpy()
    daily_precipitation_hours = daily.Variables(15).ValuesAsNumpy()
    daily_precipitation_probability_max = daily.Variables(16).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(17).ValuesAsNumpy()
    daily_wind_gusts_10m_max = daily.Variables(18).ValuesAsNumpy()
    daily_wind_direction_10m_dominant = daily.Variables(19).ValuesAsNumpy()
    daily_shortwave_radiation_sum = daily.Variables(20).ValuesAsNumpy()
    daily_et0_fao_evapotranspiration = daily.Variables(21).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["weather_code"] = daily_weather_code
    daily_data["temperature_2m_max"] = daily_temperature_2m_max
    daily_data["temperature_2m_min"] = daily_temperature_2m_min
    daily_data["apparent_temperature_max"] = daily_apparent_temperature_max
    daily_data["apparent_temperature_min"] = daily_apparent_temperature_min
    daily_data["sunrise"] = daily_sunrise
    daily_data["sunset"] = daily_sunset
    daily_data["daylight_duration"] = daily_daylight_duration
    daily_data["sunshine_duration"] = daily_sunshine_duration
    daily_data["uv_index_max"] = daily_uv_index_max
    daily_data["uv_index_clear_sky_max"] = daily_uv_index_clear_sky_max
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_data["rain_sum"] = daily_rain_sum
    daily_data["showers_sum"] = daily_showers_sum
    daily_data["snowfall_sum"] = daily_snowfall_sum
    daily_data["precipitation_hours"] = daily_precipitation_hours
    daily_data["precipitation_probability_max"] = daily_precipitation_probability_max
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max
    daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant
    daily_data["shortwave_radiation_sum"] = daily_shortwave_radiation_sum
    daily_data["et0_fao_evapotranspiration"] = daily_et0_fao_evapotranspiration

    daily_dataframe = pd.DataFrame(data = daily_data)
    filename = f"{city}_openMeteo.csv"
    save_to_csv(daily_dataframe, filename,path="data/openMeteo")

def getHistoricDate(startDate,endDate):
    getOpenMeteo(40.77373,-73.98007,"ny",startDate,endDate)
    getOpenMeteo(30.14440,-97.66876,"austin",startDate,endDate)
    getOpenMeteo(25.81253,-80.24044,"miami",startDate,endDate)
    getOpenMeteo(41.78701,-87.77166,"chicago",startDate,endDate)

def openMeteo_getDailyUpdate(date):
    getOpenMeteo(40.7128,-74.0060,"ny",date,date)
    getOpenMeteo(30.14440,-97.66876,"austin",date,date)
    getOpenMeteo(25.81253,-80.24044,"miami",date,date)
    getOpenMeteo(41.78701,-87.77166,"chicago",date,date)
if __name__ == "__main__": 
    # getting historic data from 2023-04-01 to 2024-03-17
    # getHistoricDate("2023-04-01","2024-03-17")

    # getting daily data
    openMeteo_getDailyUpdate("2024-03-24")