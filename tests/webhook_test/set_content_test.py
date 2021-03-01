import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class SetContentTest(TestCase):
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

    def test_set_content(self):
        text = 'hello world'

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=SetContentTest.get_response):
            webhook_1 = Webhook(os.environ['URL'])

        webhook_1.set_content(text)

        assert webhook_1.fields['content'] == text

    def test_if_set_content_returns_equal_webhook(self):
        text = 'hello world'

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=SetContentTest.get_response):
            webhook_1 = Webhook(os.environ['URL'])
            webhook_2 = Webhook(os.environ['URL']).set_content(text)

        webhook_1.set_content(text)

        assert webhook_1.fields['content'] == text
        assert webhook_1.fields['content'] == webhook_2.fields['content']