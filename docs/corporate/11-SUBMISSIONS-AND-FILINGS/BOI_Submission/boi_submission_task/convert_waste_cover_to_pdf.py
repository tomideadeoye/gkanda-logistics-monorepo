#!/usr/bin/env python3
"""
Convert the Waste Management and Sustainability Plan HTML cover page to PDF using ReportLab.
"""

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm

def create_waste_cover_pdf():
    """
    Create a cover page PDF using ReportLab with the background image.
    """
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
        image_path = "/Users/mac/Documents/GitHub/gkalogistics/gkaassets/hr_cover_image.jpg"
        logo_path = "/Users/mac/Documents/GitHub/gkalogistics/images/gk & a logo.png"
        pdf_file = os.path.join(base_dir, "Waste_Management_Sustainability_Cover.pdf")
        
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
        c.drawCentredString(page_width/2, page_height - margin_top - 65*mm, "GK&A LOGISTICS SERVICES LIMITED")
        
        # Add document title
        c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(page_width/2, page_height - margin_top - 90*mm, "WASTE MANAGEMENT AND SUSTAINABILITY PLAN")
        
        # Add document subtitle
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(page_width/2, page_height - margin_top - 110*mm, 
                            "Environmental Compliance and Sustainable Operations")
        
        # Document information
        c.setFont("Helvetica", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 135*mm, 
                            "Document No.: WMS-2023-001")
        c.drawCentredString(page_width/2, page_height - margin_top - 150*mm, 
                            "Version: 1.0")
        c.drawCentredString(page_width/2, page_height - margin_top - 165*mm, 
                            "Date Prepared: June 1, 2023")
        
        # Facility information
        c.setFont("Helvetica", 11)
        c.drawCentredString(page_width/2, page_height - margin_top - 190*mm, 
                            "Facility: 35-Hectare Leased Operations")
        c.drawCentredString(page_width/2, page_height - margin_top - 205*mm, 
                            "Location: Ikorodu Lighter Terminal, Ikorodu, Lagos")
        
        # Contact information
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(page_width/2, page_height - margin_top - 230*mm, 
                            "Contact: info@gkaports.com")
        
        # Footer information
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 45*mm, 
                            "This document is controlled and must be reproduced in full.")
        c.drawCentredString(page_width/2, margin_bottom + 35*mm, 
                            "Any extract or summary must be clearly identified as such.")
        c.drawCentredString(page_width/2, margin_bottom + 25*mm, 
                            "© 2023 GK&A Logistics Services Limited. All rights reserved.")
        
        # Add decorative line
        c.setLineWidth(2)
        c.setStrokeColor(colors.black)
        c.line(margin_left, margin_bottom + 60*mm, page_width - margin_right, margin_bottom + 60*mm)
        
        # Page number
        c.setFont("Helvetica", 10)
        c.drawCentredString(page_width/2, margin_bottom + 5*mm, "Page 1 of 1")
        
        # Save the PDF
        c.save()
        print(f"Successfully created Waste Management and Sustainability Plan cover PDF: {pdf_file}")
        return True
        
    except Exception as e:
        print(f"Error creating Waste Management and Sustainability Plan cover PDF with ReportLab: {e}")
        return False

def main():
    """Main function to create the Waste Management and Sustainability Plan cover PDF."""
    print("Creating Waste Management and Sustainability Plan cover page PDF...")
    if create_waste_cover_pdf():
        print("Waste Management and Sustainability Plan cover page PDF created successfully!")
    else:
        print("Failed to create Waste Management and Sustainability Plan cover page PDF")

if __name__ == "__main__":
    main()