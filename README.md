# Highest Temperature Prediction

This Python script aggregates and analyzes weather data from multiple sources for various cities. It retrieves daily updates from different weather APIs, calculates mean values for key weather parameters, and creates CSV files containing aggregated statistics for further analysis.

Key Features:
Data Retrieval: The script fetches daily weather updates from APIs including OpenMeteo, WeatherAPI, OpenWeather, and WorldWeatherOnline.

Data Aggregation: After obtaining the data, the script calculates the mean values of essential weather parameters such as maximum temperature, minimum temperature, apparent temperature, sunrise, sunset, total precipitation, and wind speed.

CSV Creation: The aggregated data is saved into CSV files, with separate files generated for each city. These files contain the aggregated weather statistics specific to each city.

City-specific Functionality: The script operates on multiple cities independently. For each city (e.g., New York, Chicago, Austin, Miami), it retrieves daily weather updates, aggregates the data, and produces CSV files containing city-specific weather statistics.

Usage:
Ensure Python and required packages (e.g., pandas, sklearn) are installed.
Run the script, specifying the desired date for retrieving weather updates.
The script will fetch weather data from APIs, aggregate it, and generate CSV files with aggregated statistics for each city.
