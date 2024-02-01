import pytest
import socket
import threading
from unittest.mock import patch, MagicMock

# Assuming your Server class is in a file named Connection.py
from testing_base import Server

def message_handler(message):
    return message
@patch('socket.socket')
def test_init(mock_socket):
    host = 'localhost'
    port = 5000
    server = Server(host, port, message_handler)

    assert server.host == host
    assert server.port == port
    mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_socket.return_value.bind.assert_called_once_with((host, port))
    assert isinstance(server.clients, list)

def test_get_clients():
    host = 'localhost'
    port = 5000
    server = Server(host, port, message_handler)

    assert server.get_clients() == server.clients

# Test sending a message to the port and assert that the value printed is the same as the value sent
def test_send():
    host = 'localhost'
    port = 5000
    server = Server(host, port, message_handler)
    server.start()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(b'Hello, world')
    client.close()

    # The message should be printed to the console
    assert server.message_handler('Hello, world') == 'Hello, world'
    server.close()