from channels.generic.websocket import WebsocketConsumer
import json
from django.utils import timezone
from .models import Data

class DataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        a = text_data_json['temp']
        value = Data(value = a,date = timezone.localtime(timezone.now()))
        value.save()
        self.send(text_data = json.dumps({
            'message': f'Done and recieved {value.value} at {value.date}'
        }))
