from django.urls import path
from . import views


urlpatterns = [
    path('layer_database/<str:group_name>/', views.channel_layer, name='channel_layer')
]
