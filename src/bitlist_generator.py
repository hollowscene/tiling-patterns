# -*- coding: utf-8 -*-
"""
Bitlist Generator.

@author: Andrew Ting
@last-modified: 2022/07/09
"""


# %% Imports

import random


# %% Functions

def generate_random_bitlist(length: int, bits: int) -> list:
    """Generate a random bitlist.

    Parameters
    ----------
    length : int
        Length of bitlist.
    bits : int
        Possible bit values from 0 to bits - 1.

    Returns
    -------
    A list of bits of the given input length.

    """
    assert length > 0
    assert bits > 0

    bitlist = []

    for _ in range(length):
        bitlist.append(random.choice(range(0, bits)))

    return bitlist


# %% Testing

if __name__ == "__main__":
    bitlist = generate_random_bitlist(100, 4)
    print(bitlist)
