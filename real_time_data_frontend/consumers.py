from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

# syncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect....', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Message receive from the client', event['text'])

        for i in range(20):
            self.send({
                'type': 'websocket.send',
                'text': str(i) 
            })
            sleep(1)

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
        for i in range(20):
            await self.send({
                'type': 'websocket.send',
                'text': str(i) 
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
        raise StopConsumer()
