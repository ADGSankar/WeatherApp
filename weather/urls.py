from weather.models import *
from weather.views import *
from django.urls import path
app_name="weather"
urlpatterns = [
    path('',WeatherData.as_view() , name='home'),
    ]
