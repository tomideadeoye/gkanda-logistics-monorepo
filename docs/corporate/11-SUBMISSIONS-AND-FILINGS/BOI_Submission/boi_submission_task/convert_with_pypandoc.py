#!/usr/bin/env python3

import os
import pypandoc
import subprocess
import shutil

def convert_md_to_pdf_with_pypandoc(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using pypandoc"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using pypandoc...")
    
    try:
        # Use pypandoc to convert markdown to PDF
        pypandoc.convert_file(
            md_file_path,
            'pdf',
            outputfile=pdf_output_path,
            extra_args=[
                '--pdf-engine=weasyprint',
                '--standalone',
                '--toc',
                '--toc-depth=2'
            ]
        )
        
        print(f"Successfully converted {os.path.basename(md_file_path)} to {os.path.basename(pdf_output_path)}")
        return True
    except Exception as e:
        print(f"Error during pypandoc conversion: {e}")
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
    svg_md_file = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")
    original_md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")

    # Use SVG-enhanced version if it exists, otherwise generate it
    if os.path.exists(svg_md_file):
        md_file = svg_md_file
        print("Using SVG-enhanced markdown file")
    else:
        print("SVG-enhanced markdown not found, generating it first...")
        result = subprocess.run(["python3", "generate_md_with_svgs_fixed.py"], capture_output=True, text=True)
        if result.returncode == 0 and os.path.exists(svg_md_file):
            md_file = svg_md_file
            print("Successfully generated SVG-enhanced markdown")
        else:
            print(f"Failed to generate SVG markdown: {result.stderr}")
            md_file = original_md_file
            print("Falling back to original markdown file")
    
    # Output files
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_Enhanced_Pypandoc.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Pypandoc.pdf")
    
    # Step 1: Convert enhanced handbook to PDF
    if convert_md_to_pdf_with_pypandoc(md_file, handbook_pdf):
        print("Enhanced handbook PDF created successfully!")
    else:
        print("Failed to create enhanced handbook PDF")
        return
    
    # Step 2: Merge cover page with handbook
    if merge_pdfs_with_pdftk([cover_pdf, handbook_pdf], final_pdf):
        print("Final document created successfully!")
        print(f"Final combined PDF: {final_pdf}")
        print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()