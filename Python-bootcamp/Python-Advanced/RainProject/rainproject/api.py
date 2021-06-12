import requests
import os

omp_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

my_api = "d43965505e81bc0f02fa8873f61e78d2"


weather_param ={
    "lat":13.213420,
    "lon":79.096740,
    "appid":my_api,
    "exclude":'current,minutely,daily'
}


responce = requests.get(omp_endpoint, params=weather_param)
responce.raise_for_status()
whether_data = responce.json()
whether_slice = whether_data["hourly"][:12]
for hour_data in whether_slice:
    data = hour_data["weather"][0]["id"]
    if data > 809 :
        print("heavy summer")
    elif data < 700:
        print("bring an umberla")
    else:
        print(data)
# print(whether_data["hourly"][0]["weather"][0])
