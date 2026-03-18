#!/usr/bin/env python3

import os
from PyPDF2 import PdfReader
import fitz  # PyMuPDF

def verify_image_centering_in_pdf(pdf_path):
    """Verify image centering in a PDF file"""
    print(f"Verifying image centering in: {pdf_path}")
    
    if not os.path.exists(pdf_path):
        print(f"PDF file not found: {pdf_path}")
        return False
    
    try:
        # Open the PDF with PyMuPDF for better image analysis
        doc = fitz.open(pdf_path)
        
        print(f"PDF has {doc.page_count} pages")
        
        # Check a few pages for images
        pages_to_check = min(5, doc.page_count)
        centered_images = 0
        total_images = 0
        
        for page_num in range(pages_to_check):
            page = doc[page_num]
            images = page.get_images()
            
            if images:
                print(f"Page {page_num + 1}: Found {len(images)} images")
                total_images += len(images)
                
                # Get page dimensions
                page_rect = page.rect
                page_width = page_rect.width
                page_height = page_rect.height
                
                print(f"  Page dimensions: {page_width:.1f} x {page_height:.1f} points")
                
                # Check each image
                for img_index, img in enumerate(images):
                    # Get image bounding box
                    img_info = page.get_image_bbox(img)
                    if img_info:
                        img_x0, img_y0, img_x1, img_y1 = img_info
                        img_width = img_x1 - img_x0
                        img_height = img_y1 - img_y0
                        
                        # Calculate centering
                        page_center = page_width / 2
                        img_center = img_x0 + (img_width / 2)
                        offset_from_center = abs(img_center - page_center)
                        
                        # Consider centered if within 20 points of center
                        is_centered = offset_from_center < 20
                        
                        print(f"  Image {img_index + 1}: {img_width:.1f} x {img_height:.1f} points")
                        print(f"    Position: ({img_x0:.1f}, {img_y0:.1f}) to ({img_x1:.1f}, {img_y1:.1f})")
                        print(f"    Center offset: {offset_from_center:.1f} points ({'Centered' if is_centered else 'Not Centered'})")
                        
                        if is_centered:
                            centered_images += 1
            else:
                print(f"Page {page_num + 1}: No images found")
        
        doc.close()
        
        if total_images > 0:
            centering_percentage = (centered_images / total_images) * 100
            print(f"\nImage Centering Summary:")
            print(f"  Total images checked: {total_images}")
            print(f"  Centered images: {centered_images}")
            print(f"  Centering success rate: {centering_percentage:.1f}%")
            
            if centering_percentage >= 75:
                print("  RESULT: Good image centering achieved!")
                return True
            else:
                print("  RESULT: Image centering needs improvement.")
                return False
        else:
            print("No images found in the PDF to verify.")
            return False
            
    except Exception as e:
        print(f"Error analyzing PDF: {e}")
        return False

def main():
    """Main function to verify image centering in all generated PDFs"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # List of PDFs to check
    pdfs_to_check = [
        "ESMS_Handbook_With_Precise_Images.pdf",
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Precise.pdf",
        "ESMS_Handbook_With_Improved_Centering.pdf",
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf",
        "ESMS_Handbook_With_Exact_Centering.pdf",
        "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf"
    ]
    
    print("IMAGE CENTERING VERIFICATION REPORT")
    print("=" * 50)
    
    for pdf_name in pdfs_to_check:
        pdf_path = os.path.join(base_dir, pdf_name)
        if os.path.exists(pdf_path):
            print(f"\nChecking: {pdf_name}")
            verify_image_centering_in_pdf(pdf_path)
            print("-" * 30)
        else:
            print(f"\nSkipping (file not found): {pdf_name}")

if __name__ == "__main__":
    main()