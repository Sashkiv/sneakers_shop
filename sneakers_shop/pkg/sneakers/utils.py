import random

LOWER_SYMBOLS = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
UPPER_SYMBOLS = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)])
NUMBERS = ''.join([str(i) for i in range(0, 10)])


def random_string(size=10, chars=LOWER_SYMBOLS+UPPER_SYMBOLS+NUMBERS):
    return ''.join(random.choice(chars) for _ in range(size))
