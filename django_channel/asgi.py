import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
# from routing.routing import websocket_urlpatterns
import routing.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channel.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket': URLRouter(
        routing.routing.websocket_urlpatterns
    ) 
})

