from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect..', event)
        # get default channel layer from a project
        print('Channel layer..', self.channel_layer)
        # get channel name
        print('Channel name..', self.channel_name  )
        
        # group add by channel layer and async to sync

        self.group_name = self.scope['url_route']['kwargs']['group_name']  
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        
        print('group_name channel database ...', self.group_name)
        self.send({
            "type": 'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('websocket receive..', event)
        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        }) 
    
    def chat_message(self, event):
        print('event...', event)
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    
    def websocket_disconnect(self, event):
        print('websocket disconnect..', event)

        # discard group when connection disconnected
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()
    

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connect..', event)
        # get default channel layer from a project
        print('Channel layer..', self.channel_layer)
        # get channel name
        print('Channel name..', self.channel_name  )

        self.group_name = self.scope['url_route']['kwargs']['group_name']  
        
        # group add by channel layer and async to sync
        await self.channel_layer.group_add(self.group_name, self.channel_name)


        await self.send({
            "type": 'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print('websocket receive..', event)
        await self.channel_layer.group_send(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        }) 
    
    async def chat_message(self, event):
        print('event...', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    
    async def websocket_disconnect(self, event):
        print('websocket disconnect..', event)

        # discard group when connection disconnected
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()


