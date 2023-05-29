import requests
import json
import sys
API_Key="3893f420e7d35b6750aaa51f02eee230"
def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_Key)
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = json.loads(response.text)
        return weather_data
    except requests.exceptions.HTTPError as e:
        print("Http Error:", e)
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    except (KeyError, IndexError) as e:
        print("Key Error & Index Error:", e)
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    city_name = input("Enter city name: ")	
    print()
    weather_data = get_weather(city_name)
    print("City:", weather_data['name'])
    print("Weather:", weather_data['weather'][0]['main'])
    print("Temperature:", round(weather_data['main']['temp']- 273.15,2),"C", "(min:", round(weather_data['main']['temp_min']- 273.15,2),"C", ", max:", round(weather_data['main']['temp_max']- 273.15,2),"C", ")")
    print("Humidity:", weather_data['main']['humidity'])
    print("Pressure:", weather_data['main']['pressure'])
    print("Wind Speed:", weather_data['wind']['speed'])
    import datetime
    print("Date and Time:", datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))
 
