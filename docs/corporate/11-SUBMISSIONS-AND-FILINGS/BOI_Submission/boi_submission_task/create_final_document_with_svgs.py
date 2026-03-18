#!/usr/bin/env python3

import os
import subprocess
import shutil

def convert_md_to_pdf_with_svgs(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using pandoc with SVG support"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF with SVG support...")
    
    try:
        # Use pandoc to convert markdown to PDF
        cmd = [
            "pandoc",
            md_file_path,
            "-o", pdf_output_path,
            "--standalone",
            "--toc",
            "--toc-depth=2",
            "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
            "--metadata", "pagetitle=ESMS Handbook"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
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

def merge_pdfs_with_pdftk(pdf_files, output_path):
    """Merge multiple PDF files into one using pdftk"""
    print(f"Merging PDFs: {[os.path.basename(f) for f in pdf_files]}")
    
    try:
        cmd = ["pdftk"] + pdf_files + ["cat", "output", output_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully merged PDFs to {output_path}")
            return True
        else:
            print(f"pdftk merge failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error during PDF merge: {e}")
        return False

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Source files
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Check if SVG version exists, otherwise fall back to original
    if not os.path.exists(md_file):
        print(f"SVG version not found, using original enhanced handbook")
        md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    
    # Output files
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_SVGs.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_SVGs.pdf")
    
    # Step 1: Convert handbook with SVGs to PDF
    if convert_md_to_pdf_with_svgs(md_file, handbook_pdf):
        print("Handbook with SVGs PDF created successfully!")
    else:
        print("Failed to create handbook with SVGs PDF")
        return
    
    # Step 2: Merge cover page with handbook
    if merge_pdfs_with_pdftk([cover_pdf, handbook_pdf], final_pdf):
        print("Final document with SVGs created successfully!")
        print(f"Final combined PDF: {final_pdf}")
        print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()