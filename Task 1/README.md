# Task 1: Securing a Communication Channel with SSL

This task demonstrates a secure client-server communication system in Python using **SSL/TLS encryption**. SSL certificates were created with **OpenSSL**, and are used to encrypt all data transmitted between the client and server to prevent eavesdropping and unauthorized access.

By using SSL sockets, this program ensures that even with tools like Wireshark, no readable data can be intercepted—highlighting the importance of encrypted communication in network security.

---

## 🔧 Files Included

- `client.py` – Connects to the SSL-secured server, sends a message, and prints the server’s reply.
- `server.py` – Listens for incoming SSL client connections, processes messages, and responds.
- `certs/` – Contains all SSL certificates and keys:
  - `ca.crt` – Barry’s Certificate Authority (CA)
  - `server.crt`, `server.key` – Jill’s server certificate and private key
  - `client.crt`, `client.key` – Chris’s client certificate and private key

---

## 🛠 Setup Instructions

### Requirements
- Python 3.7 or later
- OpenSSL (used to generate certificates)
- Wireshark (optional, for testing sniffing)
  
### SSL Certificates
SSL certificates are already included in the certs/ folder and correctly configured. Barry acts as the trusted Certificate Authority (CA), issuing certificates to both the client and server.

### Installation
Install Python packages if not already available:

```bash
pip install ssl socket
```
## ▶️ Running the Programs

### Steps

1. **Start the server**
- Open a terminal and run:
  
    ```bash
    
    python server.py
    ```
    This starts Jill’s SSL server and waits for incoming connections.

3.  **Start the client**
- In a separate terminal window, run:    
    ```bash
    python client.py
    ```
    This launches Chris’s client, establishes a secure connection, sends a message, and receives a response.

4. **Test interception (optional)**
- Open Wireshark and inspect the packets exchanged. You'll observe that intercepted data appears encrypted and unintelligible—validating the confidentiality of the communication.

