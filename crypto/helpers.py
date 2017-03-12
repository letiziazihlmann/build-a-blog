import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

def alphabet_position(letter):
    if letter in alphabet_upper:
        original_index = alphabet_upper.index(letter)
    else:
        original_index = alphabet_lower.index(letter)
    return original_index

def rotate_character(char, rot):
    #test to see if the character is alphabetic
    if char.isalpha():
        #test to see if the character is uppercase so it can be returned the same way
        if char in alphabet_upper:
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                encrypted_char = alphabet_upper[rotated_index]
            else:
                encrypted_char = alphabet_upper[rotated_index % 26]
            return encrypted_char
        #character is lower case
        else:
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                encrypted_char = alphabet_lower[rotated_index]
            else:
                encrypted_char = alphabet_lower[rotated_index % 26]
            return encrypted_char
    else:
        return char
