#!/usr/bin/env python3 

try:
    from generate_colors import generate_random_pair
    from convert_colors import convert_colors
    from verify_colors import verify_pairs
except ImportError:
    from .generate_colors import generate_random_pair
    from .convert_colors import convert_colors
    from .verify_colors import verify_pairs

def gen_valid_pair(): 
    """ 
    This function generate a valid pair that pass the verification and return the dic of the two colors
    like that : 
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
    while True:
        # Generate a random pair of colors
        random_pair = generate_random_pair()
        
        # Convert the pair to all vision types
        converted_pair = convert_colors(random_pair)
        
        # Verify if the pair passes all vision tests
        if verify_pairs(converted_pair):
            return converted_pair

def make_pairs(number=1):
    """ 
    This function use gen_valid_pair to generate X pairs
    Return a big dictionnary that contains all the dictionnary of pairs 
    """
    result = {}
    
    for i in range(number):
        # Generate a valid pair
        pair = gen_valid_pair()
        
        # Add the pair to the result dictionary with a unique key
        pair_key = f"pair_{i+1}"
        result[pair_key] = pair
    
    return result

if __name__ == "__main__":
    # Test the functions
    pair = gen_valid_pair()
    print(pair)
    
    print("\nGenerating 3 pairs")
    pairs = make_pairs(3)
    print(pairs)
    for key, value in pairs.items():
        print(f"{key}:")
        print(f"  Color 1: {value['color1']['normal']}")
        print(f"  Color 2: {value['color2']['normal']}")