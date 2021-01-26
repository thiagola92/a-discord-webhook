import os
from a_discord_webhook import Webhook

username = 'Billy'

fields = {
    'content': 'hello',
    'avatar_url': 'https://todoapk.org/wp-content/uploads/2020/09/among-us-apk.jpg',
}

webhook = Webhook(os.environ['URL']).set_username(username).update_fields(fields).execute()

for k, v in fields.items():
    assert webhook.json[k] == v

assert webhook.json['username'] == username