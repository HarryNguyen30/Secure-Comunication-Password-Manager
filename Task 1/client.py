"""
The client, it will connect to the server, send a message and receive one back.
It is currently not secure, so to fix that, set up the SSL certificates and
add the following lines to the code:

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("ca.crt")
context.check_hostname = False
context.wrap_socket(socket_object)

# For more information on how to use the ssl library, refer to https://docs.python.org/3/library/ssl.html
"""

import socket
import ssl

if __name__ == "__main__":
    HOST = 'localhost'  # Server hostname or IP
    PORT = 2250  # The same port as used by the server
    print(f"Connecting to the server at {HOST}: {PORT}")

    # SSL Context setup for client
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations("barryCA.crt")  # Load CA certificate (Barry's certificate)
    context.check_hostname = False  # Disable hostname checking (optional, based on use case)

    # Create TCP socket and wrap it with SSL
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            ssock.connect((HOST, PORT))  # Connect using SSL-wrapped socket
            ssock.sendall(b"Be careful. There's no telling what tricks they have planned.")
            data = ssock.recv(1024)  # Use ssock for receiving data
    print(f"Client <- Server: {bytes.decode(data)}")
