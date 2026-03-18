#!/usr/bin/env python3

import os
import re
from PIL import Image

def analyze_and_resize_images():
    """Analyze and resize images for optimal PDF placement"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    print("Analyzing and optimizing diagram images...")
    
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

def create_markdown_with_precise_placement():
    """Create markdown with precisely positioned and sized images"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Precise_Images.md")
    
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
        
        # Create precisely positioned image with HTML for exact control
        replacement = f"""
<div style="text-align: center; margin: 30px 0;">
    <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 800px; width: 100%; height: auto; margin: 0 auto; display: block;">
    <p style="margin-top: 10px; font-style: italic;">Diagram {diagram_num}</p>
</div>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with precisely positioned images: {output_md}")
    return True

def main():
    """Main function for precise image placement"""
    print("Creating precisely positioned and sized diagram images...")
    
    # Step 1: Analyze and resize images
    print("\nStep 1: Analyzing and resizing images...")
    analyze_and_resize_images()
    
    # Step 2: Create markdown with precise image placement
    print("\nStep 2: Creating markdown with precise image placement...")
    if create_markdown_with_precise_placement():
        print("Markdown with precisely positioned images created successfully!")
    else:
        print("Failed to create markdown with precise image placement")

if __name__ == "__main__":
    main()