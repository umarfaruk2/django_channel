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
        async_to_sync(self.channel_layer.group_add)('programmer', self.channel_name)


        self.send({
            "type": 'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('websocket receive..', event)
        self.channel_layer.group_send('programmer', {
            'type': 'chat.message',
            'message': event['text']
        }) 
    
    def websocket_disconnect(self, event):
        print('websocket disconnect..', event)

        # discard group when connection disconnected
        async_to_sync(self.channel_layer.group_discard)('programmer', self.channel_name)
        raise StopConsumer()