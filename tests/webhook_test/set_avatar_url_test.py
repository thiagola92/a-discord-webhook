import os
from unittest import TestCase, mock

from a_discord_webhook import Webhook

class SetAvatarUrlTest(TestCase):
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

    def test_set_avatar_url(self):
        avatar_url = 'https://todoapk.org/wp-content/uploads/2020/09/among-us-apk.jpg'

        with mock.patch('a_discord_webhook.webhook.Webhook.get', return_value=SetAvatarUrlTest.get_response):
            webhook = Webhook(os.environ['URL'])

        with mock.patch('a_discord_webhook.webhook.Webhook.execute'):
            webhook.set_avatar_url(avatar_url)
            
        assert webhook.fields['avatar_url'] == avatar_url