import pytest


@pytest.fixture
def bank():
    return {
        'ip': '1.2.3.4',
        'node_id': 'd5356888d'
    }


@pytest.fixture
def account():
    return {
        'number': '0cdd4ba044',
        'signature': 'f41788fe12'
    }
