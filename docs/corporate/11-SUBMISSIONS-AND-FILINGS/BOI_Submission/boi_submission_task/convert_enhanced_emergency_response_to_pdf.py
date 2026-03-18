#!/usr/bin/env python3
"""
Convert the enhanced Emergency Response Plan markdown to PDF.
"""

import os
import subprocess

def convert_markdown_to_pdf():
    """
    Convert the enhanced Emergency Response Plan markdown to PDF using pandoc.
    """
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Enhanced.md")
    pdf_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Enhanced.pdf")
    
    # Check if markdown file exists
    if not os.path.exists(md_file):
        print(f"Error: Markdown file not found: {md_file}")
        return False
    
    try:
        # Convert markdown to PDF using pandoc
        print("Converting enhanced Emergency Response Plan markdown to PDF...")
        
        # Command to convert markdown to PDF with better formatting
        cmd = [
            'pandoc',
            md_file,
            '-o', pdf_file,
            '--pdf-engine=weasyprint',
            '--css=improved_styling.css',
            '--toc',
            '--toc-depth=2',
            '--standalone',
            '--variable', 'geometry:a4paper',
            '--variable', 'fontsize=11pt',
            '--variable', 'linestretch=1.25'
        ]
        
        # Execute the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully created enhanced Emergency Response Plan PDF: {pdf_file}")
            return True
        else:
            print(f"Error converting markdown to PDF: {result.stderr}")
            # Fallback to simpler conversion
            print("Trying fallback conversion method...")
            return convert_with_fallback(md_file, pdf_file)
        
    except Exception as e:
        print(f"Error converting markdown to PDF: {e}")
        return False

def convert_with_fallback(md_file, pdf_file):
    """
    Fallback method to convert markdown to PDF.
    """
    try:
        # Simpler pandoc command
        cmd = [
            'pandoc',
            md_file,
            '-o', pdf_file,
            '--pdf-engine=weasyprint',
            '--variable', 'geometry:a4paper',
            '--variable', 'fontsize=11pt',
            '--variable', 'linestretch=1.25'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Successfully created enhanced Emergency Response Plan PDF (fallback): {pdf_file}")
            return True
        else:
            print(f"Fallback conversion also failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Fallback conversion error: {e}")
        return False

def main():
    """Main function to convert the enhanced markdown to PDF."""
    print("Converting enhanced Emergency Response Plan to PDF...")
    if convert_markdown_to_pdf():
        print("Enhanced Emergency Response Plan PDF created successfully!")
    else:
        print("Failed to create enhanced Emergency Response Plan PDF")

if __name__ == "__main__":
    main()