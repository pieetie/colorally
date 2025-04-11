#!/usr/bin/env python3

from scripts.convert_colors import *
from scripts.generate_colors import *
from scripts.render_colors import *
from scripts.verify_colors import *

def viz_pair():
    """ 
    Generate a color visualization for two colors
    """
    paire = generate_random_pair()
    #print(paire)
    dic1 = convert_colors(paire)
    #print(dic1)
    if verify_pairs(dic1):
        #print("PASS")
        final_dic = verif_colors(dic1)

        print(final_dic)
        """ 
        Result exemple for print(final_dic)
        {
            'color2': {
                'normal': '#54251e', 
                'protanopia': '#2e2a1d', 
                'deuteranopia': '#38321e', 
                'tritanopia': '#612023', 
                'grey scale': '#2e2e2e'}, 
                
            'color1': {
                'normal': '#f7ba19', 
                'protanopia': '#e4b110', 
                'deuteranopia': '#f5c31d', 
                'tritanopia': '#ff9d89', 
                'grey scale': '#bbbbbb'}
        }
        """

        if final_dic:
            render_colors(final_dic)
    else: 
        print("FAIL")

    

def main():
    """
    """
    pass 

if __name__ == "__main__":
    viz_pair()