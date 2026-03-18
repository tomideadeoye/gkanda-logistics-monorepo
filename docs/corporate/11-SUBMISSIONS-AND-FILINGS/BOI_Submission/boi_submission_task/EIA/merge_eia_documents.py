#!/usr/bin/env python3
"""
Convert all EIA markdown documents to PDF and merge them into a single PDF file.
"""

import os
import subprocess
from PyPDF2 import PdfMerger

def convert_markdown_to_pdf(input_md, output_pdf):
    """
    Convert markdown to PDF using weasyprint with proper styling.
    
    Args:
        input_md (str): Path to input markdown file
        output_pdf (str): Path to output PDF file
    """
    try:
        # First convert markdown to HTML
        html_file = output_pdf.replace('.pdf', '.html')
        
        # Command to convert markdown to HTML with styling
        cmd1 = [
            'pandoc',
            input_md,
            '-o', html_file,
            '--standalone'
        ]
        
        result1 = subprocess.run(cmd1, capture_output=True, text=True, cwd=os.path.dirname(input_md) or '.')
        
        if result1.returncode != 0:
            print(f"Error converting markdown to HTML: {result1.stderr}")
            return False
        
        # Command to convert HTML to PDF using weasyprint
        cmd2 = [
            'weasyprint',
            html_file,
            output_pdf
        ]
        
        result2 = subprocess.run(cmd2, capture_output=True, text=True, cwd=os.path.dirname(input_md) or '.')
        
        if result2.returncode == 0:
            print(f"Successfully converted {os.path.basename(input_md)} to {os.path.basename(output_pdf)}")
            # Clean up temporary HTML file
            if os.path.exists(html_file):
                os.remove(html_file)
            return True
        else:
            print(f"Error converting HTML to PDF: {result2.stderr}")
            return False
            
    except Exception as e:
        print(f"Error: {e}")
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
            merger.close()
            return False
    
    print(f"Writing merged PDF to {os.path.basename(output_path)}...")
    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs to {output_path}")
    return True

def main():
    """Main function to convert all EIA markdown files to PDF and merge them."""
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