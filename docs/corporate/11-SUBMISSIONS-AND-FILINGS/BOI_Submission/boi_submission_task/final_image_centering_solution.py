#!/usr/bin/env python3
"""
FINAL IMAGE CENTERING SOLUTION FOR ESMS HANDBOOK

This script provides the best approach to ensure images are properly centered
in the ESMS Handbook PDF generation process.

The solution uses a table-based approach which provides maximum compatibility
across different PDF renderers and viewers.
"""

import os
import re
from PIL import Image

def optimize_images():
    """Optimize images for PDF inclusion"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    print("Optimizing images for PDF...")
    
    # Process each screenshot
    for i in range(1, 5):
        screenshot_path = os.path.join(diagrams_dir, f"diagram_{i}_screenshot.png")
        optimized_path = os.path.join(diagrams_dir, f"diagram_{i}_final.png")
        
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
                        
                        # Resize the image with high quality
                        resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                        resized_img.save(optimized_path, "PNG", optimize=True)
                        print(f"  Resized to: {target_width}x{new_height} pixels")
                    else:
                        # Image is already small enough, just copy it
                        img.save(optimized_path, "PNG", optimize=True)
                        print(f"  Kept original size")
                        
            except Exception as e:
                print(f"Error processing diagram {i}: {e}")
    
    print("Image optimization complete!\n")

def create_markdown_with_best_centering():
    """Create markdown with the best image centering approach (table-based)"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Best_Centering.md")
    
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
        image_path = f"diagrams/diagram_{diagram_num}_final.png"
        
        # Create perfectly centered image using table approach (BEST METHOD)
        replacement = f"""
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none; padding: 0;">
      <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 800px; width: 100%; height: auto; display: block; margin: 0 auto;">
      <p style="margin-top: 10px; font-style: italic; text-align: center; color: #666;">Diagram {diagram_num}</p>
    </td>
  </tr>
</table>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with best image centering: {output_md}")
    return True

def create_best_css():
    """Create CSS that ensures maximum compatibility for image centering"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    css_file = os.path.join(base_dir, "best_centering_style.css")
    
    css_content = """
    /* BEST CSS FOR IMAGE CENTERING IN PDF */
    
    body {
        font-family: Arial, sans-serif;
        margin: 40px auto;
        line-height: 1.6;
        max-width: 1000px;
        padding: 20px;
    }
    
    /* TABLE-BASED CENTERING (MOST RELIABLE) */
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
    
    /* IMAGE STYLING */
    img {
        max-width: 800px !important;
        width: 100% !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    /* CAPTION STYLING */
    p[style*="font-style: italic"] {
        margin-top: 10px !important;
        font-style: italic !important;
        text-align: center !important;
        color: #666 !important;
    }
    
    /* HEADINGS */
    h1, h2, h3 {
        color: #333;
        text-align: left;
    }
    """
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    print(f"Created best centering CSS file: {css_file}")
    return css_file

def generate_final_pdf():
    """Generate the final PDF with best image centering"""
    print("To generate the final PDF with best image centering, run these commands:")
    print("\n1. First, convert markdown to HTML with our CSS:")
    print("   pandoc ESMS_Handbook_with_Best_Centering.md \\")
    print("     -o temp_best.html \\")
    print("     --standalone \\")
    print("     --toc \\")
    print("     --toc-depth=2 \\")
    print("     --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css \\")
    print("     --css=best_centering_style.css \\")
    print("     --metadata pagetitle='ESMS Handbook'")
    print("\n2. Then convert HTML to PDF:")
    print("   weasyprint temp_best.html \\")
    print("     ESMS_Handbook_With_Best_Centering.pdf \\")
    print("     --presentational-hints \\")
    print("     --optimize-images \\")
    print("     --full-fonts")
    print("\n3. Finally, merge with cover page using PyPDF2:")
    print("   (Use the merge scripts you already have)")

def main():
    """Main function - BEST SOLUTION for image centering"""
    print("FINAL IMAGE CENTERING SOLUTION")
    print("=" * 50)
    print("This solution uses table-based centering for maximum compatibility.\n")
    
    # Step 1: Optimize images
    print("Step 1: Optimizing images...")
    optimize_images()
    
    # Step 2: Create markdown with best centering
    print("Step 2: Creating markdown with best centering approach...")
    if create_markdown_with_best_centering():
        print("✓ Markdown with best image centering created successfully!")
    else:
        print("✗ Failed to create markdown with best image centering")
        return
    
    # Step 3: Create best CSS
    print("\nStep 3: Creating CSS for best centering...")
    css_file = create_best_css()
    if css_file:
        print("✓ Best centering CSS created successfully!")
    else:
        print("✗ Failed to create best centering CSS")
        return
    
    # Step 4: Instructions for PDF generation
    print("\nStep 4: Instructions for PDF generation...")
    generate_final_pdf()
    
    print("\n" + "=" * 50)
    print("SOLUTION SUMMARY:")
    print("=" * 50)
    print("✓ Images will be properly resized and optimized")
    print("✓ Table-based centering ensures maximum compatibility")
    print("✓ CSS is designed for PDF renderer compatibility")
    print("✓ Clear instructions provided for PDF generation")
    print("\nThe table-based approach is the most reliable method")
    print("because tables are well-supported across all PDF renderers.")

if __name__ == "__main__":
    main()