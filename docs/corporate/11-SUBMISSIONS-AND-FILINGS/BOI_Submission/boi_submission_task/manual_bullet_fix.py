#!/usr/bin/env python3

import os

def manually_fix_bullet_points():
    """Manually fix the specific bullet point issues"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "ESMS_Handbook_Completely_Fixed.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Manually_Fixed.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Fix specific lines with formatting issues
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Fix the ESMS implementation team section
        if "Our ESMS implementation team includes:" in line and "- **Executive Sponsor**" in line:
            # Split the line into separate lines
            parts = line.split("- ")
            fixed_lines.append(parts[0].strip() + "\n\n")
            # Add each bullet point on its own line
            for part in parts[1:]:
                if part.strip():
                    fixed_lines.append("- " + part.strip() + "\n")
        # Fix other specific formatting issues
        elif "- **Line Managers**: Accountable for day-to-day implementation" in line:
            # This line has multiple bullet points
            line = line.replace("- **Line Managers**: Accountable for day-to-day implementation in their areas           - **Worker Representatives**: Providing input from operational staff", 
                               "- **Line Managers**: Accountable for day-to-day implementation in their areas\n- **Worker Representatives**: Providing input from operational staff")
            fixed_lines.append(line)
        else:
            fixed_lines.append(line)
        
        i += 1
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"Created markdown with manually fixed bullet points: {output_md}")
    return True

def create_final_better_version():
    """Create the final version with better formatting"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    
    # Let's create a completely new approach - manually fix the most important sections
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Best_Version.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Manually fix the specific issues mentioned:
    
    # 1. Fix the ESMS implementation team section
    content = content.replace(
        "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy",
        "Our ESMS implementation team includes:\n\n- **Executive Sponsor**: Managing Director\n- **Policy Custodian**: Head of HR\n- **HSE Manager**: Responsible for health, safety, and environmental compliance\n- **Line Managers**: Accountable for day-to-day implementation in their areas\n- **Worker Representatives**: Providing input from operational staff."
    )
    
    # 2. Fix the AVOID, MINIMIZE, OFFSET sections
    content = content.replace(
        "AVOID • Establish and implement a construction waste management plan for all sites • Establish procedures for reuse, recycle, and safe disposal to licensed landfills • Train workers on proper handling and disposal of construction wastes • Locate and remove hazardous facilities prior to commencement of work • Implement rodent elimination programs prior to demolition • Conduct surveys for hazardous materials and prepare remediation plans",
        "AVOID:\n\n- Establish and implement a construction waste management plan for all sites\n- Establish procedures for reuse, recycle, and safe disposal to licensed landfills\n- Train workers on proper handling and disposal of construction wastes\n- Locate and remove hazardous facilities prior to commencement of work\n- Implement rodent elimination programs prior to demolition\n- Conduct surveys for hazardous materials and prepare remediation plans"
    )
    
    content = content.replace(
        "MINIMIZE • Develop grievance mechanisms for local residents to facilitate understanding of impacts • Deploy containers for collection and safe disposal of solid waste",
        "MINIMIZE:\n\n- Develop grievance mechanisms for local residents to facilitate understanding of impacts\n- Deploy containers for collection and safe disposal of solid waste"
    )
    
    content = content.replace(
        "OFFSET • Compensate local residents negatively affected by activities • Provide health-related examinations for individuals claiming harm...mapping our stakeholders section too. bullt points under Port-Specific Emergency Response Procedures",
        "OFFSET:\n\n- Compensate local residents negatively affected by activities\n- Provide health-related examinations for individuals claiming harm"
    )
    
    # 3. Fix some of the emergency procedure sections by ensuring proper line breaks
    # Replace patterns where multiple items are on the same line
    import re
    
    # Fix emergency scenarios section
    content = re.sub(
        r'(Key emergency scenarios for GK and A Logistics Services Ltd include:)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)',
        r'\1\n\n\2\n\3\n\4\n\5\n\6\n\7\n\8\n\9\n\10\n\11',
        content
    )
    
    # Fix emergency preparedness plan section
    content = re.sub(
        r'(Our emergency preparedness plan includes:)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)',
        r'\1\n\n\2\n\3\n\4\n\5\n\6\n\7',
        content
    )
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created best version markdown: {output_md}")
    return True

def generate_final_pdf():
    """Generate the final PDF with the best formatting"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_Best_Version.md")
    css_file = os.path.join(base_dir, "improved_styling.css")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Generate HTML
    html_file = os.path.join(base_dir, "handbook_best_version.html")
    
    import subprocess
    cmd = [
        "pandoc",
        md_file,
        "-o", html_file,
        "--standalone",
        "--toc",
        "--toc-depth=2",
        "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
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
    pdf_file = os.path.join(base_dir, "ESMS_Handbook_Best_Version.pdf")
    cmd = [
        "weasyprint",
        html_file,
        pdf_file,
        "--presentational-hints",
        "--optimize-images",
        "--full-fonts"
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
    """Main function to create the best version"""
    print("CREATING THE BEST VERSION WITH PROPER FORMATTING")
    print("=" * 50)
    
    # Create the best version
    print("\nStep 1: Creating the best version with manual fixes...")
    if create_final_better_version():
        print("✓ Best version created successfully!")
    else:
        print("✗ Failed to create best version")
        return
    
    # Generate the final PDF
    print("\nStep 2: Generating the final PDF...")
    if generate_final_pdf():
        print("✓ Final PDF generated successfully!")
    else:
        print("✗ Failed to generate final PDF")
        return
    
    print("\n" + "="*60)
    print("BEST VERSION CREATION COMPLETE!")
    print("="*60)
    print("The final PDF should now have:")
    print("✓ Properly formatted bullet points")
    print("✓ Improved text sizing (11pt base font)")
    print("✓ Better spacing and readability")
    print("✓ Professional appearance")
    
    print("\nFinal output file:")
    print("/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/ESMS_Handbook_Best_Version.pdf")

if __name__ == "__main__":
    main()