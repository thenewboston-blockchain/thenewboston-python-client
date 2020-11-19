from nacl.signing import SigningKey
from typing import Tuple


def create_account() -> Tuple[str, str]:
    """
    Create a new account
    Return signing_key, account_number
    """

    signing_key = SigningKey.generate()
    account_number = signing_key.verify_key
    return signing_key, account_number
