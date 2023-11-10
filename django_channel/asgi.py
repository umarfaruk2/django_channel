import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
# from routing.routing import websocket_urlpatterns
# import routing.routing
# import real_time_data_example.routing
# import real_time_data_frontend.routing
# import channel_layer_redis.routing
# import channel_with_database.routing
# import websocket_consumer.routing
import jsonwebsocket_consumer.routing
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
        jsonwebsocket_consumer.routing.websocket_urlpatterns
    )) 
})


