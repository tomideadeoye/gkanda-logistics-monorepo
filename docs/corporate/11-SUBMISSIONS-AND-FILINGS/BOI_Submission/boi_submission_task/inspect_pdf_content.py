#!/usr/bin/env python3

import fitz  # PyMuPDF
import os

def inspect_pdf_content(pdf_path):
    """Inspect the content of the PDF to verify diagram rendering"""
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return False
    
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        print(f"PDF Analysis: {os.path.basename(pdf_path)}")
        print(f"Total pages: {total_pages}")
        
        # Look for pages with diagrams
        diagram_pages = []
        
        for page_num in range(min(10, total_pages)):  # Check first 10 pages
            page = doc[page_num]
            text = page.get_text()
            
            # Check if this page contains diagram-related content
            if any(keyword in text.lower() for keyword in ['plan', 'do', 'check', 'act', 'elements', 'pdca']):
                diagram_pages.append(page_num + 1)
        
        print(f"\nPages that likely contain diagrams: {diagram_pages}")
        
        # Extract text from diagram pages to verify content
        for page_num in diagram_pages[:3]:  # Check first 3 diagram pages
            page = doc[page_num - 1]  # 0-indexed
            text = page.get_text()
            
            print(f"\n--- Page {page_num} Content Preview ---")
            lines = text.split('\n')
            for i, line in enumerate(lines[:15]):  # First 15 lines
                if line.strip():
                    print(f"{i+1:2d}: {line.strip()}")
            
            # Check for image references
            images = page.get_images()
            if images:
                print(f"    [Page {page_num} contains {len(images)} image(s)]")
        
        doc.close()
        
        print("\n" + "="*50)
        print("ANALYSIS COMPLETE")
        print("="*50)
        print("If the PDF contains properly rendered diagrams:")
        print("  - You should see visual elements where diagrams were placed")
        print("  - The text should NOT contain raw Mermaid code like 'graph TD'")
        print("  - Diagram content should be visible as proper flowcharts")
        
        return True
        
    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        return False

def main():
    """Main function to inspect PDF content"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Check the final generated PDF
    pdf_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final_Images.pdf")
    
    print("Inspecting PDF content for proper diagram rendering...")
    inspect_pdf_content(pdf_file)

if __name__ == "__main__":
    main()