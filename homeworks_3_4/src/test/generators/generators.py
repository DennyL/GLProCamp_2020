import os
from string import ascii_letters, digits
from random import choice
from homeworks_3_4.src.test.config import Links


def item_names_generator(length=8) -> str:
    """
        :param : desired number of random symbols following the 'item_' title
        :returns : a string 'item_' followed by a row of random numbers
    """
    chars = ascii_letters + digits
    return 'item_' + ''.join(choice(chars) for _ in range(length))


def item_codes_generator(length=3) -> str:
    """
        :param : desired number of random digits in a returned sequence
        :returns : a string sequence of random numbers
    """
    return ''.join(choice(digits) for _ in range(length))


def item_picture_provider():
    """ :returns an absolute path to a randomly picked image file from the test data images folder
        configured in Configs.Links
    """
    images_abs_paths = []
    for file in os.listdir(Links.LINK_TO_IMAGES_FOLDER):
        images_abs_paths.append(os.path.abspath(f'{Links.LINK_TO_IMAGES_FOLDER}/{file}'))
    return choice(images_abs_paths)
