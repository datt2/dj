from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm
import requests
# Create your views here.

def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=54c640173a551c2bf42d81e336810e89'
    err_msg=""
    message=""
    message_class=""

    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name']
            existing_city=City.objects.filter(name=new_city).count()

            if existing_city==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:
                    form.save()
                else:
                    err_msg='City does not exit!'
            else:
                err_msg='City already existing!'

        if err_msg:
            message=err_msg
            message_class='is-danger'
        else:
            message="City added successfully!"
            message_class='is-success'
    cities=City.objects.all()
    form=CityForm()
    weather_data=[]
    for cit in cities:
        r=requests.get(url.format(cit)).json()
        city_weather={
            'city':cit.name,
            'temperature':'{:.2f}'.format(r['main']['temp']-273.15),
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context={
    'weather_data':weather_data,
    'form':form,
    'message':message,
    'message_class':message_class,
    }

    return render(request,'home.html',context)


def delete(request,city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
