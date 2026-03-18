#!/usr/bin/env python3

import os
import subprocess
import re
import shutil
from pathlib import Path
from PyPDF2 import PdfMerger

def ensure_directories():
    """Ensure required directories exist"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    os.makedirs(diagrams_dir, exist_ok=True)
    print(f"Ensured directories exist: {diagrams_dir}")

def generate_svgs_from_mermaid():
    """Generate SVG files from Mermaid diagrams in the markdown file"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Extract mermaid diagrams
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all mermaid code blocks
    pattern = r'```mermaid\s*(.*?)\s*```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    print(f"Found {len(diagrams)} mermaid diagrams")
    
    # Generate SVG for each diagram
    for i, diagram_code in enumerate(diagrams, 1):
        svg_filename = f"diagram_{i}.svg"
        svg_path = os.path.join(diagrams_dir, svg_filename)
        
        # Create temporary mermaid file
        temp_mmd = os.path.join(base_dir, f"temp_diagram_{i}.mmd")
        with open(temp_mmd, 'w', encoding='utf-8') as f:
            f.write(diagram_code.strip())
        
        try:
            # Generate SVG using mermaid CLI - simplified approach
            result = subprocess.run([
                'npx', '@mermaid-js/mermaid-cli',
                '--input', temp_mmd,
                '--output', svg_path
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print(f"Generated SVG: {svg_filename}")
            else:
                print(f"Error generating SVG {svg_filename}: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print(f"Timeout generating SVG: {svg_filename}")
        except Exception as e:
            print(f"Error generating SVG {svg_filename}: {e}")
        finally:
            # Clean up temporary file
            if os.path.exists(temp_mmd):
                os.remove(temp_mmd)
    
    return True

def convert_svg_to_png():
    """Convert SVG files to PNG for better PDF compatibility"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    # Check if convert (ImageMagick) is available
    if not shutil.which("convert"):
        print("ImageMagick 'convert' command not found. Skipping SVG to PNG conversion.")
        return False
    
    # Convert each SVG to PNG
    for i in range(1, 5):  # We have 4 diagrams
        svg_path = os.path.join(diagrams_dir, f"diagram_{i}.svg")
        png_path = os.path.join(diagrams_dir, f"diagram_{i}.png")
        
        if os.path.exists(svg_path):
            try:
                # Convert SVG to PNG with high quality
                result = subprocess.run([
                    "convert", "-density", "300", "-resize", "800x>",
                    svg_path, png_path
                ], capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0:
                    print(f"Converted SVG to PNG: diagram_{i}.png")
                else:
                    print(f"Error converting SVG to PNG for diagram_{i}: {result.stderr}")
            except subprocess.TimeoutExpired:
                print(f"Timeout converting SVG to PNG: diagram_{i}")
            except Exception as e:
                print(f"Error converting SVG to PNG for diagram_{i}: {e}")
    
    return True

def replace_mermaid_with_image_references():
    """Replace mermaid code blocks with image references in markdown"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Images.md")
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    if not os.path.exists(md_file):
        print(f"Source markdown file not found: {md_file}")
        return False
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count mermaid blocks for replacement
    pattern = r'```mermaid\s*.*?\s*```'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain string indices
    for i, match in enumerate(reversed(matches)):
        diagram_index = len(matches) - i
        # Prefer PNG if available, otherwise use SVG
        if os.path.exists(os.path.join(diagrams_dir, f"diagram_{diagram_index}.png")):
            image_reference = f"![Diagram](diagrams/diagram_{diagram_index}.png)"
        else:
            image_reference = f"![Diagram](diagrams/diagram_{diagram_index}.svg)"
        content = content[:match.start()] + image_reference + content[match.end():]
    
    # Write updated content to output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with image references: {output_md}")
    return True

def convert_md_to_pdf_with_images():
    """Convert markdown with images to PDF using multiple engines as fallback"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Images.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Images.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Try different PDF engines in order of preference
    engines = [
        ("weasyprint", "--pdf-engine=weasyprint"),
        ("wkhtmltopdf", "--pdf-engine=wkhtmltopdf"),
        ("pdflatex", "--pdf-engine=pdflatex")
    ]
    
    for engine_name, engine_flag in engines:
        if shutil.which(engine_name.split()[0]) or engine_name == "pdflatex":
            print(f"Trying PDF engine: {engine_name}")
            try:
                # Use pandoc to convert markdown to PDF
                cmd = [
                    "pandoc",
                    md_file,
                    "-o", pdf_output,
                    "--standalone",
                    "--toc",
                    "--toc-depth=2",
                    "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
                    "--metadata", "pagetitle=ESMS Handbook",
                    engine_flag
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                
                if result.returncode == 0:
                    print(f"Successfully converted to PDF using {engine_name}: {pdf_output}")
                    return True
                else:
                    print(f"Error during pandoc conversion with {engine_name}: {result.stderr}")
            except subprocess.TimeoutExpired:
                print(f"Pandoc conversion timed out with {engine_name}")
            except Exception as e:
                print(f"Error during pandoc conversion with {engine_name}: {e}")
        else:
            print(f"PDF engine not available: {engine_name}")
    
    print("All PDF engines failed")
    return False

def merge_cover_with_handbook():
    """Merge cover page with handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_Images.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_Images.pdf")
    
    # Check if required files exist
    missing_files = []
    if not os.path.exists(cover_pdf):
        missing_files.append(cover_pdf)
    if not os.path.exists(handbook_pdf):
        missing_files.append(handbook_pdf)
    
    if missing_files:
        print(f"Missing required files: {missing_files}")
        return False
    
    try:
        # Merge PDFs
        merger = PdfMerger()
        merger.append(cover_pdf)
        merger.append(handbook_pdf)
        merger.write(final_pdf)
        merger.close()
        
        print(f"Successfully merged PDFs: {final_pdf}")
        if os.path.exists(final_pdf):
            file_size = os.path.getsize(final_pdf) / (1024*1024)
            print(f"Final file size: {file_size:.1f} MB")
        return True
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return False

def main():
    """Main function to generate complete ESMS document with proper image handling"""
    print("Starting improved ESMS document generation process...")
    
    # Step 1: Ensure directories exist
    ensure_directories()
    
    # Step 2: Generate SVGs from mermaid diagrams
    print("\nStep 1: Generating SVGs from Mermaid diagrams...")
    if not generate_svgs_from_mermaid():
        print("Failed to generate SVGs from Mermaid diagrams")
        return
    
    # Step 3: Convert SVGs to PNG for better compatibility
    print("\nStep 2: Converting SVGs to PNG...")
    convert_svg_to_png()
    
    # Step 4: Replace mermaid code with image references
    print("\nStep 3: Replacing Mermaid code with image references...")
    if not replace_mermaid_with_image_references():
        print("Failed to replace Mermaid code with image references")
        return
    
    # Step 5: Convert markdown to PDF
    print("\nStep 4: Converting markdown to PDF...")
    if not convert_md_to_pdf_with_images():
        print("Failed to convert markdown to PDF")
        return
    
    # Step 6: Merge cover with handbook
    print("\nStep 5: Merging cover page with handbook...")
    if not merge_cover_with_handbook():
        print("Failed to merge cover page with handbook")
        return
    
    print("\nImproved ESMS document generation finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_Images.pdf")

if __name__ == "__main__":
    main()