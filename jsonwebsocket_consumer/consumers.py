# Topic Generic JsonWebsocket_consumer and AsyncJsonWebsocket_consumer

from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print('Websocket connected...')
    
    def receive_json(self, content, **kwargs):
        print('Message receive from client..', content)

    
    def disconnect(self, code):
        print('Disconnected...', code)
    
class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('Websocket connected...')
    
    async def receive_json(self, content, **kwargs):
        print('Message receive from client..', content)

    
    async def disconnect(self, code):
        print('Disconnected...', code)