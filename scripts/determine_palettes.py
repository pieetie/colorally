#!/usr/bin/env python3

import time
import os
from tqdm import tqdm 
import csv

try:
    from convert_colors import convert_colors
    from verify_colors import verify_pairs
except ImportError:
    from .convert_colors import convert_colors
    from .verify_colors import verify_pairs

def is_compatible_with_palette(new_color_hex, palette_colors):
    """
    Check if a new color is compatible with all colors in the existing palette
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
    Convert a hex color string to integer
    """
    hex_color = hex_color.lstrip('#')
    return int(hex_color, 16)

def int_to_hex(int_color):
    """
    Convert an integer to hex color string
    """
    hex_color = format(int_color, '06x')
    return f'#{hex_color}'

def determine_max_palette():
    """
    Determine the largest possible color palette by systematically checking all colors
    from #000000 to #FFFFFF in linear order
    
    Returns:
        List of HEX colors in the palette
    """
    start_time = time.time()
    palette = []
    
    first_color = '#000000'
    palette.append(first_color)
    print(f"Starting palette with color: {first_color}")
    
    total_colors = 16777216 #256x256x256
    colors_checked = 1  # Already checked #000000
    
    print("Systematically checking all hex colors...")
    
    # Create progress bar
    with tqdm(total=total_colors) as pbar:
        pbar.update(1)  # Update for first color
        
        # Iterate from 1 to FFFFFF (hex)
        for i in range(1, total_colors):
            # Convert integer to hex color
            color_hex = int_to_hex(i)
            
            # Check if this color is compatible with the existing palette
            if is_compatible_with_palette(color_hex, palette):
                palette.append(color_hex)
                print(f"Added color {color_hex} - Current palette: {len(palette)} colors")
            
            # Update progress bar
            pbar.update(1)
            colors_checked += 1
            
            # Update progress description periodically
            if colors_checked % 1000000 == 0:
                pbar.set_description(f"Checked {colors_checked:,} colors, found {len(palette)} compatible")
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\nComplete palette determined in {duration:.2f} seconds")
    print(f"Total colors checked: {colors_checked:,}")
    print(f"Number of colors in palette: {len(palette)}")
    
    return palette

def save_palette_data(palette):
    """
    Save palette data to a CSV file in the data/ directory
    """
    filename = "data/data_pal_max.csv"
    file_exists = os.path.isfile(filename)
    
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "timestamp": current_time,
        "palette_size": len(palette),
        "colors": "|".join(palette)
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
    Save palette colors to a CSV file in the palettes/ directory
    """
    filename = "palettes/palettes_max.csv"
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(palette)
    
    print(f"Palette colors saved to {filename}")

if __name__ == "__main__":
    palette = determine_max_palette()
    
    if palette:
        save_palette_data(palette)
        save_palette_colors(palette)
    else:
        print("error")

