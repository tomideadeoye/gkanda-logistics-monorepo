#!/usr/bin/env python3

import fitz  # PyMuPDF
import os

def verify_images_in_pdf(pdf_path):
    """Verify that images are present in the PDF"""
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return False
    
    try:
        # Open the PDF
        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        print(f"PDF has {total_pages} pages")
        
        # Check each page for images
        images_found = 0
        for page_num in range(total_pages):
            page = doc[page_num]
            image_list = page.get_images()
            
            if image_list:
                print(f"Page {page_num + 1}: Found {len(image_list)} image(s)")
                images_found += len(image_list)
            else:
                print(f"Page {page_num + 1}: No images found")
        
        doc.close()
        
        print(f"\nTotal images found in PDF: {images_found}")
        
        if images_found > 0:
            print("✅ SUCCESS: Images are present in the PDF")
            return True
        else:
            print("❌ WARNING: No images found in the PDF")
            return False
            
    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        return False

def main():
    """Main function to verify images in the generated PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Check the latest generated PDF
    pdf_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_With_Screenshots.pdf")
    
    print("Verifying images in PDF document...")
    print(f"Checking file: {pdf_file}")
    
    if verify_images_in_pdf(pdf_file):
        print("\n🎉 The PDF document contains properly rendered images!")
        print("The Mermaid diagrams should now be visible as images instead of raw code.")
    else:
        print("\n⚠️  The PDF document may not contain properly rendered images.")
        print("You may need to check the conversion process or install additional dependencies.")

if __name__ == "__main__":
    main()