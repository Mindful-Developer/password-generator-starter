"""Password Generator"""

import random
import string


CHAR_MAP = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'numbers': string.digits,
    'special_characters': string.punctuation,
}


def generate_0(length):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)
    print(password)


def generate_1(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''

    if uppercase:
        chars += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)

    if lowercase:
        chars += string.ascii_lowercase
        password += random.choice(string.ascii_lowercase)

    if numbers:
        chars += string.digits
        password += random.choice(string.digits)

    if special_characters:
        chars += string.punctuation
        password += random.choice(string.punctuation)

    for _ in range(length - len(password)):
        password += random.choice(chars)

    random.shuffle(password)
    password = ''.join(password)

    print(password)


def generate_2(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''

    for key, value in CHAR_MAP.items():
        if locals()[key]:
            chars += value
            password += random.choice(value)

    for _ in range(length - len(password)):
        password += random.choice(chars)

    random.shuffle(password)
    password = ''.join(password)

    print(password)


def generate(length, **kwargs):
    password = []
    chars = ''

    if not any(kwargs.values()):
        return 'Please provide at least one password requirement'

    for item in kwargs:
        if kwargs[item] and CHAR_MAP.get(item):
            chars += CHAR_MAP[item]
            password += random.choice(CHAR_MAP[item])

    for _ in range(length - len(password)):
        password += random.choice(chars)

    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    print(generate(25, uppercase=True, lowercase=True, numbers=True, special_characters=True))
