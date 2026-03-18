#!/usr/bin/env python3
"""
Create a professional cover page for the Emergency Response Plan document.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm

def create_emergency_response_cover(output_path):
    """
    Create a professional cover page for the Emergency Response Plan document.
    
    Args:
        output_path (str): Path where the PDF should be saved
    """
    # Set up the canvas with A4
    page_width, page_height = A4
    c = canvas.Canvas(output_path, pagesize=A4)
    
    # Ensure all text is black
    c.setFillColor(colors.black)
    c.setStrokeColor(colors.black)
    
    # Set margins
    margin_left = 25 * mm
    margin_right = 25 * mm
    margin_top = 20 * mm
    margin_bottom = 20 * mm
    
    # Add company logo space (would be added if we had a logo)
    # For now, we'll just add the company name in large text
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(page_width/2, page_height - margin_top - 30*mm, "GK & A LOGISTICS SERVICES LTD")
    
    # Add document title
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(page_width/2, page_height - margin_top - 55*mm, "EMERGENCY RESPONSE PLAN")
    
    # Add document subtitle
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(page_width/2, page_height - margin_top - 75*mm, 
                        "Import/Export Terminal, Warehouse, and Reefer Containers")
    c.drawCentredString(page_width/2, page_height - margin_top - 85*mm, 
                        "at NPA Ikorodu")
    
    # Document information
    c.setFont("Helvetica", 12)
    c.drawCentredString(page_width/2, page_height - margin_top - 110*mm, 
                        "Document No.: ERP-IE-002")
    c.drawCentredString(page_width/2, page_height - margin_top - 125*mm, 
                        "Version: 1.5")
    c.drawCentredString(page_width/2, page_height - margin_top - 140*mm, 
                        "Effective Date: November 1, 2025")
    c.drawCentredString(page_width/2, page_height - margin_top - 155*mm, 
                        "Review Date: October 26, 2026")
    
    # Facility information
    c.setFont("Helvetica", 11)
    c.drawCentredString(page_width/2, page_height - margin_top - 180*mm, 
                        "Facility: GK & A Terminal, NPA Lighter Terminal (Ikorodu)")
    c.drawCentredString(page_width/2, page_height - margin_top - 195*mm, 
                        "NPA Lighter Terminal Complex, Ipakodo Road, Ipakodo")
    c.drawCentredString(page_width/2, page_height - margin_top - 210*mm, 
                        "Ikorodu, Lagos State, 104101, Nigeria")
    
    # Emergency contact information
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(page_width/2, page_height - margin_top - 235*mm, 
                        "Emergency Activation (Lagos State): Dial 112 or 727")
    
    # Authority information
    c.setFont("Helvetica", 11)
    c.drawCentredString(page_width/2, page_height - margin_top - 255*mm, 
                        "Plan Owner: HSE Manager")
    c.drawCentredString(page_width/2, page_height - margin_top - 270*mm, 
                        "Authority: Managing Director")
    
    # Approval information
    c.setFont("Helvetica", 10)
    c.drawCentredString(page_width/2, page_height - margin_top - 290*mm, 
                        "Approval - Distribution: Internal (All Departments), NPA Liaison, Critical Contractors on NDA")
    
    # Add decorative line
    c.setLineWidth(2)
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
    print(f"Emergency Response Plan cover created: {output_path}")

def main():
    """Main function to create the emergency response cover."""
    output_path = "Emergency_Response_Plan_Cover.pdf"
    try:
        create_emergency_response_cover(output_path)
        print("Cover page created successfully!")
    except Exception as e:
        print(f"Error creating cover page: {e}")

if __name__ == "__main__":
    main()