#!/usr/bin/env python3

import fitz  # PyMuPDF
import os

def check_pdf_content(pdf_path):
    """Check if PDF contains images or raw mermaid code"""
    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF file not found: {pdf_path}")
        return

    doc = fitz.open(pdf_path)
    print(f"PDF has {len(doc)} pages")

    mermaid_found = False
    images_found = False
    total_images = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)
        text = page.get_text()

        total_images += len(images)

        if 'graph TD' in text or '```mermaid' in text or 'mermaid' in text.lower():
            print(f"WARNING: Found raw mermaid code on page {page_num + 1}")
            mermaid_found = True

        if images:
            images_found = True
            print(f"Page {page_num + 1}: {len(images)} images")
            # Show image details
            for img in images[:2]:  # Show first 2 images per page
                print(f"  Image: {img[7] if len(img) > 7 else 'unnamed'}")

    doc.close()

    print("\nSUMMARY:")
    print(f"- Total images: {total_images}")
    print(f"- Raw mermaid code: {'FOUND' if mermaid_found else 'NOT FOUND'}")
    print(f"- Images present: {'YES' if images_found else 'NO'}")

    if mermaid_found:
        print("\n❌ ISSUE: PDF contains raw mermaid code instead of rendered diagrams")
    elif images_found:
        print("\n✅ GOOD: PDF contains images (likely rendered diagrams)")
    else:
        print("\n⚠️  WARNING: No images found in PDF")

if __name__ == "__main__":
    pdf_path = "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete_Pypandoc.pdf"
    check_pdf_content(pdf_path)