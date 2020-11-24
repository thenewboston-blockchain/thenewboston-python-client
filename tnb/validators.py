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

    def fetch_validator_config(self) -> dict:
        """
        Fetch config from validator

        Return response as a Python object
        """
        return self.fetch("/config")

    def connection_requests(self, node_id: str, signature: str) -> dict:
        """
        Send connection request

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

        return self.post("/connection_requests", body=body)

    def fetch_banks(self, offset: int = 0, limit: int = 50) -> dict:
        """
        Fetch Bank list

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as a Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/banks", params=params)

    def fetch_bank(self, node_id: str) -> dict:
        """
        Fetch Bank

        :param node_id: Node identifier

        Return response as a Python object
        """
        return self.fetch(f"/banks/{node_id}")

    def patch_bank(self, trust: float, node_id: str, signature: str) -> dict:
        """
        Set trust level

        :param trust: Trust level as float
        :param node_id: Node identifier
        :param signature: Message signed by signature key

        Return response as Python object
        """
        resource = f"/banks/{node_id}"
        body = {
            "message": {"trust": trust},
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.patch(resource, body=body)

    def fetch_validators(self, offset: int = 0, limit: int = 50) -> dict:
        """
        Fetch Validators

        :param offset: The offset to start at. Default: 0
        :param limit: The limit of results to retrieve. Default: 50

        Return response as Python object
        """
        params = {"offset": offset, "limit": limit}
        return self.fetch("/validators", params=params)

    def fetch_validator(self, node_id: str) -> dict:
        """
        Fetch Validator

        :param node_id: Node identifier

        Return response as a Python object
        """
        return self.fetch(f"/validators/{node_id}")

    def patch_validator(self, node_id: str, trust: float, signature: str) -> dict:
        """
        Set Validator trust level

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

    def post_upgrade_request(
        self, validator_node_identifier: str, node_identifier: str, signature: str
    ) -> dict:
        """
        Post an upgrade notice to a validator and get the result status code

        :param validator_node_identifier: Node identifier of bank receiving the request

        :param node_identifier: Node identifier of Validator sending the request
        :param signature: Signature of the message

        Return response as Python object
        """

        body = {
            "message": {"validator_node_identifier": validator_node_identifier},
            "node_identifier": node_identifier,
            "signature": signature,
        }

        return self.post("/upgrade_request", body=body)
