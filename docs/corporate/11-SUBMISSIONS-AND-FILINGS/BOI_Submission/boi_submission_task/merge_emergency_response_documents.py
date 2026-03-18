#!/usr/bin/env python3
"""
Merge the HTML cover page PDF with the Emergency Response Plan content PDF.
"""

import os
from PyPDF2 import PdfMerger

def merge_emergency_response_pdfs():
    """
    Merge the HTML cover page PDF with the Emergency Response Plan content PDF.
    """
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Cover page PDF (the new HTML-based one with Puppeteer)
    cover_pdf = os.path.join(base_dir, "Emergency_Response_Plan_HTML_Cover_Puppeteer.pdf")
    
    # Emergency Response Plan content PDF (fixed version)
    content_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Fixed.pdf")
    
    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Final_Fixed.pdf")
    
    # Check if files exist
    if not os.path.exists(cover_pdf):
        print(f"Error: Cover PDF not found: {cover_pdf}")
        # Fallback to the ReportLab version
        cover_pdf = os.path.join(base_dir, "Emergency_Response_Plan_HTML_Cover.pdf")
        if not os.path.exists(cover_pdf):
            print(f"Error: Fallback cover PDF not found: {cover_pdf}")
            return False
        
    if not os.path.exists(content_pdf):
        print(f"Error: Content PDF not found: {content_pdf}")
        # Fallback to complete version
        content_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Complete.pdf")
        if not os.path.exists(content_pdf):
            print(f"Error: Complete content PDF not found: {content_pdf}")
            # Final fallback to original content
            content_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan.pdf")
            if not os.path.exists(content_pdf):
                print(f"Error: Original content PDF not found: {content_pdf}")
                return False
    
    try:
        # Merge PDFs
        print("Merging Emergency Response Plan documents...")
        print(f"Cover: {os.path.basename(cover_pdf)}")
        print(f"Content: {os.path.basename(content_pdf)}")
        
        merger = PdfMerger()
        
        # Add cover page first
        print("Adding cover page...")
        merger.append(cover_pdf)
        
        # Add content
        print("Adding content...")
        merger.append(content_pdf)
        
        # Write final PDF
        print(f"Writing final merged PDF to {os.path.basename(final_pdf)}...")
        merger.write(final_pdf)
        merger.close()
        
        print(f"Successfully merged PDFs to {final_pdf}")
        print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")
        return True
        
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return False

def main():
    """Main function to merge the emergency response documents."""
    print("Merging Emergency Response Plan documents...")
    if merge_emergency_response_pdfs():
        print("Emergency Response Plan documents merged successfully!")
    else:
        print("Failed to merge Emergency Response Plan documents")

if __name__ == "__main__":
    main()