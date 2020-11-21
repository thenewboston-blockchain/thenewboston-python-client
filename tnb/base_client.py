from urllib.parse import urljoin
from typing import Union

import requests


class BaseClient(object):
    """
    Common class for sending request to server
    """

    def __init__(self, *, address: str, protocol="http", port=80):
        self.address = address
        self.protocol = protocol
        self.port = port
        self.base_url = f"{protocol}://{address}:{port}/"

    def send_request(
        self, method: str, resource: str, **kwargs: dict
    ) -> Union[dict, list]:
        """
        Fetch `resource` from a Node
        Return response as Python object
        """
        url = urljoin(self.base_url, resource)
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()

    def send_request_from_url(
        self, method: str, url: str, **kwargs: dict
    ) -> Union[dict, list]:
        """
        Fetch a ressource from a Node given a specific URL
        Return response as Python object
        """
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()

    def fetch(self, resource: str, **kwargs: dict) -> Union[dict, list]:
        """
        GET a `resource` from a Node
        Return response as Python object
        """
        return self.send_request("GET", resource, **kwargs)

    def delete(self, resource: str, **kwargs: dict) -> Union[dict, list]:
        """
        DELETE a `resource` from a Node
        Return response as Python object
        """
        return self.send_request("DELETE", resource, **kwargs)

    def patch(self, resource: str, body: dict, **kwargs: dict) -> Union[dict, list]:
        """
        PATCH a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("PATCH", resource, json=body, **kwargs)

    def post(self, resource: str, body: dict, **kwargs: dict) -> Union[dict, list]:
        """
        POST a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("POST", resource, json=body, **kwargs)

    def put(self, resource: str, body: dict, **kwargs: dict) -> Union[dict, list]:
        """
        PUT a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("PUT", resource, json=body, **kwargs)
