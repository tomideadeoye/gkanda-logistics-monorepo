#!/usr/bin/env python3

import os
import subprocess
import tempfile
from weasyprint import HTML
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_mermaid(md_file_path, pdf_output_path):
    """Convert Markdown file to PDF with proper Mermaid diagram support"""
    print(f"Converting {md_file_path} to PDF with Mermaid support...")

    # Create temporary directory for processing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Step 1: Convert MD to HTML using pandoc with mermaid support
        temp_html = os.path.join(temp_dir, "temp.html")

        # Use pandoc to convert with mermaid support
        pandoc_cmd = [
            "pandoc",
            md_file_path,
            "-o", temp_html,
            "--standalone",
            "--mathjax",
            "-V", "mermaid-filter",
            "--css", "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css"
        ]

        try:
            subprocess.run(pandoc_cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Pandoc conversion failed: {e}")
            # Fallback method
            return convert_md_to_pdf_fallback(md_file_path, pdf_output_path)

        # Step 2: Process HTML to ensure mermaid diagrams render
        with open(temp_html, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Add mermaid initialization script
        mermaid_script = '''
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({ startOnLoad: true });
        </script>
        '''

        # Insert mermaid script before closing head tag
        if '</head>' in html_content:
            html_content = html_content.replace('</head>', mermaid_script + '</head>')
        else:
            html_content = html_content.replace('<html>', '<html><head>' + mermaid_script + '</head>')

        # Save updated HTML
        processed_html = os.path.join(temp_dir, "processed.html")
        with open(processed_html, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Step 3: Convert HTML to PDF with delay for JavaScript rendering
        HTML(processed_html).write_pdf(pdf_output_path)

        print(f"Successfully converted {md_file_path} to {pdf_output_path}")

def convert_md_to_pdf_fallback(md_file_path, pdf_output_path):
    """Fallback conversion method"""
    print("Using fallback conversion method...")

    # Simple conversion with basic styling
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Document</title>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .mermaid {{ text-align: center; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <div class="markdown-body">
    """

    # Read and convert markdown content
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Simple replacement for mermaid code blocks
    import re
    def replace_mermaid(match):
        return f'<div class="mermaid">{match.group(1)}</div>'

    html_content += re.sub(r'```mermaid\s*(.*?)\s*```', replace_mermaid, md_content, flags=re.DOTALL)

    html_content += """
        </div>
    </body>
    </html>
    """

    # Save to temporary file and convert
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html_content)
        temp_html = f.name

    try:
        HTML(temp_html).write_pdf(pdf_output_path)
        print(f"Successfully converted {md_file_path} to {pdf_output_path}")
    finally:
        os.unlink(temp_html)

def merge_pdfs(pdf_files, output_path):
    """Merge multiple PDF files into one"""
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
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets.md")

    # Cover page PDF
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")

    # Temporary handbook PDF
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets_temp.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_with_Fixed_Bullets_Final.pdf")

    # Step 1: Convert Markdown to PDF
    print("Step 1: Converting Markdown to PDF...")
    convert_md_to_pdf_with_mermaid(md_file, handbook_pdf)

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