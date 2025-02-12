"""Flask application for the Dissertation Smart Home Weather Dashboard Author: S275931."""

# Import the required libraries & modules
from flask import Flask, render_template, jsonify
import os
import hashlib, requests, time, hmac
from datetime import date
import calendar
import re
import http.client
import ast
import csv
import codecs
import json

app = Flask(__name__) # Create a Flask application


@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the index.html template (landing dashboard page)"""
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb' # WeatherLink API Key
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy' # WeatherLink API Secret
    station_id = 142820 # Weather Station ID

    # current time
    local_time = int(time.time()) # Get the current local time

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest() # Create the API signature

    url = f"https://api.weatherlink.com/v2/current/{station_id}" # WeatherLink API URL
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    } # WeatherLink API parameters

    response = requests.get(url, params=params) # Get the WeatherLink API response
    current_weather = response.json() # Convert the response to JSON
    print(type(current_weather))
    print(current_weather)
    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    temperatureFarenheit = sensorData['temp'] # Get the temperature in Farenheit
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0 / 9.0 # Convert Farenheit to Celsius
    temperatureCelsius = round(temperatureCelsius, 1)  # round to 1 decimal place
    strTemperatureCelsius = str(temperatureCelsius) + "°C" # Convert the temperature to a string
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F" # Convert the temperature to a string



    response = requests.get(url, params=params) # Get the WeatherLink API response
    current_weather = response.json() # Convert the response to JSON
    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    humidity = sensorData['hum'] # Get the humidity
    strHumidity = str(humidity) + "%" # Convert the humidity to a string

    data = strTemperatureCelsius, strHumidity, strTemperatureFarenheit # Create a tuple of the data to send to front end
    print(type(data))
    print(data)
    return render_template('index.html', data=data) # Render the index.html template with the data

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    """Render the weather.html template (weather dashboard page with weather data)"""
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb' # WeatherLink API Key
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy' # WeatherLink API Secret
    station_id = 142820 # Weather Station ID

    # current time
    local_time = int(time.time()) # Get the current local time

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest() # Create the API signature

    url = f"https://api.weatherlink.com/v2/current/{station_id}" # WeatherLink API URL
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    } # WeatherLink API parameters

    response = requests.get(url, params=params) # Get the WeatherLink API response
    current_weather = response.json() # Convert the response to JSON
    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    print(sensorData)
    temperatureFarenheit = sensorData['temp'] # Get the temperature in Farenheit
    temperatureCelsius = (temperatureFarenheit - 32) * 5.0 / 9.0 # Convert Farenheit to Celsius
    print(type(temperatureCelsius))
    print("Temperature in Celsius: ", temperatureCelsius)
    temperatureCelsius1 = round(temperatureCelsius, 1)  # round to 1 decimal place
    strTemperatureCelsius1 = str(temperatureCelsius1) + "°C" # Convert the temperature to a string
    strTemperatureFarenheit = str(temperatureFarenheit) + "°F" # Convert the temperature to a string

    sensors = current_weather['sensors'] # Get the sensors data
    print(type(sensors))
    print("Sensors: ", sensors)
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    humidity = sensorData['hum'] # Get the humidity
    humidity = int(humidity) # Convert the humidity to an integer
    strHumidity = str(humidity) + "%" # Convert the humidity to a string

    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[4] # Get the sensor data for the rain sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    aqi = sensorData['aqi_val'] # Get air quality index value
    aqi_description = sensorData['aqi_desc'] # Get air quality index description
    aqi = int(aqi) # Convert the air quality index to an integer
    print("AQI: ", aqi)

    # AQI Colour and Percentage for bar chart on weather dashboard
    if aqi == 0:
        aqi_percentage ="0%"
        aqi_colour = "#00FF00" # Green
    elif aqi == 1:
        aqi_percentage = "10%"
        aqi_colour = "#7aff00" # Light Green
    elif aqi == 2:
        aqi_percentage = "20%"
        aqi_colour = "#a1ff00" # Light Green
    elif aqi == 3:
        aqi_percentage = "30%"
        aqi_colour = "#c7ff00" # Light Green
    elif aqi == 4:
        aqi_percentage = "40%"
        aqi_colour = "#faff00" # Yellow
    elif aqi == 5:
        aqi_percentage = "50%"
        aqi_colour = "#ffea00" # Yellow
    elif aqi == 6:
        aqi_percentage = "60%"
        aqi_colour = "#ffc400" # Orange
    elif aqi == 7:
        aqi_percentage = "70%"
        aqi_colour = "#ff9100" # Orange
    elif aqi == 8:
        aqi_percentage = "80%"
        aqi_colour = "#ff5e00" # Orange
    elif aqi == 9:
        aqi_percentage = "90%"
        aqi_colour = "#ff3700" # Red
    elif aqi >=  10:
        aqi_percentage = "100%"
        aqi_colour = "#ff0000" # Red


    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    print(sensorData)
    windSpeed = sensorData['wind_speed_last'] # Get the wind speed
    print("Wind Speed: ", windSpeed)
    if windSpeed == None:
        windSpeed = 0
    windSpeedKMH = windSpeed * 1.60934 # Convert wind speed to km/h
    windSpeedKMH = round(windSpeedKMH, 1) # round to 1 decimal place
    windSpeedKMH = int(windSpeedKMH) # Convert the wind speed to an integer
    strWindSpeed = str(windSpeed) + "mph" # Convert the wind speed to a string mph
    strWindSpeedKMH = str(windSpeedKMH) + "km/h" # Convert the wind speed to a string kmh

    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    windDirection = sensorData['wind_dir_last'] # Get the wind direction
    print("Wind Direction: ", windDirection)
    if windDirection >=0 and windDirection < 22.5 or windDirection >= 337.5 and windDirection <= 360:
        windDirectionDescription = "North" # Wind direction description as North
        compass = "/static/images/compassNorth.svg" # Compass image for wind direction as North
    elif windDirection >= 22.5 and windDirection < 67.5:
        windDirectionDescription = "North East" # Wind direction description as North East
        compass = "/static/images/compassNorthEast.svg" # Compass image for wind direction as North East
    elif windDirection >= 67.5 and windDirection < 112.5:
        windDirectionDescription = "East" # Wind direction description as East
        compass = "/static/images/compassEast.svg" # Compass image for wind direction as East
    elif windDirection >= 112.5 and windDirection < 157.5:
        windDirectionDescription = "South East" # Wind direction description as South East
        compass = "/static/images/compassSouthEast.svg" # Compass image for wind direction as South East
    elif windDirection >= 157.5 and windDirection < 202.5:
        windDirectionDescription = "South" # Wind direction description as South
        compass = "/static/images/compassSouth.svg" # Compass image for wind direction as South
    elif windDirection >= 202.5 and windDirection < 247.5:
        windDirectionDescription = "South West" # Wind direction description as South West
        compass = "/static/images/compassSouthWest.svg" # Compass image for wind direction as South West
    elif windDirection >= 247.5 and windDirection < 292.5:
        windDirectionDescription = "West" # Wind direction description as West
        compass = "/static/images/compassWest.svg" # Compass image for wind direction as West
    elif windDirection >= 292.5 and windDirection < 337.5:
        windDirectionDescription = "North West"   # Wind direction description as North West
        compass = "/static/images/compassNorthWest.svg" # Compass image for wind direction as North West
    print(type(windDirectionDescription))
    print("windDirectionDescription: ", windDirectionDescription)

    sensors = current_weather['sensors'] # Get the sensors data
    sensors = sensors[2] # Get the sensor data for the temperature sensor
    sensorData = sensors['data'] # Get the sensor data
    sensorData = sensorData[0] # Get the first sensor data
    UV_index= sensorData['uv_index'] # Get the UV index
    if UV_index <= 2: # UV index description based on the UV index value
        UV_index_description = " Low"
    elif UV_index >= 3 and UV_index <= 5:
        UV_index_description = " Moderate"
    elif UV_index >= 6 and UV_index <= 7:
        UV_index_description = " High"
    elif UV_index >= 8 and UV_index <= 10:
        UV_index_description = " Very High"

    UV_index = int(UV_index)

    # UV Index Colour and Percentage for bar chart on weather dashboard
    if UV_index == 0:
        UV_index_percentage ="0%"
        UV_index_colour = "#00FF00" # Green
    elif UV_index == 1:
        UV_index_percentage = "10%"
        UV_index_colour = "#7aff00" # Light Green
    elif UV_index == 2:
        UV_index_percentage = "20%"
        UV_index_colour = "#a1ff00" # Light Green
    elif UV_index == 3:
        UV_index_percentage = "30%"
        UV_index_colour = "#c7ff00" # Light Green
    elif UV_index == 4:
        UV_index_percentage = "40%"
        UV_index_colour = "#faff00" # Yellow
    elif UV_index == 5:
        UV_index_percentage = "50%"
        UV_index_colour = "#ffea00" # Yellow
    elif UV_index == 6:
        UV_index_percentage = "60%"
        UV_index_colour = "#ffc400" # Orange
    elif UV_index == 7:
        UV_index_percentage = "70%"
        UV_index_colour = "#ff9100" # Orange
    elif UV_index == 8:
        UV_index_percentage = "80%"
        UV_index_colour = "#ff5e00" # Orange
    elif UV_index == 9:
        UV_index_percentage = "90%"
        UV_index_colour = "#ff3700" # Red
    elif UV_index == 10:
        UV_index_percentage = "100%"
        UV_index_colour = "#ff0000" # Red


    openWeather_API_Key = 'cdb2f81a0c0053ff42b1db37fdb0b39b' # OpenWeather API Key
    openWeatherID = 2646057 # OpenWeather City ID for London
    local_time = int(time.time()) # Get the current local time
    params = {
        "t": local_time
    } # OpenWeather API parameters
    openWeatherURL = 'https://api.openweathermap.org/data/2.5/forecast?id=' + str(
        openWeatherID) + '&appid=' + openWeather_API_Key # OpenWeather API URL
    response = requests.get(openWeatherURL, params=params) # Get the OpenWeather API response
    openWeatherData = response.json() # Convert the response to JSON
    openWeatherData = openWeatherData['list'] # Get the list of weather data
    openWeatherDataToday = openWeatherData[0] # Get the weather data for today
    OpenWeatherDataTodayWeather = openWeatherDataToday['weather'] # Get the weather conditions for today
    OpenWeatherDataTodayWeather = OpenWeatherDataTodayWeather[0] # Get the first weather condition for today
    weatherConditionsToday = OpenWeatherDataTodayWeather['main'] # Get the main weather condition for today

    # Set the weather icon based on the weather conditions
    if weatherConditionsToday == "Rain":
        weatherConditionsTodayIcon = "/static/images/rain.svg"
    elif weatherConditionsToday == "Clouds":
        weatherConditionsTodayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsToday == "Clear":
        weatherConditionsTodayIcon = "/static/images/sunny.svg"
    elif weatherConditionsToday == "Snow":
        weatherConditionsTodayIcon = "/static/images/snow.svg"
    elif weatherConditionsToday == "Thunderstorm":
        weatherConditionsTodayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsToday == "Wind":
        weatherConditionsTodayIcon = "/static/images/wind.svg"
    elif weatherConditionsToday == "Hail":
        weatherConditionsTodayIcon = "/static/images/hailstones.svg"

    temperatureforecastToday = round(temperatureCelsius1, 0) # round to 0 decimal places
    temperatureforecastToday = int(temperatureforecastToday) # Convert the temperature to an integer
    temperatureforecastToday = str(temperatureforecastToday) + "°C" # Convert the temperature to a string

    pressure = openWeatherDataToday['main'] # Get the pressure for today
    pressure = pressure['pressure'] # Get the pressure value
    pressure = round(pressure, 0) # round to 0 decimal places
    pressure = int(pressure) # Convert the pressure to an integer
    strPressure = str(pressure) + " hPa/mbar" # Convert the pressure to a string

    # Set pressure dial angle based on the pressure value
    if pressure >= 700 and pressure <= 710:
        angle= 4.5
    elif pressure >= 711 and pressure <= 720:
        angle = 9
    elif pressure >= 721 and pressure <= 730:
        angle = 13.5
    elif pressure >= 731 and pressure <= 740:
        angle = 18
    elif pressure >= 741 and pressure <= 750:
        angle = 22.5
    elif pressure >= 751 and pressure <= 760:
        angle = 27
    elif pressure >= 761 and pressure <= 770:
        angle = 31.5
    elif pressure >= 771 and pressure <= 780:
        angle = 36
    elif pressure >= 781 and pressure <= 790:
        angle = 40.5
    elif pressure >= 791 and pressure <= 800:
        angle = 45
    elif pressure >= 801 and pressure <= 810:
        angle = 49.5
    elif pressure >= 811 and pressure <= 820:
        angle = 54
    elif pressure >= 821 and pressure <= 830:
        angle = 58.5
    elif pressure >= 831 and pressure <= 840:
        angle = 63
    elif pressure >= 841 and pressure <= 850:
        angle = 67.5
    elif pressure >= 851 and pressure <= 860:
        angle = 72
    elif pressure >= 861 and pressure <= 870:
        angle = 76.5
    elif pressure >= 871 and pressure <= 880:
        angle = 81
    elif pressure >= 881 and pressure <= 890:
        angle = 85.5
    elif pressure >= 891 and pressure <= 900:
        angle = 90
    elif pressure >= 901 and pressure <= 910:
        angle = 94.5
    elif pressure >= 911 and pressure <= 920:
        angle = 99
    elif pressure >= 921 and pressure <= 930:
        angle = 103.5
    elif pressure >= 931 and pressure <= 940:
        angle = 108
    elif pressure >= 941 and pressure <= 950:
        angle = 112.5
    elif pressure >= 951 and pressure <= 960:
        angle = 117
    elif pressure >= 961 and pressure <= 970:
        angle = 121.5
    elif pressure >= 971 and pressure <= 980:
        angle = 126
    elif pressure >= 981 and pressure <= 990:
        angle = 130.5
    elif pressure >= 991 and pressure <= 1000:
        angle = 135
    elif pressure >= 1001 and pressure <= 1010:
        angle = 139.5
    elif pressure >= 1011 and pressure <= 1020:
        angle = 144
    elif pressure >= 1021 and pressure <= 1030:
        angle = 148.5
    elif pressure >= 1031 and pressure <= 1040:
        angle = 153
    elif pressure >= 1041 and pressure <= 1050:
        angle = 157.5
    elif pressure >= 1051 and pressure <= 1060:
        angle = 162
    elif pressure >= 1061 and pressure <= 1070:
        angle = 166.5
    elif pressure >= 1071 and pressure <= 1080:
        angle = 171
    elif pressure >= 1081 and pressure <= 1090:
        angle = 175.5
    elif pressure >= 1091 and pressure <= 1100:
        angle = 180

    precipitationProbability = openWeatherDataToday['pop'] # Get the precipitation probability for today
    precipitationProbability = precipitationProbability * 100 # Convert the precipitation probability to a percentage
    precipitationProbability = round(precipitationProbability, 0) # round to 0 decimal places
    precipitationProbability = int(precipitationProbability) # Convert the precipitation probability to an integer
    strPrecipitationProbability = str(precipitationProbability) + "%" # Convert the precipitation probability to a string
    print(openWeatherDataToday)
    visibility = openWeatherDataToday['visibility'] # Get the visibility for today
    visibilityKM = visibility / 1000 # Convert the visibility to kilometres
    visibilityKM = round(visibilityKM, 0) # round to 0 decimal places
    visibilityKM = int(visibilityKM) # Convert the visibility to an integer
    strVisibilityKM = str(visibilityKM) + " Kilometres" # Convert the visibility to a string
    visibilityMiles = visibilityKM / 1.60934 # Convert the visibility to miles
    visibilityMiles = round(visibilityMiles, 0) # round to 0 decimal places
    visibilityMiles = int(visibilityMiles) # Convert the visibility to an integer
    strVisibilityMiles = str(visibilityMiles) + " Miles" # Convert the visibility to a string


    # Visibility Description based on the visibility value
    if visibilityKM >= 0 and visibilityKM <= 1:
        visibilityDescription = "Very Poor"
    elif visibilityKM >= 2 and visibilityKM <= 4:
        visibilityDescription = "Poor"
    elif visibilityKM >= 5 and visibilityKM <= 7:
        visibilityDescription = "Moderate"
    elif visibilityKM >= 8 and visibilityKM <= 10:
        visibilityDescription = "Clear"
    elif visibilityKM >= 11 and visibilityKM <= 15:
        visibilityDescription = "Very Clear"
    elif visibilityKM >= 16:
        visibilityDescription = "Perfectly Clear"

    feelsLike = openWeatherDataToday['main'] # Get the feels like temperature for today based on the temperature, wind speed, humidity wether conditions
    feelsLike = feelsLike['feels_like'] # Get the feels like temperature value
    feelsLikeCelcius = (feelsLike - 273.15) # Convert the feels like temperature to Celsius
    feelsLikeFarenheit = (feelsLike - 273.15) * 9/5 + 32 # Convert the feels like temperature to Farenheit
    feelsLikeFarenheit = round(feelsLikeFarenheit, 1) # round to 1 decimal place
    strFeelsLikeFarenheit = str(feelsLikeFarenheit) + "°F"  # Convert the feels like temperature to a string
    feelsLikeCelcius = round(feelsLikeCelcius, 1) # round to 1 decimal place
    strFeelsLikeCelcius = str(feelsLikeCelcius) + "°C" # Convert the feels like temperature to a string

    todayDate = openWeatherDataToday['dt_txt'] # Get the date for today
    todayDate = todayDate.split(" ") # Split the date
    todayDate = todayDate[0] # Get the date
    todayDate = date.fromisoformat(todayDate) # Convert the date to a date object
    todayDate = calendar.day_name[todayDate.weekday()] # Get the day name for the date
    todayDate = str(todayDate) # Convert the day name to a string
    todayDate = todayDate[0:3] # Get the first 3 characters of the day name

    #Tomorrow weather
    openWeatherDataTomorrow = openWeatherData[8] # Get the weather data for tomorrow
    OpenWeatherDataTomorrowWeather = openWeatherDataTomorrow['weather'] # Get the weather conditions for tomorrow
    OpenWeatherDataTomorrowWeather = OpenWeatherDataTomorrowWeather[0]
    weatherConditionsTomorrow = OpenWeatherDataTomorrowWeather['main']

    # Set the weather icon based on the weather conditions
    if weatherConditionsTomorrow == "Rain":
        weatherConditionsTomorrowIcon = "/static/images/rain.svg"
    elif weatherConditionsTomorrow == "Clouds":
        weatherConditionsTomorrowIcon = "/static/images/cloudy.svg"
    elif weatherConditionsTomorrow == "Clear":
        weatherConditionsTomorrowIcon = "/static/images/sunny.svg"
    elif weatherConditionsTomorrow == "Snow":
        weatherConditionsTomorrowIcon = "/static/images/snow.svg"
    elif weatherConditionsTomorrow == "Thunderstorm":
        weatherConditionsTomorrowIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsTomorrow == "Wind":
        weatherConditionsTomorrowIcon = "/static/images/wind.svg"
    elif weatherConditionsTomorrow == "Hail":
        weatherConditionsTomorrowIcon = "/static/images/hailstones.svg"

    temperatureforecastTomorrow = openWeatherDataTomorrow['main'] # Get the temperature forecast for tomorrow
    temperatureforecastTomorrow = temperatureforecastTomorrow['temp'] # Get the temperature value
    temperatureforecastTomorrow = (temperatureforecastTomorrow - 273.15) # Convert the temperature to Celsius
    temperatureforecastTomorrow = round(temperatureforecastTomorrow, 0) # round to 0 decimal places
    temperatureforecastTomorrow = int(temperatureforecastTomorrow) # Convert the temperature to an integer
    temperatureforecastTomorrow = str(temperatureforecastTomorrow) + "°C" # Convert the temperature to a string

    tomorrowDate = openWeatherDataTomorrow['dt_txt'] # Get the date for tomorrow
    tomorrowDate = tomorrowDate.split(" ") # Split the date
    tomorrowDate = tomorrowDate[0] # Get the date
    tomorrowDate = date.fromisoformat(tomorrowDate) # Convert the date to a date object
    tomorrowDate = calendar.day_name[tomorrowDate.weekday()] # Get the day name for the date
    tomorrowDate = str(tomorrowDate) # Convert the day name to a string
    tomorrowDate = tomorrowDate[0:3] # Get the first 3 characters of the day name


    tomorrowWindSpeed = openWeatherDataTomorrow['wind'] # Get the wind speed for tomorrow
    tomorrowWindSpeed = tomorrowWindSpeed['speed'] # Get the wind speed value
    tomorrowWindSpeed = tomorrowWindSpeed / 0.447  # Convert the wind speed to mph
    tomorrowWindSpeed = round(tomorrowWindSpeed, 0) # round to 0 decimal places
    tomorrowWindSpeed = int(tomorrowWindSpeed) # Convert the wind speed to an integer
    tomorrowWindSpeed = str(tomorrowWindSpeed) + "mph" # Convert the wind speed to a string

    tomorrowWindDirection = openWeatherDataTomorrow['wind'] # Get the wind direction for tomorrow
    tomorrowWindDirection = tomorrowWindDirection['deg'] # Get the wind direction value
    # Set the wind direction description based on the wind direction value
    if tomorrowWindDirection >= 0 and tomorrowWindDirection < 22.5 or tomorrowWindDirection >= 337.5 and tomorrowWindDirection <= 360:
        tomorrowWindDirectionDescription = "North"
    elif tomorrowWindDirection >= 22.5 and tomorrowWindDirection < 67.5:
        tomorrowWindDirectionDescription = "North East"
    elif tomorrowWindDirection >= 67.5 and tomorrowWindDirection < 112.5:
        tomorrowWindDirectionDescription = "East"
    elif tomorrowWindDirection >= 112.5 and tomorrowWindDirection < 157.5:
        tomorrowWindDirectionDescription = "South East"
    elif tomorrowWindDirection >= 157.5 and tomorrowWindDirection < 202.5:
        tomorrowWindDirectionDescription = "South"
    elif tomorrowWindDirection >= 202.5 and tomorrowWindDirection < 247.5:
        tomorrowWindDirectionDescription = "South West"
    elif tomorrowWindDirection >= 247.5 and tomorrowWindDirection < 292.5:
        tomorrowWindDirectionDescription = "West"
    elif tomorrowWindDirection >= 292.5 and tomorrowWindDirection < 337.5:
        tomorrowWindDirectionDescription = "North West"


    tomorrowHumidity = openWeatherDataTomorrow['main'] # Get the humidity for tomorrow
    tomorrowHumidity = tomorrowHumidity['humidity']  # Get the humidity value
    tomorrowHumidity = str(tomorrowHumidity) + "%" # Convert the humidity to a string

    precipitationProbabilityTomorrow = openWeatherDataTomorrow['pop'] # Get the precipitation probability for tomorrow
    precipitationProbabilityTomorrow = precipitationProbabilityTomorrow * 100 # Convert the precipitation probability to a percentage
    precipitationProbabilityTomorrow = round(precipitationProbabilityTomorrow, 0) # round to 0 decimal places
    precipitationProbabilityTomorrow = int(precipitationProbabilityTomorrow) # Convert the precipitation probability to an integer
    strPrecipitationProbabilityTomorrow = str(precipitationProbabilityTomorrow) + "%" # Convert the precipitation probability to a string


    # 3 Day Weather - Similar code as Tomorrow Weather
    openWeatherDataThreeDay = openWeatherData[16]
    OpenWeatherDataThreeDayWeather = openWeatherDataThreeDay['weather']
    OpenWeatherDataThreeDayWeather = OpenWeatherDataThreeDayWeather[0]
    weatherConditionsThreeDay = OpenWeatherDataThreeDayWeather['main']

    if weatherConditionsThreeDay == "Rain":
        weatherConditionsThreeDayIcon = "/static/images/rain.svg"
    elif weatherConditionsThreeDay == "Clouds":
        weatherConditionsThreeDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsThreeDay == "Clear":
        weatherConditionsThreeDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsThreeDay == "Snow":
        weatherConditionsThreeDayIcon = "/static/images/snow.svg"
    elif weatherConditionsThreeDay == "Thunderstorm":
        weatherConditionsThreeDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsThreeDay == "Wind":
        weatherConditionsThreeDayIcon = "/static/images/wind.svg"
    elif weatherConditionsThreeDay == "Hail":
        weatherConditionsThreeDayIcon = "/static/images/hailstones.svg"


    temperatureforecastThreeDay = openWeatherDataThreeDay['main']
    temperatureforecastThreeDay = temperatureforecastThreeDay['temp']
    temperatureforecastThreeDay = (temperatureforecastThreeDay - 273.15)
    temperatureforecastThreeDay = round(temperatureforecastThreeDay, 0)
    temperatureforecastThreeDay = int(temperatureforecastThreeDay)
    temperatureforecastThreeDay = str(temperatureforecastThreeDay) + "°C"

    ThreeDayDate = openWeatherDataThreeDay['dt_txt']
    ThreeDayDate = ThreeDayDate.split(" ")
    ThreeDayDate = ThreeDayDate[0]
    ThreeDayDate = date.fromisoformat(ThreeDayDate)
    ThreeDayDate = calendar.day_name[ThreeDayDate.weekday()]
    ThreeDayDate = str(ThreeDayDate)
    ThreeDayDate = ThreeDayDate[0:3]

    ThreeDayWindSpeed = openWeatherDataThreeDay['wind']
    ThreeDayWindSpeed = ThreeDayWindSpeed['speed']
    ThreeDayWindSpeed = ThreeDayWindSpeed / 0.447
    ThreeDayWindSpeed = round(ThreeDayWindSpeed, 0)
    ThreeDayWindSpeed = int(ThreeDayWindSpeed)
    ThreeDayWindSpeed = str(ThreeDayWindSpeed) + "mph"

    ThreeDayWindDirection = openWeatherDataThreeDay['wind']
    ThreeDayWindDirection = ThreeDayWindDirection['deg']
    if ThreeDayWindDirection >= 0 and ThreeDayWindDirection < 22.5 or ThreeDayWindDirection >= 337.5 and ThreeDayWindDirection <= 360:
        ThreeDayWindDirectionDescription = "North"
    elif ThreeDayWindDirection >= 22.5 and ThreeDayWindDirection < 67.5:
        ThreeDayWindDirectionDescription = "North East"
    elif ThreeDayWindDirection >= 67.5 and ThreeDayWindDirection < 112.5:
        ThreeDayWindDirectionDescription = "East"
    elif ThreeDayWindDirection >= 112.5 and ThreeDayWindDirection < 157.5:
        ThreeDayWindDirectionDescription = "South East"
    elif ThreeDayWindDirection >= 157.5 and ThreeDayWindDirection < 202.5:
        ThreeDayWindDirectionDescription = "South"
    elif ThreeDayWindDirection >= 202.5 and ThreeDayWindDirection < 247.5:
        ThreeDayWindDirectionDescription = "South West"
    elif ThreeDayWindDirection >= 247.5 and ThreeDayWindDirection < 292.5:
        ThreeDayWindDirectionDescription = "West"
    elif ThreeDayWindDirection >= 292.5 and ThreeDayWindDirection < 337.5:
        ThreeDayWindDirectionDescription = "North West"


    ThreeDayHumidity = openWeatherDataThreeDay['main']
    ThreeDayHumidity = ThreeDayHumidity['humidity']
    ThreeDayHumidity = str(ThreeDayHumidity) + "%"

    precipitationProbabilityThreeDay = openWeatherDataThreeDay['pop']
    precipitationProbabilityThreeDay = precipitationProbabilityThreeDay * 100
    precipitationProbabilityThreeDay = round(precipitationProbabilityThreeDay, 0)
    precipitationProbabilityThreeDay = int(precipitationProbabilityThreeDay)
    strPrecipitationProbabilityThreeDay = str(precipitationProbabilityThreeDay) + "%"


    # 4 Day Weather - Similar code as 4 Day Weather
    openWeatherDataFourDay = openWeatherData[24]
    OpenWeatherDataFourDayWeather = openWeatherDataFourDay['weather']
    OpenWeatherDataFourDayWeather = OpenWeatherDataFourDayWeather[0]
    weatherConditionsFourDay = OpenWeatherDataFourDayWeather['main']

    if weatherConditionsFourDay == "Rain":
        weatherConditionsFourDayIcon = "/static/images/rain.svg"
    elif weatherConditionsFourDay == "Clouds":
        weatherConditionsFourDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsFourDay == "Clear":
        weatherConditionsFourDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsFourDay == "Snow":
        weatherConditionsFourDayIcon = "/static/images/snow.svg"
    elif weatherConditionsFourDay == "Thunderstorm":
        weatherConditionsFourDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsFourDay == "Wind":
        weatherConditionsFourDayIcon = "/static/images/wind.svg"
    elif weatherConditionsFourDay == "Hail":
        weatherConditionsFourDayIcon = "/static/images/hailstones.svg"

    temperatureforecastFourDay = openWeatherDataFourDay['main']
    temperatureforecastFourDay = temperatureforecastFourDay['temp']
    temperatureforecastFourDay = (temperatureforecastFourDay - 273.15)
    temperatureforecastFourDay = round(temperatureforecastFourDay, 0)
    temperatureforecastFourDay = int(temperatureforecastFourDay)
    temperatureforecastFourDay = str(temperatureforecastFourDay) + "°C"

    FourDayDate = openWeatherDataFourDay['dt_txt']
    FourDayDate = FourDayDate.split(" ")
    FourDayDate = FourDayDate[0]
    FourDayDate = date.fromisoformat(FourDayDate)
    FourDayDate = calendar.day_name[FourDayDate.weekday()]
    FourDayDate = str(FourDayDate)
    FourDayDate = FourDayDate[0:3]

    FourDayWindSpeed = openWeatherDataFourDay['wind']
    FourDayWindSpeed = FourDayWindSpeed['speed']
    FourDayWindSpeed = FourDayWindSpeed / 0.447
    FourDayWindSpeed = round(FourDayWindSpeed, 0)
    FourDayWindSpeed = int(FourDayWindSpeed)
    FourDayWindSpeed = str(FourDayWindSpeed) + "mph"

    FourDayWindDirection = openWeatherDataFourDay['wind']
    FourDayWindDirection = FourDayWindDirection['deg']
    if FourDayWindDirection >= 0 and FourDayWindDirection < 22.5 or FourDayWindDirection >= 337.5 and FourDayWindDirection <= 360:
        FourDayWindDirectionDescription = "North"
    elif FourDayWindDirection >= 22.5 and FourDayWindDirection < 67.5:
        FourDayWindDirectionDescription = "North East"
    elif FourDayWindDirection >= 67.5 and FourDayWindDirection < 112.5:
        FourDayWindDirectionDescription = "East"
    elif FourDayWindDirection >= 112.5 and FourDayWindDirection < 157.5:
        FourDayWindDirectionDescription = "South East"
    elif FourDayWindDirection >= 157.5 and FourDayWindDirection < 202.5:
        FourDayWindDirectionDescription = "South"
    elif FourDayWindDirection >= 202.5 and FourDayWindDirection < 247.5:
        FourDayWindDirectionDescription = "South West"
    elif FourDayWindDirection >= 247.5 and FourDayWindDirection < 292.5:
        FourDayWindDirectionDescription = "West"
    elif FourDayWindDirection >= 292.5 and FourDayWindDirection < 337.5:
        FourDayWindDirectionDescription = "North West"

    FourDayHumidity = openWeatherDataFourDay['main']
    FourDayHumidity = FourDayHumidity['humidity']
    FourDayHumidity = str(FourDayHumidity) + "%"

    precipitationProbabilityFourDay = openWeatherDataFourDay['pop']
    precipitationProbabilityFourDay = precipitationProbabilityFourDay * 100
    precipitationProbabilityFourDay = round(precipitationProbabilityFourDay, 0)
    precipitationProbabilityFourDay = int(precipitationProbabilityFourDay)
    strPrecipitationProbabilityFourDay = str(precipitationProbabilityFourDay) + "%"

    # 5 Day Weather - Similar code as 5 Day Weather
    openWeatherDataFiveDay = openWeatherData[32]
    OpenWeatherDataFiveDayWeather = openWeatherDataFiveDay['weather']
    OpenWeatherDataFiveDayWeather = OpenWeatherDataFiveDayWeather[0]
    weatherConditionsFiveDay = OpenWeatherDataFiveDayWeather['main']

    if weatherConditionsFiveDay == "Rain":
        weatherConditionsFiveDayIcon = "/static/images/rain.svg"
    elif weatherConditionsFiveDay == "Clouds":
        weatherConditionsFiveDayIcon = "/static/images/cloudy.svg"
    elif weatherConditionsFiveDay == "Clear":
        weatherConditionsFiveDayIcon = "/static/images/sunny.svg"
    elif weatherConditionsFiveDay == "Snow":
        weatherConditionsFiveDayIcon = "/static/images/snow.svg"
    elif weatherConditionsFiveDay == "Thunderstorm":
        weatherConditionsFiveDayIcon = "/static/images/thunderstorms.svg"
    elif weatherConditionsFiveDay == "Wind":
        weatherConditionsFiveDayIcon = "/static/images/wind.svg"
    elif weatherConditionsFiveDay == "Hail":
        weatherConditionsFiveDayIcon = "/static/images/hailstones.svg"

    temperatureforecastFiveDay = openWeatherDataFiveDay['main']
    temperatureforecastFiveDay = temperatureforecastFiveDay['temp']
    temperatureforecastFiveDay = (temperatureforecastFiveDay - 273.15)
    temperatureforecastFiveDay = round(temperatureforecastFiveDay, 0)
    temperatureforecastFiveDay = int(temperatureforecastFiveDay)
    temperatureforecastFiveDay = str(temperatureforecastFiveDay) + "°C"

    FiveDayDate = openWeatherDataFiveDay['dt_txt']
    FiveDayDate = FiveDayDate.split(" ")
    FiveDayDate = FiveDayDate[0]
    FiveDayDate = date.fromisoformat(FiveDayDate)
    FiveDayDate = calendar.day_name[FiveDayDate.weekday()]
    FiveDayDate = str(FiveDayDate)
    FiveDayDate = FiveDayDate[0:3]

    FiveDayWindSpeed = openWeatherDataFiveDay['wind']
    FiveDayWindSpeed = FiveDayWindSpeed['speed']
    FiveDayWindSpeed = FiveDayWindSpeed / 0.447
    FiveDayWindSpeed = round(FiveDayWindSpeed, 0)
    FiveDayWindSpeed = int(FiveDayWindSpeed)
    FiveDayWindSpeed = str(FiveDayWindSpeed) + "mph"

    FiveDayWindDirection = openWeatherDataFiveDay['wind']
    FiveDayWindDirection = FiveDayWindDirection['deg']
    if FiveDayWindDirection >= 0 and FiveDayWindDirection < 22.5 or FiveDayWindDirection >= 337.5 and FiveDayWindDirection <= 360:
        FiveDayWindDirectionDescription = "North"
    elif FiveDayWindDirection >= 22.5 and FiveDayWindDirection < 67.5:
        FiveDayWindDirectionDescription = "North East"
    elif FiveDayWindDirection >= 67.5 and FiveDayWindDirection < 112.5:
        FiveDayWindDirectionDescription = "East"
    elif FiveDayWindDirection >= 112.5 and FiveDayWindDirection < 157.5:
        FiveDayWindDirectionDescription = "South East"
    elif FiveDayWindDirection >= 157.5 and FiveDayWindDirection < 202.5:
        FiveDayWindDirectionDescription = "South"
    elif FiveDayWindDirection >= 202.5 and FiveDayWindDirection < 247.5:
        FiveDayWindDirectionDescription = "South West"
    elif FiveDayWindDirection >= 247.5 and FiveDayWindDirection < 292.5:
        FiveDayWindDirectionDescription = "West"
    elif FiveDayWindDirection >= 292.5 and FiveDayWindDirection < 337.5:
        FiveDayWindDirectionDescription = "North West"


    FiveDayHumidity = openWeatherDataFiveDay['main']
    FiveDayHumidity = FiveDayHumidity['humidity']
    FiveDayHumidity = str(FiveDayHumidity) + "%"

    precipitationProbabilityFiveDay = openWeatherDataFiveDay['pop']
    precipitationProbabilityFiveDay = precipitationProbabilityFiveDay * 100
    precipitationProbabilityFiveDay = round(precipitationProbabilityFiveDay, 0)
    precipitationProbabilityFiveDay = int(precipitationProbabilityFiveDay)
    strPrecipitationProbabilityFiveDay = str(precipitationProbabilityFiveDay) + "%"


    # 6 Day Weather - Similar code as 6 Day Weather (not in use in the current version due to technical issues)

    SixDayHumidity = 1
    SixDayWindSpeed = 1
    SixDayWindDirection = 1
    SixDayDate = 1
    SixDayWindDirectionDescription = 1
    strPrecipitationProbabilitySixDay = 1
    temperatureforecastSixDay = 1
    weatherConditionsSixDayIcon = 1


    #Weather API Hourly Forecast
    # Current Weather
    weatherAPI_key = '33d91967a1b04700807201804242711' # Weather API Key
    weatherAPIurl = 'https://api.weatherapi.com/v1/forecast.json?key=' + weatherAPI_key + '&q=IP5 3RE&days=1&aqi=yes&alerts=yes' # Weather API URL
    response = requests.get(weatherAPIurl) # Get the weather API data
    weatherAPIData = response.json() # Convert the weather API data to JSON
    weatherAPIDataCurrent = weatherAPIData['current'] # Get the current weather data
    weatherAPIDataCurrentTemperature = weatherAPIDataCurrent['temp_c'] # Get the current temperature
    weatherAPIDataCurrentTemperature = round(weatherAPIDataCurrentTemperature, 0) # round to 0 decimal places
    weatherAPIDataCurrentTemperature = int(weatherAPIDataCurrentTemperature) # Convert the temperature to an integer
    weatherAPIDataCurrentTemperature = str(weatherAPIDataCurrentTemperature) + "°C" # Convert the temperature to a string
    weatherAPIDataCurrentCondition = weatherAPIDataCurrent['condition'] # Get the current weather condition
    weatherAPIDataCurrentCondition = weatherAPIDataCurrentCondition['text'] # Get the current weather condition text

    regexThunderCurrent = re.findall("Thunder|thunder", weatherAPIDataCurrentCondition) # Find the word Thunder in the current weather condition
    if regexThunderCurrent != []: # If the word Thunder is found
        regexThunderCurrent = regexThunderCurrent[0] # Get the first word Thunder
        regexThunderCurrent = regexThunderCurrent.split() # Split the word Thunder
    regexRainCurrent = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPIDataCurrentCondition) # Find the word Rain in the current weather condition
    if regexRainCurrent != []: # If the word Rain is found
        regexRainCurrent = regexRainCurrent[0] # Get the first word Rain
        regexRainCurrent = regexRainCurrent.split() # Split the word Rain
    regexCloudCurrent = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPIDataCurrentCondition) # Find the word Cloud in the current weather condition
    if regexCloudCurrent != []: # If the word Cloud is found
        regexCloudCurrent = regexCloudCurrent[0] # Get the first word Cloud
        regexCloudCurrent = regexCloudCurrent.split() # Split the word Cloud
    regexClearCurrent = re.findall("Clear|clear|Sun|sun", weatherAPIDataCurrentCondition) # Find the word Clear in the current weather condition
    if regexClearCurrent != []: # If the word Clear is found
        regexClearCurrent = regexClearCurrent[0] # Get the first word Clear
        regexClearCurrent = regexClearCurrent.split() # Split the word Clear
    regexSnowCurrent = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPIDataCurrentCondition) # Find the word Snow in the current weather condition
    if regexSnowCurrent != []: # If the word Snow is found
        regexSnowCurrent = regexSnowCurrent[0] # Get the first word Snow
        regexSnowCurrent = regexSnowCurrent.split() # Split the word Snow
    regexWindCurrent = re.findall("Wind|wind", weatherAPIDataCurrentCondition) # Find the word Wind in the current weather condition
    if regexWindCurrent != []: # If the word Wind is found
        regexWindCurrent = regexWindCurrent[0] # Get the first word Wind
        regexWindCurrent = regexWindCurrent.split() # Split the word Wind
    regexHailCurrent = re.findall("Hail|hail", weatherAPIDataCurrentCondition) # Find the word Hail in the current weather condition
    if regexHailCurrent != []: # If the word Hail is found
        regexHailCurrent = regexHailCurrent[0] # Get the first word Hail
        regexHailCurrent = regexHailCurrent.split() # Split the word Hail
    regexMistCurrent = re.findall("Mist|mist|Fog|fog", weatherAPIDataCurrentCondition) # Find the word Mist in the current weather condition
    if regexMistCurrent != []: # If the word Mist is found
        regexMistCurrent = regexMistCurrent[0] # Get the first word Mist
        regexMistCurrent = regexMistCurrent.split() # Split the word Mist
    else:
        pass


    if regexThunderCurrent == ['Thunder'] or regexThunderCurrent == ['thunder']: # If the word Thunder is found
        weatherAPIDataCurrentConditionIcon = "/static/images/thunderstorms.svg" # Set the weather icon to thunderstorms
    elif regexRainCurrent == ['Rain'] or regexRainCurrent == ['rain'] or regexRainCurrent == ['Shower'] or regexRainCurrent == ['shower'] or regexRainCurrent == ['Drizzle'] or regexRainCurrent == ['drizzle']: # If the word Rain is found
        weatherAPIDataCurrentConditionIcon = "/static/images/rain.svg" # Set the weather icon to rain
    elif regexCloudCurrent == ['Cloud'] or regexCloudCurrent == ['cloud'] or regexCloudCurrent == ['Overcast'] or regexCloudCurrent == ['overcast'] or regexCloudCurrent == ['Cloudy'] or regexCloudCurrent == ['cloudy']: # If the word Cloud is found
        weatherAPIDataCurrentConditionIcon = "/static/images/cloudy.svg" # Set the weather icon to cloudy
    elif regexClearCurrent == ['Clear'] or regexClearCurrent == ['clear'] or regexClearCurrent == ['Sun'] or regexClearCurrent == ['sun']: # If the word Clear is found
        weatherAPIDataCurrentConditionIcon = "/static/images/sunny.svg" # Set the weather icon to sunny
    elif regexSnowCurrent == ['Snow'] or regexSnowCurrent == ['snow'] or regexSnowCurrent == ['Sleet'] or regexSnowCurrent == ['sleet'] or regexSnowCurrent == ['Blizzard'] or regexSnowCurrent == ['blizzard']: # If the word Snow is found
        weatherAPIDataCurrentConditionIcon = "/static/images/snow.svg" # Set the weather icon to snow
    elif regexWindCurrent == ['Wind'] or regexWindCurrent == ['wind']: # If the word Wind is found
        weatherAPIDataCurrentConditionIcon = "/static/images/wind.svg" # Set the weather icon to wind
    elif regexHailCurrent == ['Hail'] or regexHailCurrent == ['hail']: # If the word Hail is found
        weatherAPIDataCurrentConditionIcon = "/static/images/hailstones.svg" # Set the weather icon to hail
    elif regexMistCurrent == ['Mist'] or regexMistCurrent == ['mist'] or regexMistCurrent == ['Fog'] or regexMistCurrent == ['fog']: # If the word Mist is found
        weatherAPIDataCurrentConditionIcon = "/static/images/mist.svg" # Set the weather icon to mist


    #01 Hour Forecast - Similar code as Current Weather
    weatherAPI01HourData = weatherAPIData['forecast']
    weatherAPI01HourData = weatherAPI01HourData['forecastday']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourData = weatherAPI01HourData['hour']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourDataConditionTime = weatherAPI01HourData['time']
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(" ")
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[1]
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(":")
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[0]
    weatherAPI01HourDataTemperature = weatherAPI01HourData['temp_c']
    weatherAPI01HourDataTemperature = round(weatherAPI01HourDataTemperature, 0)
    weatherAPI01HourDataTemperature = int(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataTemperature = str(weatherAPI01HourDataTemperature) + "°C"
    weatherAPI01HourDataCondition = weatherAPI01HourData['condition']
    weatherAPI01HourDataCondition = weatherAPI01HourDataCondition['text']

    regexThunder01Hour = re.findall("Thunder|thunder", weatherAPI01HourDataCondition)
    if regexThunder01Hour != []:
        regexThunder01Hour = regexThunder01Hour[0]
        regexThunder01Hour = regexThunder01Hour.split()
    regexRain01Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI01HourDataCondition)
    if regexRain01Hour != []:
        regexRain01Hour = regexRain01Hour[0]
        regexRain01Hour = regexRain01Hour.split()
    regexCloud01Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI01HourDataCondition)
    if regexCloud01Hour != []:
        regexCloud01Hour = regexCloud01Hour[0]
        regexCloud01Hour = regexCloud01Hour.split()
    regexClear01Hour = re.findall("Clear|clear|Sun|sun", weatherAPI01HourDataCondition)
    if regexClear01Hour != []:
        regexClear01Hour = regexClear01Hour[0]
        regexClear01Hour = regexClear01Hour.split()
    regexSnow01Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI01HourDataCondition)
    if regexSnow01Hour != []:
        regexSnow01Hour = regexSnow01Hour[0]
        regexSnow01Hour = regexSnow01Hour.split()
    regexWind01Hour = re.findall("Wind|wind", weatherAPI01HourDataCondition)
    if regexWind01Hour != []:
        regexWind01Hour = regexWind01Hour[0]
        regexWind01Hour = regexWind01Hour.split()
    regexHail01Hour = re.findall("Hail|hail", weatherAPI01HourDataCondition)
    if regexHail01Hour != []:
        regexHail01Hour = regexHail01Hour[0]
        regexHail01Hour = regexHail01Hour.split()
    regexMist01Hour = re.findall("Mist|mist|Fog|fog", weatherAPI01HourDataCondition)
    if regexMist01Hour != []:
        regexMist01Hour = regexMist01Hour[0]
        regexMist01Hour = regexMist01Hour.split()
    else:
        pass

    if regexThunder01Hour == ['Thunder'] or regexThunder01Hour == ['thunder']:
        weatherAPI01HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain01Hour == ['Rain'] or regexRain01Hour == ['rain'] or regexRain01Hour == [
        'Shower'] or regexRain01Hour == ['shower'] or regexRain01Hour == ['Drizzle'] or regexRain01Hour == [
        'drizzle']:
        weatherAPI01HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud01Hour == ['Cloud'] or regexCloud01Hour == ['cloud'] or regexCloud01Hour == [
        'Overcast'] or regexCloud01Hour == ['overcast'] or regexCloud01Hour == ['Cloudy'] or regexCloud01Hour == [
        'cloudy']:
        weatherAPI01HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear01Hour == ['Clear'] or regexClear01Hour == ['clear'] or regexClear01Hour == [
        'Sun'] or regexClear01Hour == ['sun']:
        weatherAPI01HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow01Hour == ['Snow'] or regexSnow01Hour == ['snow'] or regexSnow01Hour == [
        'Sleet'] or regexSnow01Hour == ['sleet'] or regexSnow01Hour == ['Blizzard'] or regexSnow01Hour == ['blizzard']:
        weatherAPI01HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind01Hour == ['Wind'] or regexWind01Hour == ['wind']:
        weatherAPI01HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail01Hour == ['Hail'] or regexHail01Hour == ['hail']:
        weatherAPI01HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist01Hour == ['Mist'] or regexMist01Hour == ['mist'] or regexMist01Hour == ['Fog'] or regexMist01Hour == ['fog']:
        weatherAPI01HourDataConditionIcon = "/static/images/mist.svg"


    #02 Hour Forecast - Similar code as 01 Hour Forecast
    weatherAPI02HourData = weatherAPIData['forecast']
    weatherAPI02HourData = weatherAPI02HourData['forecastday']
    weatherAPI02HourData = weatherAPI02HourData[0]
    weatherAPI02HourData = weatherAPI02HourData['hour']
    weatherAPI02HourData = weatherAPI02HourData[1]
    weatherAPI02HourDataConditionTime = weatherAPI02HourData['time']
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime.split(" ")
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime[1]
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime.split(":")
    weatherAPI02HourDataConditionTime = weatherAPI02HourDataConditionTime[0]
    weatherAPI02HourDataTemperature = weatherAPI02HourData['temp_c']
    weatherAPI02HourDataTemperature = round(weatherAPI02HourDataTemperature, 0)
    weatherAPI02HourDataTemperature = int(weatherAPI02HourDataTemperature)
    weatherAPI02HourDataTemperature = str(weatherAPI02HourDataTemperature) + "°C"
    weatherAPI02HourDataCondition = weatherAPI02HourData['condition']
    weatherAPI02HourDataCondition = weatherAPI02HourDataCondition['text']
    print(weatherAPI02HourDataCondition)

    regexThunder02Hour = re.findall("Thunder|thunder", weatherAPI02HourDataCondition)
    if regexThunder02Hour != []:
        regexThunder02Hour = regexThunder02Hour[0]
        regexThunder02Hour = regexThunder02Hour.split()
    regexRain02Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI02HourDataCondition)
    if regexRain02Hour != []:
        regexRain02Hour = regexRain02Hour[0]
        regexRain02Hour = regexRain02Hour.split()
    regexCloud02Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI02HourDataCondition)
    if regexCloud02Hour != []:
        regexCloud02Hour = regexCloud02Hour[0]
        regexCloud02Hour = regexCloud02Hour.split()
    regexClear02Hour = re.findall("Clear|clear|Sun|sun", weatherAPI02HourDataCondition)
    if regexClear02Hour != []:
        regexClear02Hour = regexClear02Hour[0]
        regexClear02Hour = regexClear02Hour.split()
    regexSnow02Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI02HourDataCondition)
    if regexSnow02Hour != []:
        regexSnow02Hour = regexSnow02Hour[0]
        regexSnow02Hour = regexSnow02Hour.split()
    regexWind02Hour = re.findall("Wind|wind", weatherAPI02HourDataCondition)
    if regexWind02Hour != []:
        regexWind02Hour = regexWind02Hour[0]
        regexWind02Hour = regexWind02Hour.split()
    regexHail02Hour = re.findall("Hail|hail", weatherAPI02HourDataCondition)
    if regexHail02Hour != []:
        regexHail02Hour = regexHail02Hour[0]
        regexHail02Hour = regexHail02Hour.split()
    regexMist02Hour = re.findall("Mist|mist|Fog|fog", weatherAPI02HourDataCondition)
    if regexMist02Hour != []:
        regexMist02Hour = regexMist02Hour[0]
        regexMist02Hour = regexMist02Hour.split()

    if regexThunder02Hour == ['Thunder'] or regexThunder02Hour == ['thunder']:
        weatherAPI02HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain02Hour == ['Rain'] or regexRain02Hour == ['rain'] or regexRain02Hour == [
        'Shower'] or regexRain02Hour == ['shower'] or regexRain02Hour == ['Drizzle'] or regexRain02Hour == [
        'drizzle']:
        weatherAPI02HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud02Hour == ['Cloud'] or regexCloud02Hour == ['cloud'] or regexCloud02Hour == [
        'Overcast'] or regexCloud02Hour == ['overcast'] or regexCloud02Hour == ['Cloudy'] or regexCloud02Hour == [
        'cloudy']:
        weatherAPI02HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear02Hour == ['Clear'] or regexClear02Hour == ['clear'] or regexClear02Hour == [
        'Sun'] or regexClear02Hour == ['sun']:
        weatherAPI02HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow02Hour == ['Snow'] or regexSnow02Hour == ['snow'] or regexSnow02Hour == [
        'Sleet'] or regexSnow02Hour == ['sleet'] or regexSnow02Hour == ['Blizzard'] or regexSnow02Hour == ['blizzard']:
        weatherAPI02HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind02Hour == ['Wind'] or regexWind02Hour == ['wind']:
        weatherAPI02HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail02Hour == ['Hail'] or regexHail02Hour == ['hail']:
        weatherAPI02HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist02Hour == ['Mist'] or regexMist02Hour == ['mist'] or regexMist02Hour == ['Fog'] or regexMist02Hour == ['fog']:
        weatherAPI02HourDataConditionIcon = "/static/images/mist.svg"


    #03 Hour Forecast
    weatherAPI03HourData = weatherAPIData['forecast']
    weatherAPI03HourData = weatherAPI03HourData['forecastday']
    weatherAPI03HourData = weatherAPI03HourData[0]
    weatherAPI03HourData = weatherAPI03HourData['hour']
    weatherAPI03HourData = weatherAPI03HourData[2]
    weatherAPI03HourDataConditionTime = weatherAPI03HourData['time']
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime.split(" ")
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime[1]
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime.split(":")
    weatherAPI03HourDataConditionTime = weatherAPI03HourDataConditionTime[0]
    weatherAPI03HourDataTemperature = weatherAPI03HourData['temp_c']
    weatherAPI03HourDataTemperature = round(weatherAPI03HourDataTemperature, 0)
    weatherAPI03HourDataTemperature = int(weatherAPI03HourDataTemperature)
    weatherAPI03HourDataTemperature = str(weatherAPI03HourDataTemperature) + "°C"
    weatherAPI03HourDataCondition = weatherAPI03HourData['condition']
    weatherAPI03HourDataCondition = weatherAPI03HourDataCondition['text']

    regexThunder03Hour = re.findall("Thunder|thunder", weatherAPI03HourDataCondition)
    if regexThunder03Hour != []:
        regexThunder03Hour = regexThunder03Hour[0]
        regexThunder03Hour = regexThunder03Hour.split()
    regexRain03Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI03HourDataCondition)
    if regexRain03Hour != []:
        regexRain03Hour = regexRain03Hour[0]
        regexRain03Hour = regexRain03Hour.split()
    regexCloud03Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI03HourDataCondition)
    if regexCloud03Hour != []:
        regexCloud03Hour = regexCloud03Hour[0]
        regexCloud03Hour = regexCloud03Hour.split()
    regexClear03Hour = re.findall("Clear|clear|Sun|sun", weatherAPI03HourDataCondition)
    if regexClear03Hour != []:
        regexClear03Hour = regexClear03Hour[0]
        regexClear03Hour = regexClear03Hour.split()
    regexSnow03Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI03HourDataCondition)
    if regexSnow03Hour != []:
        regexSnow03Hour = regexSnow03Hour[0]
        regexSnow03Hour = regexSnow03Hour.split()
    regexWind03Hour = re.findall("Wind|wind", weatherAPI03HourDataCondition)
    if regexWind03Hour != []:
        regexWind03Hour = regexWind03Hour[0]
        regexWind03Hour = regexWind03Hour.split()
    regexHail03Hour = re.findall("Hail|hail", weatherAPI03HourDataCondition)
    if regexHail03Hour != []:
        regexHail03Hour = regexHail03Hour[0]
        regexHail03Hour = regexHail03Hour.split()
    regexMist03Hour = re.findall("Mist|mist|Fog|fog", weatherAPI03HourDataCondition)
    if regexMist03Hour != []:
        regexMist03Hour = regexMist03Hour[0]
        regexMist03Hour = regexMist03Hour.split()

    if regexThunder03Hour == ['Thunder'] or regexThunder03Hour == ['thunder']:
        weatherAPI03HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain03Hour == ['Rain'] or regexRain03Hour == ['rain'] or regexRain03Hour == [
        'Shower'] or regexRain03Hour == ['shower'] or regexRain03Hour == ['Drizzle'] or regexRain03Hour == [
        'drizzle']:
        weatherAPI03HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud03Hour == ['Cloud'] or regexCloud03Hour == ['cloud'] or regexCloud03Hour == [
        'Overcast'] or regexCloud03Hour == ['overcast'] or regexCloud03Hour == ['Cloudy'] or regexCloud03Hour == [
        'cloudy']:
        weatherAPI03HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear03Hour == ['Clear'] or regexClear03Hour == ['clear'] or regexClear03Hour == [
        'Sun'] or regexClear03Hour == ['sun']:
        weatherAPI03HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow03Hour == ['Snow'] or regexSnow03Hour == ['snow'] or regexSnow03Hour == [
        'Sleet'] or regexSnow03Hour == ['sleet'] or regexSnow03Hour == ['Blizzard'] or regexSnow03Hour == ['blizzard']:
        weatherAPI03HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind03Hour == ['Wind'] or regexWind03Hour == ['wind']:
        weatherAPI03HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail03Hour == ['Hail'] or regexHail03Hour == ['hail']:
        weatherAPI03HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist03Hour == ['Mist'] or regexMist03Hour == ['mist'] or regexMist03Hour == ['Fog'] or regexMist03Hour == ['fog']:
        weatherAPI03HourDataConditionIcon = "/static/images/mist.svg"


    #04 Hour Forecast - Similar code as 03 Hour Forecast
    weatherAPI04HourData = weatherAPIData['forecast']
    weatherAPI04HourData = weatherAPI04HourData['forecastday']
    weatherAPI04HourData = weatherAPI04HourData[0]
    weatherAPI04HourData = weatherAPI04HourData['hour']
    weatherAPI04HourData = weatherAPI04HourData[3]
    weatherAPI04HourDataConditionTime = weatherAPI04HourData['time']
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime.split(" ")
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime[1]
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime.split(":")
    weatherAPI04HourDataConditionTime = weatherAPI04HourDataConditionTime[0]
    weatherAPI04HourDataTemperature = weatherAPI04HourData['temp_c']
    weatherAPI04HourDataTemperature = round(weatherAPI04HourDataTemperature, 0)
    weatherAPI04HourDataTemperature = int(weatherAPI04HourDataTemperature)
    weatherAPI04HourDataTemperature = str(weatherAPI04HourDataTemperature) + "°C"
    weatherAPI04HourDataCondition = weatherAPI04HourData['condition']
    weatherAPI04HourDataCondition = weatherAPI04HourDataCondition['text']

    regexThunder04Hour = re.findall("Thunder|thunder", weatherAPI04HourDataCondition)
    if regexThunder04Hour != []:
        regexThunder04Hour = regexThunder04Hour[0]
        regexThunder04Hour = regexThunder04Hour.split()
    regexRain04Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI04HourDataCondition)
    if regexRain04Hour != []:
        regexRain04Hour = regexRain04Hour[0]
        regexRain04Hour = regexRain04Hour.split()
    regexCloud04Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI04HourDataCondition)
    if regexCloud04Hour != []:
        regexCloud04Hour = regexCloud04Hour[0]
        regexCloud04Hour = regexCloud04Hour.split()
    regexClear04Hour = re.findall("Clear|clear|Sun|sun", weatherAPI04HourDataCondition)
    if regexClear04Hour != []:
        regexClear04Hour = regexClear04Hour[0]
        regexClear04Hour = regexClear04Hour.split()
    regexSnow04Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI04HourDataCondition)
    if regexSnow04Hour != []:
        regexSnow04Hour = regexSnow04Hour[0]
        regexSnow04Hour = regexSnow04Hour.split()
    regexWind04Hour = re.findall("Wind|wind", weatherAPI04HourDataCondition)
    if regexWind04Hour != []:
        regexWind04Hour = regexWind04Hour[0]
        regexWind04Hour = regexWind04Hour.split()
    regexHail04Hour = re.findall("Hail|hail", weatherAPI04HourDataCondition)
    if regexHail04Hour != []:
        regexHail04Hour = regexHail04Hour[0]
        regexHail04Hour = regexHail04Hour.split()
    regexMist04Hour = re.findall("Mist|mist|Fog|fog", weatherAPI04HourDataCondition)
    if regexMist04Hour != []:
        regexMist04Hour = regexMist04Hour[0]
        regexMist04Hour = regexMist04Hour.split()

    if regexThunder04Hour == ['Thunder'] or regexThunder04Hour == ['thunder']:
        weatherAPI04HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain04Hour == ['Rain'] or regexRain04Hour == ['rain'] or regexRain04Hour == [
        'Shower'] or regexRain04Hour == ['shower'] or regexRain04Hour == ['Drizzle'] or regexRain04Hour == [
        'drizzle']:
        weatherAPI04HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud04Hour == ['Cloud'] or regexCloud04Hour == ['cloud'] or regexCloud04Hour == [
        'Overcast'] or regexCloud04Hour == ['overcast'] or regexCloud04Hour == ['Cloudy'] or regexCloud04Hour == [
        'cloudy']:
        weatherAPI04HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear04Hour == ['Clear'] or regexClear04Hour == ['clear'] or regexClear04Hour == [
        'Sun'] or regexClear04Hour == ['sun']:
        weatherAPI04HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow04Hour == ['Snow'] or regexSnow04Hour == ['snow'] or regexSnow04Hour == [
        'Sleet'] or regexSnow04Hour == ['sleet'] or regexSnow04Hour == ['Blizzard'] or regexSnow04Hour == ['blizzard']:
        weatherAPI04HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind04Hour == ['Wind'] or regexWind04Hour == ['wind']:
        weatherAPI04HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail04Hour == ['Hail'] or regexHail04Hour == ['hail']:
        weatherAPI04HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist04Hour == ['Mist'] or regexMist04Hour == ['mist'] or regexMist04Hour == ['Fog'] or regexMist04Hour == ['fog']:
        weatherAPI04HourDataConditionIcon = "/static/images/mist.svg"


    #05 Hour Forecast - Similar code as 04 Hour Forecast
    weatherAPI05HourData = weatherAPIData['forecast']
    weatherAPI05HourData = weatherAPI05HourData['forecastday']
    weatherAPI05HourData = weatherAPI05HourData[0]
    weatherAPI05HourData = weatherAPI05HourData['hour']
    weatherAPI05HourData = weatherAPI05HourData[4]
    weatherAPI05HourDataConditionTime = weatherAPI05HourData['time']
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime.split(" ")
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime[1]
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime.split(":")
    weatherAPI05HourDataConditionTime = weatherAPI05HourDataConditionTime[0]
    weatherAPI05HourDataTemperature = weatherAPI05HourData['temp_c']
    weatherAPI05HourDataTemperature = round(weatherAPI05HourDataTemperature, 0)
    weatherAPI05HourDataTemperature = int(weatherAPI05HourDataTemperature)
    weatherAPI05HourDataTemperature = str(weatherAPI05HourDataTemperature) + "°C"
    weatherAPI05HourDataCondition = weatherAPI05HourData['condition']
    weatherAPI05HourDataCondition = weatherAPI05HourDataCondition['text']

    regexThunder05Hour = re.findall("Thunder|thunder", weatherAPI05HourDataCondition)
    if regexThunder05Hour != []:
        regexThunder05Hour = regexThunder05Hour[0]
        regexThunder05Hour = regexThunder05Hour.split()
    regexRain05Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI05HourDataCondition)
    if regexRain05Hour != []:
        regexRain05Hour = regexRain05Hour[0]
        regexRain05Hour = regexRain05Hour.split()
    regexCloud05Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI05HourDataCondition)
    if regexCloud05Hour != []:
        regexCloud05Hour = regexCloud05Hour[0]
        regexCloud05Hour = regexCloud05Hour.split()
    regexClear05Hour = re.findall("Clear|clear|Sun|sun", weatherAPI05HourDataCondition)
    if regexClear05Hour != []:
        regexClear05Hour = regexClear05Hour[0]
        regexClear05Hour = regexClear05Hour.split()
    regexSnow05Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI05HourDataCondition)
    if regexSnow05Hour != []:
        regexSnow05Hour = regexSnow05Hour[0]
        regexSnow05Hour = regexSnow05Hour.split()
    regexWind05Hour = re.findall("Wind|wind", weatherAPI05HourDataCondition)
    if regexWind05Hour != []:
        regexWind05Hour = regexWind05Hour[0]
        regexWind05Hour = regexWind05Hour.split()
    regexHail05Hour = re.findall("Hail|hail", weatherAPI05HourDataCondition)
    if regexHail05Hour != []:
        regexHail05Hour = regexHail05Hour[0]
        regexHail05Hour = regexHail05Hour.split()
    regexMist05Hour = re.findall("Mist|mist|Fog|fog", weatherAPI05HourDataCondition)
    if regexMist05Hour != []:
        regexMist05Hour = regexMist05Hour[0]
        regexMist05Hour = regexMist05Hour.split()

    if regexThunder05Hour == ['Thunder'] or regexThunder05Hour == ['thunder']:
        weatherAPI05HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain05Hour == ['Rain'] or regexRain05Hour == ['rain'] or regexRain05Hour == [
        'Shower'] or regexRain05Hour == ['shower'] or regexRain05Hour == ['Drizzle'] or regexRain05Hour == [
        'drizzle']:
        weatherAPI05HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud05Hour == ['Cloud'] or regexCloud05Hour == ['cloud'] or regexCloud05Hour == [
        'Overcast'] or regexCloud05Hour == ['overcast'] or regexCloud05Hour == ['Cloudy'] or regexCloud05Hour == [
        'cloudy']:
        weatherAPI05HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear05Hour == ['Clear'] or regexClear05Hour == ['clear'] or regexClear05Hour == [
        'Sun'] or regexClear05Hour == ['sun']:
        weatherAPI05HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow05Hour == ['Snow'] or regexSnow05Hour == ['snow'] or regexSnow05Hour == [
        'Sleet'] or regexSnow05Hour == ['sleet'] or regexSnow05Hour == ['Blizzard'] or regexSnow05Hour == ['blizzard']:
        weatherAPI05HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind05Hour == ['Wind'] or regexWind05Hour == ['wind']:
        weatherAPI05HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail05Hour == ['Hail'] or regexHail05Hour == ['hail']:
        weatherAPI05HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist05Hour == ['Mist'] or regexMist05Hour == ['mist'] or regexMist05Hour == ['Fog'] or regexMist05Hour == ['fog']:
        weatherAPI05HourDataConditionIcon = "/static/images/mist.svg"

    #06 Hour Forecast - Similar code as 05 Hour Forecast
    weatherAPI06HourData = weatherAPIData['forecast']
    weatherAPI06HourData = weatherAPI06HourData['forecastday']
    weatherAPI06HourData = weatherAPI06HourData[0]
    weatherAPI06HourData = weatherAPI06HourData['hour']
    weatherAPI06HourData = weatherAPI06HourData[5]
    weatherAPI06HourDataConditionTime = weatherAPI06HourData['time']
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime.split(" ")
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime[1]
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime.split(":")
    weatherAPI06HourDataConditionTime = weatherAPI06HourDataConditionTime[0]
    weatherAPI06HourDataTemperature = weatherAPI06HourData['temp_c']
    weatherAPI06HourDataTemperature = round(weatherAPI06HourDataTemperature, 0)
    weatherAPI06HourDataTemperature = int(weatherAPI06HourDataTemperature)
    weatherAPI06HourDataTemperature = str(weatherAPI06HourDataTemperature) + "°C"
    weatherAPI06HourDataCondition = weatherAPI06HourData['condition']
    weatherAPI06HourDataCondition = weatherAPI06HourDataCondition['text']

    regexThunder06Hour = re.findall("Thunder|thunder", weatherAPI06HourDataCondition)
    if regexThunder06Hour != []:
        regexThunder06Hour = regexThunder06Hour[0]
        regexThunder06Hour = regexThunder06Hour.split()
    regexRain06Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI06HourDataCondition)
    if regexRain06Hour != []:
        regexRain06Hour = regexRain06Hour[0]
        regexRain06Hour = regexRain06Hour.split()
    regexCloud06Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI06HourDataCondition)
    if regexCloud06Hour != []:
        regexCloud06Hour = regexCloud06Hour[0]
        regexCloud06Hour = regexCloud06Hour.split()
    regexClear06Hour = re.findall("Clear|clear|Sun|sun", weatherAPI06HourDataCondition)
    if regexClear06Hour != []:
        regexClear06Hour = regexClear06Hour[0]
        regexClear06Hour = regexClear06Hour.split()
    regexSnow06Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI06HourDataCondition)
    if regexSnow06Hour != []:
        regexSnow06Hour = regexSnow06Hour[0]
        regexSnow06Hour = regexSnow06Hour.split()
    regexWind06Hour = re.findall("Wind|wind", weatherAPI06HourDataCondition)
    if regexWind06Hour != []:
        regexWind06Hour = regexWind06Hour[0]
        regexWind06Hour = regexWind06Hour.split()
    regexHail06Hour = re.findall("Hail|hail", weatherAPI06HourDataCondition)
    if regexHail06Hour != []:
        regexHail06Hour = regexHail06Hour[0]
        regexHail06Hour = regexHail06Hour.split()
    regexMist06Hour = re.findall("Mist|mist|Fog|fog", weatherAPI06HourDataCondition)
    if regexMist06Hour != []:
        regexMist06Hour = regexMist06Hour[0]
        regexMist06Hour = regexMist06Hour.split()

    if regexThunder06Hour == ['Thunder'] or regexThunder06Hour == ['thunder']:
        weatherAPI06HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain06Hour == ['Rain'] or regexRain06Hour == ['rain'] or regexRain06Hour == [
        'Shower'] or regexRain06Hour == ['shower'] or regexRain06Hour == ['Drizzle'] or regexRain06Hour == [
        'drizzle']:
        weatherAPI06HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud06Hour == ['Cloud'] or regexCloud06Hour == ['cloud'] or regexCloud06Hour == [
        'Overcast'] or regexCloud06Hour == ['overcast'] or regexCloud06Hour == ['Cloudy'] or regexCloud06Hour == [
        'cloudy']:
        weatherAPI06HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear06Hour == ['Clear'] or regexClear06Hour == ['clear'] or regexClear06Hour == [
        'Sun'] or regexClear06Hour == ['sun']:
        weatherAPI06HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow06Hour == ['Snow'] or regexSnow06Hour == ['snow'] or regexSnow06Hour == [
        'Sleet'] or regexSnow06Hour == ['sleet'] or regexSnow06Hour == ['Blizzard'] or regexSnow06Hour == ['blizzard']:
        weatherAPI06HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind06Hour == ['Wind'] or regexWind06Hour == ['wind']:
        weatherAPI06HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail06Hour == ['Hail'] or regexHail06Hour == ['hail']:
        weatherAPI06HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist06Hour == ['Mist'] or regexMist06Hour == ['mist'] or regexMist06Hour == ['Fog'] or regexMist06Hour == ['fog']:
        weatherAPI06HourDataConditionIcon = "/static/images/mist.svg"


    #07 Hour Forecast - Similar code as 06 Hour Forecast
    weatherAPI07HourData = weatherAPIData['forecast']
    weatherAPI07HourData = weatherAPI07HourData['forecastday']
    weatherAPI07HourData = weatherAPI07HourData[0]
    weatherAPI07HourData = weatherAPI07HourData['hour']
    weatherAPI07HourData = weatherAPI07HourData[6]
    weatherAPI07HourDataConditionTime = weatherAPI07HourData['time']
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime.split(" ")
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime[1]
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime.split(":")
    weatherAPI07HourDataConditionTime = weatherAPI07HourDataConditionTime[0]
    weatherAPI07HourDataTemperature = weatherAPI07HourData['temp_c']
    weatherAPI07HourDataTemperature = round(weatherAPI07HourDataTemperature, 0)
    weatherAPI07HourDataTemperature = int(weatherAPI07HourDataTemperature)
    weatherAPI07HourDataTemperature = str(weatherAPI07HourDataTemperature) + "°C"
    weatherAPI07HourDataCondition = weatherAPI07HourData['condition']
    weatherAPI07HourDataCondition = weatherAPI07HourDataCondition['text']

    regexThunder07Hour = re.findall("Thunder|thunder", weatherAPI07HourDataCondition)
    if regexThunder07Hour != []:
        regexThunder07Hour = regexThunder07Hour[0]
        regexThunder07Hour = regexThunder07Hour.split()
    regexRain07Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI07HourDataCondition)
    if regexRain07Hour != []:
        regexRain07Hour = regexRain07Hour[0]
        regexRain07Hour = regexRain07Hour.split()
    regexCloud07Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI07HourDataCondition)
    if regexCloud07Hour != []:
        regexCloud07Hour = regexCloud07Hour[0]
        regexCloud07Hour = regexCloud07Hour.split()
    regexClear07Hour = re.findall("Clear|clear|Sun|sun", weatherAPI07HourDataCondition)
    if regexClear07Hour != []:
        regexClear07Hour = regexClear07Hour[0]
        regexClear07Hour = regexClear07Hour.split()
    regexSnow07Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI07HourDataCondition)
    if regexSnow07Hour != []:
        regexSnow07Hour = regexSnow07Hour[0]
        regexSnow07Hour = regexSnow07Hour.split()
    regexWind07Hour = re.findall("Wind|wind", weatherAPI07HourDataCondition)
    if regexWind07Hour != []:
        regexWind07Hour = regexWind07Hour[0]
        regexWind07Hour = regexWind07Hour.split()
    regexHail07Hour = re.findall("Hail|hail", weatherAPI07HourDataCondition)
    if regexHail07Hour != []:
        regexHail07Hour = regexHail07Hour[0]
        regexHail07Hour = regexHail07Hour.split()
    regexMist07Hour = re.findall("Mist|mist|Fog|fog", weatherAPI07HourDataCondition)
    if regexMist07Hour != []:
        regexMist07Hour = regexMist07Hour[0]
        regexMist07Hour = regexMist07Hour.split()

    if regexThunder07Hour == ['Thunder'] or regexThunder07Hour == ['thunder']:
        weatherAPI07HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain07Hour == ['Rain'] or regexRain07Hour == ['rain'] or regexRain07Hour == [
        'Shower'] or regexRain07Hour == ['shower'] or regexRain07Hour == ['Drizzle'] or regexRain07Hour == [
        'drizzle']:
        weatherAPI07HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud07Hour == ['Cloud'] or regexCloud07Hour == ['cloud'] or regexCloud07Hour == [
        'Overcast'] or regexCloud07Hour == ['overcast'] or regexCloud07Hour == ['Cloudy'] or regexCloud07Hour == [
        'cloudy']:
        weatherAPI07HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear07Hour == ['Clear'] or regexClear07Hour == ['clear'] or regexClear07Hour == [
        'Sun'] or regexClear07Hour == ['sun']:
        weatherAPI07HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow07Hour == ['Snow'] or regexSnow07Hour == ['snow'] or regexSnow07Hour == [
        'Sleet'] or regexSnow07Hour == ['sleet'] or regexSnow07Hour == ['Blizzard'] or regexSnow07Hour == ['blizzard']:
        weatherAPI07HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind07Hour == ['Wind'] or regexWind07Hour == ['wind']:
        weatherAPI07HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail07Hour == ['Hail'] or regexHail07Hour == ['hail']:
        weatherAPI07HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist07Hour == ['Mist'] or regexMist07Hour == ['mist'] or regexMist07Hour == ['Fog'] or regexMist07Hour == ['fog']:
        weatherAPI07HourDataConditionIcon = "/static/images/mist.svg"


    #08 Hour Forecast - Similar code as 07 Hour Forecast
    weatherAPI08HourData = weatherAPIData['forecast']
    weatherAPI08HourData = weatherAPI08HourData['forecastday']
    weatherAPI08HourData = weatherAPI08HourData[0]
    weatherAPI08HourData = weatherAPI08HourData['hour']
    weatherAPI08HourData = weatherAPI08HourData[7]
    weatherAPI08HourDataConditionTime = weatherAPI08HourData['time']
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime.split(" ")
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime[1]
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime.split(":")
    weatherAPI08HourDataConditionTime = weatherAPI08HourDataConditionTime[0]
    weatherAPI08HourDataTemperature = weatherAPI08HourData['temp_c']
    weatherAPI08HourDataTemperature = round(weatherAPI08HourDataTemperature, 0)
    weatherAPI08HourDataTemperature = int(weatherAPI08HourDataTemperature)
    weatherAPI08HourDataTemperature = str(weatherAPI08HourDataTemperature) + "°C"
    weatherAPI08HourDataCondition = weatherAPI08HourData['condition']
    weatherAPI08HourDataCondition = weatherAPI08HourDataCondition['text']

    regexThunder08Hour = re.findall("Thunder|thunder", weatherAPI08HourDataCondition)
    if regexThunder08Hour != []:
        regexThunder08Hour = regexThunder08Hour[0]
        regexThunder08Hour = regexThunder08Hour.split()
    regexRain08Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI08HourDataCondition)
    if regexRain08Hour != []:
        regexRain08Hour = regexRain08Hour[0]
        regexRain08Hour = regexRain08Hour.split()
    regexCloud08Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI08HourDataCondition)
    if regexCloud08Hour != []:
        regexCloud08Hour = regexCloud08Hour[0]
        regexCloud08Hour = regexCloud08Hour.split()
    regexClear08Hour = re.findall("Clear|clear|Sun|sun", weatherAPI08HourDataCondition)
    if regexClear08Hour != []:
        regexClear08Hour = regexClear08Hour[0]
        regexClear08Hour = regexClear08Hour.split()
    regexSnow08Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI08HourDataCondition)
    if regexSnow08Hour != []:
        regexSnow08Hour = regexSnow08Hour[0]
        regexSnow08Hour = regexSnow08Hour.split()
    regexWind08Hour = re.findall("Wind|wind", weatherAPI08HourDataCondition)
    if regexWind08Hour != []:
        regexWind08Hour = regexWind08Hour[0]
        regexWind08Hour = regexWind08Hour.split()
    regexHail08Hour = re.findall("Hail|hail", weatherAPI08HourDataCondition)
    if regexHail08Hour != []:
        regexHail08Hour = regexHail08Hour[0]
        regexHail08Hour = regexHail08Hour.split()
    regexMist08Hour = re.findall("Mist|mist|Fog|fog", weatherAPI08HourDataCondition)
    if regexMist08Hour != []:
        regexMist08Hour = regexMist08Hour[0]
        regexMist08Hour = regexMist08Hour.split()

    if regexThunder08Hour == ['Thunder'] or regexThunder08Hour == ['thunder']:
        weatherAPI08HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain08Hour == ['Rain'] or regexRain08Hour == ['rain'] or regexRain08Hour == [
        'Shower'] or regexRain08Hour == ['shower'] or regexRain08Hour == ['Drizzle'] or regexRain08Hour == [
        'drizzle']:
        weatherAPI08HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud08Hour == ['Cloud'] or regexCloud08Hour == ['cloud'] or regexCloud08Hour == [
        'Overcast'] or regexCloud08Hour == ['overcast'] or regexCloud08Hour == ['Cloudy'] or regexCloud08Hour == [
        'cloudy']:
        weatherAPI08HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear08Hour == ['Clear'] or regexClear08Hour == ['clear'] or regexClear08Hour == [
        'Sun'] or regexClear08Hour == ['sun']:
        weatherAPI08HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow08Hour == ['Snow'] or regexSnow08Hour == ['snow'] or regexSnow08Hour == [
        'Sleet'] or regexSnow08Hour == ['sleet'] or regexSnow08Hour == ['Blizzard'] or regexSnow08Hour == ['blizzard']:
        weatherAPI08HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind08Hour == ['Wind'] or regexWind08Hour == ['wind']:
        weatherAPI08HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail08Hour == ['Hail'] or regexHail08Hour == ['hail']:
        weatherAPI08HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist08Hour == ['Mist'] or regexMist08Hour == ['mist'] or regexMist08Hour == ['Fog'] or regexMist08Hour == ['fog']:
        weatherAPI08HourDataConditionIcon = "/static/images/mist.svg"

    #09 Hour Forecast - Similar code as 08 Hour Forecast
    weatherAPI09HourData = weatherAPIData['forecast']
    weatherAPI09HourData = weatherAPI09HourData['forecastday']
    weatherAPI09HourData = weatherAPI09HourData[0]
    weatherAPI09HourData = weatherAPI09HourData['hour']
    weatherAPI09HourData = weatherAPI09HourData[8]
    weatherAPI09HourDataConditionTime = weatherAPI09HourData['time']
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime.split(" ")
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime[1]
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime.split(":")
    weatherAPI09HourDataConditionTime = weatherAPI09HourDataConditionTime[0]
    weatherAPI09HourDataTemperature = weatherAPI09HourData['temp_c']
    weatherAPI09HourDataTemperature = round(weatherAPI09HourDataTemperature, 0)
    weatherAPI09HourDataTemperature = int(weatherAPI09HourDataTemperature)
    weatherAPI09HourDataTemperature = str(weatherAPI09HourDataTemperature) + "°C"
    weatherAPI09HourDataCondition = weatherAPI09HourData['condition']
    weatherAPI09HourDataCondition = weatherAPI09HourDataCondition['text']

    regexThunder09Hour = re.findall("Thunder|thunder", weatherAPI09HourDataCondition)
    if regexThunder09Hour != []:
        regexThunder09Hour = regexThunder09Hour[0]
        regexThunder09Hour = regexThunder09Hour.split()
    regexRain09Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI09HourDataCondition)
    if regexRain09Hour != []:
        regexRain09Hour = regexRain09Hour[0]
        regexRain09Hour = regexRain09Hour.split()
    regexCloud09Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI09HourDataCondition)
    if regexCloud09Hour != []:
        regexCloud09Hour = regexCloud09Hour[0]
        regexCloud09Hour = regexCloud09Hour.split()
    regexClear09Hour = re.findall("Clear|clear|Sun|sun", weatherAPI09HourDataCondition)
    if regexClear09Hour != []:
        regexClear09Hour = regexClear09Hour[0]
        regexClear09Hour = regexClear09Hour.split()
    regexSnow09Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI09HourDataCondition)
    if regexSnow09Hour != []:
        regexSnow09Hour = regexSnow09Hour[0]
        regexSnow09Hour = regexSnow09Hour.split()
    regexWind09Hour = re.findall("Wind|wind", weatherAPI09HourDataCondition)
    if regexWind09Hour != []:
        regexWind09Hour = regexWind09Hour[0]
        regexWind09Hour = regexWind09Hour.split()
    regexHail09Hour = re.findall("Hail|hail", weatherAPI09HourDataCondition)
    if regexHail09Hour != []:
        regexHail09Hour = regexHail09Hour[0]
        regexHail09Hour = regexHail09Hour.split()
    regexMist09Hour = re.findall("Mist|mist|Fog|fog", weatherAPI09HourDataCondition)
    if regexMist09Hour != []:
        regexMist09Hour = regexMist09Hour[0]
        regexMist09Hour = regexMist09Hour.split()

    if regexThunder09Hour == ['Thunder'] or regexThunder09Hour == ['thunder']:
        weatherAPI09HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain09Hour == ['Rain'] or regexRain09Hour == ['rain'] or regexRain09Hour == [
        'Shower'] or regexRain09Hour == ['shower'] or regexRain09Hour == ['Drizzle'] or regexRain09Hour == [
        'drizzle']:
        weatherAPI09HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud09Hour == ['Cloud'] or regexCloud09Hour == ['cloud'] or regexCloud09Hour == [
        'Overcast'] or regexCloud09Hour == ['overcast'] or regexCloud09Hour == ['Cloudy'] or regexCloud09Hour == [
        'cloudy']:
        weatherAPI09HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear09Hour == ['Clear'] or regexClear09Hour == ['clear'] or regexClear09Hour == [
        'Sun'] or regexClear09Hour == ['sun']:
        weatherAPI09HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow09Hour == ['Snow'] or regexSnow09Hour == ['snow'] or regexSnow09Hour == [
        'Sleet'] or regexSnow09Hour == ['sleet'] or regexSnow09Hour == ['Blizzard'] or regexSnow09Hour == ['blizzard']:
        weatherAPI09HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind09Hour == ['Wind'] or regexWind09Hour == ['wind']:
        weatherAPI09HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail09Hour == ['Hail'] or regexHail09Hour == ['hail']:
        weatherAPI09HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist09Hour == ['Mist'] or regexMist09Hour == ['mist'] or regexMist09Hour == ['Fog'] or regexMist09Hour == ['fog']:
        weatherAPI09HourDataConditionIcon = "/static/images/mist.svg"

    #10 Hour Forecast - Similar code as 09 Hour Forecast
    weatherAPI10HourData = weatherAPIData['forecast']
    weatherAPI10HourData = weatherAPI10HourData['forecastday']
    weatherAPI10HourData = weatherAPI10HourData[0]
    weatherAPI10HourData = weatherAPI10HourData['hour']
    weatherAPI10HourData = weatherAPI10HourData[9]
    weatherAPI10HourDataConditionTime = weatherAPI10HourData['time']
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime.split(" ")
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime[1]
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime.split(":")
    weatherAPI10HourDataConditionTime = weatherAPI10HourDataConditionTime[0]
    weatherAPI10HourDataTemperature = weatherAPI10HourData['temp_c']
    weatherAPI10HourDataTemperature = round(weatherAPI10HourDataTemperature, 0)
    weatherAPI10HourDataTemperature = int(weatherAPI10HourDataTemperature)
    weatherAPI10HourDataTemperature = str(weatherAPI10HourDataTemperature) + "°C"
    weatherAPI10HourDataCondition = weatherAPI10HourData['condition']
    weatherAPI10HourDataCondition = weatherAPI10HourDataCondition['text']

    regexThunder10Hour = re.findall("Thunder|thunder", weatherAPI10HourDataCondition)
    if regexThunder10Hour != []:
        regexThunder10Hour = regexThunder10Hour[0]
        regexThunder10Hour = regexThunder10Hour.split()
    regexRain10Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI10HourDataCondition)
    if regexRain10Hour != []:
        regexRain10Hour = regexRain10Hour[0]
        regexRain10Hour = regexRain10Hour.split()
    regexCloud10Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI10HourDataCondition)
    if regexCloud10Hour != []:
        regexCloud10Hour = regexCloud10Hour[0]
        regexCloud10Hour = regexCloud10Hour.split()
    regexClear10Hour = re.findall("Clear|clear|Sun|sun", weatherAPI10HourDataCondition)
    if regexClear10Hour != []:
        regexClear10Hour = regexClear10Hour[0]
        regexClear10Hour = regexClear10Hour.split()
    regexSnow10Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI10HourDataCondition)
    if regexSnow10Hour != []:
        regexSnow10Hour = regexSnow10Hour[0]
        regexSnow10Hour = regexSnow10Hour.split()
    regexWind10Hour = re.findall("Wind|wind", weatherAPI10HourDataCondition)
    if regexWind10Hour != []:
        regexWind10Hour = regexWind10Hour[0]
        regexWind10Hour = regexWind10Hour.split()
    regexHail10Hour = re.findall("Hail|hail", weatherAPI10HourDataCondition)
    if regexHail10Hour != []:
        regexHail10Hour = regexHail10Hour[0]
        regexHail10Hour = regexHail10Hour.split()
    regexMist10Hour = re.findall("Mist|mist|Fog|fog", weatherAPI10HourDataCondition)
    if regexMist10Hour != []:
        regexMist10Hour = regexMist10Hour[0]
        regexMist10Hour = regexMist10Hour.split()

    if regexThunder10Hour == ['Thunder'] or regexThunder10Hour == ['thunder']:
        weatherAPI10HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain10Hour == ['Rain'] or regexRain10Hour == ['rain'] or regexRain10Hour == [
        'Shower'] or regexRain10Hour == ['shower'] or regexRain10Hour == ['Drizzle'] or regexRain10Hour == [
        'drizzle']:
        weatherAPI10HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud10Hour == ['Cloud'] or regexCloud10Hour == ['cloud'] or regexCloud10Hour == [
        'Overcast'] or regexCloud10Hour == ['overcast'] or regexCloud10Hour == ['Cloudy'] or regexCloud10Hour == [
        'cloudy']:
        weatherAPI10HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear10Hour == ['Clear'] or regexClear10Hour == ['clear'] or regexClear10Hour == [
        'Sun'] or regexClear10Hour == ['sun']:
        weatherAPI10HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow10Hour == ['Snow'] or regexSnow10Hour == ['snow'] or regexSnow10Hour == [
        'Sleet'] or regexSnow10Hour == ['sleet'] or regexSnow10Hour == ['Blizzard'] or regexSnow10Hour == ['blizzard']:
        weatherAPI10HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind10Hour == ['Wind'] or regexWind10Hour == ['wind']:
        weatherAPI10HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail10Hour == ['Hail'] or regexHail10Hour == ['hail']:
        weatherAPI10HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist10Hour == ['Mist'] or regexMist10Hour == ['mist'] or regexMist10Hour == ['Fog'] or regexMist10Hour == ['fog']:
        weatherAPI10HourDataConditionIcon = "/static/images/mist.svg"


    #11 Hour Forecast - Similar code as 10 Hour Forecast
    weatherAPI11HourData = weatherAPIData['forecast']
    weatherAPI11HourData = weatherAPI11HourData['forecastday']
    weatherAPI11HourData = weatherAPI11HourData[0]
    weatherAPI11HourData = weatherAPI11HourData['hour']
    weatherAPI11HourData = weatherAPI11HourData[10]
    weatherAPI11HourDataConditionTime = weatherAPI11HourData['time']
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime.split(" ")
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime[1]
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime.split(":")
    weatherAPI11HourDataConditionTime = weatherAPI11HourDataConditionTime[0]
    weatherAPI11HourDataTemperature = weatherAPI11HourData['temp_c']
    weatherAPI11HourDataTemperature = round(weatherAPI11HourDataTemperature, 0)
    weatherAPI11HourDataTemperature = int(weatherAPI11HourDataTemperature)
    weatherAPI11HourDataTemperature = str(weatherAPI11HourDataTemperature) + "°C"
    weatherAPI11HourDataCondition = weatherAPI11HourData['condition']
    weatherAPI11HourDataCondition = weatherAPI11HourDataCondition['text']

    regexThunder11Hour = re.findall("Thunder|thunder", weatherAPI11HourDataCondition)
    if regexThunder11Hour != []:
        regexThunder11Hour = regexThunder11Hour[0]
        regexThunder11Hour = regexThunder11Hour.split()
    regexRain11Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI11HourDataCondition)
    if regexRain11Hour != []:
        regexRain11Hour = regexRain11Hour[0]
        regexRain11Hour = regexRain11Hour.split()
    regexCloud11Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI11HourDataCondition)
    if regexCloud11Hour != []:
        regexCloud11Hour = regexCloud11Hour[0]
        regexCloud11Hour = regexCloud11Hour.split()
    regexClear11Hour = re.findall("Clear|clear|Sun|sun", weatherAPI11HourDataCondition)
    if regexClear11Hour != []:
        regexClear11Hour = regexClear11Hour[0]
        regexClear11Hour = regexClear11Hour.split()
    regexSnow11Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI11HourDataCondition)
    if regexSnow11Hour != []:
        regexSnow11Hour = regexSnow11Hour[0]
        regexSnow11Hour = regexSnow11Hour.split()
    regexWind11Hour = re.findall("Wind|wind", weatherAPI11HourDataCondition)
    if regexWind11Hour != []:
        regexWind11Hour = regexWind11Hour[0]
        regexWind11Hour = regexWind11Hour.split()
    regexHail11Hour = re.findall("Hail|hail", weatherAPI11HourDataCondition)
    if regexHail11Hour != []:
        regexHail11Hour = regexHail11Hour[0]
        regexHail11Hour = regexHail11Hour.split()
    regexMist11Hour = re.findall("Mist|mist|Fog|fog", weatherAPI11HourDataCondition)
    if regexMist11Hour != []:
        regexMist11Hour = regexMist11Hour[0]
        regexMist11Hour = regexMist11Hour.split()

    if regexThunder11Hour == ['Thunder'] or regexThunder11Hour == ['thunder']:
        weatherAPI11HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain11Hour == ['Rain'] or regexRain11Hour == ['rain'] or regexRain11Hour == [
        'Shower'] or regexRain11Hour == ['shower'] or regexRain11Hour == ['Drizzle'] or regexRain11Hour == [
        'drizzle']:
        weatherAPI11HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud11Hour == ['Cloud'] or regexCloud11Hour == ['cloud'] or regexCloud11Hour == [
        'Overcast'] or regexCloud11Hour == ['overcast'] or regexCloud11Hour == ['Cloudy'] or regexCloud11Hour == [
        'cloudy']:
        weatherAPI11HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear11Hour == ['Clear'] or regexClear11Hour == ['clear'] or regexClear11Hour == [
        'Sun'] or regexClear11Hour == ['sun']:
        weatherAPI11HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow11Hour == ['Snow'] or regexSnow11Hour == ['snow'] or regexSnow11Hour == [
        'Sleet'] or regexSnow11Hour == ['sleet'] or regexSnow11Hour == ['Blizzard'] or regexSnow11Hour == ['blizzard']:
        weatherAPI11HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind11Hour == ['Wind'] or regexWind11Hour == ['wind']:
        weatherAPI11HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail11Hour == ['Hail'] or regexHail11Hour == ['hail']:
        weatherAPI11HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist11Hour == ['Mist'] or regexMist11Hour == ['mist'] or regexMist11Hour == ['Fog'] or regexMist11Hour == ['fog']:
        weatherAPI11HourDataConditionIcon = "/static/images/mist.svg"

    #12 Hour Forecast - Similar code as 11 Hour Forecast
    weatherAPI12HourData = weatherAPIData['forecast']
    weatherAPI12HourData = weatherAPI12HourData['forecastday']
    weatherAPI12HourData = weatherAPI12HourData[0]
    weatherAPI12HourData = weatherAPI12HourData['hour']
    weatherAPI12HourData = weatherAPI12HourData[11]
    weatherAPI12HourDataConditionTime = weatherAPI12HourData['time']
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime.split(" ")
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime[1]
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime.split(":")
    weatherAPI12HourDataConditionTime = weatherAPI12HourDataConditionTime[0]
    weatherAPI12HourDataTemperature = weatherAPI12HourData['temp_c']
    weatherAPI12HourDataTemperature = round(weatherAPI12HourDataTemperature, 0)
    weatherAPI12HourDataTemperature = int(weatherAPI12HourDataTemperature)
    weatherAPI12HourDataTemperature = str(weatherAPI12HourDataTemperature) + "°C"
    weatherAPI12HourDataCondition = weatherAPI12HourData['condition']
    weatherAPI12HourDataCondition = weatherAPI12HourDataCondition['text']

    regexThunder12Hour = re.findall("Thunder|thunder", weatherAPI12HourDataCondition)
    if regexThunder12Hour != []:
        regexThunder12Hour = regexThunder12Hour[0]
        regexThunder12Hour = regexThunder12Hour.split()
    regexRain12Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI12HourDataCondition)
    if regexRain12Hour != []:
        regexRain12Hour = regexRain12Hour[0]
        regexRain12Hour = regexRain12Hour.split()
    regexCloud12Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI12HourDataCondition)
    if regexCloud12Hour != []:
        regexCloud12Hour = regexCloud12Hour[0]
        regexCloud12Hour = regexCloud12Hour.split()
    regexClear12Hour = re.findall("Clear|clear|Sun|sun", weatherAPI12HourDataCondition)
    if regexClear12Hour != []:
        regexClear12Hour = regexClear12Hour[0]
        regexClear12Hour = regexClear12Hour.split()
    regexSnow12Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI12HourDataCondition)
    if regexSnow12Hour != []:
        regexSnow12Hour = regexSnow12Hour[0]
        regexSnow12Hour = regexSnow12Hour.split()
    regexWind12Hour = re.findall("Wind|wind", weatherAPI12HourDataCondition)
    if regexWind12Hour != []:
        regexWind12Hour = regexWind12Hour[0]
        regexWind12Hour = regexWind12Hour.split()
    regexHail12Hour = re.findall("Hail|hail", weatherAPI12HourDataCondition)
    if regexHail12Hour != []:
        regexHail12Hour = regexHail12Hour[0]
        regexHail12Hour = regexHail12Hour.split()
    regexMist12Hour = re.findall("Mist|mist|Fog|fog", weatherAPI12HourDataCondition)
    if regexMist12Hour != []:
        regexMist12Hour = regexMist12Hour[0]
        regexMist12Hour = regexMist12Hour.split()

    if regexThunder12Hour == ['Thunder'] or regexThunder12Hour == ['thunder']:
        weatherAPI12HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain12Hour == ['Rain'] or regexRain12Hour == ['rain'] or regexRain12Hour == [
        'Shower'] or regexRain12Hour == ['shower'] or regexRain12Hour == ['Drizzle'] or regexRain12Hour == [
        'drizzle']:
        weatherAPI12HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud12Hour == ['Cloud'] or regexCloud12Hour == ['cloud'] or regexCloud12Hour == [
        'Overcast'] or regexCloud12Hour == ['overcast'] or regexCloud12Hour == ['Cloudy'] or regexCloud12Hour == [
        'cloudy']:
        weatherAPI12HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear12Hour == ['Clear'] or regexClear12Hour == ['clear'] or regexClear12Hour == [
        'Sun'] or regexClear12Hour == ['sun']:
        weatherAPI12HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow12Hour == ['Snow'] or regexSnow12Hour == ['snow'] or regexSnow12Hour == [
        'Sleet'] or regexSnow12Hour == ['sleet'] or regexSnow12Hour == ['Blizzard'] or regexSnow12Hour == ['blizzard']:
        weatherAPI12HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind12Hour == ['Wind'] or regexWind12Hour == ['wind']:
        weatherAPI12HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail12Hour == ['Hail'] or regexHail12Hour == ['hail']:
        weatherAPI12HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist12Hour == ['Mist'] or regexMist12Hour == ['mist'] or regexMist12Hour == ['Fog'] or regexMist12Hour == ['fog']:
        weatherAPI12HourDataConditionIcon = "/static/images/mist.svg"

    #13 Hour Forecast - Similar code as 12 Hour Forecast
    weatherAPI13HourData = weatherAPIData['forecast']
    weatherAPI13HourData = weatherAPI13HourData['forecastday']
    weatherAPI13HourData = weatherAPI13HourData[0]
    weatherAPI13HourData = weatherAPI13HourData['hour']
    weatherAPI13HourData = weatherAPI13HourData[12]
    weatherAPI13HourDataConditionTime = weatherAPI13HourData['time']
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime.split(" ")
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime[1]
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime.split(":")
    weatherAPI13HourDataConditionTime = weatherAPI13HourDataConditionTime[0]
    weatherAPI13HourDataTemperature = weatherAPI13HourData['temp_c']
    weatherAPI13HourDataTemperature = round(weatherAPI13HourDataTemperature, 0)
    weatherAPI13HourDataTemperature = int(weatherAPI13HourDataTemperature)
    weatherAPI13HourDataTemperature = str(weatherAPI13HourDataTemperature) + "°C"
    weatherAPI13HourDataCondition = weatherAPI13HourData['condition']
    weatherAPI13HourDataCondition = weatherAPI13HourDataCondition['text']

    regexThunder13Hour = re.findall("Thunder|thunder", weatherAPI13HourDataCondition)
    if regexThunder13Hour != []:
        regexThunder13Hour = regexThunder13Hour[0]
        regexThunder13Hour = regexThunder13Hour.split()
    regexRain13Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI13HourDataCondition)
    if regexRain13Hour != []:
        regexRain13Hour = regexRain13Hour[0]
        regexRain13Hour = regexRain13Hour.split()
    regexCloud13Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI13HourDataCondition)
    if regexCloud13Hour != []:
        regexCloud13Hour = regexCloud13Hour[0]
        regexCloud13Hour = regexCloud13Hour.split()
    regexClear13Hour = re.findall("Clear|clear|Sun|sun", weatherAPI13HourDataCondition)
    if regexClear13Hour != []:
        regexClear13Hour = regexClear13Hour[0]
        regexClear13Hour = regexClear13Hour.split()
    regexSnow13Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI13HourDataCondition)
    if regexSnow13Hour != []:
        regexSnow13Hour = regexSnow13Hour[0]
        regexSnow13Hour = regexSnow13Hour.split()
    regexWind13Hour = re.findall("Wind|wind", weatherAPI13HourDataCondition)
    if regexWind13Hour != []:
        regexWind13Hour = regexWind13Hour[0]
        regexWind13Hour = regexWind13Hour.split()
    regexHail13Hour = re.findall("Hail|hail", weatherAPI13HourDataCondition)
    if regexHail13Hour != []:
        regexHail13Hour = regexHail13Hour[0]
        regexHail13Hour = regexHail13Hour.split()
    regexMist13Hour = re.findall("Mist|mist|Fog|fog", weatherAPI13HourDataCondition)
    if regexMist13Hour != []:
        regexMist13Hour = regexMist13Hour[0]
        regexMist13Hour = regexMist13Hour.split()

    if regexThunder13Hour == ['Thunder'] or regexThunder13Hour == ['thunder']:
        weatherAPI13HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain13Hour == ['Rain'] or regexRain13Hour == ['rain'] or regexRain13Hour == [
        'Shower'] or regexRain13Hour == ['shower'] or regexRain13Hour == ['Drizzle'] or regexRain13Hour == [
        'drizzle']:
        weatherAPI13HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud13Hour == ['Cloud'] or regexCloud13Hour == ['cloud'] or regexCloud13Hour == [
        'Overcast'] or regexCloud13Hour == ['overcast'] or regexCloud13Hour == ['Cloudy'] or regexCloud13Hour == [
        'cloudy']:
        weatherAPI13HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear13Hour == ['Clear'] or regexClear13Hour == ['clear'] or regexClear13Hour == [
        'Sun'] or regexClear13Hour == ['sun']:
        weatherAPI13HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow13Hour == ['Snow'] or regexSnow13Hour == ['snow'] or regexSnow13Hour == [
        'Sleet'] or regexSnow13Hour == ['sleet'] or regexSnow13Hour == ['Blizzard'] or regexSnow13Hour == ['blizzard']:
        weatherAPI13HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind13Hour == ['Wind'] or regexWind13Hour == ['wind']:
        weatherAPI13HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail13Hour == ['Hail'] or regexHail13Hour == ['hail']:
        weatherAPI13HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist13Hour == ['Mist'] or regexMist13Hour == ['mist'] or regexMist13Hour == ['Fog'] or regexMist13Hour == ['fog']:
        weatherAPI13HourDataConditionIcon = "/static/images/mist.svg"

    #14 Hour Forecast - Similar code as 13 Hour Forecast
    weatherAPI14HourData = weatherAPIData['forecast']
    weatherAPI14HourData = weatherAPI14HourData['forecastday']
    weatherAPI14HourData = weatherAPI14HourData[0]
    weatherAPI14HourData = weatherAPI14HourData['hour']
    weatherAPI14HourData = weatherAPI14HourData[13]
    weatherAPI14HourDataConditionTime = weatherAPI14HourData['time']
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime.split(" ")
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime[1]
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime.split(":")
    weatherAPI14HourDataConditionTime = weatherAPI14HourDataConditionTime[0]
    weatherAPI14HourDataTemperature = weatherAPI14HourData['temp_c']
    weatherAPI14HourDataTemperature = round(weatherAPI14HourDataTemperature, 0)
    weatherAPI14HourDataTemperature = int(weatherAPI14HourDataTemperature)
    weatherAPI14HourDataTemperature = str(weatherAPI14HourDataTemperature) + "°C"
    weatherAPI14HourDataCondition = weatherAPI14HourData['condition']
    weatherAPI14HourDataCondition = weatherAPI14HourDataCondition['text']

    regexThunder14Hour = re.findall("Thunder|thunder", weatherAPI14HourDataCondition)
    if regexThunder14Hour != []:
        regexThunder14Hour = regexThunder14Hour[0]
        regexThunder14Hour = regexThunder14Hour.split()
    regexRain14Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI14HourDataCondition)
    if regexRain14Hour != []:
        regexRain14Hour = regexRain14Hour[0]
        regexRain14Hour = regexRain14Hour.split()
    regexCloud14Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI14HourDataCondition)
    if regexCloud14Hour != []:
        regexCloud14Hour = regexCloud14Hour[0]
        regexCloud14Hour = regexCloud14Hour.split()
    regexClear14Hour = re.findall("Clear|clear|Sun|sun", weatherAPI14HourDataCondition)
    if regexClear14Hour != []:
        regexClear14Hour = regexClear14Hour[0]
        regexClear14Hour = regexClear14Hour.split()
    regexSnow14Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI14HourDataCondition)
    if regexSnow14Hour != []:
        regexSnow14Hour = regexSnow14Hour[0]
        regexSnow14Hour = regexSnow14Hour.split()
    regexWind14Hour = re.findall("Wind|wind", weatherAPI14HourDataCondition)
    if regexWind14Hour != []:
        regexWind14Hour = regexWind14Hour[0]
        regexWind14Hour = regexWind14Hour.split()
    regexHail14Hour = re.findall("Hail|hail", weatherAPI14HourDataCondition)
    if regexHail14Hour != []:
        regexHail14Hour = regexHail14Hour[0]
        regexHail14Hour = regexHail14Hour.split()
    regexMist14Hour = re.findall("Mist|mist|Fog|fog", weatherAPI14HourDataCondition)
    if regexMist14Hour != []:
        regexMist14Hour = regexMist14Hour[0]
        regexMist14Hour = regexMist14Hour.split()

    if regexThunder14Hour == ['Thunder'] or regexThunder14Hour == ['thunder']:
        weatherAPI14HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain14Hour == ['Rain'] or regexRain14Hour == ['rain'] or regexRain14Hour == [
        'Shower'] or regexRain14Hour == ['shower'] or regexRain14Hour == ['Drizzle'] or regexRain14Hour == [
        'drizzle']:
        weatherAPI14HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud14Hour == ['Cloud'] or regexCloud14Hour == ['cloud'] or regexCloud14Hour == [
        'Overcast'] or regexCloud14Hour == ['overcast'] or regexCloud14Hour == ['Cloudy'] or regexCloud14Hour == [
        'cloudy']:
        weatherAPI14HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear14Hour == ['Clear'] or regexClear14Hour == ['clear'] or regexClear14Hour == [
        'Sun'] or regexClear14Hour == ['sun']:
        weatherAPI14HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow14Hour == ['Snow'] or regexSnow14Hour == ['snow'] or regexSnow14Hour == [
        'Sleet'] or regexSnow14Hour == ['sleet'] or regexSnow14Hour == ['Blizzard'] or regexSnow14Hour == ['blizzard']:
        weatherAPI14HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind14Hour == ['Wind'] or regexWind14Hour == ['wind']:
        weatherAPI14HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail14Hour == ['Hail'] or regexHail14Hour == ['hail']:
        weatherAPI14HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist14Hour == ['Mist'] or regexMist14Hour == ['mist'] or regexMist14Hour == ['Fog'] or regexMist14Hour == ['fog']:
        weatherAPI14HourDataConditionIcon = "/static/images/mist.svg"

    #15 Hour Forecast - Similar code as 14 Hour Forecast
    weatherAPI15HourData = weatherAPIData['forecast']
    weatherAPI15HourData = weatherAPI15HourData['forecastday']
    weatherAPI15HourData = weatherAPI15HourData[0]
    weatherAPI15HourData = weatherAPI15HourData['hour']
    weatherAPI15HourData = weatherAPI15HourData[14]
    weatherAPI15HourDataConditionTime = weatherAPI15HourData['time']
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime.split(" ")
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime[1]
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime.split(":")
    weatherAPI15HourDataConditionTime = weatherAPI15HourDataConditionTime[0]
    weatherAPI15HourDataTemperature = weatherAPI15HourData['temp_c']
    weatherAPI15HourDataTemperature = round(weatherAPI15HourDataTemperature, 0)
    weatherAPI15HourDataTemperature = int(weatherAPI15HourDataTemperature)
    weatherAPI15HourDataTemperature = str(weatherAPI15HourDataTemperature) + "°C"
    weatherAPI15HourDataCondition = weatherAPI15HourData['condition']
    weatherAPI15HourDataCondition = weatherAPI15HourDataCondition['text']

    regexThunder15Hour = re.findall("Thunder|thunder", weatherAPI15HourDataCondition)
    if regexThunder15Hour != []:
        regexThunder15Hour = regexThunder15Hour[0]
        regexThunder15Hour = regexThunder15Hour.split()
    regexRain15Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI15HourDataCondition)
    if regexRain15Hour != []:
        regexRain15Hour = regexRain15Hour[0]
        regexRain15Hour = regexRain15Hour.split()
    regexCloud15Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI15HourDataCondition)
    if regexCloud15Hour != []:
        regexCloud15Hour = regexCloud15Hour[0]
        regexCloud15Hour = regexCloud15Hour.split()
    regexClear15Hour = re.findall("Clear|clear|Sun|sun", weatherAPI15HourDataCondition)
    if regexClear15Hour != []:
        regexClear15Hour = regexClear15Hour[0]
        regexClear15Hour = regexClear15Hour.split()
    regexSnow15Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI15HourDataCondition)
    if regexSnow15Hour != []:
        regexSnow15Hour = regexSnow15Hour[0]
        regexSnow15Hour = regexSnow15Hour.split()
    regexWind15Hour = re.findall("Wind|wind", weatherAPI15HourDataCondition)
    if regexWind15Hour != []:
        regexWind15Hour = regexWind15Hour[0]
        regexWind15Hour = regexWind15Hour.split()
    regexHail15Hour = re.findall("Hail|hail", weatherAPI15HourDataCondition)
    if regexHail15Hour != []:
        regexHail15Hour = regexHail15Hour[0]
        regexHail15Hour = regexHail15Hour.split()
    regexMist15Hour = re.findall("Mist|mist|Fog|fog", weatherAPI15HourDataCondition)
    if regexMist15Hour != []:
        regexMist15Hour = regexMist15Hour[0]
        regexMist15Hour = regexMist15Hour.split()

    if regexThunder15Hour == ['Thunder'] or regexThunder15Hour == ['thunder']:
        weatherAPI15HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain15Hour == ['Rain'] or regexRain15Hour == ['rain'] or regexRain15Hour == [
        'Shower'] or regexRain15Hour == ['shower'] or regexRain15Hour == ['Drizzle'] or regexRain15Hour == [
        'drizzle']:
        weatherAPI15HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud15Hour == ['Cloud'] or regexCloud15Hour == ['cloud'] or regexCloud15Hour == [
        'Overcast'] or regexCloud15Hour == ['overcast'] or regexCloud15Hour == ['Cloudy'] or regexCloud15Hour == [
        'cloudy']:
        weatherAPI15HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear15Hour == ['Clear'] or regexClear15Hour == ['clear'] or regexClear15Hour == [
        'Sun'] or regexClear15Hour == ['sun']:
        weatherAPI15HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow15Hour == ['Snow'] or regexSnow15Hour == ['snow'] or regexSnow15Hour == [
        'Sleet'] or regexSnow15Hour == ['sleet'] or regexSnow15Hour == ['Blizzard'] or regexSnow15Hour == ['blizzard']:
        weatherAPI15HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind15Hour == ['Wind'] or regexWind15Hour == ['wind']:
        weatherAPI15HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail15Hour == ['Hail'] or regexHail15Hour == ['hail']:
        weatherAPI15HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist15Hour == ['Mist'] or regexMist15Hour == ['mist'] or regexMist15Hour == ['Fog'] or regexMist15Hour == ['fog']:
        weatherAPI15HourDataConditionIcon = "/static/images/mist.svg"

    #16 Hour Forecast - Similar code as 15 Hour Forecast
    weatherAPI16HourData = weatherAPIData['forecast']
    weatherAPI16HourData = weatherAPI16HourData['forecastday']
    weatherAPI16HourData = weatherAPI16HourData[0]
    weatherAPI16HourData = weatherAPI16HourData['hour']
    weatherAPI16HourData = weatherAPI16HourData[15]
    weatherAPI16HourDataConditionTime = weatherAPI16HourData['time']
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime.split(" ")
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime[1]
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime.split(":")
    weatherAPI16HourDataConditionTime = weatherAPI16HourDataConditionTime[0]
    weatherAPI16HourDataTemperature = weatherAPI16HourData['temp_c']
    weatherAPI16HourDataTemperature = round(weatherAPI16HourDataTemperature, 0)
    weatherAPI16HourDataTemperature = int(weatherAPI16HourDataTemperature)
    weatherAPI16HourDataTemperature = str(weatherAPI16HourDataTemperature) + "°C"
    weatherAPI16HourDataCondition = weatherAPI16HourData['condition']
    weatherAPI16HourDataCondition = weatherAPI16HourDataCondition['text']

    regexThunder16Hour = re.findall("Thunder|thunder", weatherAPI16HourDataCondition)
    if regexThunder16Hour != []:
        regexThunder16Hour = regexThunder16Hour[0]
        regexThunder16Hour = regexThunder16Hour.split()
    regexRain16Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI16HourDataCondition)
    if regexRain16Hour != []:
        regexRain16Hour = regexRain16Hour[0]
        regexRain16Hour = regexRain16Hour.split()
    regexCloud16Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI16HourDataCondition)
    if regexCloud16Hour != []:
        regexCloud16Hour = regexCloud16Hour[0]
        regexCloud16Hour = regexCloud16Hour.split()
    regexClear16Hour = re.findall("Clear|clear|Sun|sun", weatherAPI16HourDataCondition)
    if regexClear16Hour != []:
        regexClear16Hour = regexClear16Hour[0]
        regexClear16Hour = regexClear16Hour.split()
    regexSnow16Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI16HourDataCondition)
    if regexSnow16Hour != []:
        regexSnow16Hour = regexSnow16Hour[0]
        regexSnow16Hour = regexSnow16Hour.split()
    regexWind16Hour = re.findall("Wind|wind", weatherAPI16HourDataCondition)
    if regexWind16Hour != []:
        regexWind16Hour = regexWind16Hour[0]
        regexWind16Hour = regexWind16Hour.split()
    regexHail16Hour = re.findall("Hail|hail", weatherAPI16HourDataCondition)
    if regexHail16Hour != []:
        regexHail16Hour = regexHail16Hour[0]
        regexHail16Hour = regexHail16Hour.split()
    regexMist16Hour = re.findall("Mist|mist|Fog|fog", weatherAPI16HourDataCondition)
    if regexMist16Hour != []:
        regexMist16Hour = regexMist16Hour[0]
        regexMist16Hour = regexMist16Hour.split()

    if regexThunder16Hour == ['Thunder'] or regexThunder16Hour == ['thunder']:
        weatherAPI16HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain16Hour == ['Rain'] or regexRain16Hour == ['rain'] or regexRain16Hour == [
        'Shower'] or regexRain16Hour == ['shower'] or regexRain16Hour == ['Drizzle'] or regexRain16Hour == [
        'drizzle']:
        weatherAPI16HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud16Hour == ['Cloud'] or regexCloud16Hour == ['cloud'] or regexCloud16Hour == [
        'Overcast'] or regexCloud16Hour == ['overcast'] or regexCloud16Hour == ['Cloudy'] or regexCloud16Hour == [
        'cloudy']:
        weatherAPI16HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear16Hour == ['Clear'] or regexClear16Hour == ['clear'] or regexClear16Hour == [
        'Sun'] or regexClear16Hour == ['sun']:
        weatherAPI16HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow16Hour == ['Snow'] or regexSnow16Hour == ['snow'] or regexSnow16Hour == [
        'Sleet'] or regexSnow16Hour == ['sleet'] or regexSnow16Hour == ['Blizzard'] or regexSnow16Hour == ['blizzard']:
        weatherAPI16HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind16Hour == ['Wind'] or regexWind16Hour == ['wind']:
        weatherAPI16HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail16Hour == ['Hail'] or regexHail16Hour == ['hail']:
        weatherAPI16HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist16Hour == ['Mist'] or regexMist16Hour == ['mist'] or regexMist16Hour == ['Fog'] or regexMist16Hour == ['fog']:
        weatherAPI16HourDataConditionIcon = "/static/images/mist.svg"



    #17 Hour Forecast - Similar code as 16 Hour Forecast
    weatherAPI17HourData = weatherAPIData['forecast']
    weatherAPI17HourData = weatherAPI17HourData['forecastday']
    weatherAPI17HourData = weatherAPI17HourData[0]
    weatherAPI17HourData = weatherAPI17HourData['hour']
    weatherAPI17HourData = weatherAPI17HourData[16]
    weatherAPI17HourDataConditionTime = weatherAPI17HourData['time']
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime.split(" ")
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime[1]
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime.split(":")
    weatherAPI17HourDataConditionTime = weatherAPI17HourDataConditionTime[0]
    weatherAPI17HourDataTemperature = weatherAPI17HourData['temp_c']
    weatherAPI17HourDataTemperature = round(weatherAPI17HourDataTemperature, 0)
    weatherAPI17HourDataTemperature = int(weatherAPI17HourDataTemperature)
    weatherAPI17HourDataTemperature = str(weatherAPI17HourDataTemperature) + "°C"
    weatherAPI17HourDataCondition = weatherAPI17HourData['condition']
    weatherAPI17HourDataCondition = weatherAPI17HourDataCondition['text']

    regexThunder17Hour = re.findall("Thunder|thunder", weatherAPI17HourDataCondition)
    if regexThunder17Hour != []:
        regexThunder17Hour = regexThunder17Hour[0]
        regexThunder17Hour = regexThunder17Hour.split()
    regexRain17Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI17HourDataCondition)
    if regexRain17Hour != []:
        regexRain17Hour = regexRain17Hour[0]
        regexRain17Hour = regexRain17Hour.split()
    regexCloud17Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI17HourDataCondition)
    if regexCloud17Hour != []:
        regexCloud17Hour = regexCloud17Hour[0]
        regexCloud17Hour = regexCloud17Hour.split()
    regexClear17Hour = re.findall("Clear|clear|Sun|sun", weatherAPI17HourDataCondition)
    if regexClear17Hour != []:
        regexClear17Hour = regexClear17Hour[0]
        regexClear17Hour = regexClear17Hour.split()
    regexSnow17Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI17HourDataCondition)
    if regexSnow17Hour != []:
        regexSnow17Hour = regexSnow17Hour[0]
        regexSnow17Hour = regexSnow17Hour.split()
    regexWind17Hour = re.findall("Wind|wind", weatherAPI17HourDataCondition)
    if regexWind17Hour != []:
        regexWind17Hour = regexWind17Hour[0]
        regexWind17Hour = regexWind17Hour.split()
    regexHail17Hour = re.findall("Hail|hail", weatherAPI17HourDataCondition)
    if regexHail17Hour != []:
        regexHail17Hour = regexHail17Hour[0]
        regexHail17Hour = regexHail17Hour.split()
    regexMist17Hour = re.findall("Mist|mist|Fog|fog", weatherAPI17HourDataCondition)
    if regexMist17Hour != []:
        regexMist17Hour = regexMist17Hour[0]
        regexMist17Hour = regexMist17Hour.split()

    if regexThunder17Hour == ['Thunder'] or regexThunder17Hour == ['thunder']:
        weatherAPI17HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain17Hour == ['Rain'] or regexRain17Hour == ['rain'] or regexRain17Hour == [
        'Shower'] or regexRain17Hour == ['shower'] or regexRain17Hour == ['Drizzle'] or regexRain17Hour == [
        'drizzle']:
        weatherAPI17HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud17Hour == ['Cloud'] or regexCloud17Hour == ['cloud'] or regexCloud17Hour == [
        'Overcast'] or regexCloud17Hour == ['overcast'] or regexCloud17Hour == ['Cloudy'] or regexCloud17Hour == [
        'cloudy']:
        weatherAPI17HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear17Hour == ['Clear'] or regexClear17Hour == ['clear'] or regexClear17Hour == [
        'Sun'] or regexClear17Hour == ['sun']:
        weatherAPI17HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow17Hour == ['Snow'] or regexSnow17Hour == ['snow'] or regexSnow17Hour == [
        'Sleet'] or regexSnow17Hour == ['sleet'] or regexSnow17Hour == ['Blizzard'] or regexSnow17Hour == ['blizzard']:
        weatherAPI17HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind17Hour == ['Wind'] or regexWind17Hour == ['wind']:
        weatherAPI17HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail17Hour == ['Hail'] or regexHail17Hour == ['hail']:
        weatherAPI17HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist17Hour == ['Mist'] or regexMist17Hour == ['mist'] or regexMist17Hour == ['Fog'] or regexMist17Hour == ['fog']:
        weatherAPI17HourDataConditionIcon = "/static/images/mist.svg"

    #18 Hour Forecast - Similar code as 17 Hour Forecast
    weatherAPI18HourData = weatherAPIData['forecast']
    weatherAPI18HourData = weatherAPI18HourData['forecastday']
    weatherAPI18HourData = weatherAPI18HourData[0]
    weatherAPI18HourData = weatherAPI18HourData['hour']
    weatherAPI18HourData = weatherAPI18HourData[17]
    weatherAPI18HourDataConditionTime = weatherAPI18HourData['time']
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime.split(" ")
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime[1]
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime.split(":")
    weatherAPI18HourDataConditionTime = weatherAPI18HourDataConditionTime[0]
    weatherAPI18HourDataTemperature = weatherAPI18HourData['temp_c']
    weatherAPI18HourDataTemperature = round(weatherAPI18HourDataTemperature, 0)
    weatherAPI18HourDataTemperature = int(weatherAPI18HourDataTemperature)
    weatherAPI18HourDataTemperature = str(weatherAPI18HourDataTemperature) + "°C"
    weatherAPI18HourDataCondition = weatherAPI18HourData['condition']
    weatherAPI18HourDataCondition = weatherAPI18HourDataCondition['text']

    regexThunder18Hour = re.findall("Thunder|thunder", weatherAPI18HourDataCondition)
    if regexThunder18Hour != []:
        regexThunder18Hour = regexThunder18Hour[0]
        regexThunder18Hour = regexThunder18Hour.split()
    regexRain18Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI18HourDataCondition)
    if regexRain18Hour != []:
        regexRain18Hour = regexRain18Hour[0]
        regexRain18Hour = regexRain18Hour.split()
    regexCloud18Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI18HourDataCondition)
    if regexCloud18Hour != []:
        regexCloud18Hour = regexCloud18Hour[0]
        regexCloud18Hour = regexCloud18Hour.split()
    regexClear18Hour = re.findall("Clear|clear|Sun|sun", weatherAPI18HourDataCondition)
    if regexClear18Hour != []:
        regexClear18Hour = regexClear18Hour[0]
        regexClear18Hour = regexClear18Hour.split()
    regexSnow18Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI18HourDataCondition)
    if regexSnow18Hour != []:
        regexSnow18Hour = regexSnow18Hour[0]
        regexSnow18Hour = regexSnow18Hour.split()
    regexWind18Hour = re.findall("Wind|wind", weatherAPI18HourDataCondition)
    if regexWind18Hour != []:
        regexWind18Hour = regexWind18Hour[0]
        regexWind18Hour = regexWind18Hour.split()
    regexHail18Hour = re.findall("Hail|hail", weatherAPI18HourDataCondition)
    if regexHail18Hour != []:
        regexHail18Hour = regexHail18Hour[0]
        regexHail18Hour = regexHail18Hour.split()
    regexMist18Hour = re.findall("Mist|mist|Fog|fog", weatherAPI18HourDataCondition)
    if regexMist18Hour != []:
        regexMist18Hour = regexMist18Hour[0]
        regexMist18Hour = regexMist18Hour.split()

    if regexThunder18Hour == ['Thunder'] or regexThunder18Hour == ['thunder']:
        weatherAPI18HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain18Hour == ['Rain'] or regexRain18Hour == ['rain'] or regexRain18Hour == [
        'Shower'] or regexRain18Hour == ['shower'] or regexRain18Hour == ['Drizzle'] or regexRain18Hour == [
        'drizzle']:
        weatherAPI18HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud18Hour == ['Cloud'] or regexCloud18Hour == ['cloud'] or regexCloud18Hour == [
        'Overcast'] or regexCloud18Hour == ['overcast'] or regexCloud18Hour == ['Cloudy'] or regexCloud18Hour == [
        'cloudy']:
        weatherAPI18HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear18Hour == ['Clear'] or regexClear18Hour == ['clear'] or regexClear18Hour == [
        'Sun'] or regexClear18Hour == ['sun']:
        weatherAPI18HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow18Hour == ['Snow'] or regexSnow18Hour == ['snow'] or regexSnow18Hour == [
        'Sleet'] or regexSnow18Hour == ['sleet'] or regexSnow18Hour == ['Blizzard'] or regexSnow18Hour == ['blizzard']:
        weatherAPI18HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind18Hour == ['Wind'] or regexWind18Hour == ['wind']:
        weatherAPI18HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail18Hour == ['Hail'] or regexHail18Hour == ['hail']:
        weatherAPI18HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist18Hour == ['Mist'] or regexMist18Hour == ['mist'] or regexMist18Hour == ['Fog'] or regexMist18Hour == ['fog']:
        weatherAPI18HourDataConditionIcon = "/static/images/mist.svg"

    #19 Hour Forecast - Similar code as 18 Hour Forecast
    weatherAPI19HourData = weatherAPIData['forecast']
    weatherAPI19HourData = weatherAPI19HourData['forecastday']
    weatherAPI19HourData = weatherAPI19HourData[0]
    weatherAPI19HourData = weatherAPI19HourData['hour']
    weatherAPI19HourData = weatherAPI19HourData[18]
    weatherAPI19HourDataConditionTime = weatherAPI19HourData['time']
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime.split(" ")
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime[1]
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime.split(":")
    weatherAPI19HourDataConditionTime = weatherAPI19HourDataConditionTime[0]
    weatherAPI19HourDataTemperature = weatherAPI19HourData['temp_c']
    weatherAPI19HourDataTemperature = round(weatherAPI19HourDataTemperature, 0)
    weatherAPI19HourDataTemperature = int(weatherAPI19HourDataTemperature)
    weatherAPI19HourDataTemperature = str(weatherAPI19HourDataTemperature) + "°C"
    weatherAPI19HourDataCondition = weatherAPI19HourData['condition']
    weatherAPI19HourDataCondition = weatherAPI19HourDataCondition['text']

    regexThunder19Hour = re.findall("Thunder|thunder", weatherAPI19HourDataCondition)
    if regexThunder19Hour != []:
        regexThunder19Hour = regexThunder19Hour[0]
        regexThunder19Hour = regexThunder19Hour.split()
    regexRain19Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI19HourDataCondition)
    if regexRain19Hour != []:
        regexRain19Hour = regexRain19Hour[0]
        regexRain19Hour = regexRain19Hour.split()
    regexCloud19Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI19HourDataCondition)
    if regexCloud19Hour != []:
        regexCloud19Hour = regexCloud19Hour[0]
        regexCloud19Hour = regexCloud19Hour.split()
    regexClear19Hour = re.findall("Clear|clear|Sun|sun", weatherAPI19HourDataCondition)
    if regexClear19Hour != []:
        regexClear19Hour = regexClear19Hour[0]
        regexClear19Hour = regexClear19Hour.split()
    regexSnow19Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI19HourDataCondition)
    if regexSnow19Hour != []:
        regexSnow19Hour = regexSnow19Hour[0]
        regexSnow19Hour = regexSnow19Hour.split()
    regexWind19Hour = re.findall("Wind|wind", weatherAPI19HourDataCondition)
    if regexWind19Hour != []:
        regexWind19Hour = regexWind19Hour[0]
        regexWind19Hour = regexWind19Hour.split()
    regexHail19Hour = re.findall("Hail|hail", weatherAPI19HourDataCondition)
    if regexHail19Hour != []:
        regexHail19Hour = regexHail19Hour[0]
        regexHail19Hour = regexHail19Hour.split()
    regexMist19Hour = re.findall("Mist|mist|Fog|fog", weatherAPI19HourDataCondition)
    if regexMist19Hour != []:
        regexMist19Hour = regexMist19Hour[0]
        regexMist19Hour = regexMist19Hour.split()

    if regexThunder19Hour == ['Thunder'] or regexThunder19Hour == ['thunder']:
        weatherAPI19HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain19Hour == ['Rain'] or regexRain19Hour == ['rain'] or regexRain19Hour == [
        'Shower'] or regexRain19Hour == ['shower'] or regexRain19Hour == ['Drizzle'] or regexRain19Hour == [
        'drizzle']:
        weatherAPI19HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud19Hour == ['Cloud'] or regexCloud19Hour == ['cloud'] or regexCloud19Hour == [
        'Overcast'] or regexCloud19Hour == ['overcast'] or regexCloud19Hour == ['Cloudy'] or regexCloud19Hour == [
        'cloudy']:
        weatherAPI19HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear19Hour == ['Clear'] or regexClear19Hour == ['clear'] or regexClear19Hour == [
        'Sun'] or regexClear19Hour == ['sun']:
        weatherAPI19HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow19Hour == ['Snow'] or regexSnow19Hour == ['snow'] or regexSnow19Hour == [
        'Sleet'] or regexSnow19Hour == ['sleet'] or regexSnow19Hour == ['Blizzard'] or regexSnow19Hour == ['blizzard']:
        weatherAPI19HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind19Hour == ['Wind'] or regexWind19Hour == ['wind']:
        weatherAPI19HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail19Hour == ['Hail'] or regexHail19Hour == ['hail']:
        weatherAPI19HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist19Hour == ['Mist'] or regexMist19Hour == ['mist'] or regexMist19Hour == ['Fog'] or regexMist19Hour == ['fog']:
        weatherAPI19HourDataConditionIcon = "/static/images/mist.svg"


    # 20 Hour Forecast - Similar code as 19 Hour Forecast
    weatherAPI20HourData = weatherAPIData['forecast']
    weatherAPI20HourData = weatherAPI20HourData['forecastday']
    weatherAPI20HourData = weatherAPI20HourData[0]
    weatherAPI20HourData = weatherAPI20HourData['hour']
    weatherAPI20HourData = weatherAPI20HourData[19]
    weatherAPI20HourDataConditionTime = weatherAPI20HourData['time']
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime.split(" ")
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime[1]
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime.split(":")
    weatherAPI20HourDataConditionTime = weatherAPI20HourDataConditionTime[0]
    weatherAPI20HourDataTemperature = weatherAPI20HourData['temp_c']
    weatherAPI20HourDataTemperature = round(weatherAPI20HourDataTemperature, 0)
    weatherAPI20HourDataTemperature = int(weatherAPI20HourDataTemperature)
    weatherAPI20HourDataTemperature = str(weatherAPI20HourDataTemperature) + "°C"
    weatherAPI20HourDataCondition = weatherAPI20HourData['condition']
    weatherAPI20HourDataCondition = weatherAPI20HourDataCondition['text']

    regexThunder20Hour = re.findall("Thunder|thunder", weatherAPI20HourDataCondition)
    if regexThunder20Hour != []:
        regexThunder20Hour = regexThunder20Hour[0]
        regexThunder20Hour = regexThunder20Hour.split()
    regexRain20Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI20HourDataCondition)
    if regexRain20Hour != []:
        regexRain20Hour = regexRain20Hour[0]
        regexRain20Hour = regexRain20Hour.split()
    regexCloud20Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI20HourDataCondition)
    if regexCloud20Hour != []:
        regexCloud20Hour = regexCloud20Hour[0]
        regexCloud20Hour = regexCloud20Hour.split()
    regexClear20Hour = re.findall("Clear|clear|Sun|sun", weatherAPI20HourDataCondition)
    if regexClear20Hour != []:
        regexClear20Hour = regexClear20Hour[0]
        regexClear20Hour = regexClear20Hour.split()
    regexSnow20Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI20HourDataCondition)
    if regexSnow20Hour != []:
        regexSnow20Hour = regexSnow20Hour[0]
        regexSnow20Hour = regexSnow20Hour.split()
    regexWind20Hour = re.findall("Wind|wind", weatherAPI20HourDataCondition)
    if regexWind20Hour != []:
        regexWind20Hour = regexWind20Hour[0]
        regexWind20Hour = regexWind20Hour.split()
    regexHail20Hour = re.findall("Hail|hail", weatherAPI20HourDataCondition)
    if regexHail20Hour != []:
        regexHail20Hour = regexHail20Hour[0]
        regexHail20Hour = regexHail20Hour.split()
    regexMist20Hour = re.findall("Mist|mist|Fog|fog", weatherAPI20HourDataCondition)
    if regexMist20Hour != []:
        regexMist20Hour = regexMist20Hour[0]
        regexMist20Hour = regexMist20Hour.split()

    if regexThunder20Hour == ['Thunder'] or regexThunder20Hour == ['thunder']:
        weatherAPI20HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain20Hour == ['Rain'] or regexRain20Hour == ['rain'] or regexRain20Hour == [
        'Shower'] or regexRain20Hour == ['shower'] or regexRain20Hour == ['Drizzle'] or regexRain20Hour == [
        'drizzle']:
        weatherAPI20HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud20Hour == ['Cloud'] or regexCloud20Hour == ['cloud'] or regexCloud20Hour == [
        'Overcast'] or regexCloud20Hour == ['overcast'] or regexCloud20Hour == ['Cloudy'] or regexCloud20Hour == [
        'cloudy']:
        weatherAPI20HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear20Hour == ['Clear'] or regexClear20Hour == ['clear'] or regexClear20Hour == [
        'Sun'] or regexClear20Hour == ['sun']:
        weatherAPI20HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow20Hour == ['Snow'] or regexSnow20Hour == ['snow'] or regexSnow20Hour == [
        'Sleet'] or regexSnow20Hour == ['sleet'] or regexSnow20Hour == ['Blizzard'] or regexSnow20Hour == ['blizzard']:
        weatherAPI20HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind20Hour == ['Wind'] or regexWind20Hour == ['wind']:
        weatherAPI20HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail20Hour == ['Hail'] or regexHail20Hour == ['hail']:
        weatherAPI20HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist20Hour == ['Mist'] or regexMist20Hour == ['mist'] or regexMist20Hour == ['Fog'] or regexMist20Hour == ['fog']:
        weatherAPI20HourDataConditionIcon = "/static/images/mist.svg"

    # 21 Hour Forecast - Similar code as 20 Hour Forecast
    weatherAPI21HourData = weatherAPIData['forecast']
    weatherAPI21HourData = weatherAPI21HourData['forecastday']
    weatherAPI21HourData = weatherAPI21HourData[0]
    weatherAPI21HourData = weatherAPI21HourData['hour']
    weatherAPI21HourData = weatherAPI21HourData[20]
    weatherAPI21HourDataConditionTime = weatherAPI21HourData['time']
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime.split(" ")
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime[1]
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime.split(":")
    weatherAPI21HourDataConditionTime = weatherAPI21HourDataConditionTime[0]
    weatherAPI21HourDataTemperature = weatherAPI21HourData['temp_c']
    weatherAPI21HourDataTemperature = round(weatherAPI21HourDataTemperature, 0)
    weatherAPI21HourDataTemperature = int(weatherAPI21HourDataTemperature)
    weatherAPI21HourDataTemperature = str(weatherAPI21HourDataTemperature) + "°C"
    weatherAPI21HourDataCondition = weatherAPI21HourData['condition']
    weatherAPI21HourDataCondition = weatherAPI21HourDataCondition['text']

    regexThunder21Hour = re.findall("Thunder|thunder", weatherAPI21HourDataCondition)
    if regexThunder21Hour != []:
        regexThunder21Hour = regexThunder21Hour[0]
        regexThunder21Hour = regexThunder21Hour.split()
    regexRain21Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI21HourDataCondition)
    if regexRain21Hour != []:
        regexRain21Hour = regexRain21Hour[0]
        regexRain21Hour = regexRain21Hour.split()
    regexCloud21Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI21HourDataCondition)
    if regexCloud21Hour != []:
        regexCloud21Hour = regexCloud21Hour[0]
        regexCloud21Hour = regexCloud21Hour.split()
    regexClear21Hour = re.findall("Clear|clear|Sun|sun", weatherAPI21HourDataCondition)
    if regexClear21Hour != []:
        regexClear21Hour = regexClear21Hour[0]
        regexClear21Hour = regexClear21Hour.split()
    regexSnow21Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI21HourDataCondition)
    if regexSnow21Hour != []:
        regexSnow21Hour = regexSnow21Hour[0]
        regexSnow21Hour = regexSnow21Hour.split()
    regexWind21Hour = re.findall("Wind|wind", weatherAPI21HourDataCondition)
    if regexWind21Hour != []:
        regexWind21Hour = regexWind21Hour[0]
        regexWind21Hour = regexWind21Hour.split()
    regexHail21Hour = re.findall("Hail|hail", weatherAPI21HourDataCondition)
    if regexHail21Hour != []:
        regexHail21Hour = regexHail21Hour[0]
        regexHail21Hour = regexHail21Hour.split()
    regexMist21Hour = re.findall("Mist|mist|Fog|fog", weatherAPI21HourDataCondition)
    if regexMist21Hour != []:
        regexMist21Hour = regexMist21Hour[0]
        regexMist21Hour = regexMist21Hour.split()

    if regexThunder21Hour == ['Thunder'] or regexThunder21Hour == ['thunder']:
        weatherAPI21HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain21Hour == ['Rain'] or regexRain21Hour == ['rain'] or regexRain21Hour == [
        'Shower'] or regexRain21Hour == ['shower'] or regexRain21Hour == ['Drizzle'] or regexRain21Hour == [
        'drizzle']:
        weatherAPI21HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud21Hour == ['Cloud'] or regexCloud21Hour == ['cloud'] or regexCloud21Hour == [
        'Overcast'] or regexCloud21Hour == ['overcast'] or regexCloud21Hour == ['Cloudy'] or regexCloud21Hour == [
        'cloudy']:
        weatherAPI21HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear21Hour == ['Clear'] or regexClear21Hour == ['clear'] or regexClear21Hour == [
        'Sun'] or regexClear21Hour == ['sun']:
        weatherAPI21HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow21Hour == ['Snow'] or regexSnow21Hour == ['snow'] or regexSnow21Hour == [
        'Sleet'] or regexSnow21Hour == ['sleet'] or regexSnow21Hour == ['Blizzard'] or regexSnow21Hour == ['blizzard']:
        weatherAPI21HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind21Hour == ['Wind'] or regexWind21Hour == ['wind']:
        weatherAPI21HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail21Hour == ['Hail'] or regexHail21Hour == ['hail']:
        weatherAPI21HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist21Hour == ['Mist'] or regexMist21Hour == ['mist'] or regexMist21Hour == ['Fog'] or regexMist21Hour == ['fog']:
        weatherAPI21HourDataConditionIcon = "/static/images/mist.svg"

    # 22 Hour Forecast - Similar code as 21 Hour Forecast
    weatherAPI22HourData = weatherAPIData['forecast']
    weatherAPI22HourData = weatherAPI22HourData['forecastday']
    weatherAPI22HourData = weatherAPI22HourData[0]
    weatherAPI22HourData = weatherAPI22HourData['hour']
    weatherAPI22HourData = weatherAPI22HourData[21]
    weatherAPI22HourDataConditionTime = weatherAPI22HourData['time']
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime.split(" ")
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime[1]
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime.split(":")
    weatherAPI22HourDataConditionTime = weatherAPI22HourDataConditionTime[0]
    weatherAPI22HourDataTemperature = weatherAPI22HourData['temp_c']
    weatherAPI22HourDataTemperature = round(weatherAPI22HourDataTemperature, 0)
    weatherAPI22HourDataTemperature = int(weatherAPI22HourDataTemperature)
    weatherAPI22HourDataTemperature = str(weatherAPI22HourDataTemperature) + "°C"
    weatherAPI22HourDataCondition = weatherAPI22HourData['condition']
    weatherAPI22HourDataCondition = weatherAPI22HourDataCondition['text']

    regexThunder22Hour = re.findall("Thunder|thunder", weatherAPI22HourDataCondition)
    if regexThunder22Hour != []:
        regexThunder22Hour = regexThunder22Hour[0]
        regexThunder22Hour = regexThunder22Hour.split()
    regexRain22Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI22HourDataCondition)
    if regexRain22Hour != []:
        regexRain22Hour = regexRain22Hour[0]
        regexRain22Hour = regexRain22Hour.split()
    regexCloud22Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI22HourDataCondition)
    if regexCloud22Hour != []:
        regexCloud22Hour = regexCloud22Hour[0]
        regexCloud22Hour = regexCloud22Hour.split()
    regexClear22Hour = re.findall("Clear|clear|Sun|sun", weatherAPI22HourDataCondition)
    if regexClear22Hour != []:
        regexClear22Hour = regexClear22Hour[0]
        regexClear22Hour = regexClear22Hour.split()
    regexSnow22Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI22HourDataCondition)
    if regexSnow22Hour != []:
        regexSnow22Hour = regexSnow22Hour[0]
        regexSnow22Hour = regexSnow22Hour.split()
    regexWind22Hour = re.findall("Wind|wind", weatherAPI22HourDataCondition)
    if regexWind22Hour != []:
        regexWind22Hour = regexWind22Hour[0]
        regexWind22Hour = regexWind22Hour.split()
    regexHail22Hour = re.findall("Hail|hail", weatherAPI22HourDataCondition)
    if regexHail22Hour != []:
        regexHail22Hour = regexHail22Hour[0]
        regexHail22Hour = regexHail22Hour.split()
    regexMist22Hour = re.findall("Mist|mist|Fog|fog", weatherAPI22HourDataCondition)
    if regexMist22Hour != []:
        regexMist22Hour = regexMist22Hour[0]
        regexMist22Hour = regexMist22Hour.split()

    if regexThunder22Hour == ['Thunder'] or regexThunder22Hour == ['thunder']:
        weatherAPI22HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain22Hour == ['Rain'] or regexRain22Hour == ['rain'] or regexRain22Hour == [
        'Shower'] or regexRain22Hour == ['shower'] or regexRain22Hour == ['Drizzle'] or regexRain22Hour == [
        'drizzle']:
        weatherAPI22HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud22Hour == ['Cloud'] or regexCloud22Hour == ['cloud'] or regexCloud22Hour == [
        'Overcast'] or regexCloud22Hour == ['overcast'] or regexCloud22Hour == ['Cloudy'] or regexCloud22Hour == [
        'cloudy']:
        weatherAPI22HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear22Hour == ['Clear'] or regexClear22Hour == ['clear'] or regexClear22Hour == [
        'Sun'] or regexClear22Hour == ['sun']:
        weatherAPI22HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow22Hour == ['Snow'] or regexSnow22Hour == ['snow'] or regexSnow22Hour == [
        'Sleet'] or regexSnow22Hour == ['sleet'] or regexSnow22Hour == ['Blizzard'] or regexSnow22Hour == ['blizzard']:
        weatherAPI22HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind22Hour == ['Wind'] or regexWind22Hour == ['wind']:
        weatherAPI22HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail22Hour == ['Hail'] or regexHail22Hour == ['hail']:
        weatherAPI22HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist22Hour == ['Mist'] or regexMist22Hour == ['mist'] or regexMist22Hour == ['Fog'] or regexMist22Hour == ['fog']:
        weatherAPI22HourDataConditionIcon = "/static/images/mist.svg"

    # 23 Hour Forecast - Similar code as 22 Hour Forecast
    weatherAPI23HourData = weatherAPIData['forecast']
    weatherAPI23HourData = weatherAPI23HourData['forecastday']
    weatherAPI23HourData = weatherAPI23HourData[0]
    weatherAPI23HourData = weatherAPI23HourData['hour']
    weatherAPI23HourData = weatherAPI23HourData[22]
    weatherAPI23HourDataConditionTime = weatherAPI23HourData['time']
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime.split(" ")
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime[1]
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime.split(":")
    weatherAPI23HourDataConditionTime = weatherAPI23HourDataConditionTime[0]
    weatherAPI23HourDataTemperature = weatherAPI23HourData['temp_c']
    weatherAPI23HourDataTemperature = round(weatherAPI23HourDataTemperature, 0)
    weatherAPI23HourDataTemperature = int(weatherAPI23HourDataTemperature)
    weatherAPI23HourDataTemperature = str(weatherAPI23HourDataTemperature) + "°C"
    weatherAPI23HourDataCondition = weatherAPI23HourData['condition']
    weatherAPI23HourDataCondition = weatherAPI23HourDataCondition['text']

    regexThunder23Hour = re.findall("Thunder|thunder", weatherAPI23HourDataCondition)
    if regexThunder23Hour != []:
        regexThunder23Hour = regexThunder23Hour[0]
        regexThunder23Hour = regexThunder23Hour.split()
    regexRain23Hour = re.findall("Rain|rain|Shower|shower|Drizzle|drizzle", weatherAPI23HourDataCondition)
    if regexRain23Hour != []:
        regexRain23Hour = regexRain23Hour[0]
        regexRain23Hour = regexRain23Hour.split()
    regexCloud23Hour = re.findall("Cloud|cloud|Overcast|overcast|Cloudy|cloudy", weatherAPI23HourDataCondition)
    if regexCloud23Hour != []:
        regexCloud23Hour = regexCloud23Hour[0]
        regexCloud23Hour = regexCloud23Hour.split()
    regexClear23Hour = re.findall("Clear|clear|Sun|sun", weatherAPI23HourDataCondition)
    if regexClear23Hour != []:
        regexClear23Hour = regexClear23Hour[0]
        regexClear23Hour = regexClear23Hour.split()
    regexSnow23Hour = re.findall("Snow|snow|Sleet|sleet|Blizzard|blizzard", weatherAPI23HourDataCondition)
    if regexSnow23Hour != []:
        regexSnow23Hour = regexSnow23Hour[0]
        regexSnow23Hour = regexSnow23Hour.split()
    regexWind23Hour = re.findall("Wind|wind", weatherAPI23HourDataCondition)
    if regexWind23Hour != []:
        regexWind23Hour = regexWind23Hour[0]
        regexWind23Hour = regexWind23Hour.split()
    regexHail23Hour = re.findall("Hail|hail", weatherAPI23HourDataCondition)
    if regexHail23Hour != []:
        regexHail23Hour = regexHail23Hour[0]
        regexHail23Hour = regexHail23Hour.split()
    regexMist23Hour = re.findall("Mist|mist|Fog|fog", weatherAPI23HourDataCondition)
    if regexMist23Hour != []:
        regexMist23Hour = regexMist23Hour[0]
        regexMist23Hour = regexMist23Hour.split()

    if regexThunder23Hour == ['Thunder'] or regexThunder23Hour == ['thunder']:
        weatherAPI23HourDataConditionIcon = "/static/images/thunderstorms.svg"
    elif regexRain23Hour == ['Rain'] or regexRain23Hour == ['rain'] or regexRain23Hour == [
        'Shower'] or regexRain23Hour == ['shower'] or regexRain23Hour == ['Drizzle'] or regexRain23Hour == [
        'drizzle']:
        weatherAPI23HourDataConditionIcon = "/static/images/rain.svg"
    elif regexCloud23Hour == ['Cloud'] or regexCloud23Hour == ['cloud'] or regexCloud23Hour == [
        'Overcast'] or regexCloud23Hour == ['overcast'] or regexCloud23Hour == ['Cloudy'] or regexCloud23Hour == [
        'cloudy']:
        weatherAPI23HourDataConditionIcon = "/static/images/cloudy.svg"
    elif regexClear23Hour == ['Clear'] or regexClear23Hour == ['clear'] or regexClear23Hour == [
        'Sun'] or regexClear23Hour == ['sun']:
        weatherAPI23HourDataConditionIcon = "/static/images/sunny.svg"
    elif regexSnow23Hour == ['Snow'] or regexSnow23Hour == ['snow'] or regexSnow23Hour == [
        'Sleet'] or regexSnow23Hour == ['sleet'] or regexSnow23Hour == ['Blizzard'] or regexSnow23Hour == ['blizzard']:
        weatherAPI23HourDataConditionIcon = "/static/images/snow.svg"
    elif regexWind23Hour == ['Wind'] or regexWind23Hour == ['wind']:
        weatherAPI23HourDataConditionIcon = "/static/images/wind.svg"
    elif regexHail23Hour == ['Hail'] or regexHail23Hour == ['hail']:
        weatherAPI23HourDataConditionIcon = "/static/images/hailstones.svg"
    elif regexMist23Hour == ['Mist'] or regexMist23Hour == ['mist'] or regexMist23Hour == ['Fog'] or regexMist23Hour == ['fog']:
        weatherAPI23HourDataConditionIcon = "/static/images/mist.svg"


    try: # Pollen Count Data API
        conn = http.client.HTTPSConnection("api.ambeedata.com") # API Connection

        headers = {
            'x-api-key': "01a4c1eae8cb507b14ee10ecd1b2c3984e8368ede6224aa2ffcd3d9ada2ce3d7",
            'Content-type': "application/json"
        } # API Headers

        conn.request("GET", "/latest/pollen/by-lat-lng?lat=52.05892202630986&lng=1.2847627151273548", headers=headers) # API Request

        res = conn.getresponse() # API Response
        data = res.read() # API Data

        pollenData = data.decode("utf-8") # API Data Decode
        pollenData = ast.literal_eval(pollenData) # API Data Literal Evaluation
        pollenData = pollenData['data'] # Pollen Data
        pollenData = pollenData[0]  # Pollen Data
        pollenRisk = pollenData['Risk'] # Pollen Risk
        pollenRiskGrass = pollenRisk['grass_pollen'] # Pollen Risk Grass
        pollenRiskTree = pollenRisk['tree_pollen'] # Pollen Risk Tree
        pollenRiskWeed = pollenRisk['weed_pollen'] # Pollen Risk Weeds
        pollenRisk = str(pollenRisk)

        # Set Pollen Risk Level for each pollen type
        # Set Pollen Risk Level for grass pollen
        if "Extreme" in pollenRiskGrass:
            pollenRiskLevelGrass = "Extreme"
        elif "Very High" in pollenRiskGrass or "Very high" in pollenRiskGrass:
            pollenRiskLevelGrass = "Very High"
        elif "High" in pollenRiskGrass:
            pollenRiskLevelGrass = "High"
        elif "Moderate" in pollenRiskGrass:
            pollenRiskLevelGrass = "Moderate"
        elif "Low" in pollenRiskGrass:
            pollenRiskLevelGrass = "Low"

        # Set Pollen Risk Level for tree pollen
        if "Extreme" in pollenRiskTree:
            pollenRiskLevelTree = "Extreme"
        elif "Very High" in pollenRiskTree or "Very high" in pollenRiskTree:
            pollenRiskLevelTree = "Very High"
        elif "High" in pollenRiskTree:
            pollenRiskLevelTree = "High"
        elif "Moderate" in pollenRiskTree:
            pollenRiskLevelTree = "Moderate"
        elif "Low" in pollenRiskTree:
            pollenRiskLevelTree = "Low"

        # Set Pollen Risk Level for weed pollen
        if "Extreme" in pollenRiskWeed:
            pollenRiskLevelWeed = "Extreme"
        elif "Very High" in pollenRiskWeed or "Very high" in pollenRiskWeed:
            pollenRiskLevelWeed = "Very High"
        elif "High" in pollenRiskWeed:
            pollenRiskLevelWeed = "High"
        elif "Moderate" in pollenRiskWeed:
            pollenRiskLevelWeed = "Moderate"
        elif "Low" in pollenRiskWeed:
            pollenRiskLevelWeed = "Low"


        pollenCount = pollenData['Count'] # Pollen Count
        pollenCountTree = pollenCount['tree_pollen'] # Pollen Count Tree
        pollenCountGrass = pollenCount['grass_pollen'] # Pollen Count Grass
        pollenCountWeed = pollenCount['weed_pollen'] # Pollen Count Weeds

        # Set Pollen Count for each pollen type (percentage and bar chart colour)
        # Set Pollen Count for tree pollen
        if pollenCountTree == 0:
            pollenCountTreePercentage = "0%"
            pollenCountColourTree = "#4CAF50" # Green
        elif pollenRiskLevelTree == "Low":
            pollenCountTreePercentage = "25%"
            pollenCountColourTree = "#4CAF50" # Green
        elif pollenRiskLevelTree == "Moderate":
            pollenCountTreePercentage = "50%"
            pollenCountColourTree = "#FFEB3B" # Yellow
        elif pollenRiskLevelTree == "High":
            pollenCountTreePercentage = "75%"
            pollenCountColourTree = "#FF9800" # Orange
        elif pollenRiskLevelTree == "Very High" or pollenRiskLevelTree == "Extreme":
            pollenCountTreePercentage = "100%"
            pollenCountColourTree = "#D84315" # Red

        # Set Pollen Count for grass pollen
        if pollenCountGrass == 0:
            pollenCountGrassPercentage = "0%"
            pollenCountColourGrass = "#4CAF50"
        elif pollenRiskLevelGrass == "Low":
            pollenCountGrassPercentage = "25%"
            pollenCountColourGrass = "#4CAF50"
        elif pollenRiskLevelGrass == "Moderate":
            pollenCountGrassPercentage = "50%"
            pollenCountColourGrass = "#FFEB3B"
        elif pollenRiskLevelGrass == "High":
            pollenCountGrassPercentage = "75%"
            pollenCountColourGrass = "#FF9800"
        elif pollenRiskLevelGrass == "Very High" or pollenRiskLevelGrass == "Extreme":
            pollenCountGrassPercentage = "100%"
            pollenCountColourGrass = "#D84315"

        # Set Pollen Count for weed pollen
        if pollenCountWeed == 0:
            pollenCountWeedPercentage = "0%"
            pollenCountColourWeed = "#4CAF50"
        elif pollenRiskLevelWeed == "Low":
            pollenCountWeedPercentage = "25%"
            pollenCountColourWeed = "#4CAF50"
        elif pollenRiskLevelWeed == "Moderate":
            pollenCountWeedPercentage = "50%"
            pollenCountColourWeed = "#FFEB3B"
        elif pollenRiskLevelWeed == "High":
            pollenCountWeedPercentage = "75%"
            pollenCountColourWeed = "#FF9800"
        elif pollenRiskLevelWeed == "Very High" or pollenRiskLevelWeed == "Extreme":
            pollenCountWeedPercentage = "100%"
            pollenCountColourWeed = "#D84315"


    except UnboundLocalError: # Error Handling for Pollen Count Data API is API is not available
        pollenRiskLevel = "Error Retrieving Pollen Count"
        pollenCountValue = "N/A"
        pollenCountPercentage = "0%"
        pollenCountColour = "#000000"
        pollenCountGrass = "N/A"
        pollenCountTree = "N/A"
        pollenCountWeed = "N/A"
        pollenCountGrassPercentage = "0%"
        pollenCountColourGrass = "#000000"
        pollenCountTreePercentage = "0%"
        pollenCountColourTree = "#000000"
        pollenCountWeedPercentage = "0%"
        pollenCountColourWeed = "#000000"
        pollenRiskLevelTree = "Error Retrieving Pollen Count"
        pollenRiskLevelGrass = "Error Retrieving Pollen Count"
        pollenRiskLevelWeed = "Error Retrieving Pollen Count"
        #x = {'a':1, 'b':2}
        #y = x['c']

    except KeyError:
        pollenRiskLevel = "Error Retrieving Pollen Count"
        pollenCountValue = "N/A"
        pollenCountPercentage = "0%"
        pollenCountColour = "#000000"
        pollenCountGrass = "N/A"
        pollenCountTree = "N/A"
        pollenCountWeed = "N/A"
        pollenCountGrassPercentage = "0%"
        pollenCountColourGrass = "#000000"
        pollenCountTreePercentage = "0%"
        pollenCountColourTree = "#000000"
        pollenCountWeedPercentage = "0%"
        pollenCountColourWeed = "#000000"
        pollenRiskLevelTree = "Error Retrieving Pollen Count"
        pollenRiskLevelGrass = "Error Retrieving Pollen Count"
        pollenRiskLevelWeed = "Error Retrieving Pollen Count"

    # Set data to be passed to the front end
    data = strTemperatureCelsius1, strHumidity, aqi, aqi_description, strWindSpeed, windDirectionDescription, UV_index, UV_index_description, UV_index_percentage, UV_index_colour, aqi_percentage, aqi_colour, compass, strTemperatureFarenheit, strWindSpeedKMH, openWeatherDataToday, temperatureforecastToday, weatherConditionsTodayIcon, tomorrowDate, weatherConditionsTomorrowIcon, temperatureforecastTomorrow, tomorrowWindSpeed, tomorrowWindDirectionDescription, tomorrowHumidity, ThreeDayDate, weatherConditionsThreeDayIcon, temperatureforecastThreeDay, ThreeDayWindSpeed, ThreeDayWindDirectionDescription, ThreeDayHumidity, FourDayDate, weatherConditionsFourDayIcon, temperatureforecastFourDay, FourDayWindSpeed, FourDayWindDirectionDescription, FourDayHumidity, FiveDayDate, weatherConditionsFiveDayIcon, temperatureforecastFiveDay, FiveDayWindSpeed, FiveDayWindDirectionDescription, FiveDayHumidity, SixDayDate, weatherConditionsSixDayIcon, temperatureforecastSixDay, SixDayWindSpeed, SixDayWindDirectionDescription, SixDayHumidity, weatherAPIDataCurrentTemperature, weatherAPIDataCurrentConditionIcon, weatherAPI01HourDataConditionTime, weatherAPI01HourDataTemperature, weatherAPI01HourDataConditionIcon, weatherAPI02HourDataConditionTime, weatherAPI02HourDataTemperature, weatherAPI02HourDataConditionIcon, weatherAPI03HourDataConditionTime, weatherAPI03HourDataTemperature, weatherAPI03HourDataConditionIcon, weatherAPI04HourDataConditionTime, weatherAPI04HourDataTemperature, weatherAPI04HourDataConditionIcon, weatherAPI05HourDataConditionTime, weatherAPI05HourDataTemperature, weatherAPI05HourDataConditionIcon, weatherAPI06HourDataConditionTime, weatherAPI06HourDataTemperature, weatherAPI06HourDataConditionIcon, weatherAPI07HourDataConditionTime, weatherAPI07HourDataTemperature, weatherAPI07HourDataConditionIcon, weatherAPI08HourDataConditionTime, weatherAPI08HourDataTemperature, weatherAPI08HourDataConditionIcon, weatherAPI09HourDataConditionTime, weatherAPI09HourDataTemperature, weatherAPI09HourDataConditionIcon, weatherAPI10HourDataConditionTime, weatherAPI10HourDataTemperature, weatherAPI10HourDataConditionIcon, weatherAPI11HourDataConditionTime, weatherAPI11HourDataTemperature, weatherAPI11HourDataConditionIcon, weatherAPI12HourDataConditionTime, weatherAPI12HourDataTemperature, weatherAPI12HourDataConditionIcon, weatherAPI13HourDataConditionTime, weatherAPI13HourDataTemperature, weatherAPI13HourDataConditionIcon, weatherAPI14HourDataConditionTime, weatherAPI14HourDataTemperature, weatherAPI14HourDataConditionIcon, weatherAPI15HourDataConditionTime, weatherAPI15HourDataTemperature, weatherAPI15HourDataConditionIcon, weatherAPI16HourDataConditionTime, weatherAPI16HourDataTemperature, weatherAPI16HourDataConditionIcon, weatherAPI17HourDataConditionTime, weatherAPI17HourDataTemperature, weatherAPI17HourDataConditionIcon, weatherAPI18HourDataConditionTime, weatherAPI18HourDataTemperature, weatherAPI18HourDataConditionIcon, weatherAPI19HourDataConditionTime, weatherAPI19HourDataTemperature, weatherAPI19HourDataConditionIcon, weatherAPI20HourDataConditionTime, weatherAPI20HourDataTemperature, weatherAPI20HourDataConditionIcon, weatherAPI21HourDataConditionTime, weatherAPI21HourDataTemperature, weatherAPI21HourDataConditionIcon, weatherAPI22HourDataConditionTime, weatherAPI22HourDataTemperature, weatherAPI22HourDataConditionIcon, weatherAPI23HourDataConditionTime, weatherAPI23HourDataTemperature, weatherAPI23HourDataConditionIcon, strPressure, angle, weatherConditionsToday, strPrecipitationProbability, strVisibilityKM, strVisibilityMiles, visibilityDescription, pollenRiskLevelGrass, pollenCountGrass, pollenCountGrassPercentage, pollenCountColourGrass, pollenRiskLevelTree, pollenCountTree, pollenCountTreePercentage, pollenCountColourTree, pollenRiskLevelWeed, pollenCountWeed, pollenCountWeedPercentage, pollenCountColourWeed, strPrecipitationProbabilityTomorrow, strPrecipitationProbabilityThreeDay, strPrecipitationProbabilityFourDay, strPrecipitationProbabilityFiveDay, strPrecipitationProbabilitySixDay, strFeelsLikeCelcius, strFeelsLikeFarenheit, todayDate


    # Return data to the front end
    return render_template('weather.html', data=data)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    """Backend for temperature page using WeatherLink API"""
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb' # WeatherLink API key
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy' # WeatherLink API secret
    station_id = 142820 # Weather station ID

    # current time
    local_time = int(time.time()) # set local current time

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest() # generate signature

    url = f"https://api.weatherlink.com/v2/current/{station_id}" # set WeatherLink API url
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    } # set parameters

    response = requests.get(url, params=params) # get response from WeatherLink API
    current_weather = response.json() # get current weather data
    sensors = current_weather['sensors'] # get sensor data
    sensors = sensors[2] # get sensor data from indoor sensor
    sensorData = sensors['data'] # get sensor data
    sensorData = sensorData[0] # get sensor data
    temperatureFarenheit1 = sensorData['temp'] # get indoor temperature in Farenheit from sensor
    temperatureCelsius = (temperatureFarenheit1 - 32) * 5.0/9.0 # convert Farenheit to Celsius
    temperatureCelsius1 = round(temperatureCelsius, 1) # round to 1 decimal place
    strTemperatureCelsius1 = str(temperatureCelsius1) + "°C" # convert celcius temperature to string
    strTemperatureFarenheit1 = str(temperatureFarenheit1) + "°F" # convert farenheit temperature to string
    current_weather = response.json() # get current weather data
    sensors = current_weather['sensors'] # get sensor data
    sensors = sensors[4] # get sensor data from outdoor sensor
    sensorData = sensors['data'] # get sensor data
    sensorData = sensorData[0] # get sensor data
    temperatureFarenheit2 = sensorData['temp'] # get outdoor temperature in Farenheit from sensor
    temperatureCelsius = (temperatureFarenheit2 - 32) * 5.0 / 9.0 # convert Farenheit to Celsius
    temperatureCelsius2 = round(temperatureCelsius, 1)  # round to 1 decimal place
    strTemperatureCelsius2 = str(temperatureCelsius2) + "°C" # convert celcius temperature to string
    strTemperatureFarenheit2 = str(temperatureFarenheit2) + "°F" # convert farenheit temperature to string



    with open('Weather_Link_Outdoor.csv', mode='r', encoding = 'latin') as file: # open WeatherLink CSV file
        csvFile = csv.reader(file) # read CSV file
        jsonFile = [] # create empty list
        for lines in csvFile: # loop through CSV file
            jsonFile.append(lines) # append lines to list


        temperatures24Hours = [] # create empty list of temperatures
        timeHours = [] # create empty list of hours
        pointerTemperature = 1 # set temperature pointer to 1
        pointerTime = 1 # set time pointer to 1
        csvLength = len(jsonFile) # get length of CSV file

        for i in range(1, 25): # loop through last 24 hours of data
            lastLine = jsonFile[csvLength - pointerTemperature] # get last line of data
            lastLineTemperature = lastLine[1] # get last line temperature
            lastLineTemperature = int(lastLineTemperature) # convert temperature to integer
            lastLineTime = lastLine[0] # get last line time
            timeHour = lastLineTime.split(" ") # split time by space
            timeHour = timeHour[1] # get time
            timeHour = timeHour.split(":") # split time by colon
            timeHour = timeHour[0] # get hour
            timeHours.append(timeHour) # append hour to list of hours
            temperatures24Hours.append(lastLineTemperature) # append temperature to list of temperatures
            pointerTemperature += 12 # increment temperature pointer
            pointerTime += 12 # increment time pointer
            temperatureData = {"hour": timeHour, "temperature": lastLineTemperature}

        graphtest = [{'hour': '00', 'temperature': 8},]

        # Get the hourly humidity data for the last 24 hours
        print(type(temperatures24Hours))
        print("Hourly Temperatures: ", temperatures24Hours)
        print(type(timeHours))
        print("Time in Hours: ", timeHours)
        hour0 = timeHours[0]
        temperature0 = temperatures24Hours[0]
        hour1 = timeHours[1]
        temperature1 = temperatures24Hours[1]
        hour2 = timeHours[2]
        temperature2 = temperatures24Hours[2]
        hour3 = timeHours[3]
        temperature3 = temperatures24Hours[3]
        hour4 = timeHours[4]
        temperature4 = temperatures24Hours[4]
        hour5 = timeHours[5]
        temperature5 = temperatures24Hours[5]
        hour6 = timeHours[6]
        temperature6 = temperatures24Hours[6]
        hour7 = timeHours[7]
        temperature7 = temperatures24Hours[7]
        hour8 = timeHours[8]
        temperature8 = temperatures24Hours[8]
        hour9 = timeHours[9]
        temperature9 = temperatures24Hours[9]
        hour10 = timeHours[10]
        temperature10 = temperatures24Hours[10]
        hour11 = timeHours[11]
        temperature11 = temperatures24Hours[11]
        hour12 = timeHours[12]
        temperature12 = temperatures24Hours[12]
        hour13 = timeHours[13]
        temperature13 = temperatures24Hours[13]
        hour14 = timeHours[14]
        temperature14 = temperatures24Hours[14]
        hour15 = timeHours[15]
        temperature15 = temperatures24Hours[15]
        hour16 = timeHours[16]
        temperature16 = temperatures24Hours[16]
        hour17 = timeHours[17]
        temperature17 = temperatures24Hours[17]
        hour18 = timeHours[18]
        temperature18 = temperatures24Hours[18]
        hour19 = timeHours[19]
        temperature19 = temperatures24Hours[19]
        hour20 = timeHours[20]
        temperature20 = temperatures24Hours[20]
        hour21 = timeHours[21]
        temperature21 = temperatures24Hours[21]
        hour22 = timeHours[22]
        temperature22 = temperatures24Hours[22]
        hour23 = timeHours[23]
        temperature23 = temperatures24Hours[23]

        pointerDate = 1 # set date pointer to 1
        pointerTemperature = 1 # set temperature pointer to 1
        dateDaily = [] # create empty list of dates
        temperatureDaily = [] # create empty list of temperatures
        csvLength = len(jsonFile) # get length of CSV file

        for i in range(1, 31): # loop through last 30 days of data
            lastLine = jsonFile[csvLength - pointerDate] # get last line of data
            lastLineDate = lastLine[0] # get last line date
            lastLineTemperature = lastLine[1] # get last line temperature
            lastLineTemperature = int(lastLineTemperature)  # convert temperature to integer
            dateDaily.append(lastLineDate) # append date to list of dates
            temperatureDaily.append(lastLineTemperature) # append temperature to list of temperatures
            pointerDate += 288 # increment date pointer
            pointerTemperature += 288 # increment temperature pointer
            temperatureData = {"date": lastLineDate, "temperature": lastLineTemperature}

        graphtest = [{'hour': '00', 'temperature': 8},]

        # Get the daily temperature data for the last 30 days
        print(type(temperatureDaily))
        print("Daily Temperatures: ", temperatureDaily)
        print(type(dateDaily))
        print("Days: ", dateDaily)
        temperatureDay0 = temperatureDaily[0]
        temperatureDay1 = temperatureDaily[1]
        temperatureDay2 = temperatureDaily[2]
        temperatureDay3 = temperatureDaily[3]
        temperatureDay4 = temperatureDaily[4]
        temperatureDay5 = temperatureDaily[5]
        temperatureDay6 = temperatureDaily[6]
        temperatureDay7 = temperatureDaily[7]
        temperatureDay8 = temperatureDaily[8]
        temperatureDay9 = temperatureDaily[9]
        temperatureDay10 = temperatureDaily[10]
        temperatureDay11 = temperatureDaily[11]
        temperatureDay12 = temperatureDaily[12]
        temperatureDay13 = temperatureDaily[13]
        temperatureDay14 = temperatureDaily[14]
        temperatureDay15 = temperatureDaily[15]
        temperatureDay16 = temperatureDaily[16]
        temperatureDay17 = temperatureDaily[17]
        temperatureDay18 = temperatureDaily[18]
        temperatureDay19 = temperatureDaily[19]
        temperatureDay20 = temperatureDaily[20]
        temperatureDay21 = temperatureDaily[21]
        temperatureDay22 = temperatureDaily[22]
        temperatureDay23 = temperatureDaily[23]
        temperatureDay24 = temperatureDaily[24]
        temperatureDay25 = temperatureDaily[25]
        temperatureDay26 = temperatureDaily[26]
        temperatureDay27 = temperatureDaily[27]
        temperatureDay28 = temperatureDaily[28]
        temperatureDay29 = temperatureDaily[29]


    pointerMonth = 6 # set month pointer to 6
    pointerTemperature = 1 # set temperature pointer to 1
    months = [] # create empty list of months
    temperaturesMonthly = [] # create empty list of temperatures
    csvLength = len(jsonFile) # get length of CSV file

    firstLine = jsonFile[pointerMonth] # get first line of data

    for i in range(len(jsonFile)): # loop through all data
        if pointerMonth < 52864: #Check if the pointer is less than the length of the CSV file
            firstLine = jsonFile[pointerMonth] # get first line of data
            firstLineMonth = firstLine[0] # get first line month
            pointerMonth += 1 # increment month pointer
            if '1/1/23 12:00' in firstLineMonth: # check if first line month is January
                if '11/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                elif '21/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                elif '31/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                else: # if first line month is January
                    firstLineTemperature = firstLine[1] # get first line temperature
                    temperaturesMonthly.append(firstLineTemperature) # append temperature to list of temperatures
                    firstLineMonth = "Jan" # set first line month to January
                    months.append(firstLineMonth) # append month to list of months
            elif '1/2/23 12:00' in firstLineMonth: # check if first line month is February (repeated code for each month)
                if '11/2/23 12:00' in firstLineMonth:
                    pass
                elif '21/2/23 12:00' in firstLineMonth:
                    pass
                elif '31/2/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Feb"
                    months.append(firstLineMonth)
            elif '1/3/23 12:00' in firstLineMonth: # check if first line month is March (repeated code for each month)
                if '11/3/23 12:00' in firstLineMonth:
                    pass
                elif '21/3/23 12:00' in firstLineMonth:
                    pass
                elif '31/3/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Mar"
                    months.append(firstLineMonth)
            elif '1/4/23 12:00' in firstLineMonth: # check if first line month is April (repeated code for each month)
                if '11/4/23 12:00' in firstLineMonth:
                    pass
                elif '21/4/23 12:00' in firstLineMonth:
                    pass
                elif '31/4/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Apr"
                    months.append(firstLineMonth)
            elif '3/5/23 17:15' in firstLineMonth: # check if first line month is May (repeated code for each month)
                if '13/5/23 17:15' in firstLineMonth:
                    pass
                elif '23/5/23 17:15' in firstLineMonth:
                    pass
                elif '31/5/23 17:15' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "May"
                    months.append(firstLineMonth)
            elif '1/6/23 12:00' in firstLineMonth: # check if first line month is June (repeated code for each month)
                if '11/6/23 12:00' in firstLineMonth:
                    pass
                elif '21/6/23 12:00' in firstLineMonth:
                    pass
                elif '31/6/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Jun"
                    months.append(firstLineMonth)
            elif '1/7/23 12:00' in firstLineMonth: # check if first line month is July (repeated code for each month)
                if '11/7/23 12:00' in firstLineMonth:
                    pass
                elif '21/7/23 12:00' in firstLineMonth:
                    pass
                elif '31/7/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Jul"
                    months.append(firstLineMonth)
            elif '1/8/23 12:00' in firstLineMonth: # check if first line month is August (repeated code for each month)
                if '11/8/23 12:00' in firstLineMonth:
                    pass
                elif '21/8/23 12:00' in firstLineMonth:
                    pass
                elif '31/8/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Aug"
                    months.append(firstLineMonth)
            elif '1/9/23 12:00' in firstLineMonth: # check if first line month is September (repeated code for each month)
                if '11/9/23 12:00' in firstLineMonth:
                    pass
                elif '21/9/23 12:00' in firstLineMonth:
                    pass
                elif '31/9/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Sep"
                    months.append(firstLineMonth)
            elif '1/10/23 12:00' in firstLineMonth: # check if first line month is October (repeated code for each month)
                if '11/10/23 12:00' in firstLineMonth:
                    pass
                elif '21/10/23 12:00' in firstLineMonth:
                    pass
                elif '31/10/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Oct"
                    months.append(firstLineMonth)
            elif '1/11/23 12:00' in firstLineMonth: # check if first line month is November (repeated code for each month)
                if '11/11/23 12:00' in firstLineMonth:
                    pass
                elif '21/11/23 12:00' in firstLineMonth:
                    pass
                elif '31/11/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Nov"
                    months.append(firstLineMonth)
            elif '1/12/23 12:00' in firstLineMonth: # check if first line month is December (repeated code for each month)
                if '11/12/23 12:00' in firstLineMonth:
                    pass
                elif '21/12/23 12:00' in firstLineMonth:
                    pass
                elif '31/12/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineTemperature = firstLine[1]
                    temperaturesMonthly.append(firstLineTemperature)
                    firstLineMonth = "Dec"
                    months.append(firstLineMonth)


    # Get the monthly temperature data for the last 12 months
    print(type(temperaturesMonthly))
    print("Monthly Temperatures: ", temperaturesMonthly)
    temperatureMonth1 = temperaturesMonthly[0]
    temperatureMonth2 = temperaturesMonthly[1]
    temperatureMonth3 = temperaturesMonthly[2]
    temperatureMonth4 = temperaturesMonthly[3]
    temperatureMonth5 = temperaturesMonthly[4]
    temperatureMonth6 = temperaturesMonthly[5]
    temperatureMonth7 = temperaturesMonthly[6]
    temperatureMonth8 = temperaturesMonthly[7]
    temperatureMonth9 = temperaturesMonthly[8]
    temperatureMonth10 = temperaturesMonthly[9]
    temperatureMonth11 = temperaturesMonthly[10]

    # Create a string of the humidity data to pass to the front end
    data = strTemperatureCelsius1, strTemperatureCelsius2, strTemperatureFarenheit1, strTemperatureFarenheit2, graphtest, hour0, temperature0, hour1, temperature1, hour2, temperature2, hour3, temperature3, hour4, temperature4, hour5, temperature5, hour6, temperature6, hour7, temperature7, hour8, temperature8, hour9, temperature9, hour10, temperature10, hour11, temperature11, hour12, temperature12, hour13, temperature13, hour14, temperature14, hour15, temperature15, hour16, temperature16, hour17, temperature17, hour18, temperature18, hour19, temperature19, hour20, temperature20, hour21, temperature21, hour22, temperature22, hour23, temperature23, temperatureDay0, temperatureDay1, temperatureDay2, temperatureDay3, temperatureDay4, temperatureDay5, temperatureDay6, temperatureDay7, temperatureDay8, temperatureDay9, temperatureDay10, temperatureDay11, temperatureDay12, temperatureDay13, temperatureDay14, temperatureDay15, temperatureDay16, temperatureDay17, temperatureDay18, temperatureDay19, temperatureDay20, temperatureDay21, temperatureDay22, temperatureDay23, temperatureDay24, temperatureDay25, temperatureDay26, temperatureDay27, temperatureDay28, temperatureDay29, temperatureMonth1, temperatureMonth2, temperatureMonth3, temperatureMonth4, temperatureMonth5, temperatureMonth6, temperatureMonth7, temperatureMonth8, temperatureMonth9, temperatureMonth10, temperatureMonth11



    return render_template('temperature.html', data=data) # render the temperature page with the data

@app.route('/humidity', methods=['GET', 'POST'])
def humidity():
    """Backend for humidity page using WeatherLink API"""
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb' #WeatherLink API Key
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy' #WeatherLink API Secret
    station_id = 142820 #Weather Station ID

    # current time
    local_time = int(time.time()) #Get the current local time

    # api signature to authenticate the request
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}" #WeatherLink API URL
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    } #Parameters for the API request

    response = requests.get(url, params=params) #Send the request to the WeatherLink API
    current_weather = response.json() #Get the JSON response from the API
    sensors = current_weather['sensors'] #Get the sensor data from the JSON response
    sensors = sensors[2] #Get the sensor data from indoor sensor
    sensorData = sensors['data'] #Get the sensor data from the indoor sensor
    sensorData = sensorData[0] #Get the sensor data from the indoor sensor
    humidity1 = sensorData['hum'] #Get the humidity data from the indoor sensor
    strHumidity1 = str(humidity1) + "%" #Convert the humidity data to a string
    current_weather = response.json() #Get the JSON response from the API
    sensors = current_weather['sensors'] #Get the sensor data from the JSON response
    sensors = sensors[4] #Get the sensor data from outdoor sensor
    sensorData = sensors['data'] #Get the sensor data from the outdoor sensor
    sensorData = sensorData[0] #Get the sensor data from the outdoor sensor
    humidity2 = sensorData['hum'] #Get the humidity data from the outdoor sensor
    strHumidity2 = str(humidity2) + "%" #Convert the humidity data to a string


    averageHumidity = (humidity1 + humidity2) / 2
    averageHumidity = round(averageHumidity, 1)
    strAverageHumidity = str(averageHumidity) + "%"

    with open('Weather_Link_Outdoor.csv', mode='r', encoding = 'latin') as file: #Open the WeatherLink historic data CSV file
        csvFile = csv.reader(file) #Read the CSV file
        jsonFile = [] #Create an empty list to store the CSV data
        for lines in csvFile: #Loop through the CSV file
            jsonFile.append(lines) #Append the CSV data to the list


        humidities24Hours = [] #Create an empty list to store the 24 hour humidity data
        timeHours = [] #Create an empty list to store the 24 hour time data
        pointerHumidity = 1 #Set the pointer for the humidity data
        pointerTime = 1 #Set the pointer for the time data
        csvLength = len(jsonFile) #Get the length of the CSV file

        for i in range(1, 25): #Loop through the 24 hours to get hourly humidity data (last 24 hours)
            lastLine = jsonFile[csvLength - pointerHumidity] #Get the last line of the CSV file
            lastLineHumidity = lastLine[4] #Get the humidity data from the last line
            lastLineHumidity = int(lastLineHumidity) #Convert the humidity data to an integer
            lastLineTime = lastLine[0] #Get the time data from the last line
            timeHour = lastLineTime.split(" ") #Split the time data to get the hour
            timeHour = timeHour[1] #Get the hour from the time data
            timeHour = timeHour.split(":") #Split the hour data to get the hour
            timeHour = timeHour[0] #Get the hour from the time data
            timeHours.append(timeHour) #Append the hour data to the timeHours list
            humidities24Hours.append(lastLineHumidity) #Append the humidity data to the humidities24Hours list
            pointerHumidity += 12 #Increment the pointer for the humidity data
            pointerTime += 12 #Increment the pointer for the time data
            temperatureData = {"hour": timeHour, "temperature": lastLineHumidity}

        graphtest = [{'hour': '00', 'temperature': 8},]

        #Get the hourly humidity data for the last 24 hours
        print(type(humidities24Hours))
        print("Hourly Humidities: ", humidities24Hours)
        print(type(timeHours))
        print("Hours: ", timeHours)
        hour0 = timeHours[0]
        temperature0 = humidities24Hours[0]
        hour1 = timeHours[1]
        temperature1 = humidities24Hours[1]
        hour2 = timeHours[2]
        temperature2 = humidities24Hours[2]
        hour3 = timeHours[3]
        temperature3 = humidities24Hours[3]
        hour4 = timeHours[4]
        temperature4 = humidities24Hours[4]
        hour5 = timeHours[5]
        temperature5 = humidities24Hours[5]
        hour6 = timeHours[6]
        temperature6 = humidities24Hours[6]
        hour7 = timeHours[7]
        temperature7 = humidities24Hours[7]
        hour8 = timeHours[8]
        temperature8 = humidities24Hours[8]
        hour9 = timeHours[9]
        temperature9 = humidities24Hours[9]
        hour10 = timeHours[10]
        temperature10 = humidities24Hours[10]
        hour11 = timeHours[11]
        temperature11 = humidities24Hours[11]
        hour12 = timeHours[12]
        temperature12 = humidities24Hours[12]
        hour13 = timeHours[13]
        temperature13 = humidities24Hours[13]
        hour14 = timeHours[14]
        temperature14 = humidities24Hours[14]
        hour15 = timeHours[15]
        temperature15 = humidities24Hours[15]
        hour16 = timeHours[16]
        temperature16 = humidities24Hours[16]
        hour17 = timeHours[17]
        temperature17 = humidities24Hours[17]
        hour18 = timeHours[18]
        temperature18 = humidities24Hours[18]
        hour19 = timeHours[19]
        temperature19 = humidities24Hours[19]
        hour20 = timeHours[20]
        temperature20 = humidities24Hours[20]
        hour21 = timeHours[21]
        temperature21 = humidities24Hours[21]
        hour22 = timeHours[22]
        temperature22 = humidities24Hours[22]
        hour23 = timeHours[23]
        temperature23 = humidities24Hours[23]

    pointerDate = 1 #Set the pointer for the date data
    pointerHumidity = 1 #Set the pointer for the humidity data
    dateDaily = [] #Create an empty list to store the daily date data
    humidityDaily = [] #Create an empty list to store the daily humidity data
    csvLength = len(jsonFile) #Get the length of the CSV file

    for i in range(1, 31): #Loop through the 30 days to get daily humidity data (last 30 days)
        lastLine = jsonFile[csvLength - pointerDate] #Get the last line of the CSV file
        lastLineDate = lastLine[0] #Get the date data from the last line
        lastLineHumidity = lastLine[4] #Get the humidity data from the last line
        lastLineHumidity = int(lastLineHumidity) #Convert the humidity data to an integer
        dateDaily.append(lastLineDate) #Append the date data to the dateDaily list
        humidityDaily.append(lastLineHumidity)  # Append the humidity data to the humidityDaily list
        pointerDate += 288 #Increment the pointer for the date data
        pointerHumidity += 288 #Increment the pointer for the humidity data
        humidityData = {"date": lastLineDate, "humidity": lastLineHumidity}

    graphtest = [{'hour': '00', 'humidity': 8}, ]

    #Get the daily humidity data for the last 30 days
    print(type(humidityDaily))
    print("Daily Humidities: ", humidityDaily)
    humidityDay0 = humidityDaily[0]
    humidityDay1 = humidityDaily[1]
    humidityDay2 = humidityDaily[2]
    humidityDay3 = humidityDaily[3]
    humidityDay4 = humidityDaily[4]
    humidityDay5 = humidityDaily[5]
    humidityDay6 = humidityDaily[6]
    humidityDay7 = humidityDaily[7]
    humidityDay8 = humidityDaily[8]
    humidityDay9 = humidityDaily[9]
    humidityDay10 = humidityDaily[10]
    humidityDay11 = humidityDaily[11]
    humidityDay12 = humidityDaily[12]
    humidityDay13 = humidityDaily[13]
    humidityDay14 = humidityDaily[14]
    humidityDay15 = humidityDaily[15]
    humidityDay16 = humidityDaily[16]
    humidityDay17 = humidityDaily[17]
    humidityDay18 = humidityDaily[18]
    humidityDay19 = humidityDaily[19]
    humidityDay20 = humidityDaily[20]
    humidityDay21 = humidityDaily[21]
    humidityDay22 = humidityDaily[22]
    humidityDay23 = humidityDaily[23]
    humidityDay24 = humidityDaily[24]
    humidityDay25 = humidityDaily[25]
    humidityDay26 = humidityDaily[26]
    humidityDay27 = humidityDaily[27]
    humidityDay28 = humidityDaily[28]
    humidityDay29 = humidityDaily[29]


    pointerMonth = 6 #Set the pointer for the month data
    pointerTemperature = 1 #Set the pointer for the temperature data
    months = [] #Create an empty list to store the monthly date data
    humiditiesMonthly = [] #Create an empty list to store the monthly humidity data
    csvLength = len(jsonFile) #Get the length of the CSV file

    firstLine = jsonFile[pointerMonth] #Get the first line of the CSV file


    for i in range(len(jsonFile)): #Loop through the CSV file
        if pointerMonth < 52864: #Check if the pointer is less than the length of the CSV file
            firstLine = jsonFile[pointerMonth] #Get the first line of the CSV file
            firstLineMonth = firstLine[0] #Get the month data from the first line
            pointerMonth += 1 #Increment the pointer for the month data
            if '1/1/23 12:00' in firstLineMonth: #Check if the month is January
                if '11/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                elif '21/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                elif '31/1/23 12:00' in firstLineMonth: #ignore repeated searches for the same month
                    pass
                else:
                    firstLineHumidity = firstLine[4] #Get the humidity data from the first line
                    humiditiesMonthly.append(firstLineHumidity) #Append the humidity data to the humiditiesMonthly list
                    firstLineMonth = "Jan" #Set the month to January
                    months.append(firstLineMonth) #Append the month data to the months list
            elif '1/2/23 12:00' in firstLineMonth: #Check if the month is February (repeated code for each month except for month searches)
                if '11/2/23 12:00' in firstLineMonth:
                    pass
                elif '21/2/23 12:00' in firstLineMonth:
                    pass
                elif '31/2/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Feb"
                    months.append(firstLineMonth)
            elif '1/3/23 12:00' in firstLineMonth: #Check if the month is March (repeated code for each month except for month searches)
                if '11/3/23 12:00' in firstLineMonth:
                    pass
                elif '21/3/23 12:00' in firstLineMonth:
                    pass
                elif '31/3/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Mar"
                    months.append(firstLineMonth)
            elif '1/4/23 12:00' in firstLineMonth: #Check if the month is April (repeated code for each month except for month searches)
                if '11/4/23 12:00' in firstLineMonth:
                    pass
                elif '21/4/23 12:00' in firstLineMonth:
                    pass
                elif '31/4/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Apr"
                    months.append(firstLineMonth)
            elif '3/5/23 17:30' in firstLineMonth: #Check if the month is May (repeated code for each month except for month searches)
                if '13/5/23 17:30' in firstLineMonth:
                    pass
                elif '23/5/23 17:30' in firstLineMonth:
                    pass
                elif '31/5/23 17:30' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "May"
                    months.append(firstLineMonth)
            elif '1/6/23 12:00' in firstLineMonth: #Check if the month is June (repeated code for each month except for month searches)
                if '11/6/23 12:00' in firstLineMonth:
                    pass
                elif '21/6/23 12:00' in firstLineMonth:
                    pass
                elif '31/6/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Jun"
                    months.append(firstLineMonth)
            elif '1/7/23 12:00' in firstLineMonth: #Check if the month is July (repeated code for each month except for month searches)
                if '11/7/23 12:00' in firstLineMonth:
                    pass
                elif '21/7/23 12:00' in firstLineMonth:
                    pass
                elif '31/7/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Jul"
                    months.append(firstLineMonth)
            elif '1/8/23 12:00' in firstLineMonth: #Check if the month is August (repeated code for each month except for month searches)
                if '11/8/23 12:00' in firstLineMonth:
                    pass
                elif '21/8/23 12:00' in firstLineMonth:
                    pass
                elif '31/8/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Aug"
                    months.append(firstLineMonth)
            elif '1/9/23 12:00' in firstLineMonth: #Check if the month is September (repeated code for each month except for month searches)
                if '11/9/23 12:00' in firstLineMonth:
                    pass
                elif '21/9/23 12:00' in firstLineMonth:
                    pass
                elif '31/9/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Sep"
                    months.append(firstLineMonth)
            elif '1/10/23 12:00' in firstLineMonth: #Check if the month is October (repeated code for each month except for month searches)
                if '11/10/23 12:00' in firstLineMonth:
                    pass
                elif '21/10/23 12:00' in firstLineMonth:
                    pass
                elif '31/10/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Oct"
                    months.append(firstLineMonth)
            elif '1/11/23 12:00' in firstLineMonth: #Check if the month is November (repeated code for each month except for month searches)
                if '11/11/23 12:00' in firstLineMonth:
                    pass
                elif '21/11/23 12:00' in firstLineMonth:
                    pass
                elif '31/11/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Nov"
                    months.append(firstLineMonth)
            elif '1/12/23 12:00' in firstLineMonth: #Check if the month is December (repeated code for each month except for month searches)
                if '11/12/23 12:00' in firstLineMonth:
                    pass
                elif '21/12/23 12:00' in firstLineMonth:
                    pass
                elif '31/12/23 12:00' in firstLineMonth:
                    pass
                else:
                    firstLineHumidity = firstLine[4]
                    humiditiesMonthly.append(firstLineHumidity)
                    firstLineMonth = "Dec"
                    months.append(firstLineMonth)


    #Get the monthly humidity data for the last 12 months
    print(type(humiditiesMonthly))
    print("Monthly Humidities: ", humiditiesMonthly)
    humidityMonth1 = humiditiesMonthly[0]
    humidityMonth2 = humiditiesMonthly[1]
    humidityMonth3 = humiditiesMonthly[2]
    humidityMonth4 = humiditiesMonthly[3]
    humidityMonth5 = humiditiesMonthly[4]
    humidityMonth6 = humiditiesMonthly[5]
    humidityMonth7 = humiditiesMonthly[6]
    humidityMonth8 = humiditiesMonthly[7]
    humidityMonth9 = humiditiesMonthly[8]
    humidityMonth10 = humiditiesMonthly[9]
    humidityMonth11 = humiditiesMonthly[10]

    #Create a string of the humidity data to pass to the front end
    data = strHumidity1, strHumidity2, strAverageHumidity, graphtest, hour0, temperature0, hour1, temperature1, hour2, temperature2, hour3, temperature3, hour4, temperature4, hour5, temperature5, hour6, temperature6, hour7, temperature7, hour8, temperature8, hour9, temperature9, hour10, temperature10, hour11, temperature11, hour12, temperature12, hour13, temperature13, hour14, temperature14, hour15, temperature15, hour16, temperature16, hour17, temperature17, hour18, temperature18, hour19, temperature19, hour20, temperature20, hour21, temperature21, hour22, temperature22, hour23, temperature23, humidityDay0, humidityDay1, humidityDay2, humidityDay3, humidityDay4, humidityDay5, humidityDay6, humidityDay7, humidityDay8, humidityDay9, humidityDay10, humidityDay11, humidityDay12, humidityDay13, humidityDay14, humidityDay15, humidityDay16, humidityDay17, humidityDay18, humidityDay19, humidityDay20, humidityDay21, humidityDay22, humidityDay23, humidityDay24, humidityDay25, humidityDay26, humidityDay27, humidityDay28, humidityDay29, humidityMonth1, humidityMonth2, humidityMonth3, humidityMonth4, humidityMonth5, humidityMonth6, humidityMonth7, humidityMonth8, humidityMonth9, humidityMonth10, humidityMonth11


    return render_template('humidity.html', data=data) #Render the humidity page with the humidity data passed to the front end

@app.route('/weathermaps')
def weathermaps():
    """Weather Maps page"""
    return render_template('weathermaps.html')

@app.route('/clocktest')
def clocktest():
    """Test Clock page"""
    return render_template('clocktest.html')

@app.route('/calendartest')
def calendartest():
    """Test Calendar page"""
    return render_template('calendartest.html')

@app.route('/tabletest1')
def tabletest():
    """Test Tables"""
    return render_template('tabletest1.html')

@app.route('/graphtest1')
def graphtest():
    """Test Graphs"""
    return render_template('graphtest1.html')

@app.route('/weatherdatatest')
def weatherdatatest():
    """Test WeatherLink API"""
    api_key = 'e9acjapvjih3rpbcnjnj8c8kfsnyivkb'
    api_secret = 'p9ltsbyvv137bkskvuerqfs7s8qbe8gy'
    station_id = 142820

    # current time
    local_time = int(time.time())

    # api signature
    data_to_sign = f"api-key{api_key}station-id{station_id}t{local_time}"
    signature = hmac.new(
        api_secret.encode('utf-8'),
        data_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

    url = f"https://api.weatherlink.com/v2/current/{station_id}"
    params = {
        "api-key": api_key,
        "t": local_time,
        "api-signature": signature
    }

    response = requests.get(url, params=params)
    current_weather = response.json()
    print(current_weather)

    return jsonify(current_weather)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/weathertest', methods=['GET', 'POST'])
def weathertest():
    """Test Weather page"""

    return render_template('weathertest.html')

@app.route('/openweathertest', methods=['GET', 'POST'])
def openweathertest():
    """Test Open Weather API"""
    openWeather_API_Key = 'cdb2f81a0c0053ff42b1db37fdb0b39b'
    openWeatherID = 2646057
    local_time = int(time.time())
    params = {
        "t": local_time
    }
    openWeatherURL = 'https://api.openweathermap.org/data/2.5/forecast?id=' + str(openWeatherID) + '&appid=' + openWeather_API_Key
    response = requests.get(openWeatherURL, params=params)
    openWeatherData = response.json()
    print("openWeatherData", openWeatherData)
    print(type(openWeatherData))
    openWeatherData = openWeatherData['list']
    openWeatherDataToday = openWeatherData[16]
    print(openWeatherDataToday)
    OpenWeatherDataTodayWeather = openWeatherDataToday['weather']
    OpenWeatherDataTodayWeather = OpenWeatherDataTodayWeather[0]
    print(OpenWeatherDataTodayWeather)
    weatherConditions = OpenWeatherDataTodayWeather['main']
    print(weatherConditions)
    tomorrowDate = openWeatherDataToday['dt_txt']
    tomorrowDate = tomorrowDate.split(" ")
    tomorrowDate = tomorrowDate[0]
    print(tomorrowDate)

    return jsonify(openWeatherData)

@app.route('/weatherapitest', methods=['GET', 'POST'])
def weatherapitest():
    """Test weather API"""
    weatherAPI_key = '33d91967a1b04700807201804242711'
    weatherAPIurl = 'https://api.weatherapi.com/v1/forecast.json?key=' + weatherAPI_key + '&q=IP5 3RE&days=1&aqi=yes&alerts=yes'
    print(weatherAPIurl)
    response = requests.get(weatherAPIurl)
    weatherAPIData = response.json()
    print(weatherAPIData)
    print(type(weatherAPIData))
    weatherAPIDataCurrent = weatherAPIData['current']
    print(weatherAPIDataCurrent)
    weatherAPIDataCurrentTemperature = weatherAPIDataCurrent['temp_c']
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentTemperature = str(weatherAPIDataCurrentTemperature) + "°C"
    print(weatherAPIDataCurrentTemperature)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrent['condition']
    print(weatherAPIDataCurrentCondition)
    weatherAPIDataCurrentCondition = weatherAPIDataCurrentCondition['text']
    print(weatherAPIDataCurrentCondition)

    weatherAPI01HourData = weatherAPIData['forecast']
    weatherAPI01HourData = weatherAPI01HourData['forecastday']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourData = weatherAPI01HourData['hour']
    weatherAPI01HourData = weatherAPI01HourData[0]
    weatherAPI01HourDataTemperature = weatherAPI01HourData['temp_c']
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataTemperature = str(weatherAPI01HourDataTemperature) + "°C"
    print(weatherAPI01HourDataTemperature)
    weatherAPI01HourDataCondition = weatherAPI01HourData['condition']
    print(weatherAPI01HourDataCondition)
    weatherAPI01HourDataCondition = weatherAPI01HourDataCondition['text']
    print(weatherAPI01HourDataCondition)
    weatherAPI01HourDataConditionTime = weatherAPI01HourData['time']
    print(weatherAPI01HourDataConditionTime)
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime.split(" ")
    weatherAPI01HourDataConditionTime = weatherAPI01HourDataConditionTime[1]
    print(weatherAPI01HourDataConditionTime)


    return jsonify(weatherAPIData)

@app.route('/pollencounttest', methods=['GET', 'POST'])
def pollencounttest():
    """Test pollen count API"""
    import http.client

    conn = http.client.HTTPSConnection("api.ambeedata.com")

    headers = {
        'x-api-key': "01a4c1eae8cb507b14ee10ecd1b2c3984e8368ede6224aa2ffcd3d9ada2ce3d7",
        'Content-type': "application/json"
    }

    conn.request("GET", "/latest/pollen/by-lat-lng?lat=52.05892202630986&lng=1.2847627151273548", headers=headers)

    res = conn.getresponse()
    data = res.read()

    decodedData = data.decode("utf-8")


    return jsonify(decodedData)

@app.route('/csvtest', methods=['GET', 'POST'])
def csvtest():
    """Test CSV file"""
    with open('Weather_Link_Outdoor.csv', mode='r', encoding = 'latin') as file:
        csvFile = csv.reader(file)
        jsonFile = []
        for lines in csvFile:
            jsonFile.append(lines)
        print(jsonFile)

    return jsonify(jsonFile)

@app.route('/classdiagramhtml', methods=['GET', 'POST'])
def classdiagramhtml():
    """Class Diagram HTML"""
    return render_template('Weather_Monitoring_Dashboard_Application_Class_Diagram.html')

@app.route('/usecasediagramhtml', methods=['GET', 'POST'])
def usecasediagramhtml():
    """Use Case Diagram HTML"""
    return render_template('Smart_House_and_Weather_Monitoring_Dashboard_Use_Case_Diagram.html')

@app.route('/architecturaldiagramhtml', methods=['GET', 'POST'])
def architecturaldiagramhtml():
    """Architectural Diagram HTML"""
    return render_template('Architectural_Diagram.html')

@app.route('/architecturaldiagram2html', methods=['GET', 'POST'])
def architecturaldiagram2html():
    """Architectural Diagram 2 HTML"""
    return render_template('Architectural_Diagram_2.html')

@app.route('/wireframehtml', methods=['GET', 'POST'])
def wireframehtml():
    """Wireframe HTML"""
    return render_template('Smart_Home_Weather_Dashboard_Wireframe_V2.html')

@app.route('/mvtarchitecturaldiagramhtml', methods=['GET', 'POST'])
def mvtarchitecturaldiagramhtml():
    """MVT Architectural Diagram"""
    return render_template('MVT_Architectural_Diagram.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # port number
    app.run(debug=True, host='0.0.0.0', port=port)  # run the application
