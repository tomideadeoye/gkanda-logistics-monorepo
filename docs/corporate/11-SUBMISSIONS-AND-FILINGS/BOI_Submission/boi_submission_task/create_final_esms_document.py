#!/usr/bin/env python3

import os
import subprocess
import tempfile
import re
from PyPDF2 import PdfMerger
from weasyprint import HTML

def convert_md_to_pdf_with_mermaid(md_file_path, pdf_output_path):
    """Convert Markdown file to PDF with proper Mermaid diagram support"""
    print(f"Converting {os.path.basename(md_file_path)} to PDF with Mermaid support...")
    
    try:
        # Try using pandoc with mermaid support first
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_html = os.path.join(temp_dir, "temp.html")
            
            # Use pandoc to convert with mermaid support
            pandoc_cmd = [
                "pandoc",
                md_file_path,
                "-o", temp_html,
                "--standalone",
                "--mathjax"
            ]
            
            result = subprocess.run(pandoc_cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                # Add mermaid initialization script
                with open(temp_html, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Add mermaid script
                mermaid_script = '''
                <script type="module">
                    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                    mermaid.initialize({ 
                        startOnLoad: true,
                        theme: 'default',
                        securityLevel: 'loose'
                    });
                    
                    // Wait for diagrams to render
                    setTimeout(() => {
                        const diagrams = document.querySelectorAll('.mermaid');
                        if (diagrams.length > 0) {
                            mermaid.run();
                        }
                    }, 1000);
                </script>
                '''
                
                # Insert mermaid script before closing head tag
                if '</head>' in html_content:
                    html_content = html_content.replace('</head>', mermaid_script + '</head>')
                else:
                    html_content = html_content.replace('</body>', mermaid_script + '</body>')
                
                # Save updated HTML
                processed_html = os.path.join(temp_dir, "processed.html")
                with open(processed_html, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                # Convert HTML to PDF
                HTML(processed_html).write_pdf(pdf_output_path)
                print(f"Successfully converted {os.path.basename(md_file_path)} to {os.path.basename(pdf_output_path)}")
                return True
            else:
                print(f"Pandoc conversion failed: {result.stderr}")
    except Exception as e:
        print(f"Error during pandoc conversion: {e}")
    
    # Fallback method - simple conversion
    print("Using fallback conversion method...")
    return convert_md_to_pdf_fallback(md_file_path, pdf_output_path)

def convert_md_to_pdf_fallback(md_file_path, pdf_output_path):
    """Fallback conversion method for Markdown to PDF"""
    try:
        # Simple conversion with basic styling
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>ESMS Handbook</title>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{ startOnLoad: true }});
            </script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 40px; }}
                .mermaid {{ text-align: center; margin: 20px 0; }}
                h1, h2, h3 {{ color: #333; }}
                table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <div class="markdown-body">
        """
        
        # Read and convert markdown content
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Simple replacement for mermaid code blocks
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
            print(f"Successfully converted {os.path.basename(md_file_path)} to {os.path.basename(pdf_output_path)}")
            return True
        finally:
            os.unlink(temp_html)
    except Exception as e:
        print(f"Error in fallback conversion: {e}")
        return False

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
            return False
    
    print(f"Writing merged PDF to {os.path.basename(output_path)}...")
    merger.write(output_path)
    merger.close()
    print(f"Successfully merged PDFs to {output_path}")
    return True

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Source files
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    
    # Output files
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_Enhanced.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Complete.pdf")
    
    # Step 1: Convert enhanced handbook to PDF with diagram support
    if convert_md_to_pdf_with_mermaid(md_file, handbook_pdf):
        print("Enhanced handbook PDF created successfully!")
    else:
        print("Failed to create enhanced handbook PDF")
        return
    
    # Step 2: Merge cover page with handbook
    if merge_pdfs([cover_pdf, handbook_pdf], final_pdf):
        print("Final document created successfully!")
        print(f"Final combined PDF: {final_pdf}")
        print(f"File size: {os.path.getsize(final_pdf) / (1024*1024):.1f} MB")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    main()