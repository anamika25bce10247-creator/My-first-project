# CAESAR CIPHER
# OBJECTIVE
This project is a python implementation of the Caesar Cipher, one of the oldest and most famous encryption techniques.It allows users to encrypt and decrypt text by shifting letters by a given key value.
# How it works 
1. The user logs in with a username and password.
2. After login, the user inputs a message and chooses whether to encrypt or decrypt.
3. The user provides a shift key (number).
4. For encryption: each letter in the message is shifted forward in the alphabet by the key.
5. For decryption: each letter is shifted backward by the key to restore the original message.
6. The program uses modular arithmetic to wrap around the alphabet (after 'z' comes 'a').
7. The process repeats until the user decides to exit.
8. Only lowercase letters are processed; other characters remain unchanged
# Features of this project 
1. Encryption of messages.
2. Decryption of messages.
3. User friendly input system.
4. Handles any shift.
5. No external libraries.
6. Beginner friendly cryptography 
# Requirments 
1.Python 3.x installed on the system to run the program.
2. Basic knowledge of Python syntax, input/output functions, and string manipulation.
3. User credentials (username: "vitb", password: "vitb@123") for login authentication.
4. Understanding of the Caesar cipher concept (shifting letters in the alphabet).
5. Support for lowercase English letters only in encryption/decryption.
6. Ability to input messages, choose between encrypt or decrypt, and specify the shift key.
7. Loop control to allow multiple operations until the user opts to exit.
# Module used = 
String: This built-in Python module is used to access the constant (string.ascii_lowercase) , which provides the alphabet for shifting letters during encryption and decryption.

# Screenshots of the output 
<img width="1128" height="460" alt="Screenshot 2025-11-23 210925" src="https://github.com/user-attachments/assets/c8b6b899-6df3-461f-962d-3fbec786609b" />


# CONCLUSION 
The Caesar Cipher project successfully demonstrates how a simple yet historically significant encryption technique can be implemented using Python. By allowing users to encrypt and decrypt messages through letter shifting, the program provides a clear understanding of the basic principles of substitution ciphers. This project highlights important programming concepts such as string manipulation, modular arithmetic, and the use of translation tables, making it an excellent beginner-friendly introduction to cryptography. Overall, the project achieves its objective of showing how classical encryption works while remaining easy to use, efficient, and educational.
