from string import ascii_letters, digits
from random import choice


def item_name_generator():
    chars = ascii_letters + digits
    return 'item_' + ''.join(choice(chars) for _ in range(8))
