#!/usr/bin/env python3

import os
import pypandoc
from weasyprint import HTML
from PyPDF2 import PdfMerger

def convert_md_to_pdf(md_file_path, pdf_output_path):
    """Convert Markdown file to PDF"""
    print(f"Converting {md_file_path} to PDF...")
    # Convert markdown to HTML first with mermaid support
    html_content = pypandoc.convert_file(md_file_path, 'html', extra_args=[
        '--embed-resources',
        '--standalone',
        '--mathjax'
    ])

    # Add mermaid script and CSS to HTML
    mermaid_css = '''
    <style>
        .mermaid {
            text-align: center;
            margin: 20px 0;
        }
    </style>
    '''

    mermaid_script = '''
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            mermaid.initialize({
                startOnLoad: true,
                theme: 'default',
                securityLevel: 'loose',
                fontFamily: 'arial',
                flowchart: {
                    useMaxWidth: false,
                    htmlLabels: true,
                    curve: 'basis'
                }
            });

            // Force render all mermaid diagrams
            setTimeout(function() {
                const diagrams = document.querySelectorAll('.mermaid');
                diagrams.forEach(function(diagram) {
                    if (diagram.innerHTML.includes('graph TD') || diagram.innerHTML.includes('flowchart TD')) {
                        mermaid.init(undefined, diagram);
                    }
                });
            }, 1000);
        });
    </script>
    '''

    html_content = html_content.replace('<style>', mermaid_css + '<style>')
    html_content = html_content.replace('</head>', mermaid_script + '</head>')

    # Write HTML to temporary file
    temp_html = md_file_path.replace('.md', '_temp.html')
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Convert HTML to PDF with proper rendering time
    import time
    time.sleep(2)  # Give time for JavaScript to execute

    HTML(temp_html).write_pdf(pdf_output_path)

    # Clean up temp file
    os.remove(temp_html)
    print(f"Successfully converted {md_file_path} to {pdf_output_path}")

def convert_html_to_pdf(html_file_path, pdf_output_path):
    """Convert HTML file to PDF"""
    print(f"Converting {html_file_path} to PDF...")
    HTML(html_file_path).write_pdf(pdf_output_path)
    print(f"Successfully converted {html_file_path} to {pdf_output_path}")

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
    
    # Convert Markdown to PDF
    convert_md_to_pdf(md_file, md_pdf)
    
    # Convert HTML to PDF
    convert_html_to_pdf(html_file, html_pdf)
    
    # Merge PDFs (cover page first, then handbook)
    merge_pdfs([html_pdf, md_pdf], final_pdf)
    
    print("All conversions and merging completed successfully!")
    print(f"Final combined PDF: {final_pdf}")

if __name__ == "__main__":
    main()