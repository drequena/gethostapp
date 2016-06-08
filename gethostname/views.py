from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    host=os.uname().nodename
    return HttpResponse("My Hostname:"+host)
