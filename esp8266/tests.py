from django.test import Client, TestCase
from .models import Data
import datetime
from django.utils import timezone
from channels.testing import WebsocketCommunicator
from esp8266.consumers import DataConsumer
import pytest, random, re

class DataTestCase(TestCase):

    def setUp(self):
        a0 = Data.objects.create(temperature = 33,humidity=75,date = datetime.datetime(2019, 2, 26, 6, 11, 40, tzinfo=timezone.utc))
        a1 = Data.objects.create(temperature = 32,humidity=75,date = timezone.now() - datetime.timedelta(seconds = 60))
        a2 = Data.objects.create(temperature = 33,humidity=80,date = timezone.now() - datetime.timedelta(seconds = 60 * 3))
        a3 = Data.objects.create(temperature = 32,humidity=80,date = timezone.now() - datetime.timedelta(seconds = 60 * 4))

    def test_value_zero_count(self):
        """
        Count of objects with temperature 32 which is to be 2
        """
        a = Data.objects.filter(temperature = 32)
        self.assertEqual(a.count(), 2)

    def test_total_count(self):
        """
        Check if all values are obtained on db access
        """
        a = Data.objects.all()
        self.assertEqual(a.count(), 4)

    def test_index(self):
        """
        Checks if home page is accessible
        """
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 301)

    def test_chart(self):
        """
        Check if charts page is accessible
        """
        c = Client()
        response = c.get("/chart")
        self.assertEqual(response.status_code, 301)

    def test_index_secure(self):
        """
        Checks if home page is accessible
        """
        c = Client()
        response = c.get("/",secure=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["values"].count(),4)

    def test_chart_secure(self):
        """
        Check if charts page is accessible
        """
        c = Client()
        response = c.get("/chart",secure=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["values"].count(),3)

'''
class TestWebSocket:

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.asyncio
    async def test_connection(self):
        """
        Check if websocket connection can be created and data is recieved
        """
        communicator = WebsocketCommunicator(DataConsumer, "/ws/post")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        await communicator.send_json_to({'temp':1})
        response = await communicator.receive_from()
        # Close
        await communicator.disconnect()

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.asyncio
    async def test_output(self):
        """
        Check if the value recieved is right from websocket connection
        """
        communicator = WebsocketCommunicator(DataConsumer, "/ws/post")
        connected, subprotocol = await communicator.connect()
        value = 1
        q = datetime.datetime.now()
        await communicator.send_json_to({'temp':value})
        response = await communicator.receive_from()
        await communicator.disconnect()
        assert re.search('Done and recieved {a} at {b}'.format(a=value,b=q.strftime('%Y-%m-%d')),response)

    @pytest.mark.asyncio
    @pytest.mark.django_db(transaction=True)
    async def test_value_count(self):
        communicator = WebsocketCommunicator(DataConsumer, "/ws/post")
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.send_json_to({'temp':1})
        await communicator.send_json_to({'temp':1})
        await communicator.send_json_to({'temp':0})
        await communicator.disconnect()
        a = Data.objects.all()
        assert a.count(), 3
        assert Data.objects.filter(value =1).count(), 2
        assert Data.objects.filter(value =0).count(), 1
'''
