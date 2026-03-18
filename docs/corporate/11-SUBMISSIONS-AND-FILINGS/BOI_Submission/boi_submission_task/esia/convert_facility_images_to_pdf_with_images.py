#!/usr/bin/env python3
"""
Script to convert the facility images HTML page to PDF using wkhtmltopdf.
"""

import os
import subprocess
import sys

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
            '--enable-local-file-access',  # Allow local file access for images
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
    """Main function to convert facility images HTML to PDF."""
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/esia"
    input_file = os.path.join(base_dir, "facility_images.html")
    output_file = os.path.join(base_dir, "pdf_output", "Facility_Images_and_Details_With_Images.pdf")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: HTML file not found: {input_file}")
        sys.exit(1)
    
    print(f"Converting {input_file} to PDF using wkhtmltopdf...")
    if html_to_pdf(input_file, output_file):
        print("Facility images document successfully converted to PDF with images!")
    else:
        print("Failed to create facility images PDF with wkhtmltopdf")

if __name__ == '__main__':
    main()