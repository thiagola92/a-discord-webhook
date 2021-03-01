from requests import Session
from .url import mount_url, extract_id_and_token

class Webhook:

    def __init__(self, url=None, identifier=None, token=None):
        self._set_credentials(url, identifier, token)

        default_fields = self.get()

        self.channel_id = default_fields.get('channel_id')
        self.guild_id = default_fields.get('guild_id')

        self.fields = {
            'content': None,
            'username': default_fields.get('name'),
            'avatar_url': default_fields.get('avatar'),
            'tts': None,
            'file': None,
            'embeds': None,
            'payload_json': None,
            'allowed_mentions': None,
        }

    def _set_credentials(self, url, identifier, token):
        if url != None:
            self.url = url
            self.identifier, self.token = extract_id_and_token(url)
        elif identifier != None and token != None:
            self.identifier = identifier
            self.token = token
            self.url = mount_url(identifier, token)
        else:
            raise TypeError("missing url or identifier with token")

    def set_content(self, content):
        if not isinstance(content, str) and avatar_url != None:
            raise TypeError("content must be a string")
        self.fields['content'] = content

        return self

    def set_username(self, username):
        if not isinstance(username, str) and avatar_url != None:
            raise TypeError("username must be a string")
        self.fields['username'] = username

        return self

    def set_avatar_url(self, avatar_url):
        if not isinstance(avatar_url, str) and avatar_url != None:
            raise TypeError("avatar_url must be a string")
        self.fields['avatar_url'] = avatar_url

        return self

    def update_fields(self, fields: dict):
        self.fields.update(fields)
        return self

    def set_fields(self, fields: dict):
        self.fields = fields
        return self

    def get(self):
        with Session() as session:
            session.headers.update({'Content-Type': 'application/json'})
            response = session.get(self.url)

            response.raise_for_status()
        
        return response.json()

    def modify(self):
        with Session() as session:
            session.headers.update({'Content-Type': 'application/json'})
            response = session.patch(self.url, json={
                'name': self.fields['username'],
                # 'avatar': self.fields['avatar_url']
            })

            response.raise_for_status()
        
        return self

    def execute(self):
        with Session() as session:
            session.headers.update({'Content-Type': 'application/json'})
            response = session.post(self.url, json=self.fields)

            response.raise_for_status()
        
        return self