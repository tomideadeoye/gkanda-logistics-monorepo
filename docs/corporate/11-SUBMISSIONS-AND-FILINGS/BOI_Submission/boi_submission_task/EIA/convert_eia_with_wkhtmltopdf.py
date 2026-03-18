#!/usr/bin/env python3
"""
Script to convert EIA HTML cover page to PDF using wkhtmltopdf.
"""

import sys
import subprocess
import os

def html_to_pdf(input_html, output_pdf):
    """
    Convert HTML to PDF with A4 page settings using wkhtmltopdf.
    """
    try:
        # wkhtmltopdf command with A4 page size
        cmd = [
            'wkhtmltopdf',
            '--page-size', 'A4',
            '--margin-top', '10mm',
            '--margin-bottom', '10mm',
            '--margin-left', '10mm',
            '--margin-right', '10mm',
            '--disable-smart-shrinking',
            input_html,
            output_pdf
        ]
        
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"PDF successfully created: {output_pdf}")
            return True
        else:
            print(f"Error converting HTML to PDF: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
    input_file = os.path.join(base_dir, "EIA_Cover_Page.html")
    output_file = os.path.join(base_dir, "EIA_Cover_Page_wkhtmltopdf.pdf")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: HTML file not found: {input_file}")
        sys.exit(1)
    
    print(f"Converting {input_file} to PDF using wkhtmltopdf...")
    if html_to_pdf(input_file, output_file):
        print("EIA cover page PDF created successfully with wkhtmltopdf!")
    else:
        print("Failed to create EIA cover page PDF with wkhtmltopdf")

if __name__ == '__main__':
    main()