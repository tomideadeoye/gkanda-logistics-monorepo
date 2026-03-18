# Image Centering Solutions for ESMS Handbook PDF Generation

## Problem Analysis

The images in the ESMS Handbook PDF were not being properly centered due to several factors:

1. **CSS Limitations**: The PDF generation tool (WeasyPrint) has limited support for some CSS properties
2. **HTML Structure**: The original HTML structure didn't provide enough specificity for centering
3. **Markdown Conversion**: Pandoc's conversion process sometimes stripped or modified styling
4. **Rendering Engine**: Different PDF rendering engines handle CSS centering differently

## Solutions Implemented

### 1. Improved Image Centering Approach
- **File**: [improved_image_centering.py](improved_image_centering.py)
- **Output**: [ESMS_Handbook_with_Improved_Centering.md](ESMS_Handbook_with_Improved_Centering.md)
- **PDF**: [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf)

**Key Improvements**:
- Enhanced HTML structure with nested divs for better centering control
- More specific CSS rules with `!important` declarations
- Better width and margin handling
- Improved caption centering

### 2. Exact Image Centering Approach
- **File**: [exact_image_centering.py](exact_image_centering.py)
- **Output**: [ESMS_Handbook_with_Exact_Centering.md](ESMS_Handbook_with_Exact_Centering.md)
- **PDF**: [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf)

**Key Improvements**:
- Table-based approach for maximum compatibility
- Explicit table cell centering
- More robust CSS with comprehensive rules
- Better handling of image dimensions

## Technical Details

### Image Processing
All approaches include image optimization:
- Resize images to 800px width while maintaining aspect ratio
- Use high-quality resampling (LANCZOS)
- Preserve image quality while reducing file size

### CSS Strategies
Multiple CSS strategies were implemented:
1. **Inline Styles**: Direct styling on HTML elements
2. **External CSS**: Separate stylesheet for better organization
3. **Specificity**: Using more specific selectors to override defaults
4. **Fallbacks**: Multiple approaches to ensure centering works

### HTML Structure Improvements
1. **Nested Divs**: Better container structure for centering
2. **Table Approach**: Maximum compatibility with PDF renderers
3. **Semantic Markup**: Proper use of HTML elements

## Why Images Were Not Centered Originally

1. **CSS Specificity**: Original CSS wasn't specific enough to override default styles
2. **PDF Renderer Limitations**: WeasyPrint doesn't support all CSS centering methods
3. **Markdown Conversion**: Pandoc modified some styling during conversion
4. **Missing Declarations**: Some necessary CSS properties were missing

## Recommendations

1. **Use the Exact Centering Approach**: The table-based method provides the most reliable centering
2. **Test with Multiple Renderers**: Verify output with different PDF viewers
3. **Check Image Sizes**: Ensure images are appropriately sized before processing
4. **Validate CSS**: Test CSS rules in browser before PDF generation

## Files Generated

- [ESMS_Handbook_with_Improved_Centering.md](ESMS_Handbook_with_Improved_Centering.md) - Markdown with improved centering
- [ESMS_Handbook_With_Improved_Centering.pdf](ESMS_Handbook_With_Improved_Centering.pdf) - PDF with improved centering
- [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Improved.pdf) - Final document with improved centering
- [ESMS_Handbook_with_Exact_Centering.md](ESMS_Handbook_with_Exact_Centering.md) - Markdown with exact centering
- [ESMS_Handbook_With_Exact_Centering.pdf](ESMS_Handbook_With_Exact_Centering.pdf) - PDF with exact centering
- [GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf](GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Exact.pdf) - Final document with exact centering

## Usage

To generate a PDF with properly centered images:

```bash
# For improved centering
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 improved_image_centering.py
python3 create_pdf_with_improved_centering.py

# For exact centering (recommended)
cd /Users/mac/Documents/GitHub/gkalogistics/boi_submission_task
python3 exact_image_centering.py
python3 create_pdf_with_exact_centering.py
```

The exact centering approach is recommended as it provides the most reliable image centering across different PDF viewers and rendering engines.