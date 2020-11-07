import pytest
from requests.exceptions import HTTPError
import requests_mock

from tnb.banks.patch_account import patch


def test_success_patch(requests_mock, bank, account):
    requests_mock.patch(
        f"http://{bank['ip']}/accounts/{account['number']}",
        json={'trust': "88.67"}
    )

    response = patch(ip=bank['ip'], account_number=account['number'],
                     trust='88.67', node_id=bank['node_id'],
                     signature=account['signature'])

    assert response['trust'] == '88.67'


def test_failed_patch(requests_mock, bank, account):
    requests_mock.patch(
        f"http://{bank['ip']}/accounts/{account['number']}",
        json={'trust': "88.67"}, status_code=404
    )
    with pytest.raises(HTTPError):
        response = patch(ip=bank['ip'], account_number=account['number'],
                         trust='88.67', node_id=bank['node_id'],
                         signature=account['signature'])
