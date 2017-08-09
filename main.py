import requests
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

class WeatherStructure:
    def __init__(self):
        self.temp = None
        self.weather = None
        self.humidity = None
        self.date = None


def getWeather(data):
    array = []
    jlist = data['list']
    for l in jlist:
        weatherObj = WeatherStructure()
        weatherObj.temp = l['main']['temp']
        print(weatherObj.temp)
        weatherObj.weather = l['weather'][0]['main']
        print(weatherObj.weather)
        weatherObj.humidity = l['main']['humidity']
        print(weatherObj.humidity)
        weatherObj.date = l['dt_txt']
        print(weatherObj.date)
        array.append(weatherObj)
    return array


def getCity(data):
    city = data['city']['name']
    return city



@app.route("/<zipcode>")
def method(zipcode):
    response = requests.get('http://127.0.0.1:5000/weather_json/' + zipcode)
    myData = json.loads(response.text)
    print(response)
    dataArray = getWeather(myData)
    city = getCity(myData)
    for d in dataArray:
        print(d.temp)
    return render_template('default.html', dataArray=dataArray)



if __name__ == "__main__":
    app.run(port=5001)



