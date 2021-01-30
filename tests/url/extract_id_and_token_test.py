from random import randint
from secrets import token_urlsafe

from a_discord_webhook.url import mount_url
from a_discord_webhook.url import extract_id_and_token

numbers = [str(randint(0,9)) for i in range(18)]

identifier = ''.join(numbers)
token = token_urlsafe(64)
url = mount_url(identifier, token)

values = extract_id_and_token(url)

print(values)

assert values[0] == identifier
assert values[1] == token
