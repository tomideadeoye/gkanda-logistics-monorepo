#!/usr/bin/env python3

import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one"""
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
    
    # Files to merge (cover page first, then handbook)
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Use the enhanced handbook with proper diagram support
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_with_Diagrams.pdf")
    
    # If the enhanced handbook doesn't exist, fall back to the original
    if not os.path.exists(handbook_pdf):
        handbook_pdf = os.path.join(base_dir, "ESMS_Handbook.pdf")
        print("Enhanced handbook not found, using original handbook PDF")
    
    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final.pdf")
    
    # Merge PDFs (cover page first, then handbook)
    merge_pdfs([cover_pdf, handbook_pdf], final_pdf)
    
    print("PDF merging completed successfully!")
    print(f"Final combined PDF: {final_pdf}")
    print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")

if __name__ == "__main__":
    main()