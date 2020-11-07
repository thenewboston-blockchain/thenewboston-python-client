import pytest
import requests_mock
from requests.exceptions import HTTPError

from tnb.banks import Bank


def test_success_fetch_accounts(requests_mock):
    result = [{
        "id": "9eca00a5-d925-454c-a8d6-ecbb26ec2f76",
        "created_date": "2020-07-08T02:14:59.307535Z",
        "modified_date": "2020-07-08T02:14:59.307553Z",
        "account_number": "4d2ec91f37bc553bc538e91195669b666e26b2ea3e4e31507e",
        "trust": "75.21"
    }]

    requests_mock.get(
        "http://10.2.3.4:80/accounts",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_accounts()
    assert response == result


def test_success_fetch_bank_transactions(requests_mock):
    result = [
        {
            "id": "a85a4692-e03d-4419-8b25-813598b367bd",
            "block": {
                "id": "e00c5522-1b73-4a46-bd03-629d446eec19",
                "created_date": "2020-07-14T03:14:36.436771Z",
                "modified_date": "2020-07-14T03:14:36.436796Z",
                "balance_key": "efa253d24ee516fe5ed45bb4e47a3146026e97f766df1",
                "sender": "0cdd4ba04456ca169baca3d66eace869520c62fe8442132908",
                "signature": "a1bbd321ad6d3f74f027de5a2c19457779fe1466708c2ea"
            },
            "amount": "12.5000000000000000",
            "recipient": "484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5"
        }
    ]
    requests_mock.get(
        "http://10.2.3.4:80/bank_transactions",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_bank_transactions()
    assert response == result


def test_success_fetch_invalid_blocks(requests_mock):
    result = [
        {
            "id": "2bcd53c5-19f9-4226-ab04-3dfb17c3a1fe",
            "created_date": "2020-07-11T18:44:16.518695Z",
            "modified_date": "2020-07-11T18:44:16.518719Z",
            "block_identifier": "65ae26192dfb9ec41f88c6d582b374a9b42ab58833e",
            "block": "3ff4ebb0-2b3d-429b-ba90-08133fcdee4e",
            "confirmation_validator": "fcd2dce8-9e4f-4bf1-8dac-cdbaf64e5ce8",
            "primary_validator": "51461a75-dd8d-4133-81f4-543a3b054149"
        }
    ]
    requests_mock.get(
        "http://10.2.3.4:80/invalid_blocks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_invalid_blocks()
    assert response == result


def test_success_fetch_validators(requests_mock):
    result = [
        {
            "account_number": "ad1f8845c6a1abb6011a2a434a079a087c460657aad543",
            "ip_address": "192.168.1.74",
            "node_identifier": "3afdf37573f1a511def0bd85553404b7091a76bcd79cd",
            "port": 8000,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": "4.0000000000000000",
            "root_account_file": ("https://gist.githubusercontent.com/"
                                  "buckyroberts/519b5cb82a0a5b5d4ae8a2175b7"
                                  "520/raw/9237deb449e27cab93cb89ea3346ecdf1"
                                  "fe9ea/0.json"),
            "root_account_file_hash": "4694e1ee1dcfd8ee5f989e59ae40a9f75181f",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "100.00"
        }
    ]
    requests_mock.get(
        "http://10.2.3.4:80/validators",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_validators()
    assert response == result


def test_success_patch_account(requests_mock):
    result = {
        "id": "64426fc5-b3ac-42fb-b75b-d5ccfcdc6872",
        "created_date": "2020-07-14T02:59:22.204580Z",
        "modified_date": "2020-07-21T00:58:01.013685Z",
        "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329",
        "trust": "99.98"
    }
    requests_mock.patch(
        "http://10.2.3.4:80/accounts/0cdd4ba04456ca169baca3d66eace869520c62",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.patch_account(
        account_number="0cdd4ba04456ca169baca3d66eace869520c62",
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1a",
        trust=99.98,
        signature="f41788fe19690a67abe3336d4ca84565c090691efae0e5cdd8bf02e126",
    )

    assert response == result


def test_success_connection_requests(requests_mock):
    result = []
    requests_mock.post(
        "http://10.2.3.4:80/connection_requests",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.connection_requests(
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1",
        signature="f41788fe19690a67abe3336d4ca84565c090691efae0e5cdd8bf02e12",
    )

    assert response == result
