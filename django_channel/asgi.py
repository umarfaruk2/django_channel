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
import channel_with_database.routing

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket': URLRouter(
        channel_with_database.routing.websocket_urlpatterns
    ) 
})


