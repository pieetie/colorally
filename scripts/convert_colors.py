#!/usr/bin/env python3 

""" 
Matrices come from the DaltonLens-Python project 
(https://github.com/DaltonLens/DaltonLens-Python/blob/master/daltonlens/simulate.py), using severity 1.0 (10)
"""

import numpy as np

def hex_to_rgb(hex_color):
    """
    Convert a hex color string to RGB values
    
    >>> hex_to_rgb('#FF0000')
    (255, 0, 0)
    >>> hex_to_rgb('#00FF00')
    (0, 255, 0)
    >>> hex_to_rgb('#0000FF')
    (0, 0, 255)
    >>> hex_to_rgb('#000000')
    (0, 0, 0)
    >>> hex_to_rgb('#FFFFFF')
    (255, 255, 255)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    """
    Convert RGB values to a hex color string
    
    >>> rgb_to_hex((255, 0, 0))
    '#ff0000'
    >>> rgb_to_hex((0, 255, 0))
    '#00ff00'
    >>> rgb_to_hex((0, 0, 255))
    '#0000ff'
    >>> rgb_to_hex((0, 0, 0))
    '#000000'
    >>> rgb_to_hex((255, 255, 255))
    '#ffffff'
    """
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

def normalize_rgb(rgb):
    """
    Convert RGB values to 0-1 range
    
    >>> normalize_rgb((255, 0, 0))
    (1.0, 0.0, 0.0)
    >>> normalize_rgb((0, 255, 0))
    (0.0, 1.0, 0.0)
    >>> normalize_rgb((0, 0, 255))
    (0.0, 0.0, 1.0)
    >>> normalize_rgb((0, 0, 0))
    (0.0, 0.0, 0.0)
    >>> normalize_rgb((255, 255, 255))
    (1.0, 1.0, 1.0)
    """
    return tuple(c / 255.0 for c in rgb)

def denormalize_rgb(rgb):
    """
    Convert RGB values from 0-1 to 0-255 range
    
    >>> denormalize_rgb((1.0, 0.0, 0.0))
    (255, 0, 0)
    >>> denormalize_rgb((0.0, 1.0, 0.0))
    (0, 255, 0)
    >>> denormalize_rgb((0.0, 0.0, 1.0))
    (0, 0, 255)
    >>> denormalize_rgb((0.0, 0.0, 0.0))
    (0, 0, 0)
    >>> denormalize_rgb((1.0, 1.0, 1.0))
    (255, 255, 255)
    """
    return tuple(min(255, max(0, int(round(c * 255)))) for c in rgb)

def srgb_to_linear(srgb):
    """
    Convert sRGB values (0-1 range) to linearRGB (0-1 range)
    """
    result = []
    for c in srgb:
        if c <= 0.04045:
            result.append(c / 12.92)
        else:
            result.append(((c + 0.055) / 1.055) ** 2.4)
    return tuple(result)

def linear_to_srgb(linear):
    """
    Convert linearRGB values (0-1 range) to sRGB (0-1 range)
    """
    result = []
    for c in linear:
        if c <= 0.0031308:
            result.append(c * 12.92)
        else:
            result.append(1.055 * (c ** (1/2.4)) - 0.055)
    return tuple(max(0, min(1, x)) for x in result)

def convert_to_protanopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with protanopia
    using the Machado et al. (2009) model.
    """
    # Convert to normalized sRGB
    srgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Convert to linearRGB for matrix operations
    linear_rgb = srgb_to_linear(srgb)
    
    # Transformation matrix for protanopia from Machado et al.
    sim_matrix = np.array([
        [0.152286, 1.052583, -0.204868],
        [0.114503, 0.786281, 0.099216],
        [-0.003882, -0.048116, 1.051998]
    ])
    
    # Apply matrix to linearRGB
    simulated_linear = np.dot(sim_matrix, linear_rgb)
    
    # Convert back to sRGB for display
    simulated_srgb = linear_to_srgb(simulated_linear)
    
    # Convert to 0-255 range and then to hex
    simulated_rgb = denormalize_rgb(simulated_srgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_deuteranopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with deuteranopia
    using the Machado et al. (2009) model.
    """
    # Convert to normalized sRGB
    srgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Convert to linearRGB for matrix operations
    linear_rgb = srgb_to_linear(srgb)
    
    # Transformation matrix for deuteranopia from Machado et al.
    sim_matrix = np.array([
        [0.367322, 0.860646, -0.227968],
        [0.280085, 0.672501, 0.047413],
        [-0.011820, 0.042940, 0.968881]
    ])
    
    # Apply matrix to linearRGB
    simulated_linear = np.dot(sim_matrix, linear_rgb)
    
    # Convert back to sRGB for display
    simulated_srgb = linear_to_srgb(simulated_linear)
    
    # Convert to 0-255 range and then to hex
    simulated_rgb = denormalize_rgb(simulated_srgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_tritanopia(hex_color):
    """
    Convert a hex color to simulate how it would appear to someone with tritanopia
    using the Machado et al. model

    Future implementations should prioritize Brettel's matrix which is recommended specifically for tritanopia.
    """
    # Convert to normalized sRGB
    srgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Convert to linearRGB for matrix operations
    linear_rgb = srgb_to_linear(srgb)
    
    # Transformation matrix for tritanopia from Machado et al.
    sim_matrix = np.array([
        [1.255528, -0.076749, -0.178779], 
        [-0.078411, 0.930809, 0.147602], 
        [0.004733, 0.691367, 0.303900]
    ])
    
    # Apply matrix to linearRGB
    simulated_linear = np.dot(sim_matrix, linear_rgb)
    
    # Convert back to sRGB for display
    simulated_srgb = linear_to_srgb(simulated_linear)
    
    # Convert to 0-255 range and then to hex
    simulated_rgb = denormalize_rgb(simulated_srgb)
    
    return rgb_to_hex(simulated_rgb)

def convert_to_grey_scale(hex_color):
    """
    Convert a hex color to grey scale using standard luminance formula.
    The formula is applied directly in sRGB space as it was designed for this color space.
    """
    # Convert to normalized sRGB
    srgb = normalize_rgb(hex_to_rgb(hex_color))
    
    # Apply luminance formula directly in sRGB space
    grey = 0.2126 * srgb[0] + 0.7152 * srgb[1] + 0.0722 * srgb[2]
    
    # Convert to 0-255 range and then to hex
    rgb_grey = denormalize_rgb((grey, grey, grey))
    grey = rgb_grey[0]  # All channels have same value
    
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

def convert_single_color(color):
    """
    Convert a single color to the full dictionary format with all vision types
    """
    color_dict = {}
    color_dict["normal"] = color
    color_dict["protanopia"] = convert_to_protanopia(color)
    color_dict["deuteranopia"] = convert_to_deuteranopia(color)
    color_dict["tritanopia"] = convert_to_tritanopia(color)
    color_dict["grey scale"] = convert_to_grey_scale(color)
    return color_dict

if __name__ == "__main__":
    # Test (debug)
    base_color = "#eb4034"
    print(base_color)
    print(convert_to_protanopia(base_color))
    print(convert_to_deuteranopia(base_color))
    print(convert_to_tritanopia(base_color))
    print(convert_to_grey_scale(base_color))
    print(convert_colors([base_color, base_color]))