#!/usr/bin/env python3

import os
import subprocess
import shutil

def check_dependencies():
    """Check if required dependencies are installed"""
    dependencies = {
        'pandoc': 'brew install pandoc',
        'wkhtmltopdf': 'brew install wkhtmltopdf'
    }
    
    missing = []
    for dep, install_cmd in dependencies.items():
        if not shutil.which(dep):
            missing.append(f"{dep} (install with: {install_cmd})")
    
    if missing:
        print("Missing dependencies:")
        for dep in missing:
            print(f"  - {dep}")
        return False
    return True

def convert_md_to_pdf_with_pandoc(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using pandoc"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using pandoc...")
    
    try:
        # Use pandoc to convert markdown to PDF via HTML
        cmd = [
            "pandoc",
            md_file_path,
            "-o", pdf_output_path,
            "--pdf-engine=wkhtmltopdf",
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

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one"""
    print(f"Merging PDFs: {[os.path.basename(f) for f in pdf_files]}")
    
    # Use pdftk or ghostscript to merge if available
    try:
        # Try pdftk first
        if shutil.which("pdftk"):
            cmd = ["pdftk"] + pdf_files + ["cat", "output", output_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully merged PDFs to {output_path}")
                return True
            else:
                print(f"pdftk merge failed: {result.stderr}")
        
        # Try ghostscript as fallback
        elif shutil.which("gs"):
            cmd = [
                "gs", "-dBATCH", "-dNOPAUSE", "-q", "-sDEVICE=pdfwrite",
                f"-sOutputFile={output_path}"
            ] + pdf_files
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully merged PDFs to {output_path}")
                return True
            else:
                print(f"Ghostscript merge failed: {result.stderr}")
        else:
            print("No PDF merging tool available (need pdftk or ghostscript)")
            return False
            
    except Exception as e:
        print(f"Error during PDF merge: {e}")
        return False

def main():
    # Check dependencies
    if not check_dependencies():
        print("\nPlease install the missing dependencies and try again.")
        return
    
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Source files
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Output files
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_Enhanced_Pandoc.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Pandoc.pdf")
    
    # Step 1: Convert enhanced handbook to PDF
    if convert_md_to_pdf_with_pandoc(md_file, handbook_pdf):
        print("Enhanced handbook PDF created successfully!")
    else:
        print("Failed to create enhanced handbook PDF")
        return
    
    # Step 2: Merge cover page with handbook
    if merge_pdfs([cover_pdf, handbook_pdf], final_pdf):
        print("Final document created successfully!")
        print(f"Final combined PDF: {final_pdf}")
        print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()