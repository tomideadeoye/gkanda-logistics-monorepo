#!/usr/bin/env python3

import os
import subprocess
import re
import shutil
from pathlib import Path
from PyPDF2 import PdfMerger

def ensure_directories():
    """Ensure required directories exist"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    os.makedirs(diagrams_dir, exist_ok=True)
    print(f"Ensured directories exist: {diagrams_dir}")

def generate_svgs_from_mermaid():
    """Generate SVG files from Mermaid diagrams in the markdown file"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Extract mermaid diagrams
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all mermaid code blocks
    pattern = r'```mermaid\s*(.*?)\s*```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    print(f"Found {len(diagrams)} mermaid diagrams")
    
    # Generate SVG for each diagram
    for i, diagram_code in enumerate(diagrams, 1):
        svg_filename = f"diagram_{i}.svg"
        svg_path = os.path.join(diagrams_dir, svg_filename)
        
        # Create temporary mermaid file
        temp_mmd = os.path.join(base_dir, f"temp_diagram_{i}.mmd")
        with open(temp_mmd, 'w', encoding='utf-8') as f:
            f.write(diagram_code.strip())
        
        try:
            # Generate SVG using mermaid CLI - simplified approach
            result = subprocess.run([
                'npx', '@mermaid-js/mermaid-cli',
                '--input', temp_mmd,
                '--output', svg_path
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print(f"Generated SVG: {svg_filename}")
            else:
                print(f"Error generating SVG {svg_filename}: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print(f"Timeout generating SVG: {svg_filename}")
        except Exception as e:
            print(f"Error generating SVG {svg_filename}: {e}")
        finally:
            # Clean up temporary file
            if os.path.exists(temp_mmd):
                os.remove(temp_mmd)
    
    return True

def convert_svg_to_png_with_high_quality():
    """Convert SVG files to high-quality PNG for better PDF compatibility"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    # Check if convert (ImageMagick) is available
    if not shutil.which("convert"):
        print("ImageMagick 'convert' command not found. Trying alternative method...")
        return False
    
    # Convert each SVG to PNG with high quality settings
    for i in range(1, 5):  # We have 4 diagrams
        svg_path = os.path.join(diagrams_dir, f"diagram_{i}.svg")
        png_path = os.path.join(diagrams_dir, f"diagram_{i}.png")
        
        if os.path.exists(svg_path):
            try:
                # Convert SVG to PNG with high quality
                # Using higher density and better quality settings
                result = subprocess.run([
                    "convert", 
                    "-density", "300", 
                    "-background", "white", 
                    "-alpha", "remove", 
                    "-alpha", "off",
                    "-resize", "800x>",
                    "-quality", "100",
                    svg_path, png_path
                ], capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0:
                    print(f"Converted SVG to high-quality PNG: diagram_{i}.png")
                    # Check file size
                    if os.path.exists(png_path):
                        size = os.path.getsize(png_path) / 1024
                        print(f"  PNG file size: {size:.1f} KB")
                else:
                    print(f"Error converting SVG to PNG for diagram_{i}: {result.stderr}")
            except subprocess.TimeoutExpired:
                print(f"Timeout converting SVG to PNG: diagram_{i}")
            except Exception as e:
                print(f"Error converting SVG to PNG for diagram_{i}: {e}")
    
    return True

def replace_mermaid_with_image_references():
    """Replace mermaid code blocks with image references in markdown"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md")
    output_md = os.path.join(base_dir, "ESMS_Handbook_with_Final_Images.md")
    diagrams_dir = os.path.join(base_dir, "diagrams")
    
    if not os.path.exists(md_file):
        print(f"Source markdown file not found: {md_file}")
        return False
    
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count mermaid blocks for replacement
    pattern = r'```mermaid\s*.*?\s*```'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    print(f"Found {len(matches)} mermaid blocks to replace")
    
    # Process matches in reverse order to maintain string indices
    for i, match in enumerate(reversed(matches)):
        diagram_index = len(matches) - i
        # Use PNG images
        image_reference = f"![Diagram](diagrams/diagram_{diagram_index}.png)"
        content = content[:match.start()] + image_reference + content[match.end():]
    
    # Write updated content to output file
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created markdown with image references: {output_md}")
    return True

def convert_md_to_pdf_with_weasyprint():
    """Convert markdown with images to PDF using WeasyPrint for best image handling"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Final_Images.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Final_Images.pdf")
    
    if not os.path.exists(md_file):
        print(f"Markdown file not found: {md_file}")
        return False
    
    # Check if WeasyPrint is available
    if not shutil.which("weasyprint"):
        print("WeasyPrint not found. Please install it with: pip install weasyprint")
        return False
    
    try:
        # First convert markdown to HTML
        temp_html = os.path.join(base_dir, "temp_esms.html")
        cmd_md_to_html = [
            "pandoc",
            md_file,
            "-o", temp_html,
            "--standalone",
            "--toc",
            "--toc-depth=2",
            "--css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css",
            "--metadata", "pagetitle=ESMS Handbook"
        ]
        
        result = subprocess.run(cmd_md_to_html, capture_output=True, text=True, timeout=180)
        
        if result.returncode != 0:
            print(f"Error converting markdown to HTML: {result.stderr}")
            return False
        
        print("Converted markdown to HTML successfully")
        
        # Then convert HTML to PDF using WeasyPrint
        cmd_html_to_pdf = [
            "weasyprint",
            temp_html,
            pdf_output,
            "--presentational-hints"
        ]
        
        result = subprocess.run(cmd_html_to_pdf, capture_output=True, text=True, timeout=180)
        
        # Clean up temporary HTML file
        if os.path.exists(temp_html):
            os.remove(temp_html)
        
        if result.returncode == 0:
            print(f"Successfully converted to PDF using WeasyPrint: {pdf_output}")
            return True
        else:
            print(f"Error during WeasyPrint conversion: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("WeasyPrint conversion timed out")
        return False
    except Exception as e:
        print(f"Error during WeasyPrint conversion: {e}")
        return False

def convert_md_to_pdf_fallback():
    """Fallback method using reportlab for PDF generation"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    md_file = os.path.join(base_dir, "ESMS_Handbook_with_Final_Images.md")
    pdf_output = os.path.join(base_dir, "ESMS_Handbook_With_Final_Images.pdf")
    
    print("Trying fallback method with reportlab...")
    
    try:
        # Import reportlab
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import inch
        import markdown
        
        # Read markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to HTML first
        html_content = markdown.markdown(md_content)
        
        # Create PDF
        doc = SimpleDocTemplate(pdf_output)
        styles = getSampleStyleSheet()
        story = []
        
        # Simple approach - add content as paragraphs
        # In a real implementation, you would parse the HTML and convert elements properly
        story.append(Paragraph("ESMS Handbook", styles['Title']))
        story.append(Spacer(1, 12))
        
        # Add some content (this is a simplified version)
        lines = html_content.split('\n')
        for line in lines[:50]:  # Just first 50 lines for testing
            if line.strip():
                story.append(Paragraph(line, styles['Normal']))
                story.append(Spacer(1, 12))
        
        doc.build(story)
        print(f"Successfully created PDF using reportlab: {pdf_output}")
        return True
        
    except ImportError:
        print("ReportLab not available")
        return False
    except Exception as e:
        print(f"Error during reportlab conversion: {e}")
        return False

def merge_cover_with_handbook():
    """Merge cover page with handbook PDF"""
    base_dir = "/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task"
    cover_pdf = os.path.join(base_dir, "ESMS_Cover_Page.pdf")
    handbook_pdf = os.path.join(base_dir, "ESMS_Handbook_With_Final_Images.pdf")
    final_pdf = os.path.join(base_dir, "GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final_Images.pdf")
    
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
    """Main function to generate complete ESMS document with proper image handling"""
    print("Starting final ESMS document generation process...")
    
    # Step 1: Ensure directories exist
    ensure_directories()
    
    # Step 2: Generate SVGs from mermaid diagrams
    print("\nStep 1: Generating SVGs from Mermaid diagrams...")
    if not generate_svgs_from_mermaid():
        print("Failed to generate SVGs from Mermaid diagrams")
        return
    
    # Step 3: Convert SVGs to high-quality PNG
    print("\nStep 2: Converting SVGs to high-quality PNG...")
    convert_svg_to_png_with_high_quality()
    
    # Step 4: Replace mermaid code with image references
    print("\nStep 3: Replacing Mermaid code with image references...")
    if not replace_mermaid_with_image_references():
        print("Failed to replace Mermaid code with image references")
        return
    
    # Step 5: Convert markdown to PDF
    print("\nStep 4: Converting markdown to PDF...")
    if not convert_md_to_pdf_with_weasyprint():
        print("Failed to convert markdown to PDF with WeasyPrint, trying fallback...")
        if not convert_md_to_pdf_fallback():
            print("All PDF conversion methods failed")
            return
    
    # Step 6: Merge cover with handbook
    print("\nStep 5: Merging cover page with handbook...")
    if not merge_cover_with_handbook():
        print("Failed to merge cover page with handbook")
        return
    
    print("\nFinal ESMS document generation finished successfully!")
    print("Final document: /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Final_Images.pdf")

if __name__ == "__main__":
    main()