from random import randint
from secrets import token_urlsafe

from a_discord_webhook.url import mount_url

numbers = [str(randint(0,9)) for i in range(18)]

identifier = int(''.join(numbers))
token = token_urlsafe(64)
url = mount_url(identifier, token)

print(url)