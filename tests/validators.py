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
