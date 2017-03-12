from helpers import alphabet_position, rotate_character

def encrypt(text, encryption_key):
    encrypt = ''
    rotation_counter = 0
    for char in text:
        if char.isalpha():
            if rotation_counter < len(encryption_key):
                rotation = alphabet_position(encryption_key[rotation_counter])
                encrypt = encrypt + rotate_character(char, rotation)
            else:
                rotation_counter = 0
                rotation = alphabet_position(encryption_key[rotation_counter])
                encrypt = encrypt + rotate_character(char, rotation)
            rotation_counter += 1
        else:
            encrypt = encrypt + char
    return encrypt

def main():
    text = input('Please enter your text:')
    encryption_key = input('enter your encryption_key:')
    print(encrypt(text, encryption_key))

if __name__ == '__main__':
    main()
