# Topic Generic Consumer websocketConsumer and AsyncWebsocketConsumer

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class MyWebSocketConsumer(WebsocketConsumer):
    def connect(self):
        print('websocket connected...')
        self.accept()

        # Reject the connection 
        # self.close()
    
    def receive(self, text_data=None, bytes_data=None):
        print('Message receive from client..', text_data)

        self.send(text_data='Message from server to client') 
    
    def disconnect(self, code):
        print('Websocket disconnected..', code)
    


class MyAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('websocket connected...')
        await self.accept()

        # Reject the connection 
        # self.close()
    
    async def receive(self, text_data=None, bytes_data=None):
        print('Message receive from client..', text_data)

        await self.send(text_data='Message from server to client') 
    
    async def disconnect(self, code):
        print('Websocket disconnected..', code)