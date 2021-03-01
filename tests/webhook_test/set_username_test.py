import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class SetUsernameTest(TestCase):
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

    def test_set_username(self):
        username = 'Bobby'

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=SetUsernameTest.get_response):
            webhook = Webhook(os.environ['URL']).set_username(username)

        assert webhook.fields['username'] == username