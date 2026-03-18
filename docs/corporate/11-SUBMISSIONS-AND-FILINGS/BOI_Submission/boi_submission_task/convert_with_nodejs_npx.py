#!/usr/bin/env python3

import os
import subprocess
import tempfile
from PyPDF2 import PdfMerger

def convert_md_to_pdf_with_nodejs_npx(md_file_path, pdf_output_path):
    """Convert Markdown to PDF using Node.js and npx puppeteer"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF using Node.js with npx...")

    # Create a Node.js script for conversion
    node_script = """
    const puppeteer = require('puppeteer');
    const fs = require('fs');
    const path = require('path');

    async function convertToPDF(inputPath, outputPath) {
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });

        const page = await browser.newPage();
        await page.setViewport({ width: 1200, height: 800 });

        // Read markdown and convert to HTML
        const mdContent = fs.readFileSync(inputPath, 'utf8');

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

        const fullHTML = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ESMS Handbook</title>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({
                    startOnLoad: true,
                    theme: 'default',
                    securityLevel: 'loose',
                    fontFamily: 'arial',
                    fontSize: 14
                });
            </script>
            <style>
                body {
                    font-family: 'Times New Roman', serif;
                    font-size: 12pt;
                    line-height: 1.4;
                    margin: 0.5in;
                    padding: 0;
                    color: #333;
                }
                h1, h2, h3, h4, h5, h6 {
                    color: #2c3e50;
                    margin-top: 1.5em;
                    margin-bottom: 0.5em;
                    page-break-after: avoid;
                }
                h1 { font-size: 24pt; border-bottom: 2px solid #3498db; padding-bottom: 0.3em; }
                h2 { font-size: 18pt; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.2em; }
                h3 { font-size: 14pt; }
                p { margin: 0.5em 0; text-align: justify; }
                ul, ol { margin: 0.5em 0; padding-left: 1.5em; }
                li { margin: 0.2em 0; }
                .mermaid {
                    text-align: center;
                    margin: 1em 0;
                    page-break-inside: avoid;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 1em 0;
                    page-break-inside: avoid;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th { background-color: #f2f2f2; font-weight: bold; }
                .toc { page-break-before: always; }
                @page {
                    size: A4;
                    margin: 0.5in;
                }
                @media print {
                    body { margin: 0; }
                    .no-print { display: none; }
                }
            </style>
        </head>
        <body>
            <div id="content">
                ${htmlContent}
            </div>
        </body>
        </html>`;

        await page.setContent(fullHTML, { waitUntil: 'networkidle0' });

        // Wait for mermaid to render
        try {
            await page.waitForSelector('.mermaid', { timeout: 10000 });
            await new Promise(resolve => setTimeout(resolve, 3000)); // Extra time for rendering
        } catch (e) {
            console.log('No mermaid diagrams found or timeout waiting for them');
        }

        // Generate PDF
        await page.pdf({
            path: outputPath,
            format: 'A4',
            margin: {
                top: '0.5in',
                right: '0.5in',
                bottom: '0.5in',
                left: '0.5in'
            },
            printBackground: true
        });

        await browser.close();
        console.log('PDF conversion completed successfully');
    }

    // Get command line arguments
    const inputPath = process.argv[2];
    const outputPath = process.argv[3];

    convertToPDF(inputPath, outputPath).catch(console.error);
    """

    # Save Node.js script to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(node_script)
        script_path = f.name

    try:
        # Run Node.js script with npx
        cmd = ['npx', 'puppeteer', script_path, md_file_path, pdf_output_path]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(md_file_path))

        if result.returncode == 0:
            print(f"Successfully converted {os.path.basename(md_file_path)} to PDF")
            return True
        else:
            print(f"Node.js npx conversion failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"Error during Node.js npx conversion: {e}")
        return False

    finally:
        # Clean up script file
        if os.path.exists(script_path):
            os.unlink(script_path)

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
    handbook_pdf = os.path.join(base_dir, "temp_handbook_nodejs_npx.pdf")

    # Final merged output
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_ESMS_Handbook_NodeJS_NPX.pdf")

    # Step 1: Convert Markdown to PDF with Node.js npx
    print("Step 1: Converting Markdown to PDF with Node.js npx...")
    if convert_md_to_pdf_with_nodejs_npx(md_file, handbook_pdf):
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