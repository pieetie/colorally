#!/usr/bin/env python3

import random

def generate_random_color():
    """
    Generate a random color in a hexadecimal format
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def generate_random_pair():
    """
    Generate a random pair of colors and return it as a list
    """
    color1 = generate_random_color()
    color2 = generate_random_color()
    return [color1, color2]

if __name__ == "__main__":
    print(generate_random_pair())