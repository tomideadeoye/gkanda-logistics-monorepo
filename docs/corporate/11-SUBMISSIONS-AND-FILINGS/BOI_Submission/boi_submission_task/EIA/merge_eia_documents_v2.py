#!/usr/bin/env python3
"""
Convert all EIA markdown documents to PDF and merge them into a single PDF file.
This version uses markdown and ReportLab libraries.
"""

import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PyPDF2 import PdfMerger

def markdown_to_html(markdown_text):
    """Convert markdown text to HTML."""
    md = markdown.Markdown()
    return md.convert(markdown_text)

def html_to_pdf(html_content, output_pdf):
    """Convert HTML content to PDF using ReportLab."""
    try:
        # Create a PDF document
        doc = SimpleDocTemplate(output_pdf, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=18,
            spaceAfter=12
        )
        
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=6
        )
        
        # Parse HTML content and create PDF elements
        story = []
        
        # Simple approach: split by lines and convert to paragraphs
        lines = html_content.split('\n')
        for line in lines:
            if line.strip():
                if line.startswith('<h1>'):
                    text = line.replace('<h1>', '').replace('</h1>', '')
                    story.append(Paragraph(text, title_style))
                    story.append(Spacer(1, 12))
                elif line.startswith('<h2>'):
                    text = line.replace('<h2>', '').replace('</h2>', '')
                    story.append(Paragraph(text, heading_style))
                    story.append(Spacer(1, 12))
                elif line.startswith('<h3>'):
                    text = line.replace('<h3>', '').replace('</h3>', '')
                    story.append(Paragraph(text, heading_style))
                    story.append(Spacer(1, 12))
                elif line.startswith('<p>'):
                    text = line.replace('<p>', '').replace('</p>', '')
                    story.append(Paragraph(text, normal_style))
                    story.append(Spacer(1, 6))
                elif line.startswith('<li>'):
                    text = line.replace('<li>', '• ').replace('</li>', '')
                    story.append(Paragraph(text, normal_style))
                    story.append(Spacer(1, 6))
                else:
                    # Handle other content as regular paragraphs
                    if not line.startswith('<'):
                        story.append(Paragraph(line, normal_style))
                        story.append(Spacer(1, 6))
        
        # Build PDF
        doc.build(story)
        return True
    except Exception as e:
        print(f"Error converting HTML to PDF: {e}")
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
        
        # Convert markdown to HTML
        html_content = markdown_to_html(markdown_content)
        
        # Convert HTML to PDF
        if html_to_pdf(html_content, output_pdf):
            print(f"Successfully converted {os.path.basename(input_md)} to {os.path.basename(output_pdf)}")
            return True
        else:
            print(f"Failed to convert {os.path.basename(input_md)} to PDF")
            return False
            
    except Exception as e:
        print(f"Error converting {input_md} to PDF: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    """
    Merge multiple PDF files into one.
    
    Args:
        pdf_files (list): List of PDF file paths to merge
        output_path (str): Path where merged PDF should be saved
    """
    print(f"Merging {len(pdf_files)} PDFs...")
    
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            print(f"Adding {os.path.basename(pdf_file)} to merger...")
            merger.append(pdf_file)
        else:
            print(f"Warning: {pdf_file} not found, skipping...")
    
    print(f"Writing merged PDF to {os.path.basename(output_path)}...")
    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs to {output_path}")
    return True

def main():
    """Main function to convert all EIA markdown files to PDF and merge them."""
    # Import markdown library
    try:
        import markdown
    except ImportError:
        print("Error: markdown library not found. Please install it with: pip install markdown")
        return
    
    # Define the EIA directory path
    eia_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
    
    # Get all markdown files in the directory
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
            pdf_files.pop()
    
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
        cleanup = input("\nDo you want to delete the individual PDF files? (y/N): ")
        if cleanup.lower() == 'y':
            for pdf_file in pdf_files:
                if os.path.exists(pdf_file):
                    os.remove(pdf_file)
                    print(f"Deleted {os.path.basename(pdf_file)}")
            print("Individual PDF files cleaned up.")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()