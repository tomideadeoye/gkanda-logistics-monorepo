#!/usr/bin/env python3
"""
Convert the OHS Policy HTML cover page to PDF using ReportLab.
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm

def create_ohs_cover_pdf():
    """
    Create a cover page PDF using ReportLab with the background image.
    """
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
        image_path = "/Users/mac/Documents/GitHub/gkalogistics/gkaassets/hr_cover_image.jpg"
        logo_path = "/Users/mac/Documents/GitHub/gkalogistics/images/gk & a logo.png"
        pdf_file = os.path.join(base_dir, "OHS_Cover.pdf")
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"Error: Image file not found: {image_path}")
            return False
            
        # Check if logo file exists
        if not os.path.exists(logo_path):
            print(f"Warning: Logo file not found: {logo_path}")
            logo_path = None
        
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
        if logo_path and os.path.exists(logo_path):
            try:
                logo_width = 80 * mm
                logo_height = 40 * mm
                c.drawImage(logo_path, (page_width - logo_width) / 2, page_height - margin_top - 45*mm, 
                            width=logo_width, height=logo_height, mask='auto')
            except Exception as e:
                print(f"Warning: Could not add logo: {e}")
        
        # Add company name
        c.setFont("Helvetica-Bold", 28)
        c.drawCentredString(page_width/2, page_height - margin_top - 65*mm, "GK & A LOGISTICS SERVICES LIMITED")
        
        # Add document title
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(page_width/2, page_height - margin_top - 90*mm, "INTEGRATED OCCUPATIONAL HEALTH, SAFETY &")
        c.drawCentredString(page_width/2, page_height - margin_top - 105*mm, "WOMEN-LED \"SAFETY-FIRST\" POLICY")
        
        # Add document subtitle
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(page_width/2, page_height - margin_top - 125*mm, 
                            "NPA Lighter Terminal (Ikorodu) Operations")
        
        # Document information
        c.setFont("Helvetica", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 150*mm, 
                            "Document No.: OHS-POL-001")
        c.drawCentredString(page_width/2, page_height - margin_top - 165*mm, 
                            "Version: 1.0")
        c.drawCentredString(page_width/2, page_height - margin_top - 180*mm, 
                            "Effective Date: November 1, 2025")
        c.drawCentredString(page_width/2, page_height - margin_top - 195*mm, 
                            "Review Date: October 31, 2026")
        
        # Facility information
        c.setFont("Helvetica", 11)
        c.drawCentredString(page_width/2, page_height - margin_top - 220*mm, 
                            "Facility: GK & A Terminal, NPA Lighter Terminal (Ikorodu)")
        c.drawCentredString(page_width/2, page_height - margin_top - 235*mm, 
                            "NPA Lighter Terminal Complex, Ipakodo Road, Ipakodo")
        c.drawCentredString(page_width/2, page_height - margin_top - 250*mm, 
                            "Ikorodu, Lagos State, 104101, Nigeria")
        
        # Contact information
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 275*mm, 
                            "Contact: info@gkaports.com")
        
        # Footer information
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 45*mm, 
                            "This document is controlled and must be reproduced in full.")
        c.drawCentredString(page_width/2, margin_bottom + 35*mm, 
                            "Any extract or summary must be clearly identified as such.")
        c.drawCentredString(page_width/2, margin_bottom + 25*mm, 
                            "© 2025 GK & A Logistics Services Ltd. All rights reserved.")
        
        # Add decorative line
        c.setLineWidth(2)
        c.setStrokeColor(colors.black)
        c.line(margin_left, margin_bottom + 60*mm, page_width - margin_right, margin_bottom + 60*mm)
        
        # Page number
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 5*mm, "Page 1 of 1")
        
        # Save the PDF
        c.save()
        print(f"Successfully created OHS Policy cover PDF: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"Error creating OHS Policy cover PDF with ReportLab: {e}")
        return False

def main():
    """Main function to create the OHS Policy cover PDF."""
    print("Creating OHS Policy cover page PDF...")
    if create_ohs_cover_pdf():
        print("OHS Policy cover page PDF created successfully!")
    else:
        print("Failed to create OHS Policy cover page PDF")

if __name__ == "__main__":
    main()