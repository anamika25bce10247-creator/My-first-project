# Caesar cipher 

import string
print("WELCOME TO THE CAESAR CIPHER PUZZLE GAME.")
def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    message = encrypted_message.translate(cipher)
    return message

message = input("Write a message: ").lower()
choice = input("Do you want to decrypt or encrypt? ")
key = int(input("How much shift do you want? "))



if choice.lower() == "encrypt":
    encrypted_message = caesar_encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")
elif choice.lower() == "decrypt":
    decrypted_message = caesar_decrypt(message, key)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid choice. Type encrypt or decrypt.")
