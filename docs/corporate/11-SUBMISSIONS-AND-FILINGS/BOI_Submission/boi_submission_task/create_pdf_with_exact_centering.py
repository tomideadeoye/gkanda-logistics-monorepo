#!/usr/bin/env python3

import os
import subprocess
import shutil
from PyPDF2 import PdfMerger

def convert_exact_md_to_pdf():
    """Convert markdown with exact image centering to PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Exact_Centering.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Exact_Centering.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Check if WeasyPrint is available
    if not shutil.which("weasyprint"):
        print("WeasyPrint not found. Please install it with: pip install weasyprint")
        return False
    
    try:
        # Create CSS for exact centering
        temp_css = os.path.join(base_dir, "exact_centering_style.css")
        
        # If CSS file doesn't exist, create it
        if not os.path.exists(temp_css):
            css_content = """
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            
            /* Table-based centering */
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
            
            img {
                max-width: 800px !important;
                width: 100% !important;
                height: auto !important;
                display: block !important;
                margin: 0 auto !important;
            }
            
            p {
                margin-top: 10px !important;
                font-style: italic !important;
                text-align: center !important;
            }
            
            h1, h2, h3 {
                color: #333;
                text-align: left;
            }
            """
            
            with open(temp_css, 'w') as f:
                f.write(css_content)
        
        # Convert markdown to HTML
        temp_html = os.path.join(base_dir, "temp_exact.html")
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
        
        # Convert HTML to PDF using WeasyPrint with optimal settings
        cmd_html_to_pdf = [
            "weasyprint",
            temp_html,
            pdf_output,
            "--presentational-hints",
            "--optimize-images",
            "--full-fonts"
        ]
        
        result = subprocess.run(cmd_html_to_pdf, capture_output=True, text=True, timeout=180)
        
        # Clean up temporary HTML file
        if os.path.exists(temp_html):
            os.remove(temp_html)
        
        if result.returncode == 0:
            print(f"Successfully converted to PDF: {pdf_output}")
            return True
        else:
            print(f"Error during PDF conversion: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("PDF conversion timed out")
        return False
    except Exception as e:
        print(f"Error during PDF conversion: {e}")
        return False

def merge_cover_with_exact_handbook():
    """Merge cover page with exact centering handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_Exact_Centering.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf")
    
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
    """Main function to generate PDF with exact image centering"""
    print("Starting PDF generation with exact image centering...")
    
    # Step 1: Convert markdown to PDF
    print("\nStep 1: Converting markdown to PDF with exact image centering...")
    if not convert_exact_md_to_pdf():
        print("Failed to convert markdown to PDF with exact image centering")
        return
    
    # Step 2: Merge cover with handbook
    print("\nStep 2: Merging cover page with exact centering handbook...")
    if not merge_cover_with_exact_handbook():
        print("Failed to merge cover page with exact centering handbook")
        return
    
    print("\nPDF generation with exact image centering finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf")

if __name__ == "__main__":
    main()