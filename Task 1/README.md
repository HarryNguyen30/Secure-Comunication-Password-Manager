# Task 1: Securing a Communication Channel with SSL

This task demonstrates a basic client-sever communication model in Python using SSL (set up certificate by OpenSSL) to ensure encrypted data transmission. The client connect to server, send a message and receives a response, all over a secure SSl/TLS connection.

client.py: A client program that connects to the server, sends a message, and receives a reply from the server.
server.py: A server program that waits for client connections, receives a message, and sends a reply back to the client.

## Setup

To run these programs you will need to install a recent version of python3, preferably version 3.7 or higher.



## Running the programs

To see what an interceptor adversary could find from the programs, you can install
and use Wireshark (https://www.wireshark.org/).

SSL certificate already set up and attached with the program.

The programs work with standard Python 3.7+, first start the server in one command prompt/terminal with `python server.py`, the server will listen for incoming connections on the specified port, which means you are ready to start the client with `python client.py`. 



The server and client will exchange messages and output what they got from each other. You can now check the interceptor, Wireshark will give random byte output and nothing meaningful that can be read.
