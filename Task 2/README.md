# Task 2: RSA-Secured Password Manager

This task implements a basic password manager with a focus on secure password transmission using a **custom-built RSA encryption algorithm**. The system consists of a client-server architecture where the client encrypts passwords before sending them to the server, ensuring that **neither the server nor any potential interceptor can view passwords in plaintext**.

---

## 🛠 Files Included

- `client.py` – Client interface that allows users to:
  - Store a password for a website
  - Retrieve stored passwords
  - Exit the application
  - Custom RSA functions for:
    - Key generation
    - Fast modular exponentiation
    - Encryption and decryption
- `server.py` – Server that listens for client requests and responds appropriately.
- `primes.txt` – File containing two large primes `p` and `q` used for RSA key generation.


---

## 🔐 Security Features

- Personal implementation of the **RSA algorithm**:
  - Computes `n`, `ϕ(n)`, `e`, and `d`
  - Implements **fast modular exponentiation**
- Passwords are encrypted on the client side using RSA **before** transmission.
- The server stores only the encrypted versions and never sees the plaintext.
- Ensures confidentiality against both external interceptors and the storage server.

---

## ▶️ Running the Programs

### Prerequisites
- Python 3.7 or later

### Steps

1. **Start the server**
- In one terminal window:
   ```bash
   python server.py
   ```
3.  **Start the client**
- In another terminal window:
       ```bash
       python client.py
       ```
3. **Interact with the system**
- Use the following commands in the client interface:
    ```
    store <website> <password> – Store a password
    get <website> – Retrieve a password
    end – Exit the client
    ```

## 💻 The following an example output and input for the client:
    Welcome to the SENG2250 password manager client.
    You have the following option:
    - store <website> <password>
    - get <website>
    - end
    
    >>> store Harry Minhtiennguyen30122003@gmail.com
    Password successfully stored. 
    
    You have the following option:
    - store <website> <password>
    - get <website>
    - end
    
    >>> get Harry
    Your password for Harry is Minhtiennguyen30122003@gmail.com
    
    You have the following option:
    - store <website> <password>
    - get <website>
    - end
    
    >>> end
    bye
