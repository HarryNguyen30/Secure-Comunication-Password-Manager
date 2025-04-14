"""
A password manager client.
You will need to give it an interface with the options to send the server a password to store, to
get a stored password from the server, and to end the programs. You will also have to implement RSA
and use it correctly so that the server and any possible interceptor can never read the passwords.
"""

import socket

def send_receive(host: str, port: int, message: bytes) -> bytes:
    """
    Send and receive a message in bytes to the specified host at the specified port.

    Arguments:
    - host: string stating the name or ip address of the server
    - port: int stating the port number of the server
    - message: bytes object containing the message to send to the server
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message)
        data = s.recv(4096)  # 1024 states the number of bytes to receive, may need to be changed
    return data


if __name__ == "__main__":
    HOST = 'localhost'  # Server hostname or IP
    PORT = 22500  # The same port as used by the server

    # TODO: Add a user interface and correct cryptographic handling of passwords
   
    # Fast modular exponentiation algoritm use for RSA (from lab 2).
    def fast_mod_expo(b,e, n):
        if n == 1:
            return 0
        result =1
        while e > 0:
            if e & 1 ==1:
                result = ( result * b) % n
            e >>= 1
            b = (b * b) % n
        return result

    # Generate public and private key based on provided p and q.
    def generate_rsa_keys():
        with open('primes.txt', 'r') as f:
            p = int(f.readline()[2:])
            q = int(f.readline()[2:])

        n = p * q

        phi_n = (p - 1) * (q - 1)

        e = 65537 # Choose public exponet e. Checked gcd(e, phi_n) == 1

        d = pow(e, -1, phi_n) # Pow() help to calculate modular multiplicative inverse of e modulo phi_n.

        return (e,n), (d, p, q)

    def rsa_encrypt(message,public_key):
        e, n = public_key
        message_int = int.from_bytes(message.encode('utf-8')) # Convert message from string to int (through byte).
        encrypted_message = fast_mod_expo(message_int,e,n)  #Use fast modular exponentiation to encrpyt message.
        return  encrypted_message

    def rsa_decrypt(encrypted_message, private_key):
        d, p, q = private_key
        n = p*q
        decrypted_message = fast_mod_expo(encrypted_message,d, n) #Use fast modular exponentiation to decrypt message.
        return  decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'big').decode('utf-8') #Convert an integer to string
    
    def menu():
        print("You have the following option:")
        print("- store <website> <password>")
        print("- get <website>")
        print("- end\n")

    public_key, private_key = generate_rsa_keys()
    print("Welcome to the SENG2250 password manager client.") 
    while True:

        menu()

        user_input = input(">>> ").strip().split(' ',2) #Transform user input from string to list for easy handling.
        try:
            if user_input[0].lower() == 'store':
                if len(user_input) != 3:
                    raise ValueError ("Error with store command: Please provide both website and password. \n")
                website, password = user_input[1], user_input[2]
                encrypted_password = rsa_encrypt(password, public_key)
                message = bytes('store '+ website + ' '+ str(encrypted_password), 'utf-8') #Format and covert message to byte and send to server
                print((send_receive(HOST,PORT,message)).decode('utf-8'),"\n")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("Unexpected error in store command:", e, "\n")

        try:
            if user_input[0].lower() == 'get':
                if len(user_input) != 2:
                    raise ValueError ("Error with get command: Please provide website name. \n")
                website = user_input[1]
                mess = 'get ' + website #Format message to send to server
                message = bytes(mess, 'utf-8') #Convert to byte to send
                response = send_receive(HOST, PORT, message).decode('utf-8')
                if response == "Website not found":
                    print(f"{response} \n")
                else:
                    encrypted_password = int(response) #Convert to int for decrypt
                    decrypted_password = rsa_decrypt(encrypted_password, private_key)
                    print(f"Your password for {website} is {decrypted_password} \n")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("Unexpected error in get command:", e, "\n")

        if user_input[0].lower() == 'end':
            print(send_receive(HOST, PORT, b'end').decode('utf-8'))
            break

        if user_input[0].lower() not in ['store', 'get', 'end']:
            print("Invalid command, please try again. \n")
