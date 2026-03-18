#!/usr/bin/env python3
"""
Merge all EIA markdown files into a single markdown file without any additional content.
"""

import os

def merge_markdown_files():
    """Merge all markdown files in the EIA directory into one file."""
    # Define the EIA directory path
    eia_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/EIA"
    
    # Get all markdown files in the directory (sorted by filename)
    md_files = []
    for filename in sorted(os.listdir(eia_dir)):
        if filename.endswith('.md'):
            md_files.append(os.path.join(eia_dir, filename))
    
    if not md_files:
        print("No markdown files found in the EIA directory.")
        return
    
    # Create the output file path
    output_file = os.path.join(eia_dir, "EIA_Documents_Combined.md")
    
    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Process each markdown file
        for i, md_file in enumerate(md_files):
            # Read and write the content
            try:
                with open(md_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    # Add a newline between files if the file doesn't end with one
                    if not content.endswith('\n'):
                        outfile.write('\n')
            except Exception as e:
                print(f"Error reading {md_file}: {e}")

    print(f"Successfully merged all markdown files into: {output_file}")

if __name__ == "__main__":
    merge_markdown_files()