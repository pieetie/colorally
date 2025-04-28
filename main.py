#!/usr/bin/env python3

import os
import csv
import time
import statistics

from scripts.convert_colors import *
from scripts.generate_colors import *
from scripts.render_colors import *
from scripts.verify_colors import * 
from scripts.verify_colors import DELTA_E_THRESHOLDS
from scripts.generate_palettes import *

def viz_pair():
    """ 
    Generate a color visualization for two colors
    """
    viz_pair_dic = gen_valid_pair()
    render_colors(viz_pair_dic)

def save_palette_data(palette, palette_size, generation_time, failures):
    """
    Save the data of a palette in a CSV file
    One line = one palette and its generation statistics
    """    
    filename = f"data/data_pal{palette_size}.csv" 
    file_exists = os.path.isfile(filename)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Extract colors from palette
    colors = [value["normal"] for value in palette.values()]
    colors_str = "|".join(colors)
    
    # Get Delta E thresholds from verify_colors
    delta_e_str = "|".join([f"{vision_type}:{threshold}" for vision_type, threshold in DELTA_E_THRESHOLDS.items()])
    #print(delta_e_str)
    
    data = {
        "timestamp": current_time,
        "palette_size": palette_size,
        "colors": colors_str,
        "generation_time": generation_time,
        "failures": failures,
        "delta_e_thresholds": delta_e_str
    }
    
    # Write in the csv
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)
    
    print(f"Data saved in {filename}")

def is_palette_duplicate(palette, existing_palettes):
    """
    Check if a palette is a duplicate
    """
    palette_colors = set(value["normal"] for value in palette.values())

    for existing_palette in existing_palettes:
        existing_colors = set(existing_palette) 
        if palette_colors == existing_colors: 
            return True
    
    return False

def save_palette_colors(palettes, palette_size):
    """
    Save the palettes in a CSV file
    """      
    filename = f"palettes/palettes_{palette_size}.csv"
    
    existing_palettes = []
    if os.path.isfile(filename):
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            existing_palettes = [row for row in reader]
    
    # Counter
    new_palettes_count = 0
    
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        for palette_id, palette in palettes.items():
            palette_colors = [value["normal"] for value in palette.values()]

            if not is_palette_duplicate(palette, existing_palettes):
                writer.writerow(palette_colors)
                existing_palettes.append(palette_colors)
                new_palettes_count += 1
    
    print(f"{new_palettes_count} new palettes saved in {filename}")

def generate_and_save_palettes(palette_size=3, num_palettes=5, max_failures=1000):
    """
    Generate palettes, save statistics and colors,
    and return the generated palettes
    """
    print(f"Generating {num_palettes} palettes with {palette_size} colors each...")
    palettes = {}
    all_stats = {"time": [], "failures": []}
    
    for i in range(num_palettes):
        start_time = time.time()
        palette, failures = generate_palette(palette_size, max_failures)
        generation_time = time.time() - start_time
        
        palette_id = f"palette_{i+1}"
        palettes[palette_id] = palette
        
        # Save data for each palette individually
        save_palette_data(palette, palette_size, generation_time, failures)
        
        # Collect statistics
        all_stats["time"].append(generation_time)
        all_stats["failures"].append(failures)
    
    # Calculate global statistics
    stats = {
        "time": {
            "mean": statistics.mean(all_stats["time"]),
            "std_dev": statistics.stdev(all_stats["time"]) if len(all_stats["time"]) > 1 else 0,
            "min": min(all_stats["time"]),
            "max": max(all_stats["time"])
        },
        "failures": {
            "mean": statistics.mean(all_stats["failures"]),
            "std_dev": statistics.stdev(all_stats["failures"]) if len(all_stats["failures"]) > 1 else 0,
            "min": min(all_stats["failures"]),
            "max": max(all_stats["failures"])
        }
    }
    
    total_time = sum(all_stats["time"])
    print(f"Generation completed in {total_time:.2f} seconds")
    
    # Display some statistics
    print(f"Average time per palette: {stats['time']['mean']:.2f}s")
    print(f"Average number of failures: {stats['failures']['mean']:.1f}")
    
    # Save palette colors
    save_palette_colors(palettes, palette_size)
    
    return palettes

def main():
    """
    Main function that generates and saves palettes
    """
    generate_and_save_palettes(palette_size=2, num_palettes=100, max_failures=5000)

if __name__ == "__main__":
    main()