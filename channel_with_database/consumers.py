from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json
from .models import Group, Chat
from channels.db import database_sync_to_async


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

        client_message = json.loads(event['text'])
        print('client message....', client_message['msg'])
        group = Group.objects.get(name = self.group_name)

        # check is user Authenticate
        if self.scope['user'].is_authenticated:
            chat = Chat(
                content = client_message['msg'],
                group = group
            )
            chat.save()

            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                'type': 'chat.message',
                'message': event['text']
            }) 
        else:
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'msg': 'Login Required'})
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

        client_message = json.loads(event['text'])
        print('client message....', client_message['msg'])
        group = await database_sync_to_async(Group.objects.get)(name = self.group_name)

        chat = Chat(
            content = client_message['msg'],
            group = group
        )
        await database_sync_to_async(chat.save())

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


