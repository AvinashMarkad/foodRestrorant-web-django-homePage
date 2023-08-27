from django.contrib import admin
from django.urls import path 
import B_app.views as views

urlpatterns = [
    path('', views.index, name='homePage')
]