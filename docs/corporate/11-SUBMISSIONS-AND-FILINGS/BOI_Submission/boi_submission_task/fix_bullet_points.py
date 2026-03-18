#!/usr/bin/env python3

import os
import re

def fix_bullet_point_formatting():
    """Fix bullet point formatting in the ESMS Handbook markdown file"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets.md")
    
    if not os.path.exists(input_md):
        print(f"Source markdown file not found: {input_md}")
        return False
    
    # Read the markdown file
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix common bullet point issues
    # Pattern to match lines that start with dash but are not properly formatted as lists
    # This looks for lines that start with "- " but are not preceded by a blank line or list context
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check if this line starts with "- " and might be a list item
        if line.strip().startswith('- ') and len(line.strip()) > 2:
            # Check if the previous line doesn't end with a colon or is not empty
            if i > 0:
                prev_line = lines[i-1].strip()
                # If previous line ends with colon, this should be a list
                if prev_line.endswith(':') or prev_line.endswith('include') or prev_line.endswith('includes'):
                    # Make sure there's a blank line before the list
                    if fixed_lines and fixed_lines[-1].strip() != '':
                        fixed_lines.append('')
                    fixed_lines.append(line)
                # If previous line is a header or paragraph, and this line starts with dash, it's likely a list
                elif (prev_line.startswith('#') or 
                      (len(prev_line) > 0 and not prev_line.startswith('-'))):
                    # Add blank line before list
                    if fixed_lines and fixed_lines[-1].strip() != '':
                        fixed_lines.append('')
                    fixed_lines.append(line)
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    
    # Additional fixes for specific patterns
    fixed_content = '\n'.join(fixed_lines)
    
    # Fix specific sections that we know have issues
    # Fix the ESMS implementation team section
    fixed_content = fixed_content.replace(
        "Our ESMS implementation team includes: - Executive Sponsor: Managing Director - Policy",
        "Our ESMS implementation team includes:\n\n- Executive Sponsor: Managing Director\n- Policy"
    )
    
    # Fix bullet points that are on the same line
    # Pattern: text followed by multiple bullet points on the same line
    def fix_inline_bullets(match):
        text = match.group(1)
        bullets = match.group(2)
        # Split bullets by "- " pattern
        bullet_items = [item.strip() for item in bullets.split(' - ') if item.strip()]
        formatted_bullets = '\n'.join([f"- {item}" for item in bullet_items])
        return f"{text}:\n\n{formatted_bullets}"
    
    # Fix inline bullets pattern
    fixed_content = re.sub(
        r'([^.]+):\s*(-\s[^:\n]+(?:\s*-\s[^:\n]+)*)',
        fix_inline_bullets,
        fixed_content
    )
    
    # Fix another common pattern
    fixed_content = re.sub(
        r'([A-Z][^.]*):\s*(-\s[^:\n.]+(?:\s*-\s[^:\n.]+)*)',
        fix_inline_bullets,
        fixed_content
    )
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Created markdown with fixed bullet points: {output_md}")
    return True

def create_markdown_with_fixed_bullets_and_exact_centering():
    """Create markdown with both fixed bullet points and exact image centering"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Fixed_Bullets_and_Exact_Centering.md")
    
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
        
        # Create exactly centered image using table approach for maximum compatibility
        replacement = f"""
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none;">
      <img src="{image_path}" alt="Diagram {diagram_num}" style="max-width: 800px; width: 100%; height: auto;">
      <p style="margin-top: 10px; font-style: italic;">Diagram {diagram_num}</p>
    </td>
  </tr>
</table>
"""
        content = content[:match.start()] + replacement + content[match.end():]
    
    # Write the updated content
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with fixed bullets and exact image centering: {output_md}")
    return True

def main():
    """Main function to fix bullet point formatting"""
    print("Fixing bullet point formatting in ESMS Handbook...")
    
    # Step 1: Fix bullet point formatting
    print("\nStep 1: Fixing bullet point formatting...")
    if fix_bullet_point_formatting():
        print("✓ Bullet point formatting fixed successfully!")
    else:
        print("✗ Failed to fix bullet point formatting")
        return
    
    # Step 2: Create markdown with fixed bullets and exact centering
    print("\nStep 2: Creating markdown with fixed bullets and exact centering...")
    if create_markdown_with_fixed_bullets_and_exact_centering():
        print("✓ Markdown with fixed bullets and exact centering created successfully!")
    else:
        print("✗ Failed to create markdown with fixed bullets and exact centering")
        return
    
    print("\n" + "="*50)
    print("BULLET POINT FIXING COMPLETE!")
    print("="*50)
    print("The fixed markdown file should now have properly formatted bullet points")
    print("that will render correctly as HTML lists and in the final PDF.")

if __name__ == "__main__":
    main()