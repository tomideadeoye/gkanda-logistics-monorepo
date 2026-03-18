#!/usr/bin/env python3

import os
import re
from PIL import Image

def analyze_and_resize_images():
    """Analyze and resize images for optimal PDF placement with exact centering control"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    print("Analyzing and optimizing diagram images for exact centering...")
    
    # Process each screenshot
    for i in range(1, 5):
        screenshot_path = os.path.join(diagrams_dir, f"diagram_{i}_screenshot.png")
        optimized_path = os.path.join(diagrams_dir, f"diagram_{i}_optimized.png")
        
        if os.path.exists(screenshot_path):
            try:
                # Open the image
                with Image.open(screenshot_path) as img:
                    # Get original dimensions
                    width, height = img.size
                    print(f"Diagram {i}: {width}x{height} pixels")
                    
                    # Resize for better PDF visibility (target width: 800px)
                    target_width = 800
                    if width > target_width:
                        # Calculate new height maintaining aspect ratio
                        ratio = target_width / width
                        new_height = int(height * ratio)
                        
                        # Resize the image
                        resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                        resized_img.save(optimized_path, "PNG")
                        print(f"  Resized to: {target_width}x{new_height} pixels")
                    else:
                        # Image is already small enough, just copy it
                        img.save(optimized_path, "PNG")
                        print(f"  Kept original size")
                        
            except Exception as e:
                print(f"Error processing diagram {i}: {e}")
    
    print("Image optimization complete!")

def create_markdown_with_improved_centering():
    """Create markdown with precisely centered images using improved positioning"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Improved_Centering.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all mermaid code blocks
    mermaid_pattern = r'```mermaid\s*[\s\S]*?\s*```'
    matches = list(re.finditer(mermaid_pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain indices
    for i, match in enumerate(reversed(matches)):
        diagram_num = len(matches) - i
        image_path = f"diagrams/diagram_{diagram_num}_optimized.png"
        
        # Create precisely centered image with improved HTML for exact control
        replacement = f"""
<div style="text-align: center; margin: 30px auto; width: 100%;">
    <div style="display: inline-block; text-align: center; width: 100%; max-width: 800px;">
        <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 100%; height: auto; margin: 0 auto; display: block;">
        <p style="margin-top: 10px; font-style: italic; text-align: center;">Diagram {diagram_num}</p>
    </div>
</div>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with improved image centering: {output_md}")
    return True

def create_improved_css():
    """Create improved CSS for better image centering control"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    css_file = os.path.join(base_dir, "improved_centering_style.css")
    
    css_content = """
    body {
        font-family: Arial, sans-serif;
        margin: 40px;
        line-height: 1.6;
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Improved centering for image containers */
    div[style*="text-align: center"] {
        text-align: center !important;
        margin: 30px auto !important;
        width: 100% !important;
    }
    
    /* Improved image styling for precise centering */
    img {
        max-width: 800px !important;
        width: auto !important;
        height: auto !important;
        margin: 0 auto !important;
        display: block !important;
        text-align: center !important;
    }
    
    /* Center captions */
    p[style*="font-style: italic"] {
        margin-top: 10px !important;
        font-style: italic !important;
        text-align: center !important;
        width: 100% !important;
        display: block !important;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #333;
        text-align: left;
    }
    
    /* Ensure proper spacing */
    div[style*="display: inline-block"] {
        text-align: center !important;
        margin: 0 auto !important;
        display: block !important;
    }
    """
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    print(f"Created improved CSS file: {css_file}")
    return css_file

def main():
    """Main function for improved image centering"""
    print("Creating improved image centering solution...")
    
    # Step 1: Analyze and resize images
    print("\nStep 1: Analyzing and resizing images...")
    analyze_and_resize_images()
    
    # Step 2: Create markdown with improved centering
    print("\nStep 2: Creating markdown with improved image centering...")
    if create_markdown_with_improved_centering():
        print("Markdown with improved image centering created successfully!")
    else:
        print("Failed to create markdown with improved image centering")
        return
    
    # Step 3: Create improved CSS
    print("\nStep 3: Creating improved CSS for better centering...")
    css_file = create_improved_css()
    if css_file:
        print("Improved CSS created successfully!")
    else:
        print("Failed to create improved CSS")

if __name__ == "__main__":
    main()