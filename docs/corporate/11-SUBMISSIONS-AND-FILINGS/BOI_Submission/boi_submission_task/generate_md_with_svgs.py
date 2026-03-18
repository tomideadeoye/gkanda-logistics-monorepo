#!/usr/bin/env python3

import os
import subprocess
import re
import shutil
from pathlib import Path

def extract_mermaid_diagrams(md_file_path):
    """Extract all mermaid diagrams from markdown file"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all mermaid code blocks
    pattern = r'```mermaid\s*(.*?)\s*```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    return diagrams

def generate_svg_from_mermaid(mermaid_code, output_path):
    """Generate SVG from mermaid code using mermaid CLI"""
    try:
        # Write mermaid code to temporary file
        temp_mmd = output_path.replace('.svg', '.mmd')
        with open(temp_mmd, 'w', encoding='utf-8') as f:
            f.write(mermaid_code)
        
        # Use mermaid CLI to generate SVG
        result = subprocess.run([
            'npx', 'mmdc', '-i', temp_mmd, '-o', output_path
        ], capture_output=True, text=True, timeout=30)
        
        # Clean up temp file
        os.remove(temp_mmd)
        
        if result.returncode == 0:
            print(f"Generated SVG: {output_path}")
            return True
        else:
            print(f"Error generating SVG: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error generating SVG: {e}")
        return False

def replace_mermaid_with_svg(md_file_path, output_file_path, diagrams_dir):
    """Replace mermaid code blocks with SVG images in markdown"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace each mermaid block
    pattern = r'```mermaid\s*.*?\s*```'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    # Process matches in reverse order to maintain string indices
    for i, match in enumerate(reversed(matches)):
        # Generate SVG filename
        svg_filename = f"diagram_{len(matches) - i}.svg"
        svg_path = os.path.join(diagrams_dir, svg_filename)
        
        # Extract mermaid code
        mermaid_code = match.group(0)[10:-3].strip()  # Remove ```mermaid and ```
        
        # Generate SVG
        if generate_svg_from_mermaid(mermaid_code, svg_path):
            # Replace with markdown image reference
            relative_svg_path = os.path.join("diagrams", svg_filename)
            replacement = f"![Diagram]({relative_svg_path})"
            content = content[:match.start()] + replacement + content[match.end():]
        else:
            # If SVG generation fails, keep original mermaid code
            print(f"Failed to generate SVG for diagram {len(matches) - i}")
    
    # Write updated content to output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with embedded SVGs: {output_file_path}")

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    # Create diagrams directory
    os.makedirs(diagrams_dir, exist_ok=True)
    
    # Extract and generate SVGs for all diagrams
    diagrams = extract_mermaid_diagrams(md_file)
    print(f"Found {len(diagrams)} mermaid diagrams")
    
    # Replace mermaid code with SVG images
    replace_mermaid_with_svg(md_file, output_md, diagrams_dir)
    
    print("Processing completed!")
    print(f"Output file: {output_md}")
    print(f"Diagrams directory: {diagrams_dir}")

if __name__ == "__main__":
    main()