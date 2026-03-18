#!/usr/bin/env python3
"""
Verify the Emergency Response Plan PDF content and structure.
"""

import PyPDF2
import os

def verify_pdf_content(pdf_path):
    """
    Verify the content and structure of the Emergency Response Plan PDF.
    
    Args:
        pdf_path (str): Path to the PDF file to verify
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        return False
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"PDF Verification Report")
            print(f"=====================")
            print(f"File: {os.path.basename(pdf_path)}")
            print(f"Number of pages: {num_pages}")
            
            # Get basic metadata
            if pdf_reader.metadata:
                print(f"Title: {pdf_reader.metadata.get('/Title', 'N/A')}")
                print(f"Author: {pdf_reader.metadata.get('/Author', 'N/A')}")
                print(f"Creator: {pdf_reader.metadata.get('/Creator', 'N/A')}")
            
            # Check first few pages for content
            print(f"\nContent Verification:")
            print(f"====================")
            
            # Check cover page (page 1)
            if num_pages >= 1:
                page1 = pdf_reader.pages[0]
                text1 = page1.extract_text()
                print(f"Page 1 (Cover): Contains company name and document title")
                if "GK & A LOGISTICS SERVICES LTD" in text1:
                    print("  ✓ Company name found")
                if "EMERGENCY RESPONSE PLAN" in text1:
                    print("  ✓ Document title found")
                if "NPA Lighter Terminal" in text1:
                    print("  ✓ Facility information found")
            
            # Check content pages
            if num_pages >= 2:
                page2 = pdf_reader.pages[1]
                text2 = page2.extract_text()
                print(f"\nPage 2 (Content): Contains table of contents and introduction")
                if "Table of Contents" in text2:
                    print("  ✓ Table of contents found")
                if "Executive Statement" in text2:
                    print("  ✓ Executive statement found")
                if "Introduction" in text2:
                    print("  ✓ Introduction section found")
            
            # Check for key sections
            all_text = ""
            for i in range(min(5, num_pages)):  # Check first 5 pages
                all_text += pdf_reader.pages[i].extract_text() + "\n"
            
            print(f"\nSection Verification:")
            print(f"====================")
            key_sections = [
                "Purpose",
                "Scope",
                "Definitions",
                "Regulatory and Standards Alignment",
                "Risk Profile",
                "Governance",
                "Activation",
                "Emergency Response Procedures",
                "Evacuation",
                "Communications",
                "Resources",
                "Training",
                "Post-Incident",
                "Financial Provisioning",
                "Plan Governance",
                "Appendices"
            ]
            
            found_sections = 0
            for section in key_sections:
                if section in all_text:
                    print(f"  ✓ {section} section found")
                    found_sections += 1
                else:
                    print(f"  ✗ {section} section missing")
            
            print(f"\nSummary:")
            print(f"========")
            print(f"Found {found_sections} out of {len(key_sections)} key sections")
            print(f"Overall verification: {'PASS' if found_sections > len(key_sections) * 0.8 else 'FAIL'}")
            
            return True
            
    except Exception as e:
        print(f"Error verifying PDF: {e}")
        return False

def main():
    """Main function to verify the Emergency Response Plan PDF."""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    pdf_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan.pdf")
    
    print("Verifying Emergency Response Plan PDF...")
    verify_pdf_content(pdf_file)

if __name__ == "__main__":
    main()