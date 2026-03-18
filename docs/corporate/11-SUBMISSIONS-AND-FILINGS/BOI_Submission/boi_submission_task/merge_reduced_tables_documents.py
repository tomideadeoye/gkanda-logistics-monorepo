import os
from PyPDF2 import PdfMerger

def merge_emergency_response_documents():
    print("Merging Emergency Response Plan documents with reduced tables...")
    
    # Define file paths
    cover_pdf = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/Emergency_Response_Plan_HTML_Cover_Puppeteer.pdf"
    content_pdf = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Reduced_Tables.pdf"
    output_pdf = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Final_Reduced_Tables.pdf"
    
    # Check if files exist
    if not os.path.exists(cover_pdf):
        print(f"Error: Cover PDF not found at {cover_pdf}")
        return
        
    if not os.path.exists(content_pdf):
        print(f"Error: Content PDF not found at {content_pdf}")
        return
    
    # Create PDF merger object
    merger = PdfMerger()
    
    # Merge PDFs
    print("Adding cover page...")
    merger.append(cover_pdf)
    
    print("Adding content...")
    merger.append(content_pdf)
    
    # Write merged PDF
    print(f"Writing final merged PDF to {output_pdf}...")
    merger.write(output_pdf)
    merger.close()
    
    # Check file size
    if os.path.exists(output_pdf):
        file_size = os.path.getsize(output_pdf)
        size_mb = file_size / (1024 * 1024)
        print(f"File size: {size_mb:.1f} MB")
    
    print("Emergency Response Plan documents with reduced tables merged successfully!")

if __name__ == "__main__":
    merge_emergency_response_documents()