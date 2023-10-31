# syncConsumer
from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect....', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('websocket receive....', event)

    def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
    
    
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connect....', event)

    async def websocket_receive(self, event):
        print('websocket receive....', event)

    async def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
    
