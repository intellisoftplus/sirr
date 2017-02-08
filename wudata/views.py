import urllib2
import urllib
import json
import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


import ibmiotf.device
import json
import time
import signal
from time import sleep
import random
import sys


options = {

	"org": "vy8sg5",
	"type": "intellisoft-sample",
	"id": "intellisoftsample1",
	"auth-method": "token",
	"auth-token": "testdevice"
}


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
@csrf_exempt
def weather(request,query):

    #query is the phone number to which the message is to be sent.

    phone = request.POST.get('query', query)
    print phone
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
                 'will_rain': will_rain, 'phonenumber': phone
             })
             return HttpResponse (r)
    will_rain = 0
    r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/weather', data={
        'will_rain': will_rain, 'phonenumber': phone
    })
    return HttpResponse (r)


def getweather(request):

    #query is the phone number to which the message is to be sent.

    n = urllib2.Request("http://127.0.0.1:8000/wudata/api/jsonz/")
    opener = urllib2.build_opener()
    f = opener.open(n)
    json2 = json.loads(f.read())
    return HttpResponse(json2)

    f3d = urllib2.urlopen('http://api.wunderground.com/api/c38818ab53c0f129/forecast/q/KE/Nandi_Hills.json')
    json_string = f3d.read()
    data = json.loads(json_string)

    # Rain
    # Chance of Rain
    # Clear
    # Partly Cloudy
    # for day in data['forecast']['simpleforecast']['forecastday']:
    #
    #     condition = str(day['conditions'])
    #
    #     if condition == "Rain" or "Chance of Rain":
    #          will_rain = 1
    #
    #          r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/weather', data={
    #              'will_rain': will_rain, 'phonenumber': phone
    #          })
    #          return HttpResponse (r)
    # will_rain = 0
    # r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/weather', data={
    #     'will_rain': will_rain, 'phonenumber': phone
    # })
    return HttpResponse (r)


def soil(request):

    r = requests.post('https://intellisoft-sms.herokuapp.com/api/alerts/soil', data={
        'value': 66,
        'tag': 'high'
    })


    return HttpResponse(r)


def test(request,query):
    m = ""
    # query = request.GET.get('query', query)
    r = main(m)
    # r = requests.get('https://github.com/timeline.json')
    # payload = {'phonenumber': '+254790331936'}
    # r = requests.get("http://127.0.0.1:8000/wudata/api/weather/+254790331936/", params=payload)
    # send = requests.post('http://127.0.0.1:8000/wudata/api/weather/+254790331936/')
    return HttpResponse(r)

def jsonz(request):
        data = {'mm': 'mm', 'time': 'time'}
        return HttpResponse(json.dumps(data), content_type='application/json')


def myCommandCallback(cmd):
	print('inside command callback')
	print cmd
### Let's try and make our exits graceful ###
def signal_handler(signal, frame):

	print('You pressed Ctrl+C!')
	signal.signal(signal.SIGINT, signal_handler)

### Main routine starts here ###

def myCommandCallback(cmd):
	print('inside command callback')
	print cmd

def main(m):
	client = ibmiotf.device.Client(options)
	client.connect()
	# client.commandCallback = myCommandCallback

	while True:
            try:
                t = time.time()
                json_data = {}
                json_data["Time"] = t
                json_data["Sensor1"] = random.randint(1,1023)
                myPayload = json_data
                client.publishEvent("status","json", myPayload)
                return random.randint(1,1023)

            except SystemExit:
                break


if __name__ == "__main__":

   	main()

