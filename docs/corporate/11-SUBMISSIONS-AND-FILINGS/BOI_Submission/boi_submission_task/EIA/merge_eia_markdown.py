#!/usr/bin/env python3
"""
Merge all EIA markdown files into a single markdown file.
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
    
    print(f"Found {len(md_files)} markdown files:")
    for md_file in md_files:
        print(f"  - {os.path.basename(md_file)}")
    
    # Create the output file path
    output_file = os.path.join(eia_dir, "EIA_Documents_Combined.md")
    
    # Open the output file for writing
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write a header
        outfile.write("# EIA Documents Combined\n\n")
        outfile.write("This file contains all EIA documents merged into a single file.\n\n")
        outfile.write("---\n\n")
        
        # Process each markdown file
        for i, md_file in enumerate(md_files):
            filename = os.path.basename(md_file)
            print(f"Processing {filename}...")
            
            # Write a section header
            outfile.write(f"# Document {i+1}: {filename}\n\n")
            
            # Read and write the content
            try:
                with open(md_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                outfile.write(f"Error: Could not read file {filename}\n\n")
            
            # Add a page break equivalent in markdown
            outfile.write("\n\n---\n\n")
    
    print(f"\nSuccessfully merged all markdown files into: {output_file}")

if __name__ == "__main__":
    merge_markdown_files()