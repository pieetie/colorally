#!/usr/bin/env python3

from scripts.convert_colors import *
from scripts.generate_colors import *
from scripts.render_colors import *
from scripts.verify_colors import *

def test1():
    """ 
    Test 1
    """
    paire = generate_random_pair()
    print(paire)
    dic1 = convert_colors(paire)
    print(dic1)
    if verify_pairs(dic1):
        print("Paire vérifiée")
        final_dic = verif_colors(dic1)
        print(final_dic)
        if final_dic:
            render_colors(final_dic)
    else: 
        print("NON")

    

def main():
    """
    """
    pass 

if __name__ == "__main__":
    test1()