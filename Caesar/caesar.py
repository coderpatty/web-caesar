from helpers import alphabet_position, rotate_character, wrap

def encrypt(text, rot):
    ret = ""

    for character in text:
        ret = ret + rotate_character(character,rot)

    return ret

def main():
        
    message = input("Please enter message to Encrypt: ")
    rot = input("Enter Offset: ")

    encrypted = encrypt(message, rot)

    print(encrypted)
   
if __name__ == "__main__":
    main()
