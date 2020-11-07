from urllib.parse import urljoin

import requests


class BaseClient(object):
    """
    Common class for sending request to server
    """
    def __init__(self, *, address, protocol='http', port=80):
        self.address = address
        self.portocol = protocol
        self.port = port
        self.base_url = f"{protocol}://{address}:{port}/"

    def send_request(self, method, resource, **kwargs):
        """
        Fetch `resouce` from a Bank
        Return response as Python object
        """
        url = urljoin(self.base_url, resource)
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()

    def fetch(self, resource, **kwargs):
        """
        GET a `resource` from a Bank
        Return response as Python object
        """
        return self.send_request('GET', resource, **kwargs)

    def delete(self, resource, **kwargs):
        """
        DELETE a `resource` fron a Bank
        Return response as Python object
        """
        return self.send_request('DELETE', resource, **kwargs)

    def patch(self, resource, body, **kwargs):
        """
        PATCH a `resource` to a Bank
        Return response as Python object
        """
        return self.send_request('PATCH', resource, json=body, **kwargs)

    def post(self, resource, body, **kwargs):
        """
        POST a `resource` to a Bank
        Return response as Python object
        """
        return self.send_request('POST', resource, json=body, **kwargs)

    def put(self, resource, body, **kwargs):
        """
        PUT a `resource` to a Bank
        Return response as Python object
        """
        return self.send_request('PUT', resource, json=body, **kwargs)
