import urllib2
import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the weather data index.")


    f = urllib2.urlopen('http://api.wunderground.com/api/c38818ab53c0f129/geolookup/conditions/q/IA/Cedar_Rapids.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    return HttpResponse("Current temperature in %s is: %s" % (location, temp_f))
    f.close