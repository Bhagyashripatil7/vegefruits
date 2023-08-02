from django.contrib import admin
from django.urls import path
from .views import statement

urlpatterns = [

    path('statement/',statement,name="statement"),

]