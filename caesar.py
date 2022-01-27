import string
from string import ascii_lowercase, whitespace, punctuation

def cipher(plain_ext: str, shift_number: int) -> str:
    string
    encrypted_text: str = ''
    shift_number = shift_number % len(ascii_lowercase)
    allowed_letters = ascii_lowercase * 2
    whitespace_and_punctuation = whitespace + punctuation
    for letter in plain_ext:
        position = allowed_letters.find(letter)
        if position != -1:
            letter_shifted = allowed_letters[position + shift_number]
            encrypted_text += letter_shifted
        elif whitespace_and_punctuation.find(letter) != -1:
            letter_shifted = allowed_letters[position + shift_number]
            encrypted_text += letter
    return encrypted_text

def cipher_with_translate(plain_text: str, shift_number: int) -> str:
    letters = ascii_lowercase
    mask = letters[shift_number:] + letters[:shift_number]
    translation_table = str.maketrans(letters, mask)
    encrypted_text = plain_text.translate(translation_table)
    return encrypted_text



if __name__=='__main__':
    plain_text = 'abcd xyz'
    shift_number = 4
    encrypted_text = cipher_with_translate(plain_text, shift_number)
    print(encrypted_text)