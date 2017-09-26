from helpers import alphabet_position, rotate_character, wrap, alpha_offset, encrypt
    
def main():
    message = input("Please enter message to Encrypt: ")
    key = input("Enter your encryption key: ")

    encrypted = encrypt(message, key)

    print(encrypted)
   
if __name__ == "__main__":
    main()
