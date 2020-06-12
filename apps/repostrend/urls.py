from django.urls import path
from . import views

app_name = 'repotrend'

urlpatterns = [
    path('', views.index),
]
