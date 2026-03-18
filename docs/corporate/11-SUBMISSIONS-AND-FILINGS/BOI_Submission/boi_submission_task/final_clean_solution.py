#!/usr/bin/env python3

import os
import re

def create_clean_markdown():
    """Create a clean markdown file with proper formatting"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Clean_Final.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix all the specific issues mentioned:
    
    # 1. Fix the ESMS implementation team section
    content = content.replace(
        "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy",
        "Our ESMS implementation team includes:\n\n- **Executive Sponsor**: Managing Director\n- **Policy Custodian**: Head of HR\n- **HSE Manager**: Responsible for health, safety, and environmental compliance\n- **Line Managers**: Accountable for day-to-day implementation in their areas\n- **Worker Representatives**: Providing input from operational staff"
    )
    
    # 2. Fix the AVOID section
    content = content.replace(
        "AVOID • Establish and implement a construction waste management plan for all sites • Establish procedures for reuse, recycle, and safe disposal to licensed landfills • Train workers on proper handling and disposal of construction wastes • Locate and remove hazardous facilities prior to commencement of work • Implement rodent elimination programs prior to demolition • Conduct surveys for hazardous materials and prepare remediation plans",
        "AVOID:\n\n- Establish and implement a construction waste management plan for all sites\n- Establish procedures for reuse, recycle, and safe disposal to licensed landfills\n- Train workers on proper handling and disposal of construction wastes\n- Locate and remove hazardous facilities prior to commencement of work\n- Implement rodent elimination programs prior to demolition\n- Conduct surveys for hazardous materials and prepare remediation plans"
    )
    
    # 3. Fix the MINIMIZE section
    content = content.replace(
        "MINIMIZE • Develop grievance mechanisms for local residents to facilitate understanding of impacts • Deploy containers for collection and safe disposal of solid waste",
        "MINIMIZE:\n\n- Develop grievance mechanisms for local residents to facilitate understanding of impacts\n- Deploy containers for collection and safe disposal of solid waste"
    )
    
    # 4. Fix the OFFSET section
    content = content.replace(
        "OFFSET • Compensate local residents negatively affected by activities • Provide health-related examinations for individuals claiming harm...mapping our stakeholders section too. bullt points under Port-Specific Emergency Response Procedures",
        "OFFSET:\n\n- Compensate local residents negatively affected by activities\n- Provide health-related examinations for individuals claiming harm"
    )
    
    # 5. Fix inline bullet points by adding proper line breaks
    # Emergency scenarios
    content = re.sub(
        r'(Key emergency scenarios for GK and A Logistics Services Ltd include:)([^#]+?)(?=\n#)',
        lambda m: f"{m.group(1)}\n\n" + '\n'.join([f"- {item.strip()}" for item in m.group(2).strip().split('- ') if item.strip()]),
        content,
        flags=re.DOTALL
    )
    
    # Emergency preparedness plan
    content = re.sub(
        r'(Our emergency preparedness plan includes:)([^#]+?)(?=\n#)',
        lambda m: f"{m.group(1)}\n\n" + '\n'.join([f"- {item.strip()}" for item in m.group(2).strip().split('- ') if item.strip()]),
        content,
        flags=re.DOTALL
    )
    
    # Replace all mermaid diagrams with images
    mermaid_pattern = r'```mermaid\s*[\s\S]*?\s*```'
    matches = list(re.finditer(mermaid_pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain indices
    for i, match in enumerate(reversed(matches)):
        diagram_num = len(matches) - i
        image_path = f"diagrams/diagram_{diagram_num}_exact_centered.png"
        
        # Create clean image with simple markdown
        replacement = f"\n\n![Diagram {diagram_num}]({image_path})\n\n*Diagram {diagram_num}*\n\n"
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created clean final markdown: {output_md}")
    return True

def create_better_css():
    """Create better CSS for improved styling"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    css_file = os.path.join(base_dir, "better_styling.css")
    
    css_content = """
/* BETTER STYLING FOR ESMS HANDBOOK */
body {
    font-family: Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    margin: 20mm;
    color: #333;
}

h1 {
    font-size: 16pt;
    color: #2c3e50;
    border-bottom: 1px solid #3498db;
    padding-bottom: 10px;
    margin-top: 20px;
    margin-bottom: 15px;
}

h2 {
    font-size: 14pt;
    color: #2c3e50;
    margin-top: 18px;
    margin-bottom: 12px;
}

h3 {
    font-size: 12pt;
    color: #2c3e50;
    margin-top: 15px;
    margin-bottom: 10px;
}

h4 {
    font-size: 11pt;
    color: #2c3e50;
    margin-top: 12px;
    margin-bottom: 8px;
    font-weight: bold;
}

p {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: left;
}

/* IMPROVED LIST STYLING */
ul, ol {
    margin-top: 10px;
    margin-bottom: 15px;
    padding-left: 20px;
}

li {
    margin-bottom: 6px;
}

ul li {
    list-style-type: disc;
}

ol li {
    list-style-type: decimal;
}

/* NESTED LISTS */
ul ul li {
    list-style-type: circle;
}

ul ul ul li {
    list-style-type: square;
}

/* IMAGES */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 20px auto;
}

/* CAPTIONS */
img + p {
    text-align: center;
    font-style: italic;
    font-size: 10pt;
    color: #666;
    margin-top: 5px;
}

/* TABLES */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

/* CODE */
code {
    font-family: 'Courier New', monospace;
    background-color: #f8f8f8;
    padding: 2px 4px;
    border-radius: 3px;
    font-size: 10pt;
}

/* BLOCKQUOTES */
blockquote {
    border-left: 3px solid #3498db;
    margin: 15px 0;
    padding: 10px 15px;
    background-color: #f8f9fa;
}

/* PAGE BREAKS */
.page-break {
    page-break-before: always;
}

/* TABLE OF CONTENTS */
.toc {
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    margin: 15px 0;
}
"""
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    print(f"Created better CSS file: {css_file}")
    return css_file

def generate_final_clean_pdf():
    """Generate the final clean PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_Clean_Final.md")
    css_file = os.path.join(base_dir, "better_styling.css")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Generate HTML
    html_file = os.path.join(base_dir, "handbook_clean_final.html")
    
    import subprocess
    cmd = [
        "pandoc",
        md_file,
        "-o", html_file,
        "--standalone",
        "--toc",
        "--toc-depth=3",
        f"--css={css_file}",
        "--metadata", "pagetitle=ESMS Handbook"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if result.returncode == 0:
            print(f"Successfully generated HTML: {html_file}")
        else:
            print(f"Error generating HTML: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error generating HTML: {e}")
        return False
    
    # Generate PDF
    pdf_file = os.path.join(base_dir, "ESMS_Handbook_Clean_Final.pdf")
    cmd = [
        "weasyprint",
        html_file,
        pdf_file,
        "--presentational-hints",
        "--optimize-images"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        if result.returncode == 0:
            print(f"Successfully generated PDF: {pdf_file}")
            return True
        else:
            print(f"Error generating PDF: {result.stderr}")
            return False
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return False

def main():
    """Main function to create the final clean solution"""
    print("CREATING FINAL CLEAN SOLUTION")
    print("=" * 40)
    
    # Step 1: Create clean markdown
    print("\nStep 1: Creating clean markdown...")
    if create_clean_markdown():
        print("✓ Clean markdown created successfully!")
    else:
        print("✗ Failed to create clean markdown")
        return
    
    # Step 2: Create better CSS
    print("\nStep 2: Creating better CSS...")
    css_file = create_better_css()
    if css_file:
        print("✓ Better CSS created successfully!")
    else:
        print("✗ Failed to create better CSS")
        return
    
    # Step 3: Generate final clean PDF
    print("\nStep 3: Generating final clean PDF...")
    if generate_final_clean_pdf():
        print("✓ Final clean PDF generated successfully!")
    else:
        print("✗ Failed to generate final clean PDF")
        return
    
    print("\n" + "="*50)
    print("FINAL CLEAN SOLUTION COMPLETE!")
    print("="*50)
    print("The final PDF should now have:")
    print("✓ Properly formatted bullet points")
    print("✓ Better text sizing (11pt base font)")
    print("✓ Improved spacing and readability")
    print("✓ Cleaner, more professional appearance")
    
    print("\nFinal output file:")
    print("/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/ESMS_Handbook_Clean_Final.pdf")

if __name__ == "__main__":
    main()