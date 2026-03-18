#!/usr/bin/env python3

import os
import pypandoc
import subprocess
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_pypandoc(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using pypandoc"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using pypandoc...")

    try:
        # Use pypandoc to convert markdown to PDF
        pypandoc.convert_file(
            md_file_path,
            'pdf',
            outputfile=pdf_output_path,
            extra_args=[
                '--pdf-engine=pdflatex',  # Use pdflatex instead of weasyprint
                '--standalone',
                '--toc',
                '--toc-depth=2'
            ]
        )

        print(f"Successfully converted {os.path.basename(md_file_path)} to {os.path.basename(pdf_output_path)}")
        return True
    except Exception as e:
        print(f"Error during pypandoc conversion: {e}")
        return False

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one using PyPDF2"""
    print(f"Merging PDFs: {[os.path.basename(f) for f in pdf_files]}")

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

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"

    # Input Markdown file (the manually edited version)
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")

    # Cover page PDF
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")

    # Temporary handbook PDF
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_Manual_Edit_temp.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Manual_Edit_Final.pdf")

    # Step 1: Convert Markdown to PDF
    print("Step 1: Converting manually edited Markdown to PDF...")
    if convert_md_to_pdf_with_pypandoc(md_file, handbook_pdf):
        print("Handbook PDF created successfully!")
    else:
        print("Failed to create handbook PDF")
        return

    # Step 2: Merge with cover page
    print("\nStep 2: Merging with cover page...")
    merge_pdfs([cover_pdf, handbook_pdf], final_pdf)

    # Clean up temporary file
    if os.path.exists(handbook_pdf):
        os.remove(handbook_pdf)
        print(f"Cleaned up temporary file: {handbook_pdf}")

    print("\nConversion and merging completed successfully!")
    print(f"Final combined PDF: {final_pdf}")
    if os.path.exists(final_pdf):
        file_size = os.path.getsize(final_pdf) / (1024*1024)
        print(f"File size: {file_size:.1f} MB")

if __name__ == "__main__":
    main()