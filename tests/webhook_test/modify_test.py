import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class ModifyTest(TestCase):
    get_response_before_modify = {
        'type': 1,
        'id': os.environ['IDENTIFIER'],
        'name': 'Billy',
        'avatar': None,
        'channel_id': '123456789123456789',
        'guild_id': '123456789123456789',
        'application_id': None,
        'token': os.environ['TOKEN']
    }

    get_response_after_modify = {
        'type': 1,
        'id': os.environ['IDENTIFIER'],
        'name': 'Bobby',
        'avatar': None,
        'channel_id': '123456789123456789',
        'guild_id': '123456789123456789',
        'application_id': None,
        'token': os.environ['TOKEN']
    }

    def test_modify(self):
        fake_username = 'Bobby'

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=ModifyTest.get_response_before_modify):
            webhook = Webhook(os.environ['URL'])

        with mock.patch('a_discord_webhook.webhook.Webhook.modify'):
            webhook.set_username(fake_username).modify()

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=ModifyTest.get_response_after_modify):
            current_username = webhook.get().get('name')

        assert current_username == fake_username