#!/usr/bin/env python3

import os
import re
from PIL import Image

def optimize_screenshots():
    """Optimize screenshots for better placement in PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    # Process each screenshot
    for i in range(1, 5):
        screenshot_path = os.path.join(diagrams_dir, f"diagram_{i}_screenshot.png")
        
        if os.path.exists(screenshot_path):
            try:
                # Open the image
                with Image.open(screenshot_path) as img:
                    # Get image dimensions
                    width, height = img.size
                    print(f"Diagram {i}: {width}x{height} pixels")
                    
                    # If image is very tall, we might want to split it or resize it
                    # For now, we'll just note the dimensions
                    if height > 800:  # Arbitrary threshold
                        print(f"  Warning: Diagram {i} is quite tall ({height}px)")
                        
            except Exception as e:
                print(f"Error processing diagram {i}: {e}")
    
    print("Screenshot optimization analysis complete!")

def create_markdown_with_optimized_images():
    """Create markdown with optimized image placement"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Optimized_Images.md")
    
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
        screenshot_path = f"diagrams/diagram_{diagram_num}_screenshot.png"
        
        # Create optimized image reference with markdown syntax for better centering
        replacement = f"""

<div align="center">

![Diagram {diagram_num}]({screenshot_path})

</div>

"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with optimized image placement: {output_md}")
    return True

def main():
    """Main function to optimize diagram placement"""
    print("Optimizing diagram placement for better PDF rendering...")
    
    # Step 1: Analyze screenshots
    print("\nStep 1: Analyzing screenshots...")
    optimize_screenshots()
    
    # Step 2: Create markdown with optimized images
    print("\nStep 2: Creating markdown with optimized image placement...")
    if create_markdown_with_optimized_images():
        print("Markdown with optimized images created successfully!")
    else:
        print("Failed to create markdown with optimized images")

if __name__ == "__main__":
    main()