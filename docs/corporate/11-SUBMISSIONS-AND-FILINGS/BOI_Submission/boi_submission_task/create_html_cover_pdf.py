#!/usr/bin/env python3
"""
Convert the HTML cover page to PDF using WeasyPrint to preserve styling.
"""

import os

def create_html_cover_pdf_with_weasyprint():
    """
    Convert the HTML cover page to PDF using WeasyPrint.
    """
    try:
        from weasyprint import HTML, CSS
        
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
        html_file = os.path.join(base_dir, "emergency_response_cover.html")
        pdf_file = os.path.join(base_dir, "Emergency_Response_Plan_HTML_Cover_WeasyPrint.pdf")
        
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
        print("Falling back to ReportLab method...")
        return create_html_cover_pdf_with_reportlab()

def create_html_cover_pdf_with_reportlab():
    """
    Fallback method: Create a cover page PDF using ReportLab with the background image.
    """
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import mm
        from reportlab.platypus import Image
        from reportlab.lib.utils import ImageReader
        
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
        image_path = "/Users/mac/Documents/GitHub/gkalogistics/gkaassets/william-william-NndKt2kF1L4-unsplash-scaled.jpg"
        logo_path = "/Users/mac/Documents/GitHub/gkalogistics/images/gk & a logo.png"
        pdf_file = os.path.join(base_dir, "Emergency_Response_Plan_HTML_Cover_WeasyPrint.pdf")
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"Error: Image file not found: {image_path}")
            return False
            
        # Check if logo file exists
        if not os.path.exists(logo_path):
            print(f"Error: Logo file not found: {logo_path}")
            return False
        
        # Set up the canvas with A4
        page_width, page_height = A4
        c = canvas.Canvas(pdf_file, pagesize=A4)
        
        # Add background image
        try:
            # Scale image to fit page (cover style)
            img_width = page_width
            img_height = page_height
            c.drawImage(image_path, 0, 0, img_width, img_height, mask='auto')
        except Exception as e:
            print(f"Warning: Could not add background image: {e}")
        
        # Add semi-transparent white overlay for text readability
        c.setFillColorRGB(1, 1, 1, 0.7)  # White with 70% opacity
        c.rect(0, 0, page_width, page_height, fill=1, stroke=0)
        
        # Reset fill color to opaque
        c.setFillColor(colors.black)
        
        # Set margins
        margin_left = 25 * mm
        margin_right = 25 * mm
        margin_top = 20 * mm
        margin_bottom = 20 * mm
        
        # Add logo
        try:
            logo_width = 80 * mm
            logo_height = 40 * mm
            c.drawImage(logo_path, (page_width - logo_width) / 2, page_height - margin_top - 45*mm, 
                        width=logo_width, height=logo_height, mask='auto')
        except Exception as e:
            print(f"Warning: Could not add logo: {e}")
        
        # Add company name
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(page_width/2, page_height - margin_top - 65*mm, "GK & A LOGISTICS SERVICES LTD")
        
        # Add document title
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(page_width/2, page_height - margin_top - 90*mm, "EMERGENCY RESPONSE PLAN")
        
        # Add document subtitle
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(page_width/2, page_height - margin_top - 110*mm, 
                            "Import/Export Terminal, Warehouse, and Reefer Containers")
        c.drawCentredString(page_width/2, page_height - margin_top - 120*mm, 
                            "at NPA Ikorodu")
        
        # Document information
        c.setFont("Helvetica", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 145*mm, 
                            "Document No.: ERP-IE-002")
        c.drawCentredString(page_width/2, page_height - margin_top - 160*mm, 
                            "Version: 1.5")
        c.drawCentredString(page_width/2, page_height - margin_top - 175*mm, 
                            "Effective Date: November 1, 2025")
        c.drawCentredString(page_width/2, page_height - margin_top - 190*mm, 
                            "Review Date: October 26, 2026")
        
        # Facility information
        c.setFont("Helvetica", 11)
        c.drawCentredString(page_width/2, page_height - margin_top - 215*mm, 
                            "Facility: GK & A Terminal, NPA Lighter Terminal (Ikorodu)")
        c.drawCentredString(page_width/2, page_height - margin_top - 230*mm, 
                            "NPA Lighter Terminal Complex, Ipakodo Road, Ipakodo")
        c.drawCentredString(page_width/2, page_height - margin_top - 245*mm, 
                            "Ikorodu, Lagos State, 104101, Nigeria")
        
        # Emergency contact information
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 270*mm, 
                            "Emergency Activation (Lagos State): Dial 112 or 727")
        
        # Authority information
        c.setFont("Helvetica", 11)
        c.drawCentredString(page_width/2, page_height - margin_top - 290*mm, 
                            "Plan Owner: HSE Manager")
        c.drawCentredString(page_width/2, page_height - margin_top - 305*mm, 
                            "Authority: Managing Director")
        
        # Approval information
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, page_height - margin_top - 325*mm, 
                            "Approval - Distribution: Internal (All Departments), NPA Liaison, Critical Contractors on NDA")
        
        # Add decorative line
        c.setLineWidth(2)
        c.setStrokeColor(colors.black)
        c.line(margin_left, margin_bottom + 60*mm, page_width - margin_right, margin_bottom + 60*mm)
        
        # Footer information
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 45*mm, 
                            "This document is controlled and must be reproduced in full.")
        c.drawCentredString(page_width/2, margin_bottom + 35*mm, 
                            "Any extract or summary must be clearly identified as such.")
        c.drawCentredString(page_width/2, margin_bottom + 25*mm, 
                            "© 2025 GK & A Logistics Services Ltd. All rights reserved.")
        
        # Page number
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 5*mm, "Page 1 of 1")
        
        # Save the PDF
        c.save()
        print(f"Successfully created HTML cover PDF using ReportLab: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"Error creating HTML cover PDF with ReportLab: {e}")
        return False

def main():
    """Main function to create the HTML cover PDF."""
    print("Creating HTML cover page PDF...")
    if create_html_cover_pdf_with_weasyprint():
        print("HTML cover page PDF created successfully!")
    else:
        print("Failed to create HTML cover page PDF")

if __name__ == "__main__":
    main()