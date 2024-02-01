import threading
import socket
import signal

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        self.client_address = client_address
        print("New connection added: ", client_address)

    def run(self):
        print("Connection from : ", self.client_address)
        # your logic here
        self.csocket.close()
    
    def send(self, message):
        self.csocket.send(message)

class Server(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.clients = []  # List to store all connected clients
        print("Server started")
        print("Waiting for client request..")

    def run(self):
        while True:
            self.server.listen(1)
            client_sock, client_address = self.server.accept()
            new_thread = ClientThread(client_address, client_sock)
            self.clients.append(new_thread)  # Add the new client to the list
            new_thread.start()

    def get_clients(self):
        return self.clients
    
    def send(self, message):
        for client in self.clients:
            client.send(message)

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
    server = Server(LOCALHOST, PORT)
    
    print("Registering signal handler for KeyboardInterrupt")
    signal.signal(signal.SIGINT, lambda signal, frame: handle_interrupt(server, signal, frame))

    server.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        handle_interrupt(server, signal, None)