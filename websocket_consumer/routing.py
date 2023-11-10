from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MyWebSocketConsumer.as_asgi()),
]