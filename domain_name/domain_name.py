from urllib.parse import urlparse

def domain_name(url:str):
    if not isinstance(url, str):
        raise TypeError("Input must be a string")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2]

    return domain