from urllib.parse import urlparse

def mount_url(identifier, token):
    if not isinstance(identifier, (str, int)):
        raise TypeError("identifier must be a string or int")

    if not isinstance(token, str):
        raise TypeError("token must be a string")
    
    return f'https://discord.com/api/webhooks/{identifier}/{token}'

def extract_id_and_token(url):
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    path = urlparse(url).path.split('/')
    identifier = path[-2]
    token = path[-1]
    
    return (identifier, token)