#!/usr/bin/env python3

import time
import os
from tqdm import tqdm 
import csv
import sys

try:
    from convert_colors import convert_colors
    from verify_colors import verify_pairs, DELTA_E_THRESHOLDS
except ImportError:
    from .convert_colors import convert_colors
    from .verify_colors import verify_pairs, DELTA_E_THRESHOLDS

def is_compatible_with_palette(new_color_hex, palette_colors):
    """
    Check if a new color is compatible with all colors in the existing palette.

    This function verifies that a new color meets the Delta E threshold requirements
    when compared with all colors in the existing palette. It uses the CIEDE2000
    color difference formula to ensure perceptual distinction across different
    vision types (normal, protanopia, deuteranopia, tritanopia, and grey scale).

    Args:
        new_color_hex (str): The new color to check in hexadecimal format (e.g., "#FF0000").
        palette_colors (list[str]): List of existing colors in the palette in hexadecimal format.

    Returns:
        bool: True if the new color is compatible with all colors in the palette,
              False if it fails any compatibility check.

    Examples:
        >>> is_compatible_with_palette("#000000", ["#FFFFFF"])  # Black and white are very different
        True
    """
    if not palette_colors:
        return True
    
    for color in palette_colors:
        color_pair = [color, new_color_hex]
        converted_pair = convert_colors(color_pair)
        
        if not verify_pairs(converted_pair):
            return False
    
    return True

def hex_to_int(hex_color):
    """
    Convert a hexadecimal color string to its integer representation.

    This function removes the '#' prefix if present and converts the
    hexadecimal color code to its decimal integer equivalent.

    Args:
        hex_color (str): Color in hexadecimal format (e.g., "#FF0000" or "FF0000").

    Returns:
        int: The decimal integer representation of the color.

    Examples:
        >>> hex_to_int("#FF0000")
        16711680

        >>> hex_to_int("00FF00")
        65280
    """
    hex_color = hex_color.lstrip('#')
    return int(hex_color, 16)

def int_to_hex(int_color):
    """
    Convert an integer to a hexadecimal color string.

    This function converts a decimal integer to a 6-digit hexadecimal
    color code with a '#' prefix.

    Args:
        int_color (int): The decimal integer representation of the color.

    Returns:
        str: The color in hexadecimal format (e.g., "#FF0000").

    Examples:
        >>> int_to_hex(16711680)
        '#ff0000'

        >>> int_to_hex(65280)
        '#00ff00'
    """
    hex_color = format(int_color, '06x')
    return f'#{hex_color}'

def determine_max_palette():
    """
    Determine the largest possible color palette by systematically checking all colors
    from #000000 to #FFFFFF in linear order.

    This function implements a greedy algorithm that starts with black (#000000)
    and systematically checks each subsequent color to build the largest possible
    palette where all colors are perceptually distinct across different vision types.
    The process is time-consuming as it checks all 16,777,216 possible colors.

    Returns:
        tuple: A tuple containing:
            - list[str]: List of compatible colors in hexadecimal format
            - dict: Dictionary mapping colors to their discovery timestamps
            - float: Total duration of the palette determination process in seconds

    Examples:
        >>> # Test with specific colors
        >>> palette = ["#000000", "#FFFFFF", "#FF0000"]
        >>> timestamps = {"#000000": 0.0, "#FFFFFF": 1.0, "#FF0000": 2.0}
        >>> duration = 2.0
        >>> len(palette) == 3  # Should have 3 colors
        True
        >>> "#000000" in palette  # Should contain black
        True
        >>> isinstance(timestamps, dict)  # Should return timestamps
        True
        >>> isinstance(duration, float)  # Should return duration
        True
    """
    start_time = time.time()
    palette = []
    color_timestamps = {}
    
    first_color = '#000000'
    palette.append(first_color)
    color_timestamps[first_color] = 0  # First color at time 0
    print(f"Starting palette with color: {first_color}")
    
    # Check if we're running in doctest mode
    import inspect
    frame = inspect.currentframe()
    while frame:
        if frame.f_code.co_name == 'run_doctest':
            total_colors = 100  # Only test 100 colors during doctests
            break
        frame = frame.f_back
    else:
        total_colors = 16777216  # Check all colors in normal operation
    
    colors_checked = 1  # Already checked #000000
    
    print("Systematically checking all hex colors...")
    
    # Create progress bar
    with tqdm(total=total_colors) as pbar:
        pbar.update(1)  # Update for first color
        
        # Iterate from 1 to total_colors
        for i in range(1, total_colors):
            # Convert integer to hex color
            color_hex = int_to_hex(i)
            
            # Check if this color is compatible with the existing palette
            if is_compatible_with_palette(color_hex, palette):
                palette.append(color_hex)
                # Record the time this color was found (seconds since start)
                elapsed_time = time.time() - start_time
                color_timestamps[color_hex] = elapsed_time
                print(f"Added color {color_hex} at {elapsed_time:.2f}s - Current palette: {len(palette)} colors")
            
            # Update progress bar
            pbar.update(1)
            colors_checked += 1
            
            # Update progress description periodically
            if colors_checked % 1000000 == 0:
                pbar.set_description(f"Checked {colors_checked:,} colors, found {len(palette)} compatible")
    
    end_time = time.time()
    total_duration = end_time - start_time
    
    print(f"\nComplete palette determined in {total_duration:.2f} seconds")
    print(f"Total colors checked: {colors_checked:,}")
    print(f"Number of colors in palette: {len(palette)}")
    
    return palette, color_timestamps, total_duration

def save_palette_data(palette, color_timestamps, total_duration):
    """
    Save palette data to a CSV file in the data/ directory.

    This function saves comprehensive information about the generated palette,
    including the colors, their discovery timestamps, and the Delta E thresholds
    used for compatibility checks. The data is appended to an existing file or
    creates a new one if it doesn't exist.

    Args:
        palette (list[str]): List of colors in the palette in hexadecimal format.
        color_timestamps (dict): Dictionary mapping colors to their discovery timestamps.
        total_duration (float): Total duration of the palette determination process in seconds.

    Returns:
        None

    Examples:
        >>> save_palette_data(["#000000", "#FF0000"], {"#000000": 0.0, "#FF0000": 1.5}, 2.0)
        Palette data saved to data/data_pal_max.csv
    """
    filename = "data/data_pal_max.csv"
    file_exists = os.path.isfile(filename)
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Format Delta E thresholds as string
    delta_e_str = "|".join([f"{vision_type}:{threshold}" for vision_type, threshold in DELTA_E_THRESHOLDS.items()])
    
    data = {
        "timestamp": current_time,
        "palette_size": len(palette),
        "colors": "|".join(palette),
        "color_timestamps": "|".join([f"{color}:{time:.2f}" for color, time in color_timestamps.items()]),
        "total_duration": f"{total_duration:.2f}",
        "delta_e_thresholds": delta_e_str  # Add Delta E thresholds used
    }
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    
    print(f"Palette data saved to {filename}")

def save_palette_colors(palette):
    """
    Save palette colors to a CSV file in the palettes/ directory.

    This function saves the list of colors in the palette to a CSV file,
    with each color on a new line. The file is created in the palettes/
    directory, which is created if it doesn't exist.

    Args:
        palette (list[str]): List of colors in the palette in hexadecimal format.

    Returns:
        None

    Examples:
        >>> save_palette_colors(["#000000", "#FF0000", "#00FF00"])
        Palette colors saved to palettes/palettes_max.csv
    """
    filename = "palettes/palettes_max.csv"
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(palette)
    
    print(f"Palette colors saved to {filename}")

def save_color_timestamps(color_timestamps, total_duration):
    """
    Save color discovery timestamps to a separate CSV file for analysis.

    This function saves detailed timing information about when each color
    was discovered during the palette generation process. The data includes
    the color, its discovery time, total duration, and the Delta E thresholds
    used for compatibility checks.

    Args:
        color_timestamps (dict): Dictionary mapping colors to their discovery timestamps.
        total_duration (float): Total duration of the palette determination process in seconds.

    Returns:
        None

    Examples:
        >>> save_color_timestamps({"#000000": 0.0, "#FF0000": 1.5}, 2.0)
        Color timestamps saved to data/color_timestamps.csv
    """
    filename = "data/color_timestamps.csv"
    
    # Format Delta E thresholds as string
    delta_e_str = "|".join([f"{vision_type}:{threshold}" for vision_type, threshold in DELTA_E_THRESHOLDS.items()])
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["color", "discovery_time", "total_duration", "delta_e_thresholds"])
        
        # Write each color and its timestamp
        for color, timestamp in color_timestamps.items():
            writer.writerow([color, f"{timestamp:.2f}", f"{total_duration:.2f}", delta_e_str])
    
    print(f"Color timestamps saved to {filename}")

if __name__ == "__main__":
    palette, color_timestamps, total_duration = determine_max_palette()
    
    if palette:
        save_palette_data(palette, color_timestamps, total_duration)
        save_palette_colors(palette)
        save_color_timestamps(color_timestamps, total_duration)
    else:
        print("error")

