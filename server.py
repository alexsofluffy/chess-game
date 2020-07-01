import socket
from _thread import *

server = "10.0.0.52"  # The local IP address of your machine.
port = 55555  # Can be any unused port.

# Creates a new socket by binding the server (IP address) to the port.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))

# Enables the socket to wait and accept the specified number of connections.
s.listen(2)
print("Server started, waiting for connection...")


def threaded_client(conn):
    """Creates a new threaded process for each connection to socket.

    Keyword arguments:
    conn -- connection object
    """
    conn.send(str.encode("Connected to server"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)  # Specifies size of data received in bits.
            reply = data.decode("utf-8")  # Decodes data in specified format.

            if not data:
                # Breaks connection once data is no longer received.
                print("Disconnected")
                break
            else:
                # Prints decoded data out.
                print("Received: ", reply)
                print("Sending: ", reply)

            # Sends back encoded data to threaded client.
            conn.sendall(str.encode(reply))
        except:
            break

    # Closes threaded connection.
    print("Lost connection")
    conn.close()


# Continuously stores incoming connections and IP addresses, prints addresses
# connected to socket, and starts new threaded client for each connection.
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))
