# Image Centering Solutions for ESMS Handbook

## Problem
Images in the ESMS Handbook PDF were not being properly centered due to limitations in CSS support by the PDF rendering engine (WeasyPrint) and the HTML structure used in the markdown files.

## Root Causes
1. **CSS Limitations**: WeasyPrint doesn't fully support all CSS centering methods
2. **HTML Structure**: Original HTML structure wasn't specific enough for reliable centering
3. **Markdown Conversion**: Pandoc's conversion process sometimes modified styling
4. **Renderer Differences**: Different PDF viewers render centering differently

## Solutions Provided

### 1. Improved Image Centering (Recommended for balance of simplicity and effectiveness)
- **Script**: [improved_image_centering.py](improved_image_centering.py)
- **Markdown Output**: [ESMS_Handbook_with_Improved_Centering.md](ESMS_Handbook_with_Improved_Centering.md)
- **Final PDF**: [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf)

### 2. Exact Image Centering (Recommended for maximum compatibility)
- **Script**: [exact_image_centering.py](exact_image_centering.py)
- **Markdown Output**: [ESMS_Handbook_with_Exact_Centering.md](ESMS_Handbook_with_Exact_Centering.md)
- **Final PDF**: [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf)

## How to Use

### For Improved Centering:
```bash
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 improved_image_centering.py
python3 create_pdf_with_improved_centering.py
```

### For Exact Centering (Best Results):
```bash
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 exact_image_centering.py
python3 create_pdf_with_exact_centering.py
```

## Technical Details

### Image Processing
All solutions include:
- Image resizing to 800px width while maintaining aspect ratio
- High-quality resampling using LANCZOS algorithm
- Optimized file sizes for better PDF performance

### HTML Structure Improvements
1. **Nested Div Approach** (Improved): Better container structure with explicit centering
2. **Table Approach** (Exact): Maximum compatibility using HTML tables for positioning

### CSS Enhancements
- More specific CSS selectors with `!important` declarations
- Comprehensive styling rules for images and captions
- Fallback methods to ensure centering works across different renderers

## Verification
You can verify the generated files using:
```bash
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 simple_verification.py
```

## Files Generated

### Markdown Files:
- [ESMS_Handbook_with_Precise_Images.md](ESMS_Handbook_with_Precise_Images.md) - Original approach
- [ESMS_Handbook_with_Improved_Centering.md](ESMS_Handbook_with_Improved_Centering.md) - Improved approach
- [ESMS_Handbook_with_Exact_Centering.md](ESMS_Handbook_with_Exact_Centering.md) - Exact approach

### PDF Files:
- [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Precise.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Precise.pdf) - Original approach result
- [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf) - Improved approach result
- [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf) - Exact approach result

## Recommendation
Use the **Exact Centering Approach** for the best results, as the table-based method provides maximum compatibility across different PDF viewers and rendering engines.