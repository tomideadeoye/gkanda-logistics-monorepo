#!/usr/bin/env python3
"""
Convert the Emergency Response Plan markdown document to PDF and merge with cover page.
"""

import os
import subprocess
from PyPDF2 import PdfMerger

def convert_markdown_to_pdf(input_md, output_pdf):
    """
    Convert markdown to PDF using weasyprint with proper styling.
    
    Args:
        input_md (str): Path to input markdown file
        output_pdf (str): Path to output PDF file
    """
    try:
        # First convert markdown to HTML
        html_file = output_pdf.replace('.pdf', '.html')
        
        # Command to convert markdown to HTML with styling
        cmd1 = [
            'pandoc',
            input_md,
            '-o', html_file,
            '--css=manual_edit_styling.css',
            '--toc',
            '--toc-depth=2',
            '--standalone'
        ]
        
        result1 = subprocess.run(cmd1, capture_output=True, text=True, cwd=os.path.dirname(input_md))
        
        if result1.returncode != 0:
            print(f"Error converting markdown to HTML: {result1.stderr}")
            return False
        
        # Command to convert HTML to PDF using weasyprint
        cmd2 = [
            'weasyprint',
            html_file,
            output_pdf
        ]
        
        result2 = subprocess.run(cmd2, capture_output=True, text=True, cwd=os.path.dirname(input_md))
        
        if result2.returncode == 0:
            print(f"Successfully converted {input_md} to {output_pdf}")
            # Clean up temporary HTML file
            if os.path.exists(html_file):
                os.remove(html_file)
            return True
        else:
            print(f"Error converting HTML to PDF: {result2.stderr}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into one.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_path (str): Path where merged PDF should be saved
    """
    print(f"Merging PDFs: {[os.path.basename(f) for f in pdf_files]}")
    
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            print(f"Adding {os.path.basename(pdf_file)} to merger...")
            merger.append(pdf_file)
        else:
            print(f"Warning: {pdf_file} not found, skipping...")
            merger.close()
            return False
    
    print(f"Writing merged PDF to {os.path.basename(output_path)}...")
    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs to {output_path}")
    return True

def main():
    """Main function to convert markdown to PDF and merge with cover page."""
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Input markdown file
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan.md")
    
    # Output PDF files
    content_pdf = os.path.join(base_dir, "Emergency_Response_Plan_Content.pdf")
    cover_pdf = os.path.join(base_dir, "Emergency_Response_Plan_Cover.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan.pdf")
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"Error: Markdown file not found: {md_file}")
        return
    
    # Step 1: Convert markdown to PDF
    print("Step 1: Converting markdown to PDF...")
    if not convert_markdown_to_pdf(md_file, content_pdf):
        print("Failed to convert markdown to PDF")
        return
    
    # Step 2: Merge with cover page
    print("\nStep 2: Merging with cover page...")
    if merge_pdfs([cover_pdf, content_pdf], final_pdf):
        print("\nPDF conversion and merging completed successfully!")
        print(f"Final combined PDF: {final_pdf}")
        
        # Show file size
        if os.path.exists(final_pdf):
            size_mb = os.path.getsize(final_pdf) / (1024*1024)
            print(f"File size: {size_mb:.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()