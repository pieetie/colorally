import matplotlib.pyplot as plt
import matplotlib.patches as patches

def render_colors(colors_dict, output_path="outputs/color_visualization.png", debug=False):
    """ 
    Take in entry a dictionnary of colors, for exemple like that :
    {'color1': 
        {'normal': '#eb4034', 
        'protanopia': '#5c5232', 
        'deuteranopia': '#816f32', 
        'tritanopia': '#ff303d', 
        'grey scale': '#636363'}
    ...
    }
    And render colors in a png format, to visualize the differences between colors for each type
    """  
    vision_types = ["normal", "protanopia", "deuteranopia", "tritanopia", "grey scale"]
    
    # Get all color keys
    color_keys = list(colors_dict.keys())
    num_colors = len(color_keys)
    
    # Create figure with appropriate size
    fig, ax = plt.subplots(figsize=(12, num_colors * 1.5))
    
    # Turn off axis
    ax.set_axis_off()
    
    # Set up grid
    ax.set_xlim(0, 100)
    ax.set_ylim(0, num_colors * 10)
    
    # Create headers
    for i, vision in enumerate(vision_types):
        ax.text(i * 20 + 10, num_colors * 10 + 1, vision.capitalize(), 
                ha="center", fontsize=10, fontweight='bold')
        
    # Add color squares with labels
    for row, color_key in enumerate(color_keys):
        y_pos = (num_colors - row - 1) * 10 + 2  # Position from bottom to top
        
        # Add color name
        ax.text(-5, y_pos + 3, color_key, ha="right", va="center", fontsize=10)
        
        color_data = colors_dict[color_key]
        
        # Add color squares for each vision type
        for i, vision in enumerate(vision_types):
            # Check if color_data is a dictionary or a list
            if isinstance(color_data, dict) and vision in color_data:
                # If it's a dictionary, access by key
                color_hex = color_data[vision]
                # Make sure the value is a valid color
                if not isinstance(color_hex, str) or not color_hex.startswith('#'):
                    if debug:
                        print(f"  Invalid color for {vision}: {color_hex}, type: {type(color_hex)}")
                    color_hex = "#CCCCCC"  # Default gray if not a valid hex color
                elif debug:
                    print(f"  Valid color for {vision}: {color_hex}")
            elif isinstance(color_data, list) and i < len(color_data):
                # If it's a list, access by index
                color_hex = color_data[i]
                # Make sure the value is a valid color
                if not isinstance(color_hex, str) or not color_hex.startswith('#'):
                    if debug:
                        print(f"  Invalid color for {vision} (index {i}): {color_hex}, type: {type(color_hex)}")
                    color_hex = "#CCCCCC"  # Default gray if not a valid hex color
                elif debug:
                    print(f"  Valid color for {vision} (index {i}): {color_hex}")
            else:
                # Default color if data not available
                if debug:
                    print(f"  No data for {vision}")
                color_hex = "#CCCCCC"
                
            x_pos = i * 20 + 1
            
            # Create rectangle
            rect = patches.Rectangle((x_pos, y_pos), 18, 6, 
                                    facecolor=color_hex, 
                                    edgecolor='black',
                                    linewidth=0.5)
            ax.add_patch(rect)
            
            # Add hex value below the rectangle
            ax.text(x_pos + 9, y_pos - 1, color_hex, 
                   ha="center", va="top", fontsize=8)
    
    # Add gridlines to separate columns
    for i in range(len(vision_types) + 1):
        ax.axvline(x=i * 20, color='gray', linestyle='-', linewidth=0.5)
    
    # Save the figure
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    return output_path