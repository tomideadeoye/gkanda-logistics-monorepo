#!/usr/bin/env python3

import os
import re

def comprehensive_bullet_fix():
    """Comprehensive fix for bullet point formatting in the ESMS Handbook"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Comprehensive_Bullet_Fix.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Handle the specific case mentioned in the query
    # "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy"
    content = re.sub(
        r'(Our ESMS implementation team includes:)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)\s*(-\s[^:\n]+)',
        r'\1\n\n\2\n\3\n\4\n\5\n\6',
        content
    )
    
    # Fix 2: Handle emergency scenarios section
    # Look for patterns where multiple bullet points are on the same line
    def fix_emergency_scenarios(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(Key emergency scenarios for GK and A Logistics Services Ltd include:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_emergency_scenarios,
        content
    )
    
    # Fix 3: Handle emergency preparedness plan
    def fix_emergency_preparedness(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(Our emergency preparedness plan includes:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_emergency_preparedness,
        content
    )
    
    # Fix 4: Handle stakeholder engagement plan
    def fix_stakeholder_engagement(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(We will engage stakeholders through:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_stakeholder_engagement,
        content
    )
    
    # Fix 5: Handle external communications
    def fix_external_communications(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(We maintain publicly accessible channels for stakeholder communication:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_external_communications,
        content
    )
    
    # Fix 6: Handle grievance mechanism
    def fix_grievance_mechanism(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(Our grievance mechanism allows stakeholders to:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_grievance_mechanism,
        content
    )
    
    # Fix 7: Handle ongoing reporting
    def fix_ongoing_reporting(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(We commit to regular communication with affected communities:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_ongoing_reporting,
        content
    )
    
    # Fix 8: Handle indicators
    def fix_indicators(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(We will track key performance indicators including:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_indicators,
        content
    )
    
    # Fix 9: Handle training
    def fix_training(match):
        text = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}\n"
    
    content = re.sub(
        r'(We will ensure all employees receive:)\s*([^-]+(?:-[^:\n.]+)*)',
        fix_training,
        content
    )
    
    # Fix 10: Handle emergency procedures with numbers
    # Pattern for numbered emergency procedures
    def fix_numbered_procedures(match):
        title = match.group(1)
        bullets = match.group(2).strip()
        # Split by dash and reformat
        bullet_items = [item.strip() for item in bullets.split('-') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"**{title}**\n\n{formatted_bullets}\n"
    
    # Fix for all numbered emergency procedures
    content = re.sub(
        r'\*\*(\d+\.\s*[^*]+)\*\*\s*([^-]+(?:-[^:\n.]+)*)',
        fix_numbered_procedures,
        content
    )
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with comprehensive bullet point fixes: {output_md}")
    return True

def create_final_fixed_version():
    """Create the final version with both bullet fixes and exact centering"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "ESMS_Handbook_Comprehensive_Bullet_Fix.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Final_Fixed_Version.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all mermaid code blocks
    mermaid_pattern = r'```mermaid\s*[\s\S]*?\s*```'
    matches = list(re.finditer(mermaid_pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain indices
    for i, match in enumerate(reversed(matches)):
        diagram_num = len(matches) - i
        image_path = f"diagrams/diagram_{diagram_num}_final.png"
        
        # Create perfectly centered image using table approach
        replacement = f"""
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none; padding: 0;">
      <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 800px; width: 100%; height: auto; display: block; margin: 0 auto;">
      <p style="margin-top: 10px; font-style: italic; text-align: center; color: #666;">Diagram {diagram_num}</p>
    </td>
  </tr>
</table>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created final fixed version: {output_md}")
    return True

def main():
    """Main function for comprehensive bullet point fixing"""
    print("COMPREHENSIVE BULLET POINT FIXING")
    print("=" * 50)
    
    # Step 1: Apply comprehensive bullet fixes
    print("\nStep 1: Applying comprehensive bullet point fixes...")
    if comprehensive_bullet_fix():
        print("✓ Comprehensive bullet point fixes applied successfully!")
    else:
        print("✗ Failed to apply comprehensive bullet point fixes")
        return
    
    # Step 2: Create final fixed version
    print("\nStep 2: Creating final fixed version with exact centering...")
    if create_final_fixed_version():
        print("✓ Final fixed version created successfully!")
    else:
        print("✗ Failed to create final fixed version")
        return
    
    print("\n" + "="*60)
    print("COMPREHENSIVE BULLET POINT FIXING COMPLETE!")
    print("="*60)
    print("The final markdown file should now have:")
    print("✓ Properly formatted bullet points that render as HTML lists")
    print("✓ Correctly centered images using table-based approach")
    print("✓ Better PDF generation with properly formatted content")
    print("\nTo generate the PDF, use:")
    print("pandoc ESMS_Handbook_Final_Fixed_Version.md \\")
    print("  -o final_fixed_handbook.html \\")
    print("  --standalone \\")
    print("  --toc \\")
    print("  --toc-depth=2 \\")
    print("  --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css \\")
    print("  --css=best_centering_style.css \\")
    print("  --metadata pagetitle='ESMS Handbook'")
    print("\nweasyprint final_fixed_handbook.html ESMS_Handbook_Final_Fixed.pdf")

if __name__ == "__main__":
    main()