from django.forms import ModelForm, TextInput
from weather.models import Citys
class CityForm(ModelForm):
    class Meta:
        model =Citys
        fields = ['cname']
        widgets = {'cname' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}