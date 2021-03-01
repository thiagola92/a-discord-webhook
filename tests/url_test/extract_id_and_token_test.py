from random import randint
from secrets import token_urlsafe
from unittest import TestCase

from a_discord_webhook.url import mount_url
from a_discord_webhook.url import extract_id_and_token

class ExtractIdAndTokenTest(TestCase):
    def test_extract_random_identifier_and_token(self):
        numbers = [str(randint(0,9)) for i in range(18)]
        identifier = ''.join(numbers)
        token = token_urlsafe(64)
        url = mount_url(identifier, token)

        values = extract_id_and_token(url)

        assert values[0] == identifier
        assert values[1] == token