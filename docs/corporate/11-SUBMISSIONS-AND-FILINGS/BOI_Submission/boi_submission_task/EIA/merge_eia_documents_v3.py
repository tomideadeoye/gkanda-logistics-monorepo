#!/usr/bin/env python3
"""
Convert all EIA markdown documents to PDF and merge them into a single PDF file.
This version uses only built-in Python libraries and ReportLab.
"""

import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from PyPDF2 import PdfMerger

def simple_markdown_to_pdf(markdown_content, output_pdf):
    """Convert simple markdown content to PDF using ReportLab."""
    try:
        # Create a PDF document
        doc = SimpleDocTemplate(output_pdf, pagesize=A4, 
                                leftMargin=72, rightMargin=72,
                                topMargin=72, bottomMargin=72)
        
        # Get styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor='black'
        )
        
        h1_style = ParagraphStyle(
            'CustomH1',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            textColor='black'
        )
        
        h2_style = ParagraphStyle(
            'CustomH2',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=15,
            textColor='black'
        )
        
        h3_style = ParagraphStyle(
            'CustomH3',
            parent=styles['Heading3'],
            fontSize=14,
            spaceAfter=12,
            textColor='black'
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            textColor='black'
        )
        
        bullet_style = ParagraphStyle(
            'CustomBullet',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=6,
            leftIndent=20,
            textColor='black'
        )
        
        # Parse markdown content and create PDF elements
        story = []
        
        # Split content into lines
        lines = markdown_content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if not line:
                # Empty line - add space
                story.append(Spacer(1, 12))
                i += 1
                continue
            
            # Handle different markdown elements
            if line.startswith('# '):
                # H1 - Title
                text = line[2:].strip()
                story.append(Paragraph(text, title_style))
                story.append(Spacer(1, 20))
            elif line.startswith('## '):
                # H2 - Heading
                text = line[3:].strip()
                story.append(Paragraph(text, h2_style))
                story.append(Spacer(1, 15))
            elif line.startswith('### '):
                # H3 - Subheading
                text = line[4:].strip()
                story.append(Paragraph(text, h3_style))
                story.append(Spacer(1, 12))
            elif line.startswith('- ') or line.startswith('* '):
                # Bullet point
                text = line[2:].strip()
                story.append(Paragraph('• ' + text, bullet_style))
                story.append(Spacer(1, 6))
            elif line.startswith('1. '):
                # Numbered list (simplified)
                text = line[3:].strip()
                story.append(Paragraph(line, normal_style))
                story.append(Spacer(1, 6))
            else:
                # Regular paragraph
                # Handle multi-line paragraphs
                paragraph_lines = [line]
                j = i + 1
                while j < len(lines) and lines[j].strip() and not (
                    lines[j].startswith('#') or 
                    lines[j].startswith('-') or 
                    lines[j].startswith('*') or
                    lines[j].startswith('1.')
                ):
                    paragraph_lines.append(lines[j].strip())
                    j += 1
                
                # Join lines and create paragraph
                paragraph_text = ' '.join(paragraph_lines)
                if paragraph_text.strip():
                    story.append(Paragraph(paragraph_text, normal_style))
                    story.append(Spacer(1, 6))
                
                # Skip the lines we've already processed
                i = j - 1
            
            i += 1
        
        # Build PDF
        doc.build(story)
        return True
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def convert_markdown_to_pdf(input_md, output_pdf):
    """
    Convert markdown file to PDF.
    
    Args:
        input_md (str): Path to input markdown file
        output_pdf (str): Path to output PDF file
    """
    try:
        # Read markdown file
        with open(input_md, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert to PDF
        if simple_markdown_to_pdf(markdown_content, output_pdf):
            print(f"Successfully converted {os.path.basename(input_md)} to {os.path.basename(output_pdf)}")
            return True
        else:
            print(f"Failed to convert {os.path.basename(input_md)} to PDF")
            return False
            
    except Exception as e:
        print(f"Error reading {input_md} or converting to PDF: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into one.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_path (str): Path where merged PDF should be saved
    """
    if not pdf_files:
        print("No PDF files to merge.")
        return False
    
    print(f"Merging {len(pdf_files)} PDFs...")
    
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            print(f"Adding {os.path.basename(pdf_file)} to merger...")
            merger.append(pdf_file)
        else:
            print(f"Warning: {pdf_file} not found, skipping...")
    
    try:
        print(f"Writing merged PDF to {os.path.basename(output_path)}...")
        merger.write(output_path)
        merger.close()
        print(f"Successfully merged PDFs to {output_path}")
        return True
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        merger.close()
        return False

def main():
    """Main function to convert all EIA markdown files to PDF and merge them."""
    # Define the EIA directory path
    eia_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
    
    # Get all markdown files in the directory (sorted by filename)
    md_files = []
    for filename in sorted(os.listdir(eia_dir)):
        if filename.endswith('.md'):
            md_files.append(os.path.join(eia_dir, filename))
    
    if not md_files:
        print("No markdown files found in the EIA directory.")
        return
    
    print(f"Found {len(md_files)} markdown files:")
    for md_file in md_files:
        print(f"  - {os.path.basename(md_file)}")
    
    # Convert each markdown file to PDF
    pdf_files = []
    print("\nConverting markdown files to PDF...")
    
    for i, md_file in enumerate(md_files):
        # Create PDF filename based on markdown filename
        pdf_filename = md_file.replace('.md', '.pdf')
        pdf_files.append(pdf_filename)
        
        # Convert markdown to PDF
        if not convert_markdown_to_pdf(md_file, pdf_filename):
            print(f"Failed to convert {md_file} to PDF. Skipping...")
            # Remove from list so we don't try to merge it
            if pdf_filename in pdf_files:
                pdf_files.remove(pdf_filename)
    
    if not pdf_files:
        print("No PDF files were successfully created.")
        return
    
    # Merge all PDF files into one
    output_pdf = os.path.join(eia_dir, "EIA_Documents_Combined.pdf")
    print(f"\nMerging {len(pdf_files)} PDF files into {os.path.basename(output_pdf)}...")
    
    if merge_pdfs(pdf_files, output_pdf):
        print("\nPDF conversion and merging completed successfully!")
        print(f"Final combined PDF: {output_pdf}")
        
        # Show file size
        if os.path.exists(output_pdf):
            size_mb = os.path.getsize(output_pdf) / (1024*1024)
            print(f"File size: {size_mb:.1f} MB")
        
        # Optionally, clean up individual PDF files
        print("\nDo you want to delete the individual PDF files? (y/N): n")
        # For automation, we'll skip the cleanup prompt and just inform the user
        print("Individual PDF files are kept in the directory.")
        print("You can manually delete them if needed.")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()