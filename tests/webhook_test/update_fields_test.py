import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class UpdateFieldsTest(TestCase):
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

    def test_update_fields(self):
        fields = {
            'username': 'Bobby',
            'content': 'hello',
            'avatar_url': 'https://todoapk.org/wp-content/uploads/2020/09/among-us-apk.jpg',
        }

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=UpdateFieldsTest.get_response):
            webhook = Webhook(os.environ['URL']).update_fields(fields)

        for k, v in fields.items():
            assert webhook.fields[k] == v

        assert webhook.fields['username'] == fields['username']