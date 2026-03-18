#!/usr/bin/env python3

import os

def show_centering_comparison():
    """Show the differences in HTML structure for image centering"""
    
    print("IMAGE CENTERING COMPARISON")
    print("=" * 50)
    
    print("\n1. ORIGINAL APPROACH (Problematic):")
    print("-" * 30)
    original = """
<div style="text-align: center; margin: 30px 0;">
    <img src="diagram_1.png" alt="Diagram 1" style="max-width: 800px; width: 100%; height: auto; margin: 0 auto; display: block;">
    <p style="margin-top: 10px; font-style: italic;">Diagram 1</p>
</div>
"""
    print(original)
    
    print("\n2. IMPROVED APPROACH (Better):")
    print("-" * 30)
    improved = """
<div style="text-align: center; margin: 30px auto; width: 100%;">
    <div style="display: inline-block; text-align: center; width: 100%; max-width: 800px;">
        <img src="diagram_1.png" alt="Diagram 1" style="max-width: 100%; height: auto; margin: 0 auto; display: block;">
        <p style="margin-top: 10px; font-style: italic; text-align: center;">Diagram 1</p>
    </div>
</div>
"""
    print(improved)
    
    print("\n3. EXACT APPROACH (Best):")
    print("-" * 30)
    exact = """
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none;">
      <img src="diagram_1.png" alt="Diagram 1" style="max-width: 800px; width: 100%; height: auto;">
      <p style="margin-top: 10px; font-style: italic;">Diagram 1</p>
    </td>
  </tr>
</table>
"""
    print(exact)
    
    print("\nKEY DIFFERENCES:")
    print("-" * 30)
    print("1. ORIGINAL: Simple div with basic centering")
    print("2. IMPROVED: Nested divs with more specific CSS")
    print("3. EXACT: Table-based approach for maximum compatibility")
    print()
    print("The table-based approach works best because:")
    print("- Tables are well-supported across all PDF renderers")
    print("- Cell alignment is more reliable than CSS margin auto")
    print("- Less susceptible to CSS stripping during conversion")

def show_css_differences():
    """Show the differences in CSS approaches"""
    
    print("\n\nCSS APPROACH COMPARISON")
    print("=" * 50)
    
    print("\n1. ORIGINAL CSS (Limited):")
    print("-" * 30)
    original_css = """
img {
    max-width: 800px !important;
    width: 100% !important;
    height: auto !important;
    margin: 0 auto !important;
    display: block !important;
}
"""
    print(original_css)
    
    print("\n2. IMPROVED CSS (Better):")
    print("-" * 30)
    improved_css = """
/* Improved centering for image containers */
div[style*="text-align: center"] {
    text-align: center !important;
    margin: 30px auto !important;
    width: 100% !important;
}

/* Improved image styling for precise centering */
img {
    max-width: 800px !important;
    width: auto !important;
    height: auto !important;
    margin: 0 auto !important;
    display: block !important;
    text-align: center !important;
}

/* Center captions */
p[style*="font-style: italic"] {
    margin-top: 10px !important;
    font-style: italic !important;
    text-align: center !important;
    width: 100% !important;
    display: block !important;
}
"""
    print(improved_css)
    
    print("\n3. EXACT CSS (Best):")
    print("-" * 30)
    exact_css = """
/* Table-based centering */
table {
    width: 100% !important;
    border-collapse: collapse !important;
    margin: 30px 0 !important;
}

td {
    text-align: center !important;
    border: none !important;
    padding: 0 !important;
}

img {
    max-width: 800px !important;
    width: 100% !important;
    height: auto !important;
    display: block !important;
    margin: 0 auto !important;
}

p {
    margin-top: 10px !important;
    font-style: italic !important;
    text-align: center !important;
}
"""
    print(exact_css)

def main():
    """Main function to demonstrate centering differences"""
    show_centering_comparison()
    show_css_differences()
    
    print("\n\nRECOMMENDATION:")
    print("=" * 50)
    print("Use the EXACT approach (table-based) for maximum compatibility")
    print("across different PDF renderers and viewers.")

if __name__ == "__main__":
    main()