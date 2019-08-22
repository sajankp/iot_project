from channels.generic.websocket import AsyncWebsocketConsumer
import json
import websockets
from django.utils import timezone
from .models import Data

class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print (text_data)
        print(self.scope["headers"])
        await self.send("got it")
        a = await websockets.connect(uri="ws://localhost",port=8765)
        print("new connection")
        print(a)
        await a.send("efwefwefwefwef")

        '''
        text_data_json = json.loads(text_data)
        a = text_data_json['temp']
        value = Data(value = a,date = timezone.localtime(timezone.now()))
        value.save()
        self.send(text_data = json.dumps({
            'message': f'Done and recieved {value.value} at {value.date}'
        }))
        '''