from requests import Session
from .url import mount_url, extract_id_and_token

class Webhook:

    def __init__(self, url=None, identifier=None, token=None):
        self.url = url
        self.identifier = identifier
        self.token = token
        self.content = None
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
        if not isinstance(content, str):
            raise TypeError("content must be a string")
        self.content = content

        return self

    def execute(self):
        with Session() as session:
            session.headers.update(self.headers)
            session.post(self.url, json={
                'content': self.content,
            })
        
        return self