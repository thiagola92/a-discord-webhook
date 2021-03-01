from random import randint
from secrets import token_urlsafe
from unittest import TestCase

from a_discord_webhook.url import mount_url

class MountUrlTest(TestCase):
    def create_random_identifier(self):
        numbers = [str(randint(0,9)) for i in range(18)]
        return ''.join(numbers)

    def test_mount_url_with_identifier_as_string(self):
        identifier = self.create_random_identifier()
        token = token_urlsafe(64)
        url = mount_url(identifier, token)

    def test_mount_url_with_identifier_as_int(self):
        identifier = int(self.create_random_identifier())
        token = token_urlsafe(64)
        url = mount_url(identifier, token)