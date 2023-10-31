# syncConsumer
from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    # this handle is called when client initially open a connection and is about to finish the websocket handshake. 
    def websocket_connect(self, event):
        print('websoket connect....')
    
    # This handle is called when data received from client
    def websocket_receive(self, event):
        print('websocket receive....')
    
    # This handle called when either connection to the client is lost, either from the client the connection, the server closing the connection, or loss of the socket.
    def websocket_disconnect(self, event):
        print('websocket disconnect...')
        
# asyncConsumer ------------------------------
from channels.consumer import AsyncConsumer


class MyAsyncConsumer(AsyncConsumer):
    # this handle is called when client initially open a connection and is about to finish the websocket handshake. 
    async def websocket_connect(self, event):
        print('websoket connect....')
    
    # This handle is called when data received from client
    async def websocket_receive(self, event):
        print('websocket receive....')
    
    # This handle called when either connection to the client is lost, either from the client the connection, the server closing the connection, or loss of the socket.
    async def websocket_disconnect(self, event):
        print('websocket disconnect...')