import os
from a_discord_webhook import Webhook

webhook_1 = Webhook(os.environ['URL'])
webhook_2 = Webhook(url=os.environ['URL'])

webhook_3 = Webhook(
    identifier=os.environ['IDENTIFIER'],
    token=os.environ['TOKEN'],
)

assert webhook_1.url == webhook_2.url
assert webhook_2.url == webhook_3.url