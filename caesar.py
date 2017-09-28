def encrypt(text, rot):
    ret = ""

    for character in text:
        ret = ret + rotate_character(character,rot)

    return ret

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
