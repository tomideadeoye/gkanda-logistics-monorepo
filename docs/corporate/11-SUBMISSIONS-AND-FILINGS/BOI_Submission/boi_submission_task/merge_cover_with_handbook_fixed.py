#!/usr/bin/env python3

import os
import subprocess
import shutil
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    dependencies = ['pdftk', 'gs']
    missing = []
    
    for dep in dependencies:
        if not shutil.which(dep):
            missing.append(dep)
    
    if missing:
        print(f"Warning: Missing dependencies: {', '.join(missing)}")
        print("Will try alternative merging methods...")
        return False
    return True

def merge_pdfs_with_pdftk(pdf_files, output_path):
    """Merge multiple PDF files into one using pdftk"""
    try:
        cmd = ["pdftk"] + pdf_files + ["cat", "output", output_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def merge_pdfs_with_ghostscript(pdf_files, output_path):
    """Merge multiple PDF files into one using ghostscript"""
    try:
        cmd = [
            "gs", "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite",
            f"-sOutputFile={output_path}"
        ] + pdf_files
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def merge_pdfs_with_pypdf2(pdf_files, output_path):
    """Merge multiple PDF files into one using PyPDF2"""
    try:
        from PyPDF2 import PdfMerger
        
        merger = PdfMerger()
        
        for pdf_file in pdf_files:
            if os.path.exists(pdf_file):
                merger.append(pdf_file)
        
        merger.write(output_path)
        merger.close()
        return True
    except Exception as e:
        print(f"PyPDF2 merge failed: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    """Merge PDFs using available tools in order of preference"""
    print(f"Merging PDFs: {[os.path.basename(f) for f in pdf_files]}")
    
    # Try pdftk first (best quality)
    if shutil.which("pdftk"):
        if merge_pdfs_with_pdftk(pdf_files, output_path):
            print(f"Successfully merged PDFs using pdftk: {output_path}")
            return True
    
    # Try ghostscript as fallback
    if shutil.which("gs"):
        if merge_pdfs_with_ghostscript(pdf_files, output_path):
            print(f"Successfully merged PDFs using ghostscript: {output_path}")
            return True
    
    # Try PyPDF2 as last resort
    try:
        if merge_pdfs_with_pypdf2(pdf_files, output_path):
            print(f"Successfully merged PDFs using PyPDF2: {output_path}")
            return True
    except ImportError:
        print("PyPDF2 not available")
    
    print("All PDF merging methods failed")
    return False

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Source files
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Try different handbook versions in order of preference
    handbook_options = [
        os.path.join(base_dir, "ESMS_Handbook_With_SVGs.pdf"),  # Handbook with SVG diagrams
        os.path.join(base_dir, "ESMS_Handbook_with_Diagrams.pdf"),  # Alternative with diagrams
        os.path.join(base_dir, "ESMS_Handbook_Enhanced_Pypandoc.pdf"),  # Enhanced version
        os.path.join(base_dir, "ESMS_Handbook.pdf")  # Basic version
    ]
    
    handbook_pdf = None
    for option in handbook_options:
        if os.path.exists(option):
            handbook_pdf = option
            print(f"Using handbook: {os.path.basename(option)}")
            break
    
    if not handbook_pdf:
        print("No handbook PDF found!")
        return
    
    # Check if cover page exists
    if not os.path.exists(cover_pdf):
        print(f"Cover page not found: {cover_pdf}")
        return
    
    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Merged.pdf")
    
    # Merge PDFs (cover page first, then handbook)
    if merge_pdfs([cover_pdf, handbook_pdf], final_pdf):
        print("PDF merging completed successfully!")
        print(f"Final combined PDF: {final_pdf}")
        if os.path.exists(final_pdf):
            file_size = os.path.getsize(final_pdf) / (1024*1024)
            print(f"File size: {file_size:.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()