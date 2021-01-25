import os
from a_discord_webhook import Webhook

username = 'Billy'

webhook = Webhook(os.environ['URL']).set_username(username).set_content('hello').execute()

assert webhook.username == username