#!/usr/bin/env python3

import os
import subprocess
import shutil
from PyPDF2 import PdfMerger

def convert_optimized_md_to_pdf():
    """Convert markdown with optimized images to PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Optimized_Images.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Optimized_Images.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Check if WeasyPrint is available
    if not shutil.which("weasyprint"):
        print("WeasyPrint not found. Please install it with: pip install weasyprint")
        return False
    
    try:
        # Create custom CSS for better image handling
        temp_css = os.path.join(base_dir, "optimized_style.css")
        css_content = """
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 90%;
            height: auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-radius: 4px;
            padding: 10px;
            background: white;
        }
        div[align="center"] {
            text-align: center;
            margin: 20px 0;
        }
        h1, h2, h3 {
            color: #333;
        }
        """
        
        with open(temp_css, 'w') as f:
            f.write(css_content)
        
        # Convert markdown to HTML
        temp_html = os.path.join(base_dir, "temp_optimized.html")
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
        
        # Convert HTML to PDF using WeasyPrint
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

def merge_cover_with_optimized_handbook():
    """Merge cover page with optimized handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_Optimized_Images.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Optimized.pdf")
    
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
    """Main function to generate final optimized ESMS document"""
    print("Starting final optimized ESMS document generation...")
    
    # Step 1: Convert markdown to PDF
    print("\nStep 1: Converting markdown to optimized PDF...")
    if not convert_optimized_md_to_pdf():
        print("Failed to convert markdown to optimized PDF")
        return
    
    # Step 2: Merge cover with handbook
    print("\nStep 2: Merging cover page with optimized handbook...")
    if not merge_cover_with_optimized_handbook():
        print("Failed to merge cover page with optimized handbook")
        return
    
    print("\nFinal optimized ESMS document generation finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Optimized.pdf")

if __name__ == "__main__":
    main()