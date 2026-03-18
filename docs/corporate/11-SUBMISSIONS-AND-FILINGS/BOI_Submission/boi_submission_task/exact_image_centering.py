#!/usr/bin/env python3

import os
import re
from PIL import Image

def analyze_and_resize_images_for_exact_centering():
    """Analyze and resize images for exact centering in PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    print("Analyzing and optimizing diagram images for exact centering...")
    
    # Process each screenshot
    for i in range(1, 5):
        screenshot_path = os.path.join(diagrams_dir, f"diagram_{i}_screenshot.png")
        optimized_path = os.path.join(diagrams_dir, f"diagram_{i}_exact_centered.png")
        
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
    
    print("Image optimization for exact centering complete!")

def create_markdown_with_exact_centering():
    """Create markdown with exactly centered images using table-based approach"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Exact_Centering.md")
    
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
        image_path = f"diagrams/diagram_{diagram_num}_exact_centered.png"
        
        # Create exactly centered image using table approach for maximum compatibility
        replacement = f"""
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none;">
      <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 800px; width: 100%; height: auto;">
      <p style="margin-top: 10px; font-style: italic;">Diagram {diagram_num}</p>
    </td>
  </tr>
</table>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with exact image centering: {output_md}")
    return True

def create_exact_centering_css():
    """Create CSS for exact image centering"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    css_file = os.path.join(base_dir, "exact_centering_style.css")
    
    css_content = """
    body {
        font-family: Arial, sans-serif;
        margin: 40px;
        line-height: 1.6;
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Table-based centering */
    table {
        width: 100% !important;
        border-collapse: collapse !important;
        margin: 30px 0 !important;
    }
    
    td {
        text-align: center !important;
        border: none !important;
        padding: 0 !important;
    }
    
    img {
        max-width: 800px !important;
        width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    p {
        margin-top: 10px !important;
        font-style: italic !important;
        text-align: center !important;
    }
    
    h1, h2, h3 {
        color: #333;
        text-align: left;
    }
    """
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    print(f"Created exact centering CSS file: {css_file}")
    return css_file

def main():
    """Main function for exact image centering"""
    print("Creating exact image centering solution...")
    
    # Step 1: Analyze and resize images
    print("\nStep 1: Analyzing and resizing images for exact centering...")
    analyze_and_resize_images_for_exact_centering()
    
    # Step 2: Create markdown with exact centering
    print("\nStep 2: Creating markdown with exact image centering...")
    if create_markdown_with_exact_centering():
        print("Markdown with exact image centering created successfully!")
    else:
        print("Failed to create markdown with exact image centering")
        return
    
    # Step 3: Create exact centering CSS
    print("\nStep 3: Creating CSS for exact centering...")
    css_file = create_exact_centering_css()
    if css_file:
        print("Exact centering CSS created successfully!")
    else:
        print("Failed to create exact centering CSS")

if __name__ == "__main__":
    main()