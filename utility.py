import pandas as pd

def getAllCsv(city):
    openMeteo = pd.read_csv(f'data/openMeteo/{city}_openMeteo.csv')
    weatherApi = pd.read_csv(f'data/weatherApi/{city}_weatherApi.csv')
    virtualCrossing = pd.read_csv(f'data/virtualCrossing/{city}_virtualCrossing.csv')
    openWeather = pd.read_csv(f'data/openWeather/{city}_openWeather.csv')
    worldWeather = pd.read_csv(f'data/worldWeatherOnline/{city}_worldWeatherOnline.csv')
    return openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather
    
def printAllCol(city):
    openMeteo, weatherApi, virtualCrossing, openWeather, worldWeather = getAllCsv(city)

    print("openMeteo")
    print(list(openMeteo.columns))
    print("weatherApi")
    print(list(weatherApi.columns))
    print("virtualCrossing")
    print(list(virtualCrossing.columns))
    print("openWeather")
    print(list(openWeather.columns))
    print("worldWeather")
    print(list(worldWeather.columns))


if __name__ == "__main__":
    printAllCol("ny")