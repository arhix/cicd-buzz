import os
from buzz import api


def test_gif_search():
    key = os.environ.get('GIPHY_KEY')
    os.environ["GIPHY_KEY"] = ""

    result = api.gif_search('pugs')
    assert result is None

    os.environ["GIPHY_KEY"] = key
    result = api.gif_search('pugs')
    assert type(result) == str


def test_image_search():
    key = os.environ.get('BING_KEY')
    os.environ["BING_KEY"] = ""

    result = api.image_search('pugs')
    assert result is None

    os.environ["BING_KEY"] = key
    result = api.image_search('pugs')
    assert type(result) == str
