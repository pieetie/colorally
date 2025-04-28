#!/usr/bin/env python3 

import matplotlib.pyplot as plt
import os
import time

try:
    from convert_colors import convert_to_protanopia, convert_to_deuteranopia, convert_to_tritanopia, convert_to_grey_scale, hex_to_rgb
except ImportError:
    from .convert_colors import convert_to_protanopia, convert_to_deuteranopia, convert_to_tritanopia, convert_to_grey_scale, hex_to_rgb

def render_palette_to_image(hex_colors, chart_type="donut", show_title=False):
    """
    Render a palette of HEX colors as a chart for each vision type and save to an image file
    """
    vision_types = ["Normal", "Protanopia", "Deuteranopia", "Tritanopia", "Grey scale"]
    converted_colors = []
    
    # Convert colors for each vision type
    converted_colors.append(hex_colors)  # Normal
    converted_colors.append([convert_to_protanopia(color) for color in hex_colors])  # Protanopia
    converted_colors.append([convert_to_deuteranopia(color) for color in hex_colors])  # Deuteranopia
    converted_colors.append([convert_to_tritanopia(color) for color in hex_colors])  # Tritanopia
    converted_colors.append([convert_to_grey_scale(color) for color in hex_colors])  # Grey scale
    
    # Create equal-sized pie segments
    num_colors = len(hex_colors)
    sizes = [1] * num_colors
    
    # Create figure with 5 charts
    fig, axes = plt.subplots(1, 5, figsize=(20, 6))
    
    # Create a chart for each vision type
    for i, (vision_type, colors) in enumerate(zip(vision_types, converted_colors)):
        ax = axes[i]
        
        if chart_type.lower() == "pie":
            # Create a simple pie chart (no borders)
            ax.pie(sizes, colors=colors, startangle=90)
        else:
            # Create a donut chart (no borders)
            wedges, _ = ax.pie(sizes, colors=colors, wedgeprops=dict(width=0.6), startangle=90)
            centre_circle = plt.Circle((0, 0), 0.2, fc='white')
            ax.add_patch(centre_circle)
        
        # Set title
        ax.set_title(vision_type)
    
    # Add main title if requested
    if show_title:
        plt.suptitle("Palette Visualization Across Different Vision Types", fontsize=16)
    
    plt.tight_layout()
    
    # Create outputs directory if it doesn't exist
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    
    # Generate filename with timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"outputs/palette_{chart_type}_{num_colors}colors_{timestamp}.png"
    
    # Save the image and close the figure
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()
    
    print(f"Saved visualization to {filename}")
    return filename

if __name__ == "__main__":
    example_colors = ["#000000","#0036f8","#007afb","#00b8a5","#00f8fc"]
    render_palette_to_image(example_colors, chart_type="donut", show_title=False)