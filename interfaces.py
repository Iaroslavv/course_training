from base_interface import BaseInterface


class RequestsInterface(BaseInterface):

    def __init__(self, base_url):
        super().__init__(base_url, 'requests')

    def send_data_api(self, http_method, path, data=None):
        return self._send_request(
            http_method=http_method,
            path=path,
            data=data,
            url=self.base_url,
            headers={'Content-Type': 'application/json'}
        ).json()
