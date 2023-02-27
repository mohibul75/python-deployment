from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def helloWorld(request):
    return Response('Hello world...')

@api_view(['GET'])
def new(request):
    return Response('Hello to the new world...')