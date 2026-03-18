#!/usr/bin/env python3

import os
import subprocess
import tempfile
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_mermaid(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using Node.js with Mermaid CLI for proper diagram rendering"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF with Mermaid CLI...")

    # Create temporary directory for processing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Step 1: Use Mermaid CLI to convert markdown to HTML with diagrams
        temp_html = os.path.join(temp_dir, "temp.html")

        # Use mermaid CLI to process the markdown
        cmd = [
            "npx",
            "@mermaid-js/mermaid-cli",
            "--input", md_file_path,
            "--output", temp_html,
            "--configFile", "mermaid-config.json",
            "--cssFile", "improved_styling.css",
            "--pdfFit"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(md_file_path))
            if result.returncode != 0:
                print(f"Mermaid CLI failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error running Mermaid CLI: {e}")
            return False

        # Step 2: Convert HTML to PDF using weasyprint
        try:
            from weasyprint import HTML
            HTML(temp_html).write_pdf(pdf_output_path)
            print(f"Successfully converted {os.path.basename(md_file_path)} to PDF")
            return True
        except Exception as e:
            print(f"Error converting HTML to PDF: {e}")
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

    # Input Markdown file with Mermaid diagrams
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets.md")

    # Cover page PDF
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")

    # Temporary handbook PDF
    handbook_pdf = os.path.join(base_dir, "temp_handbook_mermaid.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_With_Mermaid_Diagrams.pdf")

    # Step 1: Convert Markdown to PDF with Mermaid CLI
    print("Step 1: Converting Markdown to PDF with Mermaid CLI...")
    if convert_md_to_pdf_with_mermaid(md_file, handbook_pdf):
        print("PDF conversion successful!")
    else:
        print("Failed to convert to PDF")
        return

    # Check if handbook PDF was created
    if os.path.exists(handbook_pdf):
        print(f"Handbook PDF exists: {handbook_pdf}")
    else:
        print(f"Handbook PDF not found: {handbook_pdf}")
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
    print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")

if __name__ == "__main__":
    main()