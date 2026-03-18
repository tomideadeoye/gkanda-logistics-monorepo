#!/usr/bin/env python3
"""
Generate standardized cover pages for different documents using a common template.
"""

import os
from string import Template

def load_template(template_path):
    """
    Load the HTML template file.
    
    Args:
        template_path (str): Path to the HTML template file
        
    Returns:
        Template: A Template object for substitution
    """
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    return Template(template_content)

def generate_cover_page(template, output_path, **kwargs):
    """
    Generate a customized cover page from the template.
    
    Args:
        template (Template): The HTML template
        output_path (str): Path where the output HTML file should be saved
        **kwargs: Key-value pairs for template substitution
    """
    # Default values for optional parameters
    defaults = {
        'document_type': 'DOCUMENT',
        'document_status': 'CONFIDENTIAL',
        'document_title': 'Document Title',
        'document_subtitle': 'Document Subtitle',
        'document_number': 'DOC-000',
        'document_version': '1.0',
        'effective_date': 'January 1, 2025',
        'review_date': 'December 31, 2025',
        'emergency_contact': 'Dial 112 or 727',
        'authority_info': 'Authority: Managing Director',
        'distribution_info': 'Distribution: Internal',
        'year': '2025'
    }
    
    # Update defaults with provided values
    defaults.update(kwargs)
    
    # Substitute template variables
    html_content = template.substitute(defaults)
    
    # Write the customized HTML file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"Cover page generated: {output_path}")

def convert_html_to_pdf(html_path, pdf_path):
    """
    Convert HTML to PDF using Puppeteer via Node.js.
    
    Args:
        html_path (str): Path to the HTML file
        pdf_path (str): Path where the PDF should be saved
    """
    # Create a simple Node.js script for conversion
    js_script = f"""
const puppeteer = require('puppeteer');
const path = require('path');

async function convertHTMLtoPDF() {{
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Load the HTML file
  const htmlPath = path.resolve('{html_path}');
  await page.goto('file://' + htmlPath, {{ waitUntil: 'networkidle0' }});
  
  // Generate PDF
  await page.pdf({{
    path: '{pdf_path}',
    format: 'A4',
    printBackground: true,
    margin: {{
      top: '0.5in',
      right: '0.5in',
      bottom: '0.5in',
      left: '0.5in'
    }}
  }});
  
  await browser.close();
  console.log('PDF generated: {pdf_path}');
}}

convertHTMLtoPDF().catch(console.error);
    """
    
    # Write the JS script to a temporary file
    js_file = html_path.replace('.html', '_convert.js')
    with open(js_file, 'w') as f:
        f.write(js_script)
    
    # Run the conversion
    os.system(f'node "{js_file}"')
    
    # Clean up the temporary JS file
    os.remove(js_file)

def main():
    """Main function to demonstrate cover page generation."""
    # Load the template
    template_path = "emergency_response_cover.html"
    template = load_template(template_path)
    
    # Example 1: Emergency Response Plan (similar to existing)
    generate_cover_page(
        template,
        "emergency_response_plan_cover.html",
        document_type="EMERGENCY RESPONSE",
        document_status="CONFIDENTIAL",
        document_title="Emergency Response Plan",
        document_subtitle="Import/Export Terminal, Warehouse, and Reefer Containers",
        document_number="ERP-IE-002",
        document_version="1.5",
        effective_date="November 1, 2025",
        review_date="October 26, 2026",
        emergency_contact="Lagos State: Dial 112 or 727",
        authority_info="Plan Owner: HSE Manager | Authority: Managing Director",
        distribution_info="Approval - Distribution: Internal (All Departments), NPA Liaison, Critical Contractors on NDA",
        year="2025"
    )
    
    # Example 2: Safety Management System
    generate_cover_page(
        template,
        "safety_management_system_cover.html",
        document_type="SAFETY MANUAL",
        document_status="CONTROLLED",
        document_title="Safety Management System",
        document_subtitle="Health, Safety, and Environmental Management",
        document_number="SMS-001",
        document_version="2.0",
        effective_date="December 1, 2025",
        review_date="November 30, 2026",
        emergency_contact="Lagos State: Dial 112 or 727",
        authority_info="System Owner: HSE Manager | Authority: Managing Director",
        distribution_info="Distribution: All Staff, Contractors, and Regulatory Bodies",
        year="2025"
    )
    
    # Example 3: Quality Assurance Manual
    generate_cover_page(
        template,
        "quality_assurance_manual_cover.html",
        document_type="QUALITY MANUAL",
        document_status="CONTROLLED",
        document_title="Quality Assurance Manual",
        document_subtitle="Quality Management System for Logistics Operations",
        document_number="QAM-001",
        document_version="1.0",
        effective_date="January 1, 2026",
        review_date="December 31, 2026",
        emergency_contact="Lagos State: Dial 112 or 727",
        authority_info="System Owner: Quality Manager | Authority: Managing Director",
        distribution_info="Distribution: Management, Operations, and Quality Team",
        year="2026"
    )
    
    print("Standardized cover pages generated successfully!")
    print("To convert to PDF, use a tool like Puppeteer with the following command:")
    print("node convert_html_to_pdf.js")

if __name__ == "__main__":
    main()