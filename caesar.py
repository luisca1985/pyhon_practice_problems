import string
from string import ascii_lowercase, whitespace, punctuation


def shift(letter: str, shift_number: int) -> str:
    table = ascii_lowercase[shift_number:] + ascii_lowercase[:shift_number]
    position = ascii_lowercase.find(letter)
    letter_shifted = table[position] if position != -1 else letter
    return letter_shifted


def cipher(plain_text: str, shift_number: int) -> str:
    encrypted_list = [shift(letter, shift_number) for letter in plain_text]
    encrypted_text = ''.join(encrypted_list)
    return encrypted_text


def cipher_with_translate(plain_text: str, shift_number: int) -> str:
    letters = ascii_lowercase
    mask = letters[shift_number:] + letters[:shift_number]
    translation_table = str.maketrans(letters, mask)
    encrypted_text = plain_text.translate(translation_table)
    return encrypted_text


if __name__ == '__main__':
    plain_text = 'abcd xyz'
    shift_number = -1
    encrypted_text = cipher(plain_text, shift_number)
    # encrypted_text = cipher_with_translate(plain_text, shift_number)
    print(encrypted_text)
