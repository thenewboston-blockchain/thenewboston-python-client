from tnb.banks import Bank


def test_success_fetch_accounts(requests_mock):

    accounts = [
        {
            "id": "5a8c7990-393a-4299-ae92-2f096a2c7f43",
            "created_date": "2020-10-08T02:18:07.346849Z",
            "modified_date": "2020-10-08T02:18:07.346914Z",
            "account_number": "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f",
            "trust": "0.00",
        },
        {
            "id": "2682963f-06b1-47d7-a2e1-1f8ec6ae98dc",
            "created_date": "2020-10-08T02:39:44.071810Z",
            "modified_date": "2020-10-08T02:39:44.071853Z",
            "account_number": "cc8fb4ebbd2b9a98a767e801ac2b0d296ced88b5d3b7d6d6e12e1d2d7635d724",
            "trust": "0.00",
        },
    ]

    result = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": accounts,
    }

    requests_mock.get(
        "http://10.2.3.4:80/accounts",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_accounts()
    assert response == result


def test_success_fetch_bank_transactions(requests_mock):
    bank_transactions = [
        {
            "id": "8d422974-7ca2-4386-a2aa-26ac0cab00b8",
            "block": {
                "id": "370b5e8c-03ed-4d72-b649-940e1ec82fca",
                "created_date": "2020-11-19T17:55:22.188130Z",
                "modified_date": "2020-11-19T17:55:22.188176Z",
                "balance_key": "0c10b6bd8f6effc2ed5ffc927363f73ebb81b3f086805d7d57bea416fc9796c6",
                "sender": "0d304450eae6b5094240cc58b008066316d9f641878d9af9dd70885f065913a0",
                "signature": "743bc0bfcc8db0cd0b736e5cbaf0c5fd1866fd73e805e58cdb2afd3a19"
                "8d53636a5d9d4560ec047a8c8e221da29a0f7b1b20f3bf879e7bb7c281f0890b413e02",
            },
            "amount": 1,
            "recipient": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
        },
        {
            "id": "e98c8ce2-d89e-4b72-8e90-61f431a83dd1",
            "block": {
                "id": "370b5e8c-03ed-4d72-b649-940e1ec82fca",
                "created_date": "2020-11-19T17:55:22.188130Z",
                "modified_date": "2020-11-19T17:55:22.188176Z",
                "balance_key": "0c10b6bd8f6effc2ed5ffc927363f73ebb81b3f086805d7d57bea416fc9796c6",
                "sender": "0d304450eae6b5094240cc58b008066316d9f641878d9af9dd70885f065913a0",
                "signature": "743bc0bfcc8db0cd0b736e5cbaf0c5fd1866fd73e805e58cdb2afd3a19"
                "8d53636a5d9d4560ec047a8c8e221da29a0f7b1b20f3bf879e7bb7c281f0890b413e02",
            },
            "amount": 19600,
            "recipient": "82ad4b185c2ac04440c8f1c54854819ac2ea374255e8fecc54a6f28d4fcc4814",
        },
    ]

    result = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": bank_transactions,
    }

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

    result = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": blocks,
    }

    requests_mock.get(
        "http://10.2.3.4:80/confirmation_blocks",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_confirmation_blocks()
    assert response == result


def test_success_fetch_validator_confirmation_services(requests_mock):
    confirmation_services = [
        {
            "id": "5634f7d5-fa93-40c4-8e53-472055f1aa1c",
            "created_date": "2020-09-24T22:15:09.375150Z",
            "modified_date": "2020-09-24T22:15:09.375197Z",
            "end": "2021-01-27T22:15:09.343282Z",
            "start": "2020-09-24T22:15:09.343282Z",
            "validator": "e2a138b0-ebe9-47d2-a146-fb4d9d9ca378",
        },
        {
            "id": "817a91bc-9dca-44d2-92ea-55547660e60e",
            "created_date": "2020-09-24T22:15:30.057923Z",
            "modified_date": "2020-09-24T22:15:30.057980Z",
            "end": "2020-11-30T14:15:29.982900Z",
            "start": "2020-09-24T22:15:29.982900Z",
            "validator": "97a878ac-328a-47b6-ac93-be6deee75d94",
        },
    ]
    result = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": confirmation_services,
    }

    requests_mock.get(
        "http://10.2.3.4:80/validator_confirmation_services",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_validator_confirmation_services()

    assert response == result


def test_success_create_validator_confirmation_service(requests_mock):
    result = {
        "id": "2558fd55-e132-4667-8d39-d3b5e8eb9c4d",
        "created_date": "2020-07-10T02:38:44.917554Z",
        "modified_date": "2020-07-10T02:38:44.917601Z",
        "end": "2020-07-09T22:10:25Z",
        "start": "2020-08-09T22:10:25Z",
        "validator": "fcd2dce8-9e4f-4bf1-8dac-cdbaf64e5ce8",
    }

    requests_mock.post(
        "http://10.2.3.4:80/validator_confirmation_services",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.create_validator_confirmation_service(
        msg_start="2020-07-09T22:10:25Z",
        msg_end="2020-07-09T22:10:25Z",
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1a",
        signature="f41788fe19690a67abe3336d4ca84565c090691efae0e5cdd8bf02e126",
    )

    assert response == result


def test_success_fetch_validators(requests_mock):
    validators = [
        {
            "account_number": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
            "ip_address": "54.183.17.224",
            "node_identifier": "2262026a562b0274163158e92e8fbc4d28e519bc5ba8c1cf403703292be84a51",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "https://gist.githubusercontent.com/"
            "buckyroberts/0688f136b6c1332be472a8baf10f78c5/raw/323fcd29672e392be2b934b82ab9eac8d15e840f/alpha-00.json",
            "root_account_file_hash": "0f775023bee79884fbd9a90a76c5eacfee38a8ca52735f7ab59dab63a75cbee1",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "100.00",
        },
        {
            "account_number": "4699a423c455a40feb1d6b90b167584a880659e1bf9adf9954a727d534ff0c16",
            "ip_address": "54.219.178.46",
            "node_identifier": "b1b232503b3db3975524faf98674f22c83f4357c3d946431b8a8568715d7e1d9",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "http://54.219.178.46/media/root_account_file.json",
            "root_account_file_hash": "cc9390cc579dc8a99a1f34c1bea5d54a0f45b27ecee7e38662f0cd853f76744d",
            "seed_block_identifier": "",
            "daily_confirmation_rate": 1,
            "trust": "98.00",
        },
    ]
    result = {"count": 2, "next": None, "previous": None, "results": validators}

    requests_mock.get(
        "http://10.2.3.4:80/validators",
        json=result,
    )

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_validators()
    assert response == result


def test_success_fetch_banks(requests_mock):

    banks = [
        {
            "account_number": "dfddf07ec15cbf363ecb52eedd7133b70b3ec896b488460bcecaba63e8e36be5",
            "ip_address": "143.110.137.54",
            "node_identifier": "6dbaff44058e630cb375955c82b0d3bd7bc7e20cad93e74909a8951f747fb8a4",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "trust": "100.00",
        },
        {
            "account_number": "7977b7f7a6f52bf9ebda93694d9276e9e23049eb40b263799fb2a35fa9316b9b",
            "ip_address": "143.110.141.4",
            "node_identifier": "735bfc11f802dbb8365998703539823d751ac5f5f82905143fba8a84d967f29b",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 2,
            "trust": "0.00",
        },
    ]

    result = {"count": 2, "next": None, "previous": None, "results": banks}

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
        signature="d11c5f7fcc5f541a94ceee7c73972b21c73912e41f06cc22989863fa22529"
        "f55d0b81bc9f95a203191be0259518bdfe073de77d87a7230d37bb14f21666ee40a",
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
        "root_account_file": "https://gist.githubusercontent.com/buckyroberts/519b5cb82a0a5b5d4ae8a2175b722520"
        "/raw/9237deb449e27cab93cb89ea3346ecdfc61fe9ea/0.json",
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
        signature="b9106148b9c6d445f6a5fe7bb54b552ac2ff639cb72e2af70f75659"
        "04120dbb2040987c6cad559d7aa3b507c8d475af9291e4faee4930b"
        "324996c7a3c0696805",
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


def test_success_fetch_blocks(requests_mock):
    result = [
        {
            "id": "2bcd53c5-19f9-4226-ab04-3dfb17c3a1fe",
            "created_date": "2020-07-11T18:44:16.518695Z",
            "modified_date": "2020-07-11T18:44:16.518719Z",
            "block_identifier": "65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5",
            "block": "3ff4ebb0-2b3d-429b-ba90-08133fcdee4e",
            "confirmation_validator": "fcd2dce8-9e4f-4bf1-8dac-cdbaf64e5ce8",
            "primary_validator": "51461a75-dd8d-4133-81f4-543a3b054149",
        }
    ]
    requests_mock.get("http://10.2.3.4:80/blocks", json=result)

    bank = Bank(address="10.2.3.4")
    response = bank.fetch_blocks()
    assert response == result


def test_success_post_block(requests_mock):
    result = {
        "id": "3ff4ebb0-2b3d-429b-ba90-08133fcdee4e",
        "created_date": "2020-07-09T21:45:25.909512Z",
        "modified_date": "2020-07-09T21:45:25.909557Z",
        "balance_key": "ce51f0d9facaa7d3e69657429dd3f961ce70077a8efb53dcda508c7c0a19d2e3",
        "sender": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb",
        "signature": "ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc38093918610ea88a7ad47c7f3192ed95"
        "5d9d1529e7e390013e43f25a5915c0f",
    }

    requests_mock.post("http://10.2.3.4:80/blocks", json=result)

    bank = Bank(address="10.2.3.4")

    response = bank.post_block(
        account_number="0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb",
        balance_key="ce51f0d9facaa7d3e69657429dd3f961ce70077a8efb53dcda508c7c0a19d2e3",
        transactions=[
            {
                "amount": 12.5,
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
        signature="ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc38093918610ea88a7ad47c7f3192ed955d9"
        "d1529e7e390013e43f25a5915c0f",
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
            "signature": "ee5a2f2a2f5261c1b633e08dd61182fd0db5604c853ebd8498f6f28ce8e2ccbbc"
            "38093918610ea88a7ad47c7f3192ed955d9d1529e7e390013e43f25a5915c0f",
        },
        block_identifier="65ae26192dfb9ec41f88c6d582b374a9b42ab58833e1612452d7a8f685dcd4d5",
        primary_validator_node_identifier="3afdf37573f1a511def0bd85553404b7091a76bcd79cdcebba1310527b167521",
        node_identifier="59479a31c3b91d96bb7a0b3e07f18d4bf301f1bb0bde05f8d36d9611dcbe7cbf",
        signature="c61ef8067307f8a48979a656699709e415692eb7b7b0083e3cd41da4ff6cb388e7347896b5cacb0a74200390d"
        "228b30547f73a72029ebd4ed10482db5e925b0c",
    )

    assert response == result


def test_success_post_upgrade_notice(requests_mock):
    result = [200, {}]

    requests_mock.post(
        "http://10.2.3.4:80/upgrade_notice",
        json=result,
        status_code=200,
    )

    bank = Bank(address="10.2.3.4")
    bank_nid = "banknodeidentifier1234"
    node_id = "validatoridentifier1234"
    signature = "signature"
    response = bank.post_upgrade_notice(bank_nid, node_id, signature)

    assert response == result
