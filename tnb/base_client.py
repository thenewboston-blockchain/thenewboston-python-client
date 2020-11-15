from urllib.parse import urljoin

import requests


class BaseClient(object):
    """
    Common class for sending request to server
    """

    def __init__(self, *, address, protocol="http", port=80):
        self.address = address
        self.protocol = protocol
        self.port = port
        self.base_url = f"{protocol}://{address}:{port}/"

    def send_request(self, method, resource, **kwargs):
        """
        Fetch `resource` from a Node
        Return response as Python object
        """
        url = urljoin(self.base_url, resource)
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()

    def send_request_from_url(self, method, url, **kwargs):
        """
        Fetch a ressource from a Node given a specific URL
        Return response as Python object
        """
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()

        return response.json()

    def fetch(self, resource, **kwargs):
        """
        GET a `resource` from a Node
        Return response as Python object
        """
        return self.send_request("GET", resource, **kwargs)

    def fetch_multiple_page(self, resource, **kwargs):
        """
        GET a complete `resource` from a Node where this resource is splited into
        multiple pages.
        Return response as Python object
        """
        complete_response = []
        current_response = self.fetch(resource)
        complete_response += current_response["results"]
        next_url = current_response["next"]

        while next_url is not None:
            current_response = self.send_request_from_url(
                "GET", current_response["next"]
            )
            complete_response += current_response["results"]
            next_url = current_response["next"]

        return complete_response

    def delete(self, resource, **kwargs):
        """
        DELETE a `resource` from a Node
        Return response as Python object
        """
        return self.send_request("DELETE", resource, **kwargs)

    def patch(self, resource, body, **kwargs):
        """
        PATCH a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("PATCH", resource, json=body, **kwargs)

    def post(self, resource, body, **kwargs):
        """
        POST a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("POST", resource, json=body, **kwargs)

    def put(self, resource, body, **kwargs):
        """
        PUT a `resource` to a Node
        Return response as Python object
        """
        return self.send_request("PUT", resource, json=body, **kwargs)
