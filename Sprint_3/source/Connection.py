import threading
import socket
import signal

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket, message_handler):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.client_address = client_address
        self.message_handler = message_handler
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", self.client_address)
        self.receive_messages()  # Call the method to handle incoming messages
        self.csocket.close()
    
    def send(self, message):
        self.csocket.send(message)
    
    def receive_messages(self):
        while True:
            try:
                data = self.csocket.recv(1024).decode()  # Receive data from the client
                if not data:
                    break  # If no data received, break the loop
                print("Received message:", data)
                self.message_handler(data)  # Call the message handler function
            except ConnectionResetError:
                break  # If connection reset by the client, break the loop


class Server(threading.Thread):
    def __init__(self, host, port, message_handler):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.clients = []  # List to store all connected clients
        self.message_handler = message_handler
        print("Server started")
        print("Waiting for client request..")

    def run(self):
        while True:
            self.server.listen(1)
            client_sock, client_address = self.server.accept()
            new_thread = ClientThread(client_address, client_sock, self.message_handler)
            self.clients.append(new_thread)  # Add the new client to the list
            new_thread.start()

    def get_clients(self):
        return self.clients
    
    def send(self, message):
        for client in self.clients:
            client.send(message)
    
    def close(self):
        for client in self.clients:
            client.csocket.close()
        self.server.close()

def handle_interrupt(server, signal, frame):
    print("KeyboardInterrupt detected. Disconnecting...")
    for client in server.get_clients():
        client.csocket.close()
    server.server.close()
    exit(0)


# Usage example:
if __name__ == "__main__":
    LOCALHOST = "127.0.0.1"
    PORT = 8080

    def message_handler(message):
        # Perform your logic with the received message here
        print("Handling message:", message)

    server = Server(LOCALHOST, PORT, message_handler)
    
    print("Registering signal handler for KeyboardInterrupt")
    signal.signal(signal.SIGINT, lambda signal, frame: handle_interrupt(server, signal, frame))

    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        handle_interrupt(server, signal, None)