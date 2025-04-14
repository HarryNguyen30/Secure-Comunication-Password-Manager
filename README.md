# SENG2250 - Secure Communication & Password Manager

This repository contains the assignment for the **SENG2250 - System and Network Security** course at the University of Newcastle. It demonstrates core concepts of cryptography and secure communication using SSL and RSA, implemented in Python.

## 🔐 Project Overview

The project is divided into two main tasks:

### Task 1: SSL-Secured Communication Channel

A client-server chat system enhanced with **SSL encryption** to protect messages from interception. SSL certificates are generated manually using XCA or OpenSSL, with Barry acting as the Certificate Authority (CA).

- Implements SSL socket communication in Python.
- Prevents message sniffing via Wireshark.
- Certificates include a CA, client cert, and server cert.

### Task 2: Encrypted Password Manager with RSA

A single-client password manager where passwords are securely transmitted using a **custom-built RSA algorithm**.

- Implements custom RSA encryption/decryption.
- Uses fast modular exponentiation.
- Ensures passwords are never seen in plaintext by the server or interceptors.
- Interactive CLI interface for storing and retrieving passwords.

---

## 🛠 Technologies Used

- Python 3
- SSL (via `ssl` module)
- Sockets (`socket`)
- XCA / OpenSSL (for certificate generation)
- Custom RSA implementation (no 3rd-party crypto libraries)
- Wireshark (for testing sniffing prevention)

---

## 📁 Repository Structure
```
secure-communication-password-manager/
├── task1/
│   ├── client.py             # SSL-enabled client (Chris)
│   ├── server.py             # SSL-enabled server (Jill)
│   ├── certs/                # Folder containing CA, server, and client certificates
│   └── README.md             # Instructions for Task 1
│
├── task2/
│   ├── client.py             # Password manager client with RSA encryption
│   ├── server.py             # Password manager server
│   ├── primes.txt            # Input primes for RSA key generation
│   ├── rsa_utils.py          # (If applicable) RSA encryption/decryption functions
│   └── README.md             # Instructions for Task 2
│
├── reflections.pdf           # Written reflections for both tasks
├── .gitignore                # Ignore compiled files, certs, etc.
└── README.md                 # Top-level overview and project documentation
```

## 🚀 Getting Started

To run either task, see the `README.md` files inside the `task1/` and `task2/` folders for specific setup and execution instructions.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- XCA or OpenSSL (for SSL certificate generation)
- Wireshark (optional for sniffing demo)

---

## 📄 Reflections

Reflections on both tasks, including learning outcomes, real-world relevance, and technical challenges, are available in `reflections.pdf`.

---

## 👨‍💻 Author

**Minh Tien Nguyen**  
Bachelor of Information Technology – University of Newcastle  

---

## 📝 License

This repository is part of an academic submission. For learning and demonstration purposes only.
