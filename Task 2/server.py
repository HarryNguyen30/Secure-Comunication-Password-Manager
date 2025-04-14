"""
A password manager server.
You will need to give it the ability to correctly store passwords and to send them back to the
client when requested.
"""


import socket


password_storage = {}

def handle_message(conn: socket.socket, data: bytes) -> bool:
    """
    Take a received message from the client and perform the action specified in its message, return
    whether the program should end.

    Arguments:
    - conn: The client socket object, for sending messages back to the client
    - data: bytes containing the message received by the client
    """
    message = data.decode('utf-8').strip().split(' ',2) #Transform message from byte to list (through string) for easy handling.

    if data == b"end":
        conn.sendall(b"bye")
        return True
    # TODO: Add handling for the other messages (including handling the passwords correctly)
   
    # Store command - Store password is mapped to the website
    elif message[0] == "store" and len(message) == 3:
        website, encrypted_password = message[1], message[2]
        password_storage[website] = encrypted_password
        conn.sendall(b"Password successfully stored.")

    # Get command - send back the password is mapped to specified website to client 
    elif message[0] == "get" and len(message) == 2:
        website = message[1]
        if website in password_storage:
            encrypted_password_str = password_storage[website]
            conn.sendall(bytes(encrypted_password_str, 'utf-8'))
        else:
            conn.sendall(b'Website not found')
    else:
        conn.sendall(b'Invalid command')

    #print(f"Client -> Server: {data}")
    return False


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 22500  # Arbitrary non-privileged port
    end = False
    print(f"Listening for a client on port {PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while not end:
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(4096)
                    if not data: break
                    end = handle_message(conn, data)
