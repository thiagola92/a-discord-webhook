import os
from a_discord_webhook import Webhook

fields = {
    'username': 'Billy',
    'content': 'hello',
    'avatar_url': 'https://todoapk.org/wp-content/uploads/2020/09/among-us-apk.jpg',
}

webhook = Webhook(os.environ['URL']).set_fields(fields).execute()

for k, v in fields.items():
    assert webhook.json[k] == v