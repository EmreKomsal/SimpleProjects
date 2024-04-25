def encryption(plain_text, key):
    cipher_text = ""
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        
        if char.isupper():
            cipher_text += chr((ord(char) + key - 65) % 26 + 65)
        elif char == " ":
            cipher_text += " "
        else:
            cipher_text += chr((ord(char) + key - 97) % 26 + 97)
            
    return cipher_text

def decryption(cipher_text, key):
    plain_text = ""
    
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        
        if char.isupper():
            plain_text += chr((ord(char) - key - 65) % 26 + 65)
        elif char == " ":
            plain_text += " "
        else:
            plain_text += chr((ord(char) - key - 97) % 26 + 97)
    
    return plain_text

def main():
    plain_text = input("Enter the text to encrypt: ")
    key = int(input("Enter the key for encryption: "))
    
    cipher_text = encryption(plain_text, key)
    print("The encrypted text is:", cipher_text)
    
    decrypted_text = decryption(cipher_text, key)
    print("The decrypted text is:", decrypted_text)
    
if __name__ == "__main__":
    main()