from django.test import TestCase
from decouple import config
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Nilton Moura', cpf='12345678901',
                    email=config('EMAIL_ADDRESS'), phone='21-12345-6789')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = config('EMAIL_ADDRESS')
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = [config('EMAIL_ADDRESS'), config('EMAIL_ADDRESS')]
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Nilton Moura', '12345678901',
                    config('EMAIL_ADDRESS'), '21-12345-6789']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
