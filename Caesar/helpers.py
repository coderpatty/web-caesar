def alphabet_position(letter):
    ret = ord(letter) - alpha_offset(letter)

    return ret

def rotate_character(char, rot):
    if alpha_offset(char) == 0:
        ret = char
    else:   
        ret = chr(wrap(char, rot) + alpha_offset(char))

    return ret

def wrap(char, rot):
    ret = (alphabet_position(char) + int(rot))%26

    return ret

def alpha_offset(char):
    if ord(char) >= 65 and ord(char) <= 90:
        ret = 65
    elif ord(char) >= 97 and ord(char) <= 122:
        ret = 97
    else:
        ret = 0
    
    return ret

def encrypt(text, key):
    ret = ""
    key_offset = 0

    for character in text:
        if alpha_offset(character) == 0:
            ret += character
            continue
        ret += rotate_character(character, alphabet_position(key[key_offset]))
        if key_offset == len(key)-1:
            key_offset = 0
        else:
            key_offset += 1

    return ret