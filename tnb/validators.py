from tnb.base_client import BaseClient


class Validator(BaseClient):
    def fetch_accounts(self):
        """
        Fetch accounts from validator
        Return response as a Python object
        """

        return self.fetch("/accounts")

    def fetch_account_balance(self, account_number):
        """
        Fetch account balance from account with number account_number
        Return response as a Python object
        """

        return self.fetch("/accounts/{}/balance".format(account_number))

    def fetch_account_balance_lock(self, account_number):
        """
        Fetch balance lock for account with number account_number
        Return response as a Python object
        """
        return self.fetch("/accounts/{}/balance_lock".format(account_number))

    def fetch_confirmation_blocks(self, block_identifier):
        """
        Fetch confirmation block by block_identifier
        Return response as Python object
        """

        return self.fetch("/confirmation_blocks/{}/valid".format(block_identifier))