from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    host=os.uname().nodename
    arch=os.uname().machine
    return HttpResponse("My Hostname:"+host+" and my Arch:"+arch)
