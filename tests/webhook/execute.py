import os
import time
from a_discord_webhook import Webhook

text = 'message 1'
webhook = Webhook(os.environ['URL']).set_content(text).execute()

time.sleep(5)
webhook.set_content('message 2').execute()