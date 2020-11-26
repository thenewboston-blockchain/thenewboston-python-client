from tnb.validators import Validator


def test_success_fetch_accounts(requests_mock):
    accounts = [
        {
            "id": "4cb1cdbe-ebbf-43c8-9f86-826aaa2af250",
            "account_number": "9bfa37627e2dba0ae48165b219e76ceaba036b3db8e84108af73a1cce01fad35",
            "balance": 6,
            "balance_lock": "749f6faa4eeeda50f51334e903a1eaae084435d53d2a85fb0993a518fef27273",
        },
        {
            "id": "9c6dd61a-438c-4a95-b1d2-33f90bd7f6ad",
            "account_number": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
            "balance": 380,
            "balance_lock": "aca94f4d2f472c6b9b662f60aab247b9c6aef2079d63b870e2cc02308a7c822b",
        },
    ]

    result = {
        "count": 2,
        "next": None,
        "previous": None,
        "results": accounts,
    }

    requests_mock.get("http://42.0.6.9:80/accounts", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_accounts()
    assert response == result


def test_success_fetch_accounts_on_page_2(requests_mock):
    results = [
        {
            "id": "4cb1cdbe-ebbf-43c8-9f86-826aaa2af250",
            "account_number": "9bfa37627e2dba0ae48165b219e76ceaba036b3db8e84108af73a1cce01fad35",
            "balance": 6,
            "balance_lock": "749f6faa4eeeda50f51334e903a1eaae084435d53d2a85fb0993a518fef27273",
        },
        {
            "id": "9c6dd61a-438c-4a95-b1d2-33f90bd7f6ad",
            "account_number": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
            "balance": 380,
            "balance_lock": "aca94f4d2f472c6b9b662f60aab247b9c6aef2079d63b870e2cc02308a7c822b",
        },
    ]

    address = "42.0.6.9"
    url = f"http://{address}:80/accounts"

    payload = {
        "count": 6,
        "next": f"{url}?limit=2&offset=4",
        "previous": f"{url}?limit=2",
        "results": results,
    }

    requests_mock.get(f"{url}?limit=2&offset=2", json=payload)

    validator = Validator(address=address)
    response = validator.fetch_accounts(offset=2, limit=2)
    assert response == payload


def test_success_fetch_account_balance(requests_mock):
    result = {"balance": 50546}

    requests_mock.get(
        "http://42.0.6.9:80/accounts/a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f/balance",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_account_balance(
        "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"
    )
    assert response == result


def test_success_fetch_account_balance_lock(requests_mock):
    result = {
        "balance_lock": "e9a91c4aed7593fd08bae4daac411e3a6bd1e01dc56cd2f5f060f8c790414f35"
    }

    requests_mock.get(
        "http://42.0.6.9:80/accounts/a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f/balance_lock",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_account_balance_lock(
        "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"
    )
    assert response == result


def test_success_fetch_confirmation_blocks(requests_mock):
    result = {
        "message": {
            "block": {
                "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84421329086e03d91a68acdb",
                "message": {
                    "balance_key": "e6a41b658e17ab2db4355176c8160de6a66b07e5cbdd85244b55b38b4fd26e92",
                    "txs": [
                        {
                            "amount": 60,
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
                "signature": "d857184b7d3121a8f9dccab09062fafc82dd0fb30a5d53e19ab25a587171bb9c6b33858353cd3ff7ddc1ad2bf\
                            c59a885e85827799bcfc082fd048f9bf34bd404",
            }
        }
    }

    requests_mock.get(
        "http://42.0.6.9:80/confirmation_blocks/4c9595b2b661a23e665256d6826ae940bd4ea82bef0c1ba7b3104e40a4c42b91/valid",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_confirmation_block(
        "4c9595b2b661a23e665256d6826ae940bd4ea82bef0c1ba7b3104e40a4c42b91"
    )
    assert response == result


def test_success_fetch_config(requests_mock):
    result = {
        "primary_validator": None,
        "account_number": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
        "ip_address": "54.183.17.224",
        "node_identifier": "2262026a562b0274163158e92e8fbc4d28e519bc5ba8c1cf403703292be84a51",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "root_account_file": "http://54.183.17.224/media/root_account_file.json",
        "root_account_file_hash": "cc9390cc579dc8a99a1f34c1bea5d54a0f45b27ecee7e38662f0cd853f76744d",
        "seed_block_identifier": "",
        "daily_confirmation_rate": None,
        "node_type": "PRIMARY_VALIDATOR",
    }

    requests_mock.get(
        "http://42.0.6.9:80/config",
        json=result,
    )
    validator = Validator(address="42.0.6.9")
    response = validator.fetch_validator_config()

    assert response == result


def test_success_connection_request(requests_mock):
    result = {}

    requests_mock.post(
        "http://42.0.6.9:80/connection_requests",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.connection_requests(
        address="42.0.6.10",
        port=80,
        protocol="http",
        node_id="d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        signature="3c88665e123e7e25a8b9d9592f3269ab4efc4bcba989a103a898e2625933261b"
        "1cccdaf2f52eca9c58d2bf033968ab6b702089bca8fc6e0c80b3b002a5e05b03",
    )

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
            "confirmation_expiration": None,
            "trust": "0.00",
        },
        {
            "account_number": "7977b7f7a6f52bf9ebda93694d9276e9e23049eb40b263799fb2a35fa9316b9b",
            "ip_address": "143.110.141.4",
            "node_identifier": "735bfc11f802dbb8365998703539823d751ac5f5f82905143fba8a84d967f29b",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 2,
            "confirmation_expiration": None,
            "trust": "0.00",
        },
    ]

    results = {"count": 2, "next": None, "previous": None, "results": banks}

    requests_mock.get("http://42.0.6.9:80/banks", json=results)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_banks()

    assert response == results


def test_success_fetch_banks_page_2(requests_mock):
    results = [
        {
            "account_number": "da8500cb8e2ffd728f919cfae82b1c4e97ca2558f2545ab1b020a4172642dce3",
            "ip_address": "54.175.144.139",
            "node_identifier": "3464d43af1c920dc5fb20b1717431345e244035e76d3a37b4ef97e6040b9d464",
            "port": 80,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 2,
            "confirmation_expiration": None,
            "trust": "0.00",
        },
        {
            "account_number": "da8500cb8e2ffd728f919cfae82b1c4e97ca2558f2545ab1b020a4172642dce3",
            "ip_address": "34.202.233.224",
            "node_identifier": "3d6de056dc9ecbca2b4c832017dcb5dbdc2c95dd3175244acf7dfbc21add76de",
            "port": 80,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "confirmation_expiration": None,
            "trust": "0.00",
        },
    ]

    request_data = {
        "count": 2,
        "next": "http://42.0.6.9:80/banks?limit=2&offset=4",
        "previous": "http://42.0.6.9:80/banks?limit=2",
        "results": results,
    }

    requests_mock.get("http://42.0.6.9:80/banks", json=request_data)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_banks(offset=2, limit=2)

    assert response == request_data


def test_success_fetch_bank(requests_mock):
    result = {
        "account_number": "dfddf07ec15cbf363ecb52eedd7133b70b3ec896b488460bcecaba63e8e36be5",
        "ip_address": "143.110.137.54",
        "node_identifier": "6dbaff44058e630cb375955c82b0d3bd7bc7e20cad93e74909a8951f747fb8a4",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "confirmation_expiration": None,
        "trust": "0.00",
    }

    node_id = "6dbaff44058e630cb375955c82b0d3bd7bc7e20cad93e74909a8951f747fb8a4"
    requests_mock.get(f"http://42.0.6.9:80/banks/{node_id}", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_bank(node_id=node_id)

    assert response == result


def test_success_patch_bank(requests_mock):
    result = {
        "account_number": "dfddf07ec15cbf363ecb52eedd7133b70b3ec896b488460bcecaba63e8e36be5",
        "ip_address": "143.110.137.54",
        "node_identifier": "d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "confirmation_expiration": None,
        "trust": "0.00",
    }

    node_id = "d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1"
    signature = (
        "3c88665e123e7e25a8b9d9592f3269ab4efc4bcba989a103a898e2625933261b1cccdaf2f52eca9c5"
        "8d2bf033968ab6b702089bca8fc6e0c80b3b002a5e05b03"
    )
    requests_mock.patch(f"http://42.0.6.9:80/banks/{node_id}", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.patch_bank(trust=99.99, signature=signature, node_id=node_id)

    assert response == result


def test_success_fetch_validators(requests_mock):
    validators = [
        {
            "account_number": "4699a423c455a40feb1d6b90b167584a880659e1bf9adf9954a727d534ff0c16",
            "ip_address": "54.219.178.46",
            "node_identifier": "b1b232503b3db3975524faf98674f22c83f4357c3d946431b8a8568715d7e1d9",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "https://gist.githubusercontent.com/buckyroberts/0688f136b6c1332be472a8b"
            "af10f78c5/raw/323fcd29672e392be2b934b82ab9eac8d15e840f/alpha-00.json",
            "root_account_file_hash": "0f775023bee79884fbd9a90a76c5eacfee38a8ca52735f7ab59dab63a75cbee1",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "0.00",
        },
        {
            "account_number": "d5c4db217c032ef21df84be4201766b73e623940ce6d95aedf153da2f8c38626",
            "ip_address": "54.67.72.197",
            "node_identifier": "61dbf00c2dd7886f01fda60aca6fffd9799f4612110fe804220570add6b28923",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "https://gist.githubusercontent.com/buckyroberts/0688f136b6c1332be472a8baf1"
            "0f78c5/raw/323fcd29672e392be2b934b82ab9eac8d15e840f/alpha-00.json",
            "root_account_file_hash": "0f775023bee79884fbd9a90a76c5eacfee38a8ca52735f7ab59dab63a75cbee1",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "0.00",
        },
    ]

    results = {"count": 2, "next": None, "previous": None, "results": validators}

    requests_mock.get("http://42.0.6.9:80/validators", json=results)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_validators()

    assert response == results


def test_success_fetch_validators_page_2(requests_mock):
    validators = [
        {
            "account_number": "4699a423c455a40feb1d6b90b167584a880659e1bf9adf9954a727d534ff0c16",
            "ip_address": "54.219.178.46",
            "node_identifier": "b1b232503b3db3975524faf98674f22c83f4357c3d946431b8a8568715d7e1d9",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "https://gist.githubusercontent.com/buckyroberts/0688f136b6c1332be472"
            "a8baf10f78c5/raw/323fcd29672e392be2b934b82ab9eac8d15e840f/alpha-00.json",
            "root_account_file_hash": "0f775023bee79884fbd9a90a76c5eacfee38a8ca52735f7ab59dab63a75cbee1",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "0.00",
        },
        {
            "account_number": "d5c4db217c032ef21df84be4201766b73e623940ce6d95aedf153da2f8c38626",
            "ip_address": "54.67.72.197",
            "node_identifier": "61dbf00c2dd7886f01fda60aca6fffd9799f4612110fe804220570add6b28923",
            "port": None,
            "protocol": "http",
            "version": "v1.0",
            "default_transaction_fee": 1,
            "root_account_file": "https://gist.githubusercontent.com/buckyroberts/0688f136b6c1332be472a"
            "8baf10f78c5/raw/323fcd29672e392be2b934b82ab9eac8d15e840f/alpha-00.json",
            "root_account_file_hash": "0f775023bee79884fbd9a90a76c5eacfee38a8ca52735f7ab59dab63a75cbee1",
            "seed_block_identifier": "",
            "daily_confirmation_rate": None,
            "trust": "0.00",
        },
    ]

    request_data = {
        "count": 2,
        "next": "http://42.0.6.9:80/validators?limit=2&offset=4",
        "previous": "http://42.0.6.9:80/validators?limit=2",
        "results": validators,
    }

    requests_mock.get("http://42.0.6.9:80/validators", json=request_data)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_validators(offset=2, limit=2)

    assert response == request_data


def test_success_fetch_validator(requests_mock):
    result = {
        "account_number": "2e86f48216567302527b69eae6c6a188097ed3a9741f43cc3723e570cf47644c",
        "ip_address": "54.183.17.224",
        "node_identifier": "2262026a562b0274163158e92e8fbc4d28e519bc5ba8c1cf403703292be84a51",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "root_account_file": "http://54.183.17.224/media/root_account_file.json",
        "root_account_file_hash": "cc9390cc579dc8a99a1f34c1bea5d54a0f45b27ecee7e38662f0cd853f76744d",
        "seed_block_identifier": "",
        "daily_confirmation_rate": None,
        "trust": "100.00",
    }

    node_id = "2262026a562b0274163158e92e8fbc4d28e519bc5ba8c1cf403703292be84a51"
    requests_mock.get(f"http://42.0.6.9:80/validators/{node_id}", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_validator(node_id=node_id)
    print(response)
    assert response == result


def test_success_patch_validator(requests_mock):
    result = {
        "account_number": "dfddf07ec15cbf363ecb52eedd7133b70b3ec896b488460bcecaba63e8e36be5",
        "ip_address": "143.110.137.54",
        "node_identifier": "d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1",
        "port": None,
        "protocol": "http",
        "version": "v1.0",
        "default_transaction_fee": 1,
        "confirmation_expiration": None,
        "trust": "0.00",
    }

    node_id = "d5356888dc9303e44ce52b1e06c3165a7759b9df1e6a6dfbd33ee1c3df1ab4d1"
    signature = (
        "3c88665e123e7e25a8b9d9592f3269ab4efc4bcba989a103a898e2625933261b1cccdaf2"
        "f52eca9c58d2bf033968ab6b702089bca8fc6e0c80b3b002a5e05b03"
    )
    requests_mock.patch(f"http://42.0.6.9:80/validators/{node_id}", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.patch_validator(
        trust=99.99, signature=signature, node_id=node_id
    )

    assert response == result


def test_success_post_upgrade_request(requests_mock):
    result = [200, {}]

    requests_mock.post(
        "http://42.0.6.9:80/upgrade_request", json=result, status_code=200
    )

    validator = Validator(address="42.0.6.9")
    response = validator.post_upgrade_request(
        validator_node_identifier="validatornodeidentifier1234",
        node_identifier="validatoridentifier1234",
        signature="signature",
    )

    assert response == result
