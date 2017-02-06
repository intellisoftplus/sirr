import urllib2
import urllib
import json
import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the weather data index.")


    # f = urllib2.urlopen('http://api.wunderground.com/api/c38818ab53c0f129/geolookup/conditions/q/KE/Nandi_Hills.json')
    # json_string = f.read()
    # parsed_json = json.loads(json_string)
    # location = parsed_json['location']['city']
    # temp_f = parsed_json['current_observation']['temp_f']
    # return HttpResponse("Current temperature in %s is: %s" % (location, temp_f))
    # f.close
    # +19095126282 trillio phone number

    #Request from sms
    dsms = "Monday"

    f3d = urllib2.urlopen('http://api.wunderground.com/api/c38818ab53c0f129/forecast/q/KE/Nandi_Hills.json')
    json_string = f3d.read()
    data = json.loads(json_string)

    for day in data['forecast']['simpleforecast']['forecastday']:
        # return HttpResponse(day['date']['weekday'])
        d = day['date']['weekday']
        r = day['date']['weekday'] + " " + "Condition " + " " +  day['conditions'] + " " +  " Temp Low" + " " +day['low']['celsius'] + " " + "Temp High " + " " + day['high']['celsius'] + " " + "Av Humidity " +  " " +str(day['avehumidity'])
        return HttpResponse(r)


        # if d == dsms:

    r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts', data={
        'phonenumber': '+254790331936',
        'message': 'Your text message.'
    })

    return HttpResponse (r)


    f3d.close

def weather(request):

    f3d = urllib2.urlopen('http://api.wunderground.com/api/c38818ab53c0f129/forecast/q/KE/Nandi_Hills.json')
    json_string = f3d.read()
    data = json.loads(json_string)

    # Rain
    # Chance of Rain
    # Clear
    # Partly Cloudy
    for day in data['forecast']['simpleforecast']['forecastday']:

        condition = str(day['conditions'])

        if condition == "Rain" or "Chance of Rain":
             will_rain = 1

             r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/weather', data={
                 'will_rain': will_rain
             })
             return HttpResponse (r)
    will_rain = 0
    r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/weather', data={
        'will_rain': will_rain
    })
    return HttpResponse (r)


def soil(request):

    r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/soil', data={
        'value': 20,
        'tag': 'low'
    })

