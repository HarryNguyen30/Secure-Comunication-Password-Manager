# Task 2: A basic password manager

This password manager client communicates with a server to securely store and retrieve passwords. The client-server communication is encrypted using RSA, ensuring that passwords remain private and secure from potential interceptors.

client.py: The client application where users can store, retrieve, and manage passwords.
server.py: The server application that stores encrypted passwords and sends them back upon request.

## Running the programs

The programs work with standard Python 3.7+, first start the server in one command prompt/terminal with `python server.py`, then start the client in another command prompt/terminal with `python client.py`. 


## The following an example output and input for the client:
```
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
```
