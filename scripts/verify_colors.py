try: 
    from convert_colors import hex_to_rgb
except ImportError:
    from .convert_colors import hex_to_rgb
    
import math

# Delta E thresholds for different vision types
NORMAL_DELTA_E_THRESHOLD = 10.0
PROTANOPIA_DELTA_E_THRESHOLD = 15.0
DEUTERANOPIA_DELTA_E_THRESHOLD = 15.0
TRITANOPIA_DELTA_E_THRESHOLD = 15.0
GREY_SCALE_DELTA_E_THRESHOLD = 15.0 

# Dictionary mapping vision types to their respective thresholds for easy reference
DELTA_E_THRESHOLDS = {
    "normal": NORMAL_DELTA_E_THRESHOLD,
    "protanopia": PROTANOPIA_DELTA_E_THRESHOLD, 
    "deuteranopia": DEUTERANOPIA_DELTA_E_THRESHOLD,
    "tritanopia": TRITANOPIA_DELTA_E_THRESHOLD,
    "grey scale": GREY_SCALE_DELTA_E_THRESHOLD
}


def rgb_to_lab(rgb):
    """
    Converts an sRGB color to CIELAB color space via linear
    RGB and XYZ conversions.

    This function performs the following steps:
    sRGB (0–255) → Linear RGB → XYZ → CIELAB. It assumes input is in the sRGB
    color space and outputs values in the LAB color space.

    Args:
        rgb (tuple[int, int, int]): RGB color as a tuple of integers
            in the range 0–255.

    Returns:
        list[float]: A list of three floats representing
            the corresponding CIELAB color [L, a, b].

    Examples:
        >>> [round(x, 2) for x in rgb_to_lab((255, 0, 0))]
        [53.23, 80.11, 67.22]

        >>> [round(x, 2) for x in rgb_to_lab((0, 255, 0))]
        [87.74, -86.18, 83.18]

        >>> [round(x, 2) for x in rgb_to_lab((0, 0, 255))]
        [32.3, 79.2, -107.86]
    """
    r, g, b = [c/255.0 for c in rgb]
    
    # Convert sRGB to Linear RGB
    r = r/12.92 if r <= 0.04045 else ((r+0.055)/1.055)**2.4
    g = g/12.92 if g <= 0.04045 else ((g+0.055)/1.055)**2.4
    b = b/12.92 if b <= 0.04045 else ((b+0.055)/1.055)**2.4
    
    # Convert to XYZ
    r *= 100
    g *= 100
    b *= 100
    
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    
    # Convert XYZ to Lab
    x /= 95.047
    y /= 100.0
    z /= 108.883
    
    x = x**(1/3) if x > 0.008856 else 7.787*x + 16/116
    y = y**(1/3) if y > 0.008856 else 7.787*y + 16/116
    z = z**(1/3) if z > 0.008856 else 7.787*z + 16/116
    
    L = 116 * y - 16
    a = 500 * (x - y)
    b = 200 * (y - z)
    
    return [L, a, b]


def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)


def radians_to_degrees(radians):
    return radians * (180 / math.pi)


def calculate_delta_e_2000(lab1, lab2):
    """
    Calculates the Delta E (CIEDE2000) color difference between two LAB colors.

    This function implements the official CIEDE2000 formula for computing
    perceptual color difference between two colors in the CIELAB color space.
    It accounts for differences in lightness, chroma, and hue to reflect
    human perception more accurately than older formulas like CIE76 or CIE94.

    Source: http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE2000.html

    Args:
        lab1 (list[float]): First color in LAB format [L, a, b].
        lab2 (list[float]): Second color in LAB format [L, a, b].

    Returns:
        float: The Delta E value representing the perceptual difference
            between the two colors. A value of 0.0 means the colors are identical.

    Examples:
        >>> round(calculate_delta_e_2000(
        ...     [50.0, 2.6772, -79.7751],
        ...     [50.0, 0.0, -82.7485]
        ... ), 4)
        1.8693

        >>> round(calculate_delta_e_2000(
        ...     [50.0, 3.1571, -77.2803],
        ...     [50.0, 0.0, -82.7485]
        ... ), 4)
        2.5797
    """
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    C_mean = (C1 + C2) / 2

    G = 0.5 * (1 - math.sqrt(C_mean**7 / (C_mean**7 + 25**7)))

    a1_prime = a1 * (1 + G)
    a2_prime = a2 * (1 + G)

    C1_prime = math.sqrt(a1_prime**2 + b1**2)
    C2_prime = math.sqrt(a2_prime**2 + b2**2)
    C_prime_mean = (C1_prime + C2_prime) / 2
    
    h1_prime = 0 if (a1_prime == 0 and b1 == 0) else radians_to_degrees(math.atan2(b1, a1_prime)) % 360
    h2_prime = 0 if (a2_prime == 0 and b2 == 0) else radians_to_degrees(math.atan2(b2, a2_prime)) % 360
    
    delta_h_prime = 0
    if C1_prime * C2_prime == 0:
        delta_h_prime = 0
    else:
        if abs(h2_prime - h1_prime) <= 180:
            delta_h_prime = h2_prime - h1_prime
        elif h2_prime - h1_prime > 180:
            delta_h_prime = h2_prime - h1_prime - 360
        elif h2_prime - h1_prime < -180:
            delta_h_prime = h2_prime - h1_prime + 360
    
    delta_H_prime = 2 * math.sqrt(C1_prime * C2_prime) * math.sin(degrees_to_radians(delta_h_prime / 2))
    
    if C1_prime * C2_prime == 0:
        h_prime_mean = h1_prime + h2_prime
    else:
        if abs(h1_prime - h2_prime) <= 180:
            h_prime_mean = (h1_prime + h2_prime) / 2
        elif abs(h1_prime - h2_prime) > 180 and h1_prime + h2_prime < 360:
            h_prime_mean = (h1_prime + h2_prime + 360) / 2
        elif abs(h1_prime - h2_prime) > 180 and h1_prime + h2_prime >= 360:
            h_prime_mean = (h1_prime + h2_prime - 360) / 2
    
    L_prime_mean = (L1+L2) / 2
    delta_L_prime = L2 - L1
    delta_C_prime = C2_prime - C1_prime
    
    T = (1 - 0.17 * math.cos(degrees_to_radians(h_prime_mean - 30))
        + 0.24 * math.cos(degrees_to_radians(2 * h_prime_mean))
        + 0.32 * math.cos(degrees_to_radians(3 * h_prime_mean + 6))
        - 0.20 * math.cos(degrees_to_radians(4 * h_prime_mean - 63)))
    
    S_L = 1 + (0.015 * (L_prime_mean - 50)**2) / math.sqrt(20 + (L_prime_mean - 50)**2)
    S_C = 1 + 0.045 * C_prime_mean
    S_H = 1 + 0.015 * C_prime_mean * T
    
    delta_theta = 30 * math.exp(-((h_prime_mean - 275) / 25)**2)
    R_C = 2 * math.sqrt(C_prime_mean**7 / (C_prime_mean**7 + 25**7))
    R_T = -R_C * math.sin(degrees_to_radians(delta_theta))
    
    k_L = k_C = k_H = 1

    # Calculate Delta E
    delta_E = math.sqrt(
        (delta_L_prime / (k_L * S_L))**2 +
        (delta_C_prime / (k_C * S_C))**2 +
        (delta_H_prime / (k_H * S_H))**2 +
        R_T * (delta_C_prime / (k_C * S_C)) * (delta_H_prime / (k_H * S_H))
    )
    
    return delta_E


def calculate_delta_e(color1, color2):
    """
    Calculates the Delta E color difference between two hexadecimal colors.

    This function computes how perceptually different two colors are using
    the CIEDE2000 formula. The input colors are expected in hexadecimal format
    and are internally converted to LAB color space.

    Args:
        color1 (str): First color in hexadecimal format (e.g., "#FF0000").
        color2 (str): Second color in hexadecimal format (e.g., "#00FF00").

    Returns:
        float: The Delta E (ΔE) value representing the perceptual difference
               between the two colors. A value of 0.0 means the colors are identical.

    Examples:
        >>> calculate_delta_e("#FF0000", "#FF0000")
        0.0

        >>> round(calculate_delta_e("#FF0000", "#00FF00"), 2)
        86.62

        >>> round(calculate_delta_e("#FF0000", "#0000FF"), 2)
        52.88
    """
    # Convert HEX colors to RGB
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    # Convert RGB to Lab through linear RGB and XYZ
    lab1 = rgb_to_lab(rgb1)
    lab2 = rgb_to_lab(rgb2)
    
    # CIEDE2000 is preferred over CIE76 because it more accurately reflects human color perception 
    # by correcting non-uniformities in the Lab color space
    delta_e = calculate_delta_e_2000(lab1, lab2)
    return delta_e


def verify_pairs(colors_dict):
    """ 
    This function will verify if a pair of color pass the test
    for normal, protanopia, deuteranopia, tritanopia and grey scale
    Each vision type uses its own Delta E threshold from the global settings.
    
    Example input:
    {'color1': 
        {'normal': '#cbf56d', 
        'protanopia': '#ffe266', 
        'deuteranopia': '#ffe271', 
        'tritanopia': '#d8e4cb', 
        'grey scale': '#e2e2e2'}, 

    'color2': 
        {'normal': '#7dd17c', 
        'protanopia': '#d5be77', 
        'deuteranopia': '#c5b57f', 
        'tritanopia': '#76cbb6', 
        'grey scale': '#b9b9b9'}}
    """
    results = {}
    
    # Check difference for each vision type
    vision_types = ["normal", "protanopia", "deuteranopia", "tritanopia", "grey scale"]
    
    for vision in vision_types:
        color1 = colors_dict["color1"][vision]
        color2 = colors_dict["color2"][vision]
        delta_e = calculate_delta_e(color1, color2)
        
        # Use the specific threshold for this vision type
        threshold = DELTA_E_THRESHOLDS[vision]
        results[vision] = delta_e >= threshold
    
    # Return True only if all vision types have sufficient difference
    return all(results.values())

def verif_colors(colors_dict):
    """ 
    This function will take a dictionnary of n colors, for exemple :
    {'color1': 
        {'normal': '#eb4034', 
        'protanopia': '#5c5232', 
        'deuteranopia': '#816f32', 
        'tritanopia': '#ff303d', 
        'grey scale': '#636363'}
    ...
    }
    It will give a new dictionnary with the more colors compatibles possible
    structure like that :
    {   
        'color1': {'normal': '#8290e7', ...}, 
        'color2': {'normal': '#e789a0', ...},
        'color3': {'normal': '#e459a0', ...}...
    }
    """
    compatible_keys = set()
    compatibility_map = {}
    color_keys = list(colors_dict.keys())
    
    # First, identify all colors that are compatible with at least one other color
    for i in range(len(color_keys)):
        current_color = color_keys[i]
        compatible_with_current = []
        
        for j in range(len(color_keys)):
            if i != j:  # Don't compare a color with itself
                comparison_color = color_keys[j]
                
                # Create a temporary dictionary in the format expected by verify_pairs
                temp_dict = {
                    "color1": colors_dict[current_color],
                    "color2": colors_dict[comparison_color]
                }
                
                # Check if the pair passes all vision tests
                if verify_pairs(temp_dict):
                    compatible_with_current.append(comparison_color)
                    compatible_keys.add(current_color)
                    compatible_keys.add(comparison_color)
        
        # Store compatibility information for debugging or other uses
        if compatible_with_current:
            compatibility_map[current_color] = compatible_with_current
    
    # Create the result dictionary containing only the compatible colors
    results = {}
    for key in compatible_keys:
        results[key] = colors_dict[key]
    
    return results

def verify_color_with_palette(color, palette):
    """
    Verify if a color is valid with all colors in the palette
    """
    for key in palette:
        # Create a temporary pair for verification
        temp_pair = {
            "color1": palette[key],
            "color2": color
        }
        # If any pair fails verification, return False
        if not verify_pairs(temp_pair):
            return False
    return True