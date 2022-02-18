from datetime import datetime
from decouple import config
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Nilton Moura',
            cpf='12345678901',
            email=config('EMAIL_ADDRESS'),
            phone='21-12345-6789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto create_att attr."""
        self.assertIsInstance(self.obj.created_at, datetime)