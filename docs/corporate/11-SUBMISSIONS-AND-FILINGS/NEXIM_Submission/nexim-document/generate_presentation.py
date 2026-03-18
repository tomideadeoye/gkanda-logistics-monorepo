#!/usr/bin/env python3
"""
Script to generate PDF presentation for NEXIM from markdown
"""

import os
from weasyprint import HTML

def generate_pdf():
    # Define paths
    markdown_file = "NEXIM_Port_Terminal_Presentation.md"
    html_file = "NEXIM_Port_Terminal_Presentation.html"
    pdf_file = "NEXIM_Port_Terminal_Presentation.pdf"
    
    # Change to the nexim-document directory
    os.chdir("nexim-document")
    
    # Convert markdown to HTML using pandoc
    os.system(f"pandoc {markdown_file} -o {html_file} --metadata title='GKAL Port Terminal Presentation for NEXIM'")
    
    # Convert HTML to PDF using weasyprint
    HTML(html_file).write_pdf(pdf_file)
    
    print(f"PDF presentation generated: {pdf_file}")

if __name__ == "__main__":
    generate_pdf()