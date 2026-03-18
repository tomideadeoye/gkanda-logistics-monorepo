#!/usr/bin/env python3

import os
import asyncio
import subprocess
from pyppeteer import launch
from PyPDF2 import PdfMerger

async def convert_md_to_pdf_with_puppeteer(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using Puppeteer with Mermaid support"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using Puppeteer...")

    # Read markdown content
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Create HTML content with Mermaid support
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>ESMS Handbook</title>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{
                startOnLoad: true,
                theme: 'default',
                securityLevel: 'loose',
                fontFamily: 'arial',
                fontSize: 14
            }});
        </script>
        <style>
            body {{
                font-family: 'Times New Roman', serif;
                font-size: 12pt;
                line-height: 1.4;
                margin: 0.5in;
                padding: 0;
                color: #333;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #2c3e50;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
                page-break-after: avoid;
            }}
            h1 {{ font-size: 24pt; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }}
            h2 {{ font-size: 18pt; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }}
            h3 {{ font-size: 14pt; }}
            p {{ margin: 0.5em 0; text-align: justify; }}
            ul, ol {{ margin: 0.5em 0; padding-left: 1.5em; }}
            li {{ margin: 0.2em 0; }}
            .mermaid {{
                text-align: center;
                margin: 1em 0;
                page-break-inside: avoid;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1em 0;
                page-break-inside: avoid;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }}
            th {{ background-color: #f2f2f2; font-weight: bold; }}
            .toc {{ page-break-before: always; }}
            @page {{
                size: A4;
                margin: 0.5in;
            }}
            @media print {{
                body {{ margin: 0; }}
                .no-print {{ display: none; }}
            }}
        </style>
    </head>
    <body>
        <div id="content">
    """

    # Convert markdown to basic HTML (simple conversion)
    import re

    # Headers
    html_content += re.sub(r'^# (.+)$', r'<h1>\1</h1>', md_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)

    # Bold and italic
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_content)

    # Lists
    html_content = re.sub(r'^- (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'(?m)^(\d+)\. (.+)$', r'<li>\2</li>', html_content)

    # Group consecutive list items
    html_content = re.sub(r'(<li>.*?</li>\s*)+', r'<ul>\n\1\n</ul>', html_content, flags=re.DOTALL)

    # Mermaid diagrams
    html_content = re.sub(r'```mermaid\s*(.*?)\s*```', r'<div class="mermaid">\1</div>', html_content, flags=re.DOTALL)

    # Images
    html_content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" style="max-width: 100%; height: auto;">', html_content)

    # Links
    html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)

    # Paragraphs
    lines = html_content.split('\n')
    html_lines = []
    for line in lines:
        if line.strip() and not line.startswith('<') and not line.startswith('```'):
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append(line)

    html_content = '\n'.join(html_lines)

    # Close HTML
    html_content += """
        </div>
    </body>
    </html>
    """

    # Save HTML to temporary file
    temp_html = os.path.join(os.path.dirname(pdf_output_path), "temp_handbook.html")
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    try:
        # Launch browser and convert to PDF
        browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
        page = await browser.newPage()

        await page.setViewport({'width': 1200, 'height': 800})
        await page.goto(f'file://{os.path.abspath(temp_html)}')

        # Wait for mermaid to render
        await page.waitForSelector('.mermaid', timeout=10000)
        await asyncio.sleep(3)  # Give extra time for rendering

        # Generate PDF
        await page.pdf({
            'path': pdf_output_path,
            'format': 'A4',
            'margin': {
                'top': '0.5in',
                'right': '0.5in',
                'bottom': '0.5in',
                'left': '0.5in'
            },
            'printBackground': True
        })

        await browser.close()

        # Clean up
        if os.path.exists(temp_html):
            os.remove(temp_html)

        print(f"Successfully converted {os.path.basename(md_file_path)} to PDF")
        return True

    except Exception as e:
        print(f"Error during Puppeteer conversion: {e}")
        if os.path.exists(temp_html):
            os.remove(temp_html)
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

    # Temporary handbook PDF
    handbook_pdf = os.path.join(base_dir, "temp_handbook_puppeteer.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_Puppeteer.pdf")

    # Step 1: Convert Markdown to PDF with Puppeteer
    print("Step 1: Converting Markdown to PDF with Puppeteer...")
    success = asyncio.run(convert_md_to_pdf_with_puppeteer(md_file, handbook_pdf))

    if success:
        print("PDF conversion successful!")
    else:
        print("Failed to convert to PDF")
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