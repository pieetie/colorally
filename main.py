#!/usr/bin/env python3

from scripts.convert_colors import *
from scripts.generate_colors import *
from scripts.render_colors import *
from scripts.verify_colors import *
from scripts.generate_palettes import *

def viz_pair():
    """ 
    Generate a color visualization for two colors
    """
    viz_pair_dic = gen_valid_pair()
    render_colors(viz_pair_dic)

def main():
    """
    """
    pass 

if __name__ == "__main__":
    viz_pair()