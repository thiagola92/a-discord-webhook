import os
from a_discord_webhook import Webhook

text = 'hello world'

webhook_1 = Webhook(os.environ['URL'])
webhook_1.set_content(text)

webhook_2 = Webhook(os.environ['URL']).set_content(text)

assert webhook_1.json['content'] == text
assert webhook_1.json['content'] == webhook_2.json['content']