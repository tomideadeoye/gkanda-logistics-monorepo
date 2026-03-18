#!/usr/bin/env python3

import os
import re

def fix_bullet_point_formatting_completely():
    """Completely fix bullet point formatting issues"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Completely_Fixed.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the specific issue mentioned in the query
    content = content.replace(
        "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy",
        "Our ESMS implementation team includes:\n\n- **Executive Sponsor**: Managing Director\n- **Policy Custodian**: Head of HR\n- **HSE Manager**: Responsible for health, safety, and environmental compliance\n- **Line Managers**: Accountable for day-to-day implementation in their areas\n- **Worker Representatives**: Providing input from operational staff"
    )
    
    # Fix inline bullet points that are all on one line
    def fix_inline_bullets_completely(match):
        prefix = match.group(1)
        items_str = match.group(2)
        # Split items by dash and clean them
        items = [item.strip() for item in items_str.split('-') if item.strip()]
        formatted_items = '\n'.join([f"- {item}" for item in items if item])
        return f"{prefix}:\n\n{formatted_items}"
    
    # Patterns to fix various inline bullet issues
    patterns = [
        r'(Key emergency scenarios for GK and A Logistics Services Ltd include):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Our emergency preparedness plan includes):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will ensure all employees receive):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will engage stakeholders through):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We maintain publicly accessible channels for stakeholder communication):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Our grievance mechanism allows stakeholders to):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We commit to regular communication with affected communities):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will track key performance indicators including):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Benefits for GK and A Logistics Services Ltd):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Business Benefits):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Key areas for integration include):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, fix_inline_bullets_completely, content)
    
    # Fix emergency procedures with numbers
    def fix_numbered_procedures_completely(match):
        title = match.group(1)
        items_str = match.group(2)
        # Split items by dash and clean them
        items = [item.strip() for item in items_str.split('-') if item.strip()]
        formatted_items = '\n'.join([f"- {item}" for item in items if item])
        return f"**{title}**\n\n{formatted_items}"
    
    # Fix all numbered emergency procedures
    content = re.sub(
        r'\*\*(\d+\.\s*[^*]+)\*\*\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        fix_numbered_procedures_completely,
        content
    )
    
    # Fix the AVOID, MINIMIZE, OFFSET sections
    def fix_action_sections(match):
        title = match.group(1)
        items_str = match.group(2)
        # Split items by bullet character and clean them
        items = [item.strip() for item in items_str.split('•') if item.strip()]
        formatted_items = '\n'.join([f"- {item}" for item in items if item])
        return f"{title}:\n\n{formatted_items}"
    
    content = re.sub(
        r'(AVOID)\s*•\s*([^\n]+(?:\s*•\s*[^\n]+)*)',
        fix_action_sections,
        content
    )
    
    content = re.sub(
        r'(MINIMIZE)\s*•\s*([^\n]+(?:\s*•\s*[^\n]+)*)',
        fix_action_sections,
        content
    )
    
    content = re.sub(
        r'(OFFSET)\s*•\s*([^\n]+(?:\s*•\s*[^\n]+)*)',
        fix_action_sections,
        content
    )
    
    # Find all mermaid code blocks and replace with images
    mermaid_pattern = r'```mermaid\s*[\s\S]*?\s*```'
    matches = list(re.finditer(mermaid_pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain indices
    for i, match in enumerate(reversed(matches)):
        diagram_num = len(matches) - i
        image_path = f"diagrams/diagram_{diagram_num}_exact_centered.png"
        
        # Create properly formatted image with table-based centering
        replacement = f"""
<table>
  <tr>
    <td>
      <img src="{image_path}" alt="Diagram {diagram_num}">
      <p style="font-style: italic; text-align: center;">Diagram {diagram_num}</p>
    </td>
  </tr>
</table>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with completely fixed formatting: {output_md}")
    return True

def generate_pdf_with_improved_styling():
    """Generate PDF with improved styling"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_Completely_Fixed.md")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Generate HTML
    html_file = os.path.join(base_dir, "handbook_improved_styling.html")
    css_file = os.path.join(base_dir, "improved_styling.css")
    
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
    
    import subprocess
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
    pdf_file = os.path.join(base_dir, "ESMS_Handbook_Improved_Styling.pdf")
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

def merge_with_cover():
    """Merge the generated PDF with the cover page"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_Improved_Styling.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final.pdf")
    
    # Check if required files exist
    missing_files = []
    if not os.path.exists(cover_pdf):
        missing_files.append(cover_pdf)
    if not os.path.exists(handbook_pdf):
        missing_files.append(handbook_pdf)
    
    if missing_files:
        print(f"Missing required files: {missing_files}")
        return False
    
    try:
        from PyPDF2 import PdfMerger
        # Merge PDFs
        merger = PdfMerger()
        merger.append(cover_pdf)
        merger.append(handbook_pdf)
        merger.write(final_pdf)
        merger.close()
        
        print(f"Successfully merged PDFs: {final_pdf}")
        if os.path.exists(final_pdf):
            file_size = os.path.getsize(final_pdf) / (1024*1024)
            print(f"Final file size: {file_size:.1f} MB")
        return True
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return False

def main():
    """Main function to fix formatting and generate PDF with improved styling"""
    print("FIXING FORMATTING AND IMPROVING STYLING")
    print("=" * 50)
    
    # Step 1: Fix bullet point formatting completely
    print("\nStep 1: Fixing bullet point formatting completely...")
    if fix_bullet_point_formatting_completely():
        print("✓ Bullet point formatting fixed successfully!")
    else:
        print("✗ Failed to fix bullet point formatting")
        return
    
    # Step 2: Generate PDF with improved styling
    print("\nStep 2: Generating PDF with improved styling...")
    if generate_pdf_with_improved_styling():
        print("✓ PDF with improved styling generated successfully!")
    else:
        print("✗ Failed to generate PDF with improved styling")
        return
    
    # Step 3: Merge with cover page
    print("\nStep 3: Merging with cover page...")
    if merge_with_cover():
        print("✓ Final PDF with cover page created successfully!")
    else:
        print("✗ Failed to merge with cover page")
        return
    
    print("\n" + "="*60)
    print("FORMATTING FIX AND STYLING IMPROVEMENT COMPLETE!")
    print("="*60)
    print("The final PDF should now have:")
    print("✓ Properly formatted bullet points")
    print("✓ Improved text sizing (11pt base font)")
    print("✓ Better spacing and readability")
    print("✓ Properly centered images")
    print("✓ Professional appearance")
    
    print("\nFinal output file:")
    print("/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final.pdf")

if __name__ == "__main__":
    main()