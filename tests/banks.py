import pytest

from tnb.banks import Bank


def test_success_fetch_accounts(requests_mock):
    result = [
        {
            "id": "9eca00a5-d925-454c-a8d6-ecbb26ec2f76",
            "created_date": "2020-07-08T02:14:59.307535Z",
            "modified_date": "2020-07-08T02:14:59.307553Z",
            "account_number": "4d2ec91f37bc553bc538e91195669b666e26b2ea3e4e31507e",
            "trust": "75.21",
        }
    ]

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
                "signature": "a1bbd321ad6d3f74f027de5a2c19457779fe1466708c2ea",
            },
            "amount": "12.5000000000000000",
            "recipient": "484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5",
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
            "primary_validator": "51461a75-dd8d-4133-81f4-543a3b054149",
        }
    ]
    requests_mock.get(
        "http://10.2.3.4:80/invalid_blocks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_invalid_blocks()
    assert response == result


def test_success_fetch_confirmations_blocks(requests_mock):

    blocks = [
        {
            "id": "e7c5c2e0-8ed1-4eb3-abd8-97fa2e5ca8db",
            "created_date": "2020-10-08T02:18:07.908635Z",
            "modified_date": "2020-10-08T02:18:07.908702Z",
            "block_identifier": "824614aa97edb391784b17ce6956b70aed31edf741c1858d43ae4d566b2a13ed",
            "block": "c6fc11cf-8948-4d32-96c9-d56caa6d5b24",
            "validator": "e2a138b0-ebe9-47d2-a146-fb4d9d9ca378",
        },
        {
            "id": "78babf4b-74ed-442e-b5ab-7b23345c18f8",
            "created_date": "2020-10-08T02:18:07.998146Z",
            "modified_date": "2020-10-08T02:18:07.998206Z",
            "block_identifier": "824614aa97edb391784b17ce6956b70aed31edf741c1858d43ae4d566b2a13ed",
            "block": "c6fc11cf-8948-4d32-96c9-d56caa6d5b24",
            "validator": "97a878ac-328a-47b6-ac93-be6deee75d94",
        },
    ]

    result_page1 = {
        "count": 2,
        "next": "http://10.2.3.4:80/confirmation_blocks?limit=50&offset=1",
        "previous": None,
        "results": [
            blocks[0],
        ],
    }

    result_page2 = {
        "count": 2,
        "next": None,
        "previous": "http://10.2.3.4:80/confirmation_blocks",
        "results": [
            blocks[1],
        ],
    }
    requests_mock.get(
        "http://10.2.3.4:80/confirmation_blocks",
        json=result_page1,
    )
    requests_mock.get(
        "http://10.2.3.4:80/confirmation_blocks?limit=50&offset=1",
        json=result_page2,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_confirmation_blocks()
    assert response == blocks


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
            "root_account_file": (
                "https://gist.githubusercontent.com/"
                "buckyroberts/519b5cb82a0a5b5d4ae8a2175b7"
                "520/raw/9237deb449e27cab93cb89ea3346ecdf1"
                "fe9ea/0.json"
            ),
            "root_account_file_hash": "4694e1ee1dcfd8ee5f989e59ae40a9f75181f",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "100.00",
        }
    ]
    requests_mock.get(
        "http://10.2.3.4:80/validators",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_validators()
    assert response == result


def test_success_fetch_banks(requests_mock):
    result = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "account_number": "7977b7f7a6f52bf9ebda93694d9276e9e23049eb40b263799fb2a35fa9316b9b",
                "ip_address": "143.110.141.4",
                "node_identifier": "735bfc11f802dbb8365998703539823d751ac5f5f82905143fba8a84d967f29b",
                "port": None,
                "protocol": "http",
                "version": "v1.0",
                "default_transaction_fee": 2,
                "trust": "0.00",
            }
        ],
    }

    requests_mock.get(
        "http://10.2.3.4:80/banks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_banks()

    assert response == result


def test_success_fetch_config(requests_mock):
    result = {
        "primary_validator": {
            "account_number": "1a105575c681c5c4bbd9e88a90346f356051646dcee254afd5fdc67782cc6e56",
            "ip_address": "20.188.33.93",
            "node_identifier": "4a02e9e03ca6f2e64fe8dc675da73e31b8112e435439189012944f0b7adebf50",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "http://20.188.33.93/media/root_account_file.json",
            "root_account_file_hash": "b2885f94cd099a8c5ba5355ff9cdd69252b4cad2541e32d20152702397722cf5",
            "seed_block_identifier": "",
            "daily_confirmation_rate": 100,
            "trust": "100.00",
        },
        "account_number": "5878f25f576eb9d398ab1b6dd8b2e831ad74a58e6d6b8c8bea1c48f69a9db42d",
        "ip_address": "20.188.58.140",
        "node_identifier": "d1f994720d89c9d3b300367fdb85a452fd1fbb7d60c2e2707ff059e8df48e081",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "node_type": "BANK",
    }
    requests_mock.get(
        "http://10.2.3.4:80/config",
        json=result,
    )
    bank = Bank(address="10.2.3.4")
    response = bank.fetch_config()
    assert response == result


def test_success_patch_trust_level(requests_mock):
    result = {
        "account_number": "5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8",
        "ip_address": "192.168.1.232",
        "node_identifier": "d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        "port": "80",
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": "1.0000000000000000",
        "trust": "76.26",
    }
    requests_mock.patch(
        "http://10.2.3.4:80/banks/d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.patch_trust_level(
        trust=99.98,
        signature="d11c5f7fcc5f541a94ceee7c73972b21c73912e41f06cc22989863fa22529f55d0b81bc9f95a203191be0259518bdfe073de77d87a7230d37bb14f21666ee40a",
        node_identifier="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
    )

    assert response == result


def test_success_patch_account(requests_mock):
    result = {
        "id": "64426fc5-b3ac-42fb-b75b-d5ccfcdc6872",
        "created_date": "2020-07-14T02:59:22.204580Z",
        "modified_date": "2020-07-21T00:58:01.013685Z",
        "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329",
        "trust": "99.98",
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


def test_success_patch_validator(requests_mock):
    result = {
        "account_number": "ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314",
        "ip_address": "192.168.1.75",
        "node_identifier": "3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": "4.0000000000000000",
        "root_account_file": "https://gist.githubusercontent.com/buckyroberts/519b5cb82a0a5b5d4ae8a2175b722520/raw/9237deb449e27cab93cb89ea3346ecdfc61fe9ea/0.json",
        "root_account_file_hash": "4694e1ee1dcfd8ee5f989e59ae40a9f751812bf5ca52aca2766b322c4060672b",
        "seed_block_identifier": "",
        "daily_confirmation_rate": None,
        "trust": "76.28",
    }

    requests_mock.patch(
        "http://10.2.3.4:80/validators/d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        json=result,
    )

    bank = Bank(address="10.2.3.4")

    response = bank.patch_validator(
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        trust=76.28,
        signature="b9106148b9c6d445f6a5fe7bb54b552ac2ff639cb72e2af70f7565904120dbb2040987c6cad559d7aa3b507c8d475af9291e4faee4930b324996c7a3c0696805",
    )

    assert response == result


def test_success_send_confirmation_block(requests_mock):
    result = []
    requests_mock.post(
        "http://10.2.3.4:80/confirmation_blocks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.send_confirmation_block(
        message={"block": None},
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1",
        signature="f41788fe19690a67abe3336d4ca84565c090691efae0e5cdd8bf02e12",
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


def test_success_post_invalid_block(requests_mock):
    result = {
        "id": "2bcd53c5-19f9-4226-ab04-3dfb17c3a1fe",
        "created_date": "2020-07-11T18:44:16.518695Z",
        "modified_date": "2020-07-11T18:44:16.518719Z",
        "block_identifier": "65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5",
        "block": "3ff4ebb0-2b3d-429b-ba90-08133fcdee4e",
        "confirmation_validator": "fcd2dce8-9e4f-4bf1-8dac-cdbaf64e5ce8",
        "primary_validator": "51461a75-dd8d-4133-81f4-543a3b054149",
    }

    requests_mock.post(
        "http://10.2.3.4:80/invalid_blocks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")

    response = bank.post_invalid_block(
        block={
            "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb",
            "message": {
                "balance_key": "ce51f0d9facaa7d3e69657429dd3f961ce70077a8efb53dcda508c7c0a19d2e3",
                "txs": [
                    {
                        "amount": 12,
                        "recipient": "484b3176c63d5f37d808404af1a12c4b9649cd6f6769f35bdf5a816133623fbc",
                    },
                    {
                        "amount": 1,
                        "recipient": "5e12967707909e62b2bb2036c209085a784fabbc3deccefee70052b6181c8ed8",
                    },
                    {
                        "amount": 4,
                        "recipient": "ad1f8845c6a1abb6011a2a434a079a087c460657aad54329a84b406dce8bf314",
                    },
                ],
            },
            "signature": "ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc38093918610ea88a7ad47c7f3192ed955d9d1529e7e390013e43f25a5915c0f",
        },
        block_identifier="65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5",
        primary_validator_node_identifier="3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521",
        node_identifier="59479a31c3b91d96bb7a0b3e07f18d4bf301f1bb0bde05f8d36d9611dcbe7cbf",
        signature="c61ef8067307f8a48979a656699709e415692eb7b7b0083e3cd41da4ff6cb388e7347896b5cacb0a74200390d228b30547f73a72029ebd4ed10482db5e925b0c",
    )

    assert response == result
