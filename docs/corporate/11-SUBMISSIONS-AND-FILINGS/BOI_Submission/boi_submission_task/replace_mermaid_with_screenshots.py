#!/usr/bin/env python3

import os
import re

def replace_mermaid_with_screenshots(md_file_path, output_file_path):
    """Replace mermaid code blocks with centered screenshot image references"""
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all mermaid code blocks
    mermaid_pattern = r'```mermaid\s*[\s\S]*?\s*```'
    matches = list(re.finditer(mermaid_pattern, content, re.DOTALL))

    # Process matches in reverse order to maintain indices
    for i, match in enumerate(reversed(matches)):
        diagram_num = len(matches) - i
        screenshot_path = f"diagrams/diagram_{diagram_num}_screenshot.png"
        # Center the image using HTML div for better control
        replacement = f'<div align="center">\n\n![Diagram {diagram_num}]({screenshot_path})\n\n</div>'
        content = content[:match.start()] + replacement + content[match.end():]

    # Write the updated content
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created markdown with centered screenshot images: {output_file_path}")

def main():
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    input_md = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Screenshots.md")

    replace_mermaid_with_screenshots(input_md, output_md)

    print("Mermaid diagrams replaced with centered screenshots successfully!")

if __name__ == "__main__":
    main()