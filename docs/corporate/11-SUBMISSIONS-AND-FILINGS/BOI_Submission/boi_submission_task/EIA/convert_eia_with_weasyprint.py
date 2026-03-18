#!/usr/bin/env python3
"""
Convert the EIA HTML cover page to PDF using WeasyPrint to preserve styling.
"""

import os
from weasyprint import HTML, CSS

def create_eia_cover_pdf_with_weasyprint():
    """
    Convert the EIA HTML cover page to PDF using WeasyPrint.
    """
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
        html_file = os.path.join(base_dir, "EIA_Cover_Page.html")
        pdf_file = os.path.join(base_dir, "EIA_Cover_Page_WeasyPrint.pdf")
        
        # Check if HTML file exists
        if not os.path.exists(html_file):
            print(f"Error: HTML file not found: {html_file}")
            return False
        
        # Convert HTML to PDF using WeasyPrint
        print("Converting HTML to PDF using WeasyPrint...")
        html = HTML(filename=html_file)
        
        # Add CSS for proper page size
        css = CSS(string='''
            @page {
                size: A4;
                margin: 0;
            }
            body {
                margin: 0;
                padding: 0;
            }
        ''')
        
        html.write_pdf(pdf_file, stylesheets=[css])
        
        print(f"Successfully created HTML cover PDF: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"Error converting HTML to PDF with WeasyPrint: {e}")
        return False

def main():
    """Main function to create the EIA cover PDF."""
    print("Creating EIA cover page PDF with WeasyPrint...")
    if create_eia_cover_pdf_with_weasyprint():
        print("EIA cover page PDF created successfully with WeasyPrint!")
    else:
        print("Failed to create EIA cover page PDF with WeasyPrint")

if __name__ == "__main__":
    main()