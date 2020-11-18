from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('surveyhome/', views.surveyhome, name='surveyhome'),
    path('results/', views.results, name='results'),
    path('vote/', views.vote, name='vote')
]