import os
from a_discord_webhook import Webhook

avatar_url = 'https://todoapk.org/wp-content/uploads/2020/09/among-us-apk.jpg'

webhook = Webhook(os.environ['URL']).set_avatar_url(avatar_url).set_content('hello').execute()

assert webhook.json['avatar_url'] == avatar_url