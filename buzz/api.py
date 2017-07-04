import os
import secrets
import requests
from urllib.parse import parse_qs, urlparse


def gif_search(query):
    api_url = "http://api.giphy.com/v1/stickers/search"
    data = {
        "q": query,
        "api_key": os.environ.get('GIPHY_KEY')
    }
    results = request_to_api(api_url, 'data', data)

    if len(results) == 0:
        return None

    return secrets.choice(results)["images"]["fixed_height"]["url"]


def image_search(query):
    api_url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search"
    data = {
        "q": query
    }
    headers = {
        "Ocp-Apim-Subscription-Key": os.environ.get('BING_KEY')
    }
    results = request_to_api(api_url, 'value', data, headers)

    if len(results) == 0:
        return None

    url = secrets.choice(results)["contentUrl"]
    return parse_qs(urlparse(url).query, keep_blank_values=True)["r"][0]


def request_to_api(api_url, key, data=None, headers=None):
    headers = {} if headers is None else headers
    data = {} if data is None else data
    r = requests.get(api_url, params=data, headers=headers)
    return r.json().get(key, [])
