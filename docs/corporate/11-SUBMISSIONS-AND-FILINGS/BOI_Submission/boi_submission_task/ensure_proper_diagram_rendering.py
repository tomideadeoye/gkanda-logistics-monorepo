#!/usr/bin/env python3

import os
import subprocess
import re
import shutil
from pathlib import Path

def ensure_mermaid_cli():
    """Ensure mermaid CLI is available"""
    try:
        # Check if npx is available
        subprocess.run(["npx", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("npx not found. Please install Node.js to get npx.")
        return False

def convert_md_to_pdf_with_svgs_fixed(md_file_path, pdf_output_path):
    """Convert Markdown to PDF ensuring SVG diagrams are properly rendered"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF with proper SVG support...")
    
    try:
        # Use pandoc with proper parameters for SVG support
        cmd = [
            "pandoc",
            md_file_path,
            "-o", pdf_output_path,
            "--standalone",
            "--toc",
            "--toc-depth=2",
            "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
            "--metadata", "pagetitle=ESMS Handbook",
            "--pdf-engine=weasyprint"  # WeasyPrint handles SVG better
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        
        if result.returncode == 0:
            print(f"Successfully converted {os.path.basename(md_file_path)} to {os.path.basename(pdf_output_path)}")
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

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Source files
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Check if required files exist
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return
    
    if not os.path.exists(cover_pdf):
        print(f"Cover PDF not found: {cover_pdf}")
        return
    
    # Output files
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_SVGs_Rendered.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Fixed.pdf")
    
    # Step 1: Convert handbook with SVGs to PDF
    if convert_md_to_pdf_with_svgs_fixed(md_file, handbook_pdf):
        print("Handbook with SVGs PDF created successfully!")
    else:
        print("Failed to create handbook with SVGs PDF")
        return
    
    # Step 2: Merge cover page with handbook
    try:
        from PyPDF2 import PdfMerger
        
        merger = PdfMerger()
        merger.append(cover_pdf)
        merger.append(handbook_pdf)
        merger.write(final_pdf)
        merger.close()
        
        print("Final document created successfully!")
        print(f"Final combined PDF: {final_pdf}")
        if os.path.exists(final_pdf):
            file_size = os.path.getsize(final_pdf) / (1024*1024)
            print(f"File size: {file_size:.1f} MB")
    except Exception as e:
        print(f"Error during PDF merge: {e}")

if __name__ == "__main__":
    main()