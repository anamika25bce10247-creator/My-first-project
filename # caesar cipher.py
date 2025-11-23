# caesar cipher
print(" \n===== WELCOME TO THE CAESAR CIPHER PUZZLE GAME. ===== ")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "vitb" and password == "vitb@123":
    import string
  
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

    while True:
        message = input("Write a message: ").lower()
        choice = input("Do you want to decrypt or encrypt? ").lower()
        key = int(input("How much shift do you want? "))

        if choice == "encrypt":
            print("Encrypted message:", caesar_encrypt(message, key))
        elif choice == "decrypt":
            print("Decrypted message:", caesar_decrypt(message, key))
        else:
            print("Please type encrypt or decrypt.")

        again = input("Do you want to do it with another message? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for using this game\nExiting....")
            break
else:
    print("Wrong Username or Password.....Access denied.")