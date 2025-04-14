"""
The server, it will look for a client, receive a message and send one back.
It is current not secure, so to fix that, set up the SSL certificates and
add the following lines to the code:

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.pem")
context.wrap_socket(socket_connection, server_side=True)

# For more information on how to use the ssl library, refer to https://docs.python.org/3/library/ssl.html
"""


import socket
import ssl

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 2250  # Arbitrary non-privileged port
    print(f"Listening for a client on port {PORT}")

    # SSL Context setup for server
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="jill.crt", keyfile="jill.pem")

    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        
        # Wrap the accepted connection with SSL
        with context.wrap_socket(conn, server_side=True) as ssock:
            print('Connected by', addr)
            while True:
                data = ssock.recv(1024)  # Receive data securely
                if not data:
                    break
                print(f"Client -> Server: {data.decode()}")
                ssock.sendall(b"I'll do the best I can. Let's get moving.")  # Send data securely
