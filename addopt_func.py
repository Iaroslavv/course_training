import requests

def test_url(url, status_code):
    assert requests.get(url).status_code == int(status_code)
