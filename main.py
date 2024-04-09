import pandas as pd
from utility import getAllCsv, printAllCol
# from api.save import save_to_csv
from datetime import datetime, timedelta

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

from api.openMeteo import openMeteo_getDailyUpdate
from api.weatherApi import weatherapi_getDailyUpdate
from api.openWeather import openWeather_getDailyUpdate
from api.worldweatheronline import worldweatheronline_getDailyUpdate



def create_max_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    # rename all col to: max_temp
    openMeteo = openMeteo.rename(columns={"temperature_2m_max": "openMeteo_max_temp"})
    weatherApi = weatherApi.rename(columns={"day_maxtemp_c": "weatherApi_max_temp"})
    virtualCrossing = virtualCrossing.rename(columns={"tempmax": "virtualCrossing_max_temp"})
    openWeather = openWeather.rename(columns={"temperature.max": "openWeather_max_temp"})
    worldWeather = worldWeather.rename(columns={"maxtempC": "worldWeather_max_temp"})

    # only concatenate the max_temp col
    max_temp_aggregate = pd.concat([
        openMeteo['openMeteo_max_temp'],
        weatherApi['weatherApi_max_temp'],
        virtualCrossing['virtualCrossing_max_temp'],
        openWeather['openWeather_max_temp'],
        worldWeather['worldWeather_max_temp']
    ], axis=1)

    filename = f"{city}_max_temp_aggregate.csv"
    max_temp_aggregate.to_csv(filename, index=True)
    # print(max_temp_aggregate)


def create_min_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    # rename all col to: min_temp
    openMeteo = openMeteo.rename(columns={"temperature_2m_min": "openMeteo_min_temp"})
    weatherApi = weatherApi.rename(columns={"day_mintemp_c": "weatherApi_min_temp"})
    virtualCrossing = virtualCrossing.rename(columns={"tempmin": "virtualCrossing_min_temp"})
    openWeather = openWeather.rename(columns={"temperature.min": "openWeather_min_temp"})
    worldWeather = worldWeather.rename(columns={"mintempC": "worldWeather_min_temp"})

    # only concatenate the max_temp col
    max_temp_aggregate = pd.concat([
        openMeteo['openMeteo_min_temp'],
        weatherApi['weatherApi_min_temp'],
        virtualCrossing['virtualCrossing_min_temp'],
        openWeather['openWeather_min_temp'],
        worldWeather['worldWeather_min_temp']
    ], axis=1)

    filename = f"{city}_min_temp_aggregate.csv"
    max_temp_aggregate.to_csv(filename, index=True)
    # print(max_temp_aggregate)


def create_max_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    # rename all col to: max_temp
    openMeteo = openMeteo.rename(columns={"temperature_2m_max": "openMeteo_max_temp"})
    weatherApi = weatherApi.rename(columns={"day_maxtemp_c": "weatherApi_max_temp"})
    virtualCrossing = virtualCrossing.rename(columns={"tempmax": "virtualCrossing_max_temp"})
    openWeather = openWeather.rename(columns={"temperature.max": "openWeather_max_temp"})
    worldWeather = worldWeather.rename(columns={"maxtempC": "worldWeather_max_temp"})

    # only concatenate the max_temp col
    max_temp_aggregate = pd.concat([
        openMeteo['openMeteo_max_temp'],
        weatherApi['weatherApi_max_temp'],
        virtualCrossing['virtualCrossing_max_temp'],
        openWeather['openWeather_max_temp'],
        worldWeather['worldWeather_max_temp']
    ], axis=1)

    filename = f"{city}_max_temp_aggregate.csv"
    max_temp_aggregate.to_csv(filename, index=True)
    # print(max_temp_aggregate)

def create_max_apparent_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    # rename all col to: apparent_temp: only 2 sources have this information
    openMeteo = openMeteo.rename(columns={"apparent_temperature_max": "openMeteo_max_apparent_temp"})
    virtualCrossing = virtualCrossing.rename(columns={"feelslikemax": "virtualCrossing_max_apparent_temp"})

    colName="_max_apparent_temp"
    # only concatenate the max_temp col
    max_temp_aggregate = pd.concat([
        openMeteo[f'openMeteo{colName}'],
        virtualCrossing[f'virtualCrossing{colName}'],
    ], axis=1)

    filename = f"{city}{colName}_aggregate.csv"
    max_temp_aggregate.to_csv(filename, index=True)

def create_min_apparent_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    # rename all col to: apparent_temp: only 2 sources have this information
    openMeteo = openMeteo.rename(columns={"apparent_temperature_min": "openMeteo_min_apparent_temp"})
    virtualCrossing = virtualCrossing.rename(columns={"feelslikemin": "virtualCrossing_min_apparent_temp"})

    colName="_min_apparent_temp"
    # only concatenate the max_temp col
    max_temp_aggregate = pd.concat([
        openMeteo[f'openMeteo{colName}'],
        virtualCrossing[f'virtualCrossing{colName}'],
    ], axis=1)

    filename = f"{city}{colName}_aggregate.csv"
    max_temp_aggregate.to_csv(filename, index=True)

def create_sun_rise_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    colName = "_mean_sunrise"
    virtualCrossing = virtualCrossing.rename(columns={"sunrise": "mean_sunrise"})
    sunrise_aggregate = pd.concat([
        virtualCrossing['mean_sunrise'],
    ], axis=1)
    filename = f"{city}{colName}_aggregate.csv"
    sunrise_aggregate.to_csv(filename, index=True)

def create_sun_set_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    colName = "_mean_sunset"
    virtualCrossing = virtualCrossing.rename(columns={"sunset": "mean_sunset"})
    sunrise_aggregate = pd.concat([
        virtualCrossing['mean_sunset'],
    ], axis=1)
    filename = f"{city}{colName}_aggregate.csv"
    sunrise_aggregate.to_csv(filename, index=True)

def create_total_precipitation_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    colName="_total_precipitation"
    # rename all col to: apparent_temp: only 4 sources have this information
    openMeteo = openMeteo.rename(columns={"precipitation_sum": f"openMeteo{colName}"})
    virtualCrossing = virtualCrossing.rename(columns={"precip": f"virtualCrossing{colName}"})
    openWeather = openWeather.rename(columns={"precipitation.total": f"openWeather{colName}"})
    weatherApi = weatherApi.rename(columns={"day_totalprecip_mm": f"weatherApi{colName}"})

    total_precipitation_aggregate = pd.concat([
        openMeteo[f'openMeteo{colName}'],
        virtualCrossing[f'virtualCrossing{colName}'],
        openWeather[f'openWeather{colName}'],
        weatherApi[f'weatherApi{colName}'],
    ], axis=1)

    filename = f"{city}{colName}_aggregate.csv"
    total_precipitation_aggregate.to_csv(filename, index=True)

def create_wind_speed_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city):
    colName="_wind_speed"
    # rename all col to: apparent_temp: only 4 sources have this information
    openMeteo = openMeteo.rename(columns={"wind_speed_10m_max": f"openMeteo{colName}"})
    virtualCrossing = virtualCrossing.rename(columns={"windspeed": f"virtualCrossing{colName}"})
    openWeather = openWeather.rename(columns={"wind.max.speed": f"openWeather{colName}"})
    weatherApi = weatherApi.rename(columns={"day_maxwind_kph": f"weatherApi{colName}"})

    # convert m/s to km/h
    openWeather[f"openWeather{colName}"] = openWeather[f"openWeather{colName}"] * 3.6

    wind_speed_aggregate = pd.concat([
        openMeteo[f'openMeteo{colName}'],
        virtualCrossing[f'virtualCrossing{colName}'],
        openWeather[f'openWeather{colName}'],
        weatherApi[f'weatherApi{colName}'],
    ], axis=1)

    filename = f"{city}{colName}_aggregate.csv"
    wind_speed_aggregate.to_csv(filename, index=True)

 
def create_all_data_cvs(city):
    openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather = getAllCsv(city)

    ## rename date + ensure consistant formatting
    virtualCrossing = virtualCrossing.rename(columns={"datetime": "date"})
    openMeteo['date'] = pd.to_datetime(openMeteo['date']).dt.strftime('%Y-%m-%d')

    openMeteo.set_index('date', inplace=True)
    weatherApi.set_index('date', inplace=True)
    virtualCrossing.set_index('date', inplace=True)
    openWeather.set_index('date', inplace=True)
    worldWeather.set_index('date', inplace=True)

    data_frames = {
    'worldWeather': worldWeather,
    'openWeather': openWeather,
    'virtualCrossing': virtualCrossing,
    'weatherApi': weatherApi,
    'openMeteo': openMeteo
}

    for name, df in data_frames.items():
        has_duplicates = df.index.duplicated().any()
        if has_duplicates:
            print(f"{name} has duplicates: {has_duplicates}")
            duplicate_rows = df[df.duplicated()]
            print(duplicate_rows)
        else:
            print(f"{name} has no duplicates.")

    
    ## creating csv files for each important col
    create_max_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_min_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_max_apparent_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_min_apparent_temp_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_sun_rise_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_sun_set_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)

    create_total_precipitation_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)
    create_wind_speed_csv(openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather,city)

def create_aggregate_average_csv(city):
    # create csv with individual features that we need
    create_all_data_cvs(city) 

    # get access to the csv files
    max_temp = pd.read_csv(f'{city}_max_temp_aggregate.csv',index_col='date')
    min_temp = pd.read_csv(f'{city}_min_temp_aggregate.csv',index_col='date')
    max_apprent_temp = pd.read_csv(f'{city}_max_apparent_temp_aggregate.csv',index_col='date')
    min_apparent_temp = pd.read_csv(f'{city}_min_apparent_temp_aggregate.csv',index_col='date')
    sunrise = pd.read_csv(f'{city}_mean_sunrise_aggregate.csv',index_col='date')
    sunset = pd.read_csv(f'{city}_mean_sunset_aggregate.csv',index_col='date')
    total_precipitation = pd.read_csv(f'{city}_total_precipitation_aggregate.csv',index_col='date')
    wind_speed = pd.read_csv(f'{city}_wind_speed_aggregate.csv',index_col='date')

    # getting the min of each value
    max_temp_mean = max_temp.mean(axis=1, skipna=True).to_frame(name='mean_max_temp')
    min_temp_mean = min_temp.mean(axis=1, skipna=True).to_frame(name='mean_min_temp')
    max_apprent_temp_mean = max_apprent_temp.mean(axis=1, skipna=True).to_frame(name='mean_max_apparent_temp')
    min_apparent_temp_mean = min_apparent_temp.mean(axis=1, skipna=True).to_frame(name='mean_min_apparent_temp')
    sunrise_mean = sunrise
    sunset_mean = sunset
    total_precipitation_mean = total_precipitation.mean(axis=1, skipna=True).to_frame(name='mean_total_precipitation')
    wind_speed_mean = wind_speed.mean(axis=1, skipna=True).to_frame(name='mean_wind_speed')

    # form the aggregate average csv
    # remove sunrise_mean sunset_mean
    aggregate = pd.concat([max_temp_mean, min_temp_mean,max_apprent_temp_mean,min_apparent_temp_mean,total_precipitation_mean,wind_speed_mean], axis=1)

    aggregate.to_csv(f'{city}_aggregate.csv', index=True, index_label='date')
    return aggregate

def getDailyUpdate(date):
    openMeteo_getDailyUpdate(date)
    weatherapi_getDailyUpdate(date)
    openWeather_getDailyUpdate(date)
    worldweatheronline_getDailyUpdate(date)

if __name__ == "__main__":

    getDailyUpdate("2024-03-25")
    ny_aggregate = create_aggregate_average_csv("ny")
    chicago_aggregate = create_aggregate_average_csv("chicago")
    austin_aggregate = create_aggregate_average_csv("austin")
    miami_aggregate = create_aggregate_average_csv("miami")
   