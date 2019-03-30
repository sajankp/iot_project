from django.test import Client, TestCase
from .models import Data
import datetime
from django.utils import timezone
from channels.testing import WebsocketCommunicator
from esp8266.consumers import DataConsumer
import pytest

class DataTestCase(TestCase):

    def setUp(self):
        a0 = Data.objects.create(value = 1,date = datetime.datetime(2019, 2, 26, 6, 11, 40, tzinfo=timezone.utc))
        a1 = Data.objects.create(value = 1,date = timezone.now() - datetime.timedelta(seconds = 60))
        a2 = Data.objects.create(value = 1,date = timezone.now() - datetime.timedelta(seconds = 60 * 3))
        a3 = Data.objects.create(value = 0,date = timezone.now() - datetime.timedelta(seconds = 60 * 4))

    def test_value_zero_count(self):
        """
        Count of objects with value 1 which is to be 1
        """
        a = Data.objects.filter(value = 0)
        self.assertEqual(a.count(), 1)

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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["values"].count(), 4)

    def test_chart(self):
        """
        Check if charts page is accessible
        """
        c = Client()
        response = c.get("/chart")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["values"].count(), 3)


class TestWebSocket:

    @pytest.mark.django_db(transaction=True)
    @pytest.mark.asyncio
    async def test_connection(self):
        """
        Check if websocket connection can be created
        """
        communicator = WebsocketCommunicator(DataConsumer, "/ws/post")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        await communicator.send_json_to({'value':1})
        response = await communicator.receive_from()
        #print (response)
        # Close
        await communicator.disconnect()
