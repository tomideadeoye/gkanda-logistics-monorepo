#!/usr/bin/env python3

import os
import re

def simple_bullet_fix():
    """Simple and effective fix for bullet point formatting"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Simple_Bullet_Fix.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Handle the specific case mentioned in the query
    content = content.replace(
        "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy",
        "Our ESMS implementation team includes:\n\n- **Executive Sponsor**: Managing Director\n- **Policy Custodian**: Head of HR\n- **HSE Manager**: Responsible for health, safety, and environmental compliance\n- **Line Managers**: Accountable for day-to-day implementation in their areas\n- **Worker Representatives**: Providing input from operational staff."
    )
    
    # Fix 2: Handle inline bullet points by adding proper line breaks
    # Pattern: text followed by multiple dash-separated items
    def fix_inline_bullets(match):
        prefix = match.group(1)
        items_str = match.group(2)
        # Split items by dash
        items = [item.strip() for item in items_str.split(' - ') if item.strip()]
        formatted_items = '\n'.join([f"- {item}" for item in items])
        return f"{prefix}:\n\n{formatted_items}"
    
    # Apply to common patterns
    patterns = [
        r'(Key emergency scenarios for GK and A Logistics Services Ltd include):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Our emergency preparedness plan includes):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will ensure all employees receive):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will engage stakeholders through):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We maintain publicly accessible channels for stakeholder communication):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(Our grievance mechanism allows stakeholders to):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We commit to regular communication with affected communities):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        r'(We will track key performance indicators including):\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, fix_inline_bullets, content)
    
    # Fix 3: Handle emergency procedures with better formatting
    # Find all emergency procedure sections
    def fix_emergency_procedure(match):
        title = match.group(1)
        items_str = match.group(2)
        # Split items by dash
        items = [item.strip() for item in items_str.split(' - ') if item.strip()]
        formatted_items = '\n'.join([f"- {item}" for item in items])
        return f"**{title}**\n\n{formatted_items}"
    
    # Pattern for numbered emergency procedures
    content = re.sub(
        r'\*\*(\d+\.\s*[^*]+)\*\*\s*([^-]+(?:\s*-\s*[^:\n.]+)+)',
        fix_emergency_procedure,
        content
    )
    
    # Fix 4: Handle the AVOID, MINIMIZE, OFFSET sections
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
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with simple bullet point fixes: {output_md}")
    return True

def create_final_version_with_proper_bullets():
    """Create final version with proper bullet points and exact centering"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "ESMS_Handbook_Simple_Bullet_Fix.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_Final_With_Proper_Bullets.md")
    
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
        image_path = f"diagrams/diagram_{diagram_num}_exact_centered.png"
        
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
    
    print(f"Created final version with proper bullets: {output_md}")
    return True

def main():
    """Main function for simple bullet point fixing"""
    print("SIMPLE BULLET POINT FIXING")
    print("=" * 40)
    
    # Step 1: Apply simple bullet fixes
    print("\nStep 1: Applying simple bullet point fixes...")
    if simple_bullet_fix():
        print("✓ Simple bullet point fixes applied successfully!")
    else:
        print("✗ Failed to apply simple bullet point fixes")
        return
    
    # Step 2: Create final version with proper bullets
    print("\nStep 2: Creating final version with proper bullets and exact centering...")
    if create_final_version_with_proper_bullets():
        print("✓ Final version with proper bullets created successfully!")
    else:
        print("✗ Failed to create final version with proper bullets")
        return
    
    print("\n" + "="*50)
    print("SIMPLE BULLET POINT FIXING COMPLETE!")
    print("="*50)
    print("The final markdown file should now have:")
    print("✓ Properly formatted bullet points")
    print("✓ Correctly centered images")
    print("✓ Better PDF generation")
    
    print("\nTo generate HTML:")
    print("pandoc ESMS_Handbook_Final_With_Proper_Bullets.md \\")
    print("  -o final_with_proper_bullets.html \\")
    print("  --standalone \\")
    print("  --toc \\")
    print("  --toc-depth=2 \\")
    print("  --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css \\")
    print("  --css=best_centering_style.css")
    
    print("\nTo generate PDF:")
    print("weasyprint final_with_proper_bullets.html ESMS_Handbook_Final_With_Proper_Bullets.pdf")

if __name__ == "__main__":
    main()