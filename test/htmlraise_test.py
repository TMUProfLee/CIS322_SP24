import pytest
from mac_import import * 
from source.CardGames import *
from source.flask_file import app, pot

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_raise_button(client):
    client.post('/process_form', data={'input_name':' John Doe', 'input_money': 500})
    
    response = client.post('/player_action', data={'action': 'raise', 'amount': 100})
    assert response.status_code == 200
    assert 'Raise successful' in response.data.decode('utf-8')
    
def test_insufficient_funds(client):
    response = client.post('/process_form', data={'input_name': 'Player 1', 'input_money': 50})
    response = client.post('/player_action', data={'action': 'raise', 'amount': 100, 'player_index': 1})
    assert response.status_code == 200
    assert 'You do not have enough money for this bet.' in response.data.decode('utf-8'), "Unexpected message: {}".format(response.data.decode('utf-8'))


if __name__ == '__main__':
    pytest.main()

