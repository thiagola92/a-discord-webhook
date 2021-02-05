import os
import time
from a_discord_webhook import Webhook

webhook = Webhook(os.environ['URL']).set_content('message 1').execute()
time.sleep(5)
webhook.set_content('message 2').execute()