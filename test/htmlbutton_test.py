import pytest
from mac_import import *

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Input Form' in response.data

def test_process_form(client):
    response = client.post('/process_form', data={'input_name': 'John Doe', 'input_money': '100'})
    assert response.status_code == 200
    assert b'John Doe' in response.data
    assert b'100' in response.data

def test_player_action(client):
    response = client.post('/player_action', data={'amount': '50'})
    assert response.status_code == 200
    assert b'Current Pot' in response.data
    assert b'Pot: $50' in response.data

if __name__ == '__main__':
    pytest.main()
