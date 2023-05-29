import requests
import json
import sys

# how to add API key
API_Key="3893f420e7d35b6750aaa51f02eee230"


#add get_weather function
def get_weather(city):

    #add url
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_Key)
    
    #handle exception
    try:
        #add response
        response = requests.get(url)
        #what is requests.get(url)???
        #requests.get(url) is a method that will send a GET request to the specified url
        #ex) requests.get("http://www.google.com") will send a GET request to http://www.google.com
        #ex) requests.get("http://www.naver.com") will send a GET request to http://www.naver.com


        response.raise_for_status()
        #what is raise_for_status()???
        #raise_for_status() is a method that will raise an exception if the status code is not 200
        #200 means that the request was successful
        #ex) 404 means that the request was not found
        #ex) 500 means that the server has encountered an error


        #add json loads
        weather_data = json.loads(response.text)
        #what is json.loads(response.text)???
        #json.loads(response.text) is a method that will convert the response.text into a dictionary
        #ex) response.text = '{"name": "Seoul", "age": 20}'
        #ex) json.loads(response.text) = {"name": "Seoul", "age": 20}

        #add weather
        #weather = weather_data['weather'][0]['main']
        #what is weather_data['weather'][0]['main']???
        #weather_data['weather'][0]['main'] is a way to access the weather data
        #weather_data['weather'] will return a list
        #weather_data['weather'][0] will return the first element of the list
        #weather_data['weather'][0]['main'] will return the value of the key 'main' in the first element of the list

        #add temp
        #temp = weather_data['main']['temp']
        #what is weather_data['main']['temp']???
        #weather_data['main']['temp'] is a way to access the temperature data
        #weather_data['main'] will return a dictionary
        #weather_data['main']['temp'] will return the value of the key 'temp' in the dictionary

        #return weather and temp
        #return weather, temp
        return weather_data

    #handle exception
    #HTTPError
    except requests.exceptions.HTTPError as e:
        print("Http Error:", e)
    #request exception
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
    #key error & index error
    except (KeyError, IndexError) as e:
        print("Key Error & Index Error:", e)
    #exception
    except Exception as e:
        print("Error:", e)


#how to run
if __name__ == "__main__":

    city_name = input("Enter city name: ")	
    print()

    #get weather and temp
    weather_data = get_weather(city_name) 

    #print weather and temp
    '''
    print("Weather:", weather)
    print("Temperature:", temp)
    '''

    #what will display
    #Weather: Clouds
    #Temperature: 281.15

    #this is working

    #what else can we know from this API?
    #we can know the humidity, pressure, and wind speed
    #we can also know the minimum and maximum temperature
    #we can also know the latitude and longitude of the city
    #we can also know the sunrise and sunset time
    #we can also know the country code
    #we can also know the time of data calculation
    #we can also know the visibility
    #we can also know the timezone
    #we can also know the id of the city

    #i want to know all this
    #how can i do this?
   # print("Weather Data:", weather_data)
    #what will display
    #Weather Data: {'coord': {'lon': 126.9778, 'lat': 37.5683}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 281.15, 'feels_like': 279.82, 'temp_min': 280.15, 'temp_max': 282.15, 'pressure': 1023, 'humidity': 71}, 'visibility': 10000, 'wind': {'speed': 1.54, 'deg': 0}, 'clouds': {'all': 75}, 'dt': 1612464190, 'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1612470190, 'sunset': 1612507130}, 'timezone': 32400, 'id': 1835848, 'name': 'Seoul', 'cod': 200}

    #it is showing error
    #NameError: name 'weather_data' is not defined
    #why?
    #because weather_data is defined inside the get_weather function
    #so we cannot access it outside the get_weather function

    #how can we solve this?
    # we can return weather_data
    # and we can access it outside the get_weather function
    #okay

    #print("Weather Data:", weather_data)


    #i want to improve the display of the weather data  
    #how can i do this?
    #we can use json.dumps(weather_data, indent=4)
    #what is json.dumps(weather_data, indent=4)?
    #json.dumps(weather_data, indent=4) is a method that will convert the weather_data into a string
    #and it will indent the string by 4 spaces
    #ex) weather_data = {"name": "Seoul", "age": 20}
    #ex) json.dumps(weather_data, indent=4) = {
    #                                               "name": "Seoul",
    #                                               "age": 20
    #                                           }
    #okay
    #print("Weather Data:", json.dumps(weather_data, indent=4))

    #this is still not perfect
    #i want to display the weather data in a better way
    #i will tell what i need to show
    # 1. weather: Clouds
    # 2. temperature: 281.15 (min: 280.15, max: 282.15)
    # 3. humidity: 71
    # 4. pressure: 1023
    # 5. wind speed: 1.54

    #how can i do this?
    #we can use the weather_data dictionary
    #okay

    #i want temperature to be displayed in celsius

    #how can i do this?
    #we can use the temperature in kelvin and convert it to celsius
    #okay

    #how can i convert kelvin to celsius?
    #we can use the formula celsius = kelvin - 273.15
    #okay

    #give print statements
    print("City:", weather_data['name'])
    print("Weather:", weather_data['weather'][0]['main'])
    #print("Temperature:", weather_data['main']['temp'],"K", "(min:", weather_data['main']['temp_min'],"K", ", max:", weather_data['main']['temp_max'],"K", ")")
    print("Temperature:", round(weather_data['main']['temp']- 273.15,2),"C", "(min:", round(weather_data['main']['temp_min']- 273.15,2),"C", ", max:", round(weather_data['main']['temp_max']- 273.15,2),"C", ")")
    print("Humidity:", weather_data['main']['humidity'])
    print("Pressure:", weather_data['main']['pressure'])
    print("Wind Speed:", weather_data['wind']['speed'])

    #also add city name
    #print("City:", weather_data['name'])

    #can this data also display date and time?
    #no

    #this data is not showing current weather?
    #yes
    #this data is showing current weather

    #so i also want to display the current date and time
    #how can i do this?
    #we can use the datetime module
    #okay

    import datetime
    #print current date and time
    #print("Date and Time:", datetime.datetime.now())

    #we need to change the format of date and time
    #how can we do this?
    #we can use strftime() method
    #okay

    #print current date and time
    #print("Date and Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    #time is perfect
    #but i want to display the date in a different format
    #how can i do this?
    #we can use the datetime module
    #okay

    #print current date and time
    print("Date and Time:", datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))

    #this is perfect

    #what else can we do?
    #we can also display the sunrise and sunset time
    #okay no need


    




    