#!/usr/bin/env python3

import os
import markdown
from weasyprint import HTML, CSS
from PyPDF2 import PdfMerger

def convert_md_to_html(md_file_path):
    """Convert Markdown file to HTML string"""
    print(f"Converting {md_file_path} to HTML...")
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Wrap in basic HTML structure
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>ESMS Handbook</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2, h3, h4, h5, h6 {{ color: #333; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    return full_html

def save_html(html_content, output_path):
    """Save HTML content to file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML saved to {output_path}")

def convert_html_to_pdf(html_file_path, pdf_output_path):
    """Convert HTML file to PDF"""
    print(f"Converting {html_file_path} to PDF...")
    HTML(html_file_path).write_pdf(pdf_output_path)
    print(f"Successfully converted {html_file_path} to {pdf_output_path}")

def convert_md_to_pdf_via_html(md_file_path, pdf_output_path):
    """Convert Markdown to PDF via HTML"""
    # First convert MD to HTML
    html_content = convert_md_to_html(md_file_path)
    temp_html_path = md_file_path.replace('.md', '_temp.html')
    save_html(html_content, temp_html_path)
    
    # Then convert HTML to PDF
    convert_html_to_pdf(temp_html_path, pdf_output_path)
    
    # Clean up temp HTML file
    os.remove(temp_html_path)
    print(f"Removed temporary HTML file {temp_html_path}")

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one"""
    print(f"Merging PDFs: {pdf_files}")
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        print(f"Adding {pdf_file} to merger...")
        merger.append(pdf_file)
    
    print(f"Writing merged PDF to {output_path}...")
    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs to {output_path}")

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Files to convert
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    html_file = os.path.join(base_dir, "ESMS_Cover_Page.html")
    
    # Output PDF files
    md_pdf = os.path.join(base_dir, "ESMS_Handbook.pdf")
    html_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced_with_Cover.pdf")
    
    # Convert HTML cover page to PDF
    convert_html_to_pdf(html_file, html_pdf)
    
    # Convert Markdown handbook to PDF via HTML
    convert_md_to_pdf_via_html(md_file, md_pdf)
    
    # Merge PDFs (cover page first, then handbook)
    merge_pdfs([html_pdf, md_pdf], final_pdf)
    
    print("All conversions and merging completed successfully!")
    print(f"Final combined PDF: {final_pdf}")

if __name__ == "__main__":
    main()