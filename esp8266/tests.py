from django.test import Client, TestCase

from .models import Data
import datetime
from django.utils import timezone

class DataTestCase(TestCase):

    def setUp(self):
        a0 = Data.objects.create(value = 1,date = datetime.datetime(2019, 2, 26, 6, 11, 40, tzinfo=timezone.utc))
        a1 = Data.objects.create(value = 1,date = timezone.now() - datetime.timedelta(seconds = 60))
        a2 = Data.objects.create(value = 1,date = timezone.now() - datetime.timedelta(seconds = 60 * 3))
        a3 = Data.objects.create(value = 0,date = timezone.now() - datetime.timedelta(seconds = 60 * 4))

    def test_value_zero_count(self):
        a = Data.objects.filter(value = 0)
        self.assertEqual(a.count(), 1)

    def test_total_count(self):
        a = Data.objects.all()
        self.assertEqual(a.count(), 4)

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["values"].count(), 4)

    def test_chart(self):
        c = Client()
        response = c.get("/chart")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["values"].count(), 3)
