import os
from random import randint
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class InitTest(TestCase):
    get_response = {
        'type': 1,
        'id': os.environ['IDENTIFIER'],
        'name': 'Billy',
        'avatar': None,
        'channel_id': '123456789123456789',
        'guild_id': '123456789123456789',
        'application_id': None,
        'token': os.environ['TOKEN']
    }

    def test_init_in_different_ways(self):
        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=InitTest.get_response):
            webhook_1 = Webhook(os.environ['URL'])
            webhook_2 = Webhook(url=os.environ['URL'])
            webhook_3 = Webhook(
                identifier=os.environ['IDENTIFIER'],
                token=os.environ['TOKEN'],
            )

        assert webhook_1.url == webhook_2.url
        assert webhook_2.url == webhook_3.url