from django.urls import path
from . import views

urlpatterns=[
    path('',views.helloWorld),
    path('new/',views.new),
    path('nothing/',views.nothing),
]