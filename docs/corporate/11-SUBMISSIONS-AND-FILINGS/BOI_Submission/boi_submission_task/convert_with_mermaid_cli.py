#!/usr/bin/env python3

import os
import subprocess
import tempfile
from PyPDF2 import PdfMerger

def convert_md_to_html_with_mermaid(md_file_path, html_output_path):
    """Convert Markdown to HTML with Mermaid CLI"""
    print(f"Converting {os.path.basename(md_file_path)} to HTML with Mermaid CLI...")

    try:
        # Use mermaid CLI to convert markdown to HTML
        cmd = [
            "npx",
            "@mermaid-js/mermaid-cli",
            "--input", md_file_path,
            "--output", html_output_path,
            "--configFile", "mermaid-config.json",
            "--cssFile", "best_centering_style.css",
            "--pdfFit"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(md_file_path))

        if result.returncode == 0:
            print(f"Successfully converted {os.path.basename(md_file_path)} to HTML")
            return True
        else:
            print(f"Mermaid CLI conversion failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"Error during Mermaid CLI conversion: {e}")
        return False

def convert_html_to_pdf(html_file_path, pdf_output_path):
    """Convert HTML to PDF using weasyprint"""
    print(f"Converting {os.path.basename(html_file_path)} to PDF...")

    try:
        # Use weasyprint to convert HTML to PDF
        cmd = [
            "weasyprint",
            html_file_path,
            pdf_output_path
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Successfully converted {os.path.basename(html_file_path)} to PDF")
            return True
        else:
            print(f"WeasyPrint conversion failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"Error during WeasyPrint conversion: {e}")
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

    # Input Markdown file
    md_file = os.path.join(base_dir, "ESMS_Handbook_Final_Fixed_Version.md")

    # Cover page PDF
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")

    # Temporary files
    temp_html = os.path.join(base_dir, "temp_handbook.html")
    handbook_pdf = os.path.join(base_dir, "temp_handbook.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_Mermaid_CLI.pdf")

    # Step 1: Convert Markdown to HTML with Mermaid CLI
    print("Step 1: Converting Markdown to HTML with Mermaid CLI...")
    if convert_md_to_html_with_mermaid(md_file, temp_html):
        print("HTML conversion successful!")
    else:
        print("Failed to convert to HTML")
        return

    # Step 2: Convert HTML to PDF
    print("\nStep 2: Converting HTML to PDF...")
    if convert_html_to_pdf(temp_html, handbook_pdf):
        print("PDF conversion successful!")
    else:
        print("Failed to convert to PDF")
        return

    # Step 3: Merge with cover page
    print("\nStep 3: Merging with cover page...")
    merge_pdfs([cover_pdf, handbook_pdf], final_pdf)

    # Clean up temporary files
    for temp_file in [temp_html, handbook_pdf]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Cleaned up temporary file: {temp_file}")

    print("\nConversion and merging completed successfully!")
    print(f"Final combined PDF: {final_pdf}")
    print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")

if __name__ == "__main__":
    main()