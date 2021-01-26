import os
from a_discord_webhook import Webhook

webhook = Webhook(os.environ['URL']).set_content('test modify')
original_username = webhook.fields['username']
fake_username = "Billy"

webhook.set_username(fake_username).modify().execute()
actual_username = webhook.get().get('name')
assert actual_username == fake_username

webhook.set_username(original_username).modify().execute()
actual_username = webhook.get().get('name')
assert actual_username == original_username