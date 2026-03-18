#!/usr/bin/env python3

import os
import subprocess
import tempfile
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_nodejs_inline(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using Node.js inline script"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using Node.js inline...")

    # Read markdown content
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Escape quotes and newlines for the inline script
    escaped_md = md_content.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')

    # Create inline Node.js script
    inline_script = f'''
const puppeteer = require("puppeteer");
const fs = require("fs");

async function convertToPDF() {{
    console.log("Starting PDF conversion...");

    const browser = await puppeteer.launch({{
        headless: true,
        args: ["--no-sandbox", "--disable-setuid-sandbox"]
    }});

    const page = await browser.newPage();
    await page.setViewport({{ width: 1200, height: 800 }});

    // Markdown content
    const mdContent = "{escaped_md}";

    // Simple markdown to HTML conversion
    let htmlContent = mdContent
        .replace(/^# (.+)$/gm, '<h1>$1</h1>')
        .replace(/^## (.+)$/gm, '<h2>$1</h2>')
        .replace(/^### (.+)$/gm, '<h3>$1</h3>')
        .replace(/^#### (.+)$/gm, '<h4>$1</h4>')
        .replace(/^##### (.+)$/gm, '<h5>$1</h5>')
        .replace(/^###### (.+)$/gm, '<h6>$1</h6>')
        .replace(/\\*\\*([^\\*]+)\\*\\*/g, '<strong>$1</strong>')
        .replace(/\\*([^\\*]+)\\*/g, '<em>$1</em>')
        .replace(/^\\* (.+)$/gm, '<li>$1</li>')
        .replace(/^\\d+\\. (.+)$/gm, '<li>$1</li>')
        .replace(/(<li>.*?<\/li>\\s*)+/gs, '<ul>$1</ul>')
        .replace(/```mermaid\\s*([\\s\\S]*?)```/g, '<div class="mermaid">$1</div>')
        .replace(/!\\[([^\\]]*)\\]\\(([^)]+)\\)/g, '<img src="$2" alt="$1" style="max-width: 100%; height: auto;">')
        .replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g, '<a href="$2">$1</a>')
        .replace(/^([^<\\n].*)$/gm, '<p>$1</p>');

    console.log(`Converted to HTML: ${{htmlContent.length}} characters`);

    const fullHTML = `
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
                font-size: 11pt;
                line-height: 1.3;
                margin: 0.75in;
                padding: 0;
                color: #333;
            }}
            h1, h2, h3, h4, h5, h6 {{
                color: #2c3e50;
                margin-top: 1.2em;
                margin-bottom: 0.5em;
                page-break-after: avoid;
            }}
            h1 {{ font-size: 22pt; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }}
            h2 {{ font-size: 16pt; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }}
            h3 {{ font-size: 13pt; }}
            p {{ margin: 0.4em 0; text-align: justify; }}
            ul, ol {{ margin: 0.4em 0; padding-left: 1.2em; }}
            li {{ margin: 0.15em 0; }}
            .mermaid {{
                text-align: center;
                margin: 0.8em 0;
                page-break-inside: avoid;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 0.8em 0;
                page-break-inside: avoid;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 6px;
                text-align: left;
            }}
            th {{ background-color: #f2f2f2; font-weight: bold; }}
            .toc {{ page-break-before: always; }}
            @page {{
                size: A4;
                margin: 0.75in;
            }}
            @media print {{
                body {{ margin: 0; }}
                .no-print {{ display: none; }}
            }}
        </style>
    </head>
    <body>
        <div id="content">
            ${{htmlContent}}
        </div>
    </body>
    </html>`;

    console.log('Setting page content...');
    await page.setContent(fullHTML, {{ waitUntil: 'networkidle0' }});

    // Wait for mermaid to render
    try {{
        console.log('Waiting for mermaid diagrams...');
        await page.waitForSelector('.mermaid', {{ timeout: 10000 }});
        console.log('Found mermaid diagrams, waiting for rendering...');
        await new Promise(resolve => setTimeout(resolve, 3000)); // Extra time for rendering
    }} catch (e) {{
        console.log('No mermaid diagrams found or timeout waiting for them');
    }}

    console.log('Generating PDF...');
    // Generate PDF with better page handling
    await page.pdf({{
        path: '{pdf_output_path}',
        format: 'A4',
        margin: {{
            top: '0.75in',
            right: '0.75in',
            bottom: '0.75in',
            left: '0.75in'
        }},
        printBackground: true,
        preferCSSPageSize: true
    }});

    console.log('PDF generated, checking file...');
    const stats = fs.statSync('{pdf_output_path}');
    console.log(`PDF file size: ${{stats.size}} bytes`);

    await browser.close();
    console.log('PDF conversion completed successfully');
}}

convertToPDF().catch(console.error);
'''

    try:
        # Run inline Node.js script
        result = subprocess.run(['node', '-e', inline_script],
                              capture_output=True, text=True, cwd=os.path.dirname(md_file_path))

        print(f"Return code: {result.returncode}")
        print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")

        if result.returncode == 0 and os.path.exists(pdf_output_path):
            print(f"Successfully converted {os.path.basename(md_file_path)} to PDF")
            return True
        else:
            print(f"Node.js inline conversion failed")
            return False

    except Exception as e:
        print(f"Error during Node.js inline conversion: {e}")
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
    handbook_pdf = os.path.join(base_dir, "temp_handbook_nodejs_inline.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_Inline.pdf")

    # Step 1: Convert Markdown to PDF with Node.js inline
    print("Step 1: Converting Markdown to PDF with Node.js inline...")
    if convert_md_to_pdf_with_nodejs_inline(md_file, handbook_pdf):
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