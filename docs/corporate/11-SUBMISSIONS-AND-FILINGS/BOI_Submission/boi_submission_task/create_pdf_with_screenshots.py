#!/usr/bin/env python3

import os
import subprocess
import shutil
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_screenshots():
    """Convert markdown with screenshots to PDF using WeasyPrint"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Screenshots.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Screenshots.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Check if WeasyPrint is available
    if not shutil.which("weasyprint"):
        print("WeasyPrint not found. Please install it with: pip install weasyprint")
        return False
    
    try:
        # First convert markdown to HTML with custom CSS for centering
        temp_html = os.path.join(base_dir, "temp_esms_screenshots.html")
        temp_css = os.path.join(base_dir, "temp_style.css")
        
        # Create custom CSS for better image centering
        css_content = """
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 100%;
            height: auto;
        }
        div[align="center"] {
            text-align: center;
        }
        """
        
        with open(temp_css, 'w') as f:
            f.write(css_content)
        
        cmd_md_to_html = [
            "pandoc",
            md_file,
            "-o", temp_html,
            "--standalone",
            "--toc",
            "--toc-depth=2",
            "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
            f"--css={temp_css}",
            "--metadata", "pagetitle=ESMS Handbook"
        ]
        
        result = subprocess.run(cmd_md_to_html, capture_output=True, text=True, timeout=180)
        
        # Clean up temporary CSS file
        if os.path.exists(temp_css):
            os.remove(temp_css)
        
        if result.returncode != 0:
            print(f"Error converting markdown to HTML: {result.stderr}")
            return False
        
        print("Converted markdown to HTML successfully")
        
        # Then convert HTML to PDF using WeasyPrint
        cmd_html_to_pdf = [
            "weasyprint",
            temp_html,
            pdf_output,
            "--presentational-hints"
        ]
        
        result = subprocess.run(cmd_html_to_pdf, capture_output=True, text=True, timeout=180)
        
        # Clean up temporary HTML file
        if os.path.exists(temp_html):
            os.remove(temp_html)
        
        if result.returncode == 0:
            print(f"Successfully converted to PDF using WeasyPrint: {pdf_output}")
            return True
        else:
            print(f"Error during WeasyPrint conversion: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("WeasyPrint conversion timed out")
        return False
    except Exception as e:
        print(f"Error during WeasyPrint conversion: {e}")
        return False

def merge_cover_with_handbook():
    """Merge cover page with handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_Screenshots.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_Screenshots.pdf")
    
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
    """Main function to generate complete ESMS document with screenshot images"""
    print("Starting ESMS document generation with centered screenshots...")
    
    # Step 1: Convert markdown to PDF
    print("\nStep 1: Converting markdown to PDF with centered screenshots...")
    if not convert_md_to_pdf_with_screenshots():
        print("Failed to convert markdown to PDF with centered screenshots")
        return
    
    # Step 2: Merge cover with handbook
    print("\nStep 2: Merging cover page with handbook...")
    if not merge_cover_with_handbook():
        print("Failed to merge cover page with handbook")
        return
    
    print("\nESMS document generation with centered screenshots finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_Screenshots.pdf")

if __name__ == "__main__":
    main()