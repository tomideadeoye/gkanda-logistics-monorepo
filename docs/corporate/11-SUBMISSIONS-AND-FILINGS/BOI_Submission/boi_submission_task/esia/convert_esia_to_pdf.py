#!/usr/bin/env python3
"""
Script to convert the ESIA text file to PDF using ReportLab.
"""

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas

def convert_esia_to_pdf():
    """
    Convert the ESIA text file to PDF with proper formatting.
    """
    try:
        # Define file paths
        base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/esia"
        input_file = os.path.join(base_dir, "esia")
        output_file = os.path.join(base_dir, "pdf_output", "ESIA_Document.pdf")
        
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file not found: {input_file}")
            return False
            
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
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
        
        heading3_style = ParagraphStyle(
            'CustomHeading3',
            parent=styles['Heading3'],
            fontSize=14,
            spaceAfter=8,
            alignment=TA_LEFT
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            leading=14
        )
        
        # Process content
        flowables = []
        
        # Split content into lines
        lines = content.split('\n')
        
        # Add title page
        flowables.append(Paragraph("ENVIRONMENTAL AND SOCIAL IMPACT ASSESSMENT (ESIA)", title_style))
        flowables.append(Spacer(1, 20*mm))
        flowables.append(Paragraph("FOR", normal_style))
        flowables.append(Spacer(1, 10*mm))
        flowables.append(Paragraph("GK & A LOGISTICS SERVICES LIMITED", heading1_style))
        flowables.append(Spacer(1, 10*mm))
        flowables.append(Paragraph("OPERATIONS AT NPA LIGHTER TERMINAL, IKORODU, LAGOS STATE, NIGERIA", normal_style))
        flowables.append(Spacer(1, 20*mm))
        flowables.append(Paragraph("DRAFT v1.0", heading2_style))
        flowables.append(Spacer(1, 10*mm))
        flowables.append(Paragraph("November 1, 2025", normal_style))
        flowables.append(PageBreak())
        
        # Process each line
        for line in lines:
            # Skip empty lines
            if not line.strip():
                flowables.append(Spacer(1, 6))
                continue
                
            # Handle different types of lines
            if line.startswith('## '):
                # Main headings
                heading_text = line[3:].strip()
                flowables.append(Paragraph(heading_text, heading1_style))
                flowables.append(Spacer(1, 12))
            elif line.startswith('### '):
                # Subheadings
                heading_text = line[4:].strip()
                flowables.append(Paragraph(heading_text, heading2_style))
                flowables.append(Spacer(1, 10))
            elif line.startswith('#### '):
                # Sub-subheadings
                heading_text = line[5:].strip()
                flowables.append(Paragraph(heading_text, heading3_style))
                flowables.append(Spacer(1, 8))
            elif line.startswith('- ') or line.startswith('    - '):
                # Bullet points
                flowables.append(Paragraph(line, normal_style))
            elif line.startswith('**') and line.endswith('**'):
                # Bold text sections
                flowables.append(Paragraph(line, heading2_style))
                flowables.append(Spacer(1, 10))
            elif '|' in line and line.count('|') > 3:
                # Table rows - convert to normal text
                flowables.append(Paragraph(line.replace('|', ' | '), normal_style))
            elif line.startswith('```'):
                # Code blocks - skip
                continue
            elif line.startswith('---'):
                # Section breaks
                flowables.append(Spacer(1, 15))
            else:
                # Regular text
                if line.strip():
                    flowables.append(Paragraph(line, normal_style))
        
        # Build PDF
        doc.build(flowables)
        
        print(f"Successfully created ESIA PDF: {output_file}")
        return True
        
    except Exception as e:
        print(f"Error creating ESIA PDF: {e}")
        return False

def main():
    """Main function to convert ESIA to PDF."""
    print("Converting ESIA document to PDF...")
    if convert_esia_to_pdf():
        print("ESIA document successfully converted to PDF!")
    else:
        print("Failed to convert ESIA document to PDF")

if __name__ == "__main__":
    main()