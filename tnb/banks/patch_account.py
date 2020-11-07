import requests


def patch(*, ip, account_number, trust,
          node_id, signature, schema="http"):
    """
    Send a PATCH request of an account to a Bank
    Return response as Python object
    """
    url = f"{schema}://{ip}/accounts/{account_number}"
    body = {
        "message": {
            "trust": trust
        },
        "node_identifier": node_id,
        "signature": signature
    }

    response = requests.patch(url, json=body)
    response.raise_for_status()

    return response.json()
