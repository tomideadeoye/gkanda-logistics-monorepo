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

def replace_mermaid_with_svg_references():
    """Replace mermaid code blocks with SVG image references in markdown"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
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
        svg_reference = f"![Diagram](diagrams/diagram_{diagram_index}.svg)"
        content = content[:match.start()] + svg_reference + content[match.end():]
    
    # Write updated content to output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with SVG references: {output_md}")
    return True

def convert_md_to_pdf():
    """Convert markdown with SVGs to PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_SVGs.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
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
            "--pdf-engine=weasyprint"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print(f"Successfully converted to PDF: {pdf_output}")
            return True
        else:
            print(f"Error during pandoc conversion: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("Pandoc conversion timed out")
        return False
    except Exception as e:
        print(f"Error during pandoc conversion: {e}")
        return False

def merge_cover_with_handbook():
    """Merge cover page with handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_SVGs.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Final.pdf")
    
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
    """Main function to generate complete ESMS document"""
    print("Starting complete ESMS document generation process...")
    
    # Step 1: Ensure directories exist
    ensure_directories()
    
    # Step 2: Generate SVGs from mermaid diagrams
    print("\nStep 1: Generating SVGs from Mermaid diagrams...")
    if not generate_svgs_from_mermaid():
        print("Failed to generate SVGs from Mermaid diagrams")
        return
    
    # Step 3: Replace mermaid code with SVG references
    print("\nStep 2: Replacing Mermaid code with SVG references...")
    if not replace_mermaid_with_svg_references():
        print("Failed to replace Mermaid code with SVG references")
        return
    
    # Step 4: Convert markdown to PDF
    print("\nStep 3: Converting markdown to PDF...")
    if not convert_md_to_pdf():
        print("Failed to convert markdown to PDF")
        return
    
    # Step 5: Merge cover with handbook
    print("\nStep 4: Merging cover page with handbook...")
    if not merge_cover_with_handbook():
        print("Failed to merge cover page with handbook")
        return
    
    print("\nComplete ESMS document generation finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Final.pdf")

if __name__ == "__main__":
    main()