from tnb.validators import Validator


def test_success_fetch_accounts(requests_mock):
    result = [
        {
            "id": "4cb1cdbe-ebbf-43c8-9f86-826aaa2af250",
            "account_number": "9bfa37627e2dba0ae48165b219e76ceaba036b3db8e841"
            "08af73a1cce01fad35",
            "balance": 6,
            "balance_lock": "749f6faa4eeeda50f51334e903a1eaae084435d53d2a85fb"
            "0993a518fef27273",
        }
    ]

    requests_mock.get("http://42.0.6.9:80/accounts", json=result)

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_accounts()
    assert response == result


def test_success_fetch_account_balance(requests_mock):
    result = {"balance": 50546}

    requests_mock.get(
        "http://42.0.6.9:80/accounts/a37e2836805975f334108b55523634c995bd2a4d"
        "b610062f404510617e83126f/balance",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_account_balance(
        "a37e2836805975f334108b55523634c995bd2a4db610062f404510617e83126f"
    )
    assert response == result


def test_success_fetch_account_balance_lock(requests_mock):
    result = {
        "balance_lock": "e9a91c4aed7593fd08bae4daac411e3a6bd1e01dc56cd2f5f060"
        "f8c790414f35"
    }

    requests_mock.get(
        "http://42.0.6.9:80/accounts/a37e2836805975f334108b55523634c995bd2a4d"
        "b610062f404510617e83126f/balance_lock",
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
                "account_number": "0cdd4ba04456ca169baca3d66eace869520c62fe84"
                "421329086e03d91a68acdb",
                "message": {
                    "balance_key": "e6a41b658e17ab2db4355176c8160de6a66b07e5c"
                    "bdd85244b55b38b4fd26e92",
                    "txs": [
                        {
                            "amount": 60,
                            "recipient": "484b3176c63d5f37d808404af1a12c4b964"
                            "9cd6f6769f35bdf5a816133623fbc",
                        },
                        {
                            "amount": 1,
                            "recipient": "5e12967707909e62b2bb2036c209085a784"
                            "fabbc3deccefee70052b6181c8ed8",
                        },
                        {
                            "amount": 4,
                            "recipient": "ad1f8845c6a1abb6011a2a434a079a087c4"
                            "60657aad54329a84b406dce8bf314",
                        },
                    ],
                },
                "signature": "d857184b7d3121a8f9dccab09062fafc82dd0fb30a5d53e\
                    19ab25a587171bb9c6b33858353cd3ff7ddc1ad2bfc59a885e8582779\
                        9bcfc082fd048f9bf34bd404",
            }
        }
    }

    requests_mock.get(
        "http://42.0.6.9:80/confirmation_blocks/4c9595b2b661a23e665256d6826ae\
            940bd4ea82bef0c1ba7b3104e40a4c42b91/valid",
        json=result,
    )

    validator = Validator(address="42.0.6.9")
    response = validator.fetch_confirmation_block(
        "4c9595b2b661a23e665256d6826ae940bd4ea82bef0c1ba7b3104e40a4c42b91"
    )
    assert response == result
