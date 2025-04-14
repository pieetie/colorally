#!/usr/bin/env python3 

try:
    from generate_colors import generate_random_pair, generate_random_color
    from convert_colors import convert_colors, convert_single_color
    from verify_colors import verify_pairs, verify_color_with_palette
except ImportError:
    from .generate_colors import generate_random_pair, generate_random_color
    from .convert_colors import convert_colors, convert_single_color
    from .verify_colors import verify_pairs, verify_color_with_palette

import time
import statistics

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

def generate_palette(size=3, max_failures=1000):
    """
    Generate a palette of n colors that all pass the verification tests with each other
    """
    if size < 2:
        raise ValueError("Palette size must be at least 2")
    
    total_failures = 0
    current_failures = 0
    restart_count = 0
    
    while True:
        # Generate the first valid pair
        initial_pair = gen_valid_pair()
        
        # Initialize palette
        palette = {
            "color1": initial_pair["color1"],
            "color2": initial_pair["color2"]
        }
        
        # Track failed colors to avoid regenerating them
        failed_colors = set()
        current_failures = 0
        
        # Add remaining colors
        while len(palette) < size:
            # Check if we've had too many failures and need to restart
            if current_failures >= max_failures:
                print(f"Too many failures ({current_failures}). Restarting with a new color pair...")
                total_failures += current_failures
                restart_count += 1
                break  # Break the inner loop to restart with a new pair
                
            # Generate a new random color that hasn't failed before
            while True:
                new_color_hex = generate_random_color()
                if new_color_hex not in failed_colors:
                    break
            
            # Convert to our format
            new_color = convert_single_color(new_color_hex)
            
            # Check if this color works with all existing colors in the palette
            if verify_color_with_palette(new_color, palette):
                # Add to palette
                palette[f"color{len(palette)+1}"] = new_color
            else:
                # Add to failed colors
                failed_colors.add(new_color_hex)
                current_failures += 1
        
        # If we've successfully created a palette of the requested size, we're done
        if len(palette) == size:
            total_failures += current_failures
            if restart_count > 0:
                print(f"Successfully generated a palette after {restart_count} restarts")
            return palette, total_failures

def generate_palettes(num_palettes=3, palette_size=5):
    """
    Generate n palettes of n colors each
    Report statistics on generation time and failure counts
    """
    times = []
    fail_counts = []
    palettes = {}
    
    for i in range(num_palettes):
        start_time = time.time()
        palette, fails = generate_palette(palette_size)
        end_time = time.time()
        
        generation_time = end_time - start_time
        times.append(generation_time)
        fail_counts.append(fails)
        
        palettes[f"palette_{i+1}"] = palette
    
    # Calculate statistics
    stats = {
        "time": {
            "mean": statistics.mean(times),
            "std_dev": statistics.stdev(times) if len(times) > 1 else 0,
            "min": min(times),
            "max": max(times) 
        },
        "failures": {
            "mean": statistics.mean(fail_counts),
            "std_dev": statistics.stdev(fail_counts) if len(fail_counts) > 1 else 0,
            "min": min(fail_counts),
            "max": max(fail_counts)
        }
    }
    
    return palettes, stats

if __name__ == "__main__":
    # Tests
    print("Generating a palette of 4 colors...")
    palette, fails = generate_palette(4)
    print(f"Generated palette with {len(palette)} colors after {fails} failures")
    for key, value in palette.items():
        print(f"{key}: {value['normal']}")
    
    print("\nGenerating 3 palettes of 3 colors each...")
    palettes, stats = generate_palettes(3, 3)
    
    print("\nStatistics:")
    print(f"Generation time: mean={stats['time']['mean']:.2f}s, std_dev={stats['time']['std_dev']:.2f}s, min={stats['time']['min']:.2f}s, max={stats['time']['max']:.2f}s")
    print(f"Failures: mean={stats['failures']['mean']:.1f}, std_dev={stats['failures']['std_dev']:.1f}, min={stats['failures']['min']}, max={stats['failures']['max']}")

