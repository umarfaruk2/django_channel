from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

# syncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect....', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Message receive from the client', event['text'])
        self.send({
            'type': 'websocket.send',
            'text': 'Message send to client'
        })

    def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
        raise StopConsumer()
        
    
    
# asyncConsumer
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connect....', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Message receive from the client', event['text'])
        await self.send({
            'type': 'websocket.send',
            'text': 'Message send to client'
        })

    async def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
        raise StopConsumer()
