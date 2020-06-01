from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions 
from polls.models import Autor
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

