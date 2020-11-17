from tnb.base_client import BaseClient


class Bank(BaseClient):
    def fetch_accounts(self):
        """
        Fetch accounts from a Bank
        Return response as Python object
        """
        return self.fetch("/accounts")

    def fetch_bank_transactions(self):
        """
        Get transactions from a Bank
        Return response as Python object
        """
        return self.fetch("/bank_transactions")

    def fetch_blocks(self):
        """
        Get blocks from a Bank
        Return response as Python object
        """
        return self.fetch('/blocks')

    def fetch_invalid_blocks(self):
        """
        Get invalid block from a Bank
        Return response as Python object
        """
        return self.fetch("/invalid_blocks")

    def fetch_confirmation_blocks(self):
        """
        Get confirmation blocks from a Bank
        Return response as Python object
        """
        return self.fetch_multiple_page("/confirmation_blocks")

    def fetch_validators(self):
        """
        Get validators from a Bank
        Return response as Python object
        """
        return self.fetch("/validators")

    def fetch_validator_confirmation_services(self):
        """
        Get validators confirmation services from a Bank

        Return response as list
        """
        return self.fetch("/validator_confirmation_services")

    def create_validator_confirmation_service(
        self, msg_end, msg_start, node_id, signature
    ):
        """
        Get validators confirmation services from a Bank

        :param msg_end: ISO 8601 string that represents the end datetime
            of message
        :param msg_start: ISO 8601 string that represents the start datetime
            of message
        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as dict
        """
        body = {
            "message": {"end": msg_end, "start": msg_start},
            "node_identifier": node_id,
            "signature": signature,
        }
        return self.post("/validator_confirmation_services", body=body)

    def fetch_banks(self):
        """
        Get banks from current bank.
        Return response as a Python object
        """

        return self.fetch("/banks")

    def fetch_config(self):
        """
        Get config from a Bank
        Return response as Python object
        """
        return self.fetch("/config")

    def patch_trust_level(self, trust, node_identifier, signature):
        """
        Set bank trust level
        :param trust: Trust value as a float
        :param node_identifier: Node identifier of bank
        :param signature: Message signed by signing key
        Returns response as Python object
        """
        resource = f"/banks/{node_identifier}"
        body = {
            "message": {"trust": trust},
            "node_identifier": node_identifier,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def patch_account(self, account_number, node_id, trust, signature):
        """
        Send a PATCH request of an account to a Bank

        :param account_number: Specify the account will be patched
        :param node_id: The Node Identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f"/accounts/{account_number}"
        body = {
            "message": {"trust": trust},
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def patch_validator(self, node_id, trust, signature):
        """
        Send a PATCH request of a validator to a Bank

        :param node_id: Node identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f"/validators/{node_id}"

        body = {
            "message": {"trust": trust},
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def send_confirmation_block(self, message, node_id, signature):
        """
        Send a confirmation block to a Bank.

        :param message: The message inside the confirmation block
        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": message,
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post("/confirmation_blocks", body=body)

    def connection_requests(self, node_id, signature):
        """
        Send a connection request to a Bank

        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": {
                "ip_address": self.address,
                "port": self.port,
                "protocol": self.protocol,
            },
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post('/connection_requests', body=body)

    def post_block(self, account_number, balance_key, transactions, signature):
        """
        Send a block request to a Bank

        :param account_number: The sender's account number
        :param balance_key: The balance_key matching the sending accounts balance_lock
        :param transactions: A list of transactions
        :param signature: Hex value of the signed message

        Return response as Python object
        """

        body = {
            "account_number": account_number,
            "message": {
                "balance_key": balance_key,
                "txs": transactions,
            },
            "signature": signature

        }

        return self.post("/blocks", body=body)

    def post_invalid_block(self, block, block_identifier, primary_validator_node_identifier, node_identifier,
                           signature):
        """
        Post an invalid block to a Bank

        :param block: The invalid block
        :param block_identifier: ID for the block
        :param primary_validator_node_identifier: Primary Validator's Node Identifier
        :param node_identifier: Node Identifier of Confirmation Validator sending the request
        :param signature: Hex value of the signed message

        Return response as Python object
        """

        body = {
            "message": {
                "block": block,
                "block_identifier": block_identifier,
                "primary_validator_node_identifier": primary_validator_node_identifier,
            },
            "node_identifier": node_identifier,
            "signature": signature,
        }

        return self.post("/invalid_blocks", body=body)
