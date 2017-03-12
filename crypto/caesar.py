from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypt = ''
    for char in text:
        encrypt = encrypt + rotate_character(char, rot)
    return encrypt

def main():
    text = input('Please enter a text to be encrypted:')
    rotation = int(input('Please enter a number for rotation'))
    print(encrypt(text, rotation))
if __name__=='__main__':
    main()

#test as you go
#per Shane, add input to main function not inside helper function
