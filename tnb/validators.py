from tnb.base_client import BaseClient


class Validator(BaseClient):
    def fetch_accounts(self, offset: int = 0, limit: int = 50) -> dict:
        """
        Fetch accounts from validator

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as a Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/accounts", params=params)

    def fetch_account_balance(self, account_number: str) -> dict:
        """
        Fetch account balance from account
        :param account_number: The account number of the account

        Return response as a Python object
        """

        return self.fetch(f"/accounts/{account_number}/balance")

    def fetch_account_balance_lock(self, account_number: str) -> dict:
        """
        Fetch balance lock for account with number account_number
        :param account_number: The account number of the account

        Return response as a Python object
        """
        return self.fetch(f"/accounts/{account_number}/balance_lock")

    def fetch_confirmation_block(self, block_identifier: str) -> dict:
        """
        Fetch confirmation block by block_identifier
        :param block_identifier: ID for the block

        Return response as Python object
        """

        return self.fetch(f"/confirmation_blocks/{block_identifier}/valid")
