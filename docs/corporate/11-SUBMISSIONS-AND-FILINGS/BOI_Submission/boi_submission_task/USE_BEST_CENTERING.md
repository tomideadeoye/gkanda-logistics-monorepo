# How to Use the Best Image Centering Solution

## Quick Start

To generate a PDF with properly centered images, follow these steps:

### 1. Run the Final Solution Script
```bash
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 final_image_centering_solution.py
```

This will:
- Optimize all diagram images
- Create [ESMS_Handbook_with_Best_Centering.md](ESMS_Handbook_with_Best_Centering.md)
- Generate [best_centering_style.css](best_centering_style.css)

### 2. Convert to HTML
```bash
pandoc ESMS_Handbook_with_Best_Centering.md \
  -o temp_best.html \
  --standalone \
  --toc \
  --toc-depth=2 \
  --css=https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css \
  --css=best_centering_style.css \
  --metadata pagetitle='ESMS Handbook'
```

### 3. Convert to PDF
```bash
weasyprint temp_best.html \
  ESMS_Handbook_With_Best_Centering.pdf \
  --presentational-hints \
  --optimize-images \
  --full-fonts
```

### 4. Merge with Cover Page
Use your existing merge scripts to combine with the cover page.

## Why This Works

### Table-Based Centering
The solution uses HTML tables for image positioning because:

1. **Universal Support**: Tables work in all PDF renderers
2. **Reliable Alignment**: Cell text-align is more dependable than CSS margins
3. **Consistent Results**: Works the same way across different platforms

### Image Optimization
Images are resized to 800px width while maintaining aspect ratio, ensuring:
- Fast PDF generation
- Good quality for printing
- Reasonable file sizes

### Robust CSS
The CSS uses `!important` declarations to ensure styles aren't overridden by:
- GitHub Markdown CSS
- Browser default styles
- PDF renderer defaults

## Files Generated

- **[ESMS_Handbook_with_Best_Centering.md](ESMS_Handbook_with_Best_Centering.md)**: Markdown with table-based image centering
- **[best_centering_style.css](best_centering_style.css)**: CSS optimized for PDF rendering
- **Optimized Images**: Resized diagram images in the `diagrams` folder

## Troubleshooting

If images still aren't centered:

1. **Check image paths**: Ensure all image paths are correct
2. **Verify CSS loading**: Make sure the CSS file is being loaded
3. **Test in browser**: Open the HTML file in a browser to verify centering
4. **Check PDF viewer**: Some PDF viewers may not display centering perfectly

## Alternative Approaches

If you prefer other methods:

1. **Improved Centering**: Use the improved_image_centering.py script
2. **Exact Centering**: Use the exact_image_centering.py script

But the table-based approach in final_image_centering_solution.py is recommended for maximum compatibility.