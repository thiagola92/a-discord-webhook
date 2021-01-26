from requests import Session
from .url import mount_url, extract_id_and_token

class Webhook:

    def __init__(self, url=None, identifier=None, token=None):
        self.url = url
        self.identifier = identifier
        self.token = token

        self.json = {
            'content': None,
            'username': None,
            'avatar_url': None,
            'file': None,
            'embeds': None,
            'payload_json': None,
            'allowed_mentions': None,
        }

        self.headers = {
            'Content-Type': 'application/json',
        }

        if url != None:
            self.identifier, self.token = extract_id_and_token(url)
        elif identifier != None and token != None:
           self.url = mount_url(identifier, token)
        else:
            raise TypeError("missing url or identifier with token")

    def set_content(self, content):
        if not isinstance(content, (str, None)):
            raise TypeError("content must be a string")
        self.json['content'] = content

        return self

    def set_username(self, username):
        if not isinstance(username, (str, None)):
            raise TypeError("username must be a string")
        self.json['username'] = username

        return self

    def execute(self):
        with Session() as session:
            session.headers.update(self.headers)
            session.post(self.url, json=self.json)
        
        return self