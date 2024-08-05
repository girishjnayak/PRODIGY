def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            char_code = ord(char)
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            new_char = chr(base + (char_code - base + shift_amount) % 26)
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice.lower() == 'e':
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
