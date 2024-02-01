import pytest
import socket
import threading
from unittest.mock import patch, MagicMock

# Assuming your Server class is in a file named Connection.py
from testing_base import Server

@patch('socket.socket')
def test_init(mock_socket):
    host = 'localhost'
    port = 5000
    server = Server(host, port)

    assert server.host == host
    assert server.port == port
    mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_socket.return_value.bind.assert_called_once_with((host, port))
    assert isinstance(server.clients, list)

def test_get_clients():
    host = 'localhost'
    port = 5000
    server = Server(host, port)

    assert server.get_clients() == server.clients
