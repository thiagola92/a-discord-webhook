import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class ExecuteTest(TestCase):
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

    def test_execute(self):
        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=ExecuteTest.get_response):
            with mock.patch('a_discord_webhook.webhook.Webhook.execute'):
                webhook = Webhook(os.environ['URL'])
                
        with mock.patch('a_discord_webhook.webhook.Webhook.execute'):
            webhook.set_content('message 1').execute()
            webhook.set_content('message 2').execute()