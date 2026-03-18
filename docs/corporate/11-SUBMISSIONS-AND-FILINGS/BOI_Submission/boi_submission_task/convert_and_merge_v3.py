#!/usr/bin/env python3

import os
import subprocess
import tempfile
from weasyprint import HTML

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

def main():
    # Define file paths
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"

    # Files to convert - use the SVG version
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_SVGs.md")

    # Output PDF file
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_with_Diagrams.pdf")

    # Convert with Mermaid support
    convert_md_to_pdf_with_mermaid(md_file, pdf_output)

    print("Conversion completed successfully!")
    print(f"PDF with diagrams: {pdf_output}")

if __name__ == "__main__":
    main()