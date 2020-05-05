import socket
from _thread import *
import sys

server = "10.0.0.52"  # The local IP address of your machine.
port = 55555  # Can be any unused port.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialize new socket.

# Binds the server (IP address) to the port thus creating a new socket.
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Enables the socket to wait and accept the specified number of connections.
s.listen(2)
print("Waiting for a connection, server started")


def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    # Closes threaded connection.
    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()  # Stores incoming connections and IP addresses.
    print("Connected to: ", addr)  # Prints addresses connected to socket.
    start_new_thread(threaded_client, (conn,))