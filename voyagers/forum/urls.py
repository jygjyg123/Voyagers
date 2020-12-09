from django.urls import path
from . import views

urlpatterns = [
    path('count/', views.count, name='count'),
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('newthread/', views.new_thread, name='new_thread'),
]