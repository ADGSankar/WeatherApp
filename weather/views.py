from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView,TemplateView,UpdateView,DeleteView
from weather.templates.form import *
import requests

cityes=["vishakhapatnam","vizianagaram","srikakulam","vijayawada","kakinada","hyderabad"]

class WeatherData(View):
    def get_weather(self):
        city_weather = []
        for i in cityes:
            dict1 = {"q":i , 'APPID': "90430210d48b16259ea901f5e2905db1"}
            # elif city_id:
            #     dict1 = {"q": city_id, 'APPID': "90430210d48b16259ea901f5e2905db1"}
            r = requests.request('GET', "http://api.openweathermap.org/data/2.5/weather", params=dict1)
            data = r.json()
            city_weather.append({
                'city': data['name'],
                'temperature': round(data['main']['temp'] - 273.15, 2),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            })
        return city_weather

    def get(self,request):

        city_weather=self.get_weather()
        form =CityForm


        print(city_weather)
        return render(request,
                      template_name="weather.html",
                      context={'form': form,'cw':city_weather ,'c':0}
                      )
    def post(self,request,*args,**kwargs):
        city_weather=self.get_weather()
        form =CityForm
        city_weather1=[]
        dict1 = {"q":request.POST["cname"], 'APPID': "90430210d48b16259ea901f5e2905db1"}
        # elif city_id:
        #     dict1 = {"q": city_id, 'APPID': "90430210d48b16259ea901f5e2905db1"}
        r = requests.request('GET', "http://api.openweathermap.org/data/2.5/weather", params=dict1)
        data = r.json()
        print(data)
        try:
            city_weather1.append(  {
                'city' : request.POST["cname"],
                'temperature' : round(data['main']['temp']-273.15,2),
                'description' : data['weather'][0]['description'],
                'icon' : data['weather'][0]['icon'],
            })
        except KeyError:
            print("No city")

        return render(request,
                      template_name="weather.html",
                      context={'cw1': city_weather1,'cw':city_weather,'form':form,'c':1}
                      )

