from django.urls import path
from . import views


urlpatterns = [
    path('layer/', views.channel_layer, name='channel_layer')
]
