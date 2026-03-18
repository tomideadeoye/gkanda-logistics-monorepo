#!/usr/bin/env python3
"""
Script to convert the facility images HTML page to PDF using ReportLab with actual images.
"""

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def convert_html_to_pdf_with_images():
    """
    Convert the facility images HTML page to PDF with actual images using ReportLab.
    """
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/esia"
        output_file = os.path.join(base_dir, "pdf_output", "Facility_Images_and_Details_With_Images.pdf")
        images_dir = "/Users/mac/Documents/GitHub/gkalogistics/gkaassets"
        
        # Create PDF document
        doc = SimpleDocTemplate(
            output_file,
            pagesize=A4,
            leftMargin=25*mm,
            rightMargin=25*mm,
            topMargin=25*mm,
            bottomMargin=25*mm
        )
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor='#2E4A66'
        )
        
        heading1_style = ParagraphStyle(
            'CustomHeading1',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=12,
            alignment=TA_LEFT,
            textColor='#2E4A66'
        )
        
        heading2_style = ParagraphStyle(
            'CustomHeading2',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=10,
            alignment=TA_LEFT,
            textColor='#3E5A76'
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            leading=14
        )
        
        # Create content
        flowables = []
        
        # Title
        flowables.append(Paragraph("GK & A Logistics Services Limited", title_style))
        flowables.append(Paragraph("NPA Lighter Terminal, Ikorodu, Lagos State, Nigeria", 
                                 ParagraphStyle('Subtitle', parent=normal_style, fontSize=14, alignment=TA_CENTER)))
        flowables.append(Spacer(1, 20*mm))
        
        # Document info
        flowables.append(Paragraph("Facility Images and Details", heading1_style))
        flowables.append(Spacer(1, 10))
        flowables.append(Paragraph("This document presents key images of the facility conditions, layout, and operational procedures at the NPA Lighter Terminal, Ikorodu.", normal_style))
        flowables.append(Spacer(1, 10))
        flowables.append(Paragraph("<strong>Document:</strong> Environmental and Social Impact Assessment (ESIA)", normal_style))
        flowables.append(Paragraph("<strong>Date:</strong> November 12, 2025", normal_style))
        flowables.append(Spacer(1, 15*mm))
        
        # Image sections
        images_data = [
            {
                "title": "Site Conditions and Facility Layout",
                "description": "Overview of the current site conditions and facility layout at the NPA Lighter Terminal, Ikorodu. This image shows the spatial arrangement of operational areas, including quay/berth areas for barges/lighters, laydown yards, warehouses, and supporting infrastructure.",
                "filename": "Screenshot 2025-11-12 at 10.00.58.png"
            },
            {
                "title": "Environmental Monitoring Equipment and Procedures",
                "description": "Equipment used for environmental monitoring including air quality analyzers, noise measurement devices, and water quality testing instruments. This image also shows the procedures followed for baseline environmental data collection.",
                "filename": "Screenshot 2025-11-12 at 09.59.11.png"
            },
            {
                "title": "Safety Measures and Personnel Protective Equipment",
                "description": "Safety measures implemented throughout the facility and examples of personal protective equipment (PPE) used by personnel. This includes safety signage, equipment guarding, and proper use of PPE during various operational activities.",
                "filename": "Screenshot 2025-11-12 at 09.58.59.png"
            },
            {
                "title": "Waste Management and Spill Prevention Measures",
                "description": "Waste management systems in place including segregation points, storage areas, and disposal methods. Also shows spill prevention equipment such as bunding, spill kits, and containment systems for fuel and chemical storage areas.",
                "filename": "Screenshot 2025-11-12 at 09.58.38.png"
            }
        ]
        
        # Add each image section
        for i, image_data in enumerate(images_data):
            # Section title
            flowables.append(Paragraph(image_data["title"], heading2_style))
            flowables.append(Spacer(1, 8))
            
            # Add image if it exists
            image_path = os.path.join(images_dir, image_data["filename"])
            if os.path.exists(image_path):
                try:
                    # Add image with a maximum width and height
                    img = Image(image_path, width=6*inch, height=4*inch)
                    img.hAlign = 'CENTER'
                    flowables.append(img)
                except Exception as e:
                    flowables.append(Paragraph(f"<i>Image could not be loaded: {image_data['filename']}</i>", 
                                             ParagraphStyle('ImageError', parent=normal_style, 
                                                           textColor='#dc3545', fontStyle='italic')))
            else:
                flowables.append(Paragraph(f"<i>Image not found: {image_data['filename']}</i>", 
                                         ParagraphStyle('ImageMissing', parent=normal_style, 
                                                       textColor='#6c757d', fontStyle='italic')))
            
            flowables.append(Spacer(1, 8))
            
            # Description
            flowables.append(Paragraph(image_data["description"], normal_style))
            flowables.append(Spacer(1, 15*mm))
            
            # Add page break after each section except the last one
            if i < len(images_data) - 1:
                flowables.append(PageBreak())
        
        # Footer information
        flowables.append(Paragraph("GK & A Logistics Services Limited", 
                                 ParagraphStyle('FooterTitle', parent=normal_style, 
                                               fontSize=12, alignment=TA_CENTER, textColor='#2E4A66')))
        flowables.append(Paragraph("NPA Lighter Terminal, Ikorodu, Lagos State, Nigeria", 
                                 ParagraphStyle('Footer', parent=normal_style, 
                                               fontSize=10, alignment=TA_CENTER)))
        flowables.append(Paragraph("Contact: info@gkaports.com", 
                                 ParagraphStyle('Footer', parent=normal_style, 
                                               fontSize=10, alignment=TA_CENTER)))
        flowables.append(Spacer(1, 5*mm))
        flowables.append(Paragraph("© 2025 GK & A Logistics Services Ltd. All rights reserved.", 
                                 ParagraphStyle('Copyright', parent=normal_style, 
                                               fontSize=8, alignment=TA_CENTER, textColor='#6c757d')))
        
        # Build PDF
        doc.build(flowables)
        
        print(f"Successfully created facility images PDF with actual images: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error creating facility images PDF with images: {e}")
        return False

def main():
    """Main function to convert facility images HTML to PDF with actual images."""
    print("Converting facility images document to PDF with actual images...")
    if convert_html_to_pdf_with_images():
        print("Facility images document successfully converted to PDF with actual images!")
    else:
        print("Failed to convert facility images document to PDF with actual images")

if __name__ == "__main__":
    main()