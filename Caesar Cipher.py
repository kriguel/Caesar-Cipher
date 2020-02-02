"""                    CIFRA DE CAESAR / CAESAR CIPHER                       """


def cipher_encrypt(txt, k):
    """ Receives a text and a key to encrypt the text."""
    result = ""

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]

        # Character is uppercase.
        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        # Character is lowercase.
        elif char.islower():
            result += chr((ord(char) + k - 97) % 26 + 97)
        # Character is a space.
        elif char == " ":
            result += char

    return result


def cipher_decrypt(txt, k):
    """ Receives the encrypted text and the key to decrypt the text."""
    result = ""

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]

        # The character is uppercase.
        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)
        # The character is lowercase.
        elif char.islower():
            result += chr((ord(char) - k - 97) % 26 + 97)
        # The character is a space.
        elif char == " ":
            result += char

    return result


action = input("Press 'e' to encrypt or 'd' to decrypt: ")

# User select Encrypt.
if action == "e":
    text = input("Text that will be encrypted: ")
    key = int(input("Enter the key number(1-25): "))

    # Tests for a valid key.
    while key not in range(1, 25):
        key = int(input("Invalid key. Must be a number betwen 1-25. "))

    print(f"Encrypted text:\n {cipher_encrypt(text, key)}")

# User selected Decrypt
elif action == "d":
    text = input("Text that will be decrypted: ")
    key = int(input("Enter the key number(1-25): "))

    # Tests for a valid key.
    while key not in range(1, 25):
        key = int(input("Invalid key. Must be a number betwen 1-25. "))

    print(f"Encrypted text:\n {cipher_decrypt(text, key)}")
