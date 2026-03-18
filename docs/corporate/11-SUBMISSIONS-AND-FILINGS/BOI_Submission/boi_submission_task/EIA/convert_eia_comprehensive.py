#!/usr/bin/env python3
"""
Comprehensive script to convert EIA HTML cover page to PDF using multiple methods with fallbacks.
"""

import os
import sys
import subprocess

def try_weasyprint():
    """Try to convert using WeasyPrint."""
    try:
        from weasyprint import HTML, CSS
        
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
        
    except ImportError:
        print("WeasyPrint not installed or not working properly")
        return False
    except Exception as e:
        print(f"Error converting HTML to PDF with WeasyPrint: {e}")
        return False

def try_wkhtmltopdf():
    """Try to convert using wkhtmltopdf."""
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
        input_file = os.path.join(base_dir, "EIA_Cover_Page.html")
        output_file = os.path.join(base_dir, "EIA_Cover_Page_wkhtmltopdf.pdf")
        
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: HTML file not found: {input_file}")
            return False
        
        # wkhtmltopdf command with A4 page size
        cmd = [
            'wkhtmltopdf',
            '--page-size', 'A4',
            '--margin-top', '10mm',
            '--margin-bottom', '10mm',
            '--margin-left', '10mm',
            '--margin-right', '10mm',
            '--disable-smart-shrinking',
            input_file,
            output_file
        ]
        
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"PDF successfully created: {output_file}")
            return True
        else:
            print(f"Error converting HTML to PDF with wkhtmltopdf: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("wkhtmltopdf not found in system PATH")
        return False
    except Exception as e:
        print(f"Error with wkhtmltopdf: {e}")
        return False

def use_reportlab_fallback():
    """Use the existing ReportLab method as fallback."""
    try:
        # Import and run the existing ReportLab script
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
        sys.path.append(base_dir)
        
        # Run the existing convert_eia_cover_to_pdf.py script
        import convert_eia_cover_to_pdf
        result = convert_eia_cover_to_pdf.create_eia_cover_pdf()
        return result
    except Exception as e:
        print(f"Error with ReportLab fallback: {e}")
        return False

def main():
    """Main function to create the EIA cover PDF using available methods."""
    print("Creating EIA cover page PDF using comprehensive approach...")
    
    # Try methods in order of preference
    methods = [
        ("WeasyPrint", try_weasyprint),
        ("wkhtmltopdf", try_wkhtmltopdf),
        ("ReportLab (fallback)", use_reportlab_fallback)
    ]
    
    for method_name, method_func in methods:
        print(f"\nTrying {method_name}...")
        if method_func():
            print(f"EIA cover page PDF created successfully with {method_name}!")
            return
        else:
            print(f"Failed to create EIA cover page PDF with {method_name}")
    
    print("\nAll methods failed to create the PDF.")

if __name__ == "__main__":
    main()