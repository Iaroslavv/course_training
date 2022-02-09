import requests
import json

from exceptions import HttpError

def check_response(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if result.status_code not in (200, 201):
            raise HttpError(
                f'HTTP Error!\nStatus: {result.status_code} {result.reason}.\nRequest url: {result.url}',
                result.text
            )
        return result

    return wrapper

def load_data_from_file(filename):
    with open(f'{filename}', 'r') as json_file:
            data = json.load(json_file)
    return data

class BaseInterface:
    def __init__(self, base_url, mode='requests'):
        self.base_url = base_url # static url
        if mode == 'session':
            self._session = requests.session()
        else:
            self._session = requests

    @check_response
    def _send_request(self, http_method, path, data=None, url=None, **kwargs):
        if not url:
            url = self.base_url
        if data:
            data = json.dumps(data)
        response = getattr(self._session, http_method)(
            f'{url}{path}',
            data=data,
            **kwargs,
        )
        return response
