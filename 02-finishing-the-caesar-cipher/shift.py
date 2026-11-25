
# --- wrap around ✅ Uppercase letter ✅ lowercase letter ✅ characters (ignored) ❌---


Alphabet_size: int =  26

message: str = input("Message: ")
key: int = int(input ("Key: "))


# -- Encryption --


ciphertext: str = ""

for character in message:

    if ("A" <= character <= "Z"):                    # checks if the character is a capital letter 
        shifted: int = ord(character) + key         
        if shifted > ord("Z"):
            shifted -= Alphabet_size
        ciphertext += chr(shifted)

    elif ("a" <= character <= "z"):                  # checks if the character is a simple letter 
        shifted: int = ord(character) + key         
        if shifted > ord("z"):
            shifted -= Alphabet_size
        ciphertext += chr(shifted)

    else:
        ciphertext += character          

print("Ciphertext: ",ciphertext)


# -- Decryption --


plaintext: str = ""

for character in ciphertext:

    if ("A" <= character <= "Z"):                    # checks if the character is a capital letter 
        shifted: int = ord(character) - key         
        if shifted < ord("A"):
            shifted += Alphabet_size
        plaintext += chr(shifted)

    elif ("a" <= character <= "z"):                  # checks if the character is a simple letter 
        shifted: int = ord(character) - key         
        if shifted < ord("a"):
            shifted += Alphabet_size
        plaintext += chr(shifted)

    else:
        plaintext += character          

print("Plaintext: ",plaintext)


assert message == plaintext, "The encryption - decryption loop dosen't work"
