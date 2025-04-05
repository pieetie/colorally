#!/usr/bin/env python3 

""" 
Matrices come from the DaltonLens-Python project 
(https://github.com/DaltonLens/DaltonLens-Python/blob/master/daltonlens/simulate.py), using severity 1.0 (10)
"""

import numpy as np

def hex_to_rgb(hex_color):
    """
    Convert a hex color string to RGB values
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """
    Convert RGB values to a hex color string
    """
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def normalize_rgb(rgb):
    """
    Convert RGB values to 0-1 range
    """
    return tuple(c / 255.0 for c in rgb)

def denormalize_rgb(rgb):
    """
    Convert RGB values from 0-1 to 0-255 range
    """
    return tuple(min(255, max(0, c * 255)) for c in rgb)

def convert_to_protanopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with protanopia
    using the Machado et al. (2009) model.
    """
    rgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Transformation matrix for protanopia from Machado et al.
    sim_matrix = np.array([
        [0.152286, 1.052583, -0.204868],
        [0.114503, 0.786281, 0.099216],
        [-0.003882, -0.048116, 1.051998]
    ])
    
    simulated_rgb = np.dot(sim_matrix, rgb)
    simulated_rgb = denormalize_rgb(simulated_rgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_deuteranopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with deuteranopia
    using the Machado et al. (2009) model.
    """
    rgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Transformation matrix for deuteranopia from Machado et al.
    sim_matrix = np.array([
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501, 0.047413],
        [-0.011820, 0.042940, 0.968881]
    ])
    
    simulated_rgb = np.dot(sim_matrix, rgb)
    simulated_rgb = denormalize_rgb(simulated_rgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_tritanopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with tritanopia
    using the Machado et al. model

    TO DO : Future implementations should prioritize Brettel's matrix which is recommended specifically for tritanopia.
    """
    rgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Transformation matrix for tritanopia from Machado et al.
    sim_matrix = np.array([
        [1.255528, -0.076749, -0.178779], 
        [-0.078411, 0.930809, 0.147602], 
        [0.004733, 0.691367, 0.303900]
    ])
    
    simulated_rgb = np.dot(sim_matrix, rgb)
    simulated_rgb = denormalize_rgb(simulated_rgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_grey_scale(hex_color):
    """
    Convert a hex color to greyscale using standard luminance formula.
    """
    rgb = hex_to_rgb(hex_color)
    
    # Luminance formula for greyscale
    grey = int(0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])
    
    return "#{:02x}{:02x}{:02x}".format(grey, grey, grey)

def convert_colors(pair):
    """ 
    This function take a pair of 2 colors (list) and return a dictionnary with the HEX for the different
    types of visions such as : 
    - normal vision
    - protanopia
    - deuteranopia
    - tritanopia
    - achromatopsia (grey scale)
    """
    result = {
        "color1": {},
        "color2": {}
    }
    
    # Normal vision
    result["color1"]["normal"] = pair[0]
    result["color2"]["normal"] = pair[1]
    
    # Protanopia
    result["color1"]["protanopia"] = convert_to_protanopia(pair[0])
    result["color2"]["protanopia"] = convert_to_protanopia(pair[1])
    
    # Deuteranopia
    result["color1"]["deuteranopia"] = convert_to_deuteranopia(pair[0])
    result["color2"]["deuteranopia"] = convert_to_deuteranopia(pair[1])
    
    # Tritanopia
    result["color1"]["tritanopia"] = convert_to_tritanopia(pair[0])
    result["color2"]["tritanopia"] = convert_to_tritanopia(pair[1])
    
    # Grey scale
    result["color1"]["grey scale"] = convert_to_grey_scale(pair[0])
    result["color2"]["grey scale"] = convert_to_grey_scale(pair[1])
    
    return result

if __name__ == "__main__":
    # Test (debug)
    base_color = "#eb4034"
    print(base_color)
    print(convert_to_protanopia(base_color))
    print(convert_to_deuteranopia(base_color))
    print(convert_to_tritanopia(base_color))
    print(convert_to_grey_scale(base_color))
    print(convert_colors([base_color, base_color]))