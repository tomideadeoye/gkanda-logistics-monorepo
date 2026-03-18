# Why Images Were Not Being Properly Centered and How We Fixed It

## The Problem

Images in the ESMS Handbook PDF were not being properly centered despite using CSS centering techniques like `margin: 0 auto` and `text-align: center`. This was a frustrating issue that affected the document's professional appearance.

## Root Causes

### 1. **PDF Renderer Limitations**
- **WeasyPrint**, the tool used to convert HTML to PDF, has limited CSS support
- Many CSS properties that work in browsers don't work the same way in PDF renderers
- `margin: 0 auto` is not reliably supported for centering in WeasyPrint

### 2. **HTML Structure Issues**
- Simple div-based centering relies on proper parent-child relationships
- The original HTML structure wasn't specific enough for PDF renderers
- Missing explicit width declarations caused unpredictable behavior

### 3. **Markdown Conversion Artifacts**
- **Pandoc** modifies HTML during markdown conversion
- Some inline styles were stripped or altered
- Class and ID attributes might be modified during processing

### 4. **CSS Specificity Problems**
- Original CSS rules weren't specific enough to override defaults
- Missing `!important` declarations allowed other styles to take precedence
- Conflicting styles from GitHub Markdown CSS interfered with centering

## Our Solutions

### Solution 1: Improved Nested Div Approach
```html
<!-- Better than original but still not perfect -->
<div style="text-align: center; margin: 30px auto; width: 100%;">
    <div style="display: inline-block; text-align: center; width: 100%; max-width: 800px;">
        <img src="diagram.png" style="max-width: 100%; height: auto; margin: 0 auto; display: block;">
        <p>Caption</p>
    </div>
</div>
```

### Solution 2: Table-Based Approach (BEST SOLUTION)
```html
<!-- Most reliable method for PDF centering -->
<table style="width: 100%; border-collapse: collapse; margin: 30px 0;">
  <tr>
    <td style="text-align: center; border: none; padding: 0;">
      <img src="diagram.png" style="max-width: 800px; width: 100%; height: auto; display: block; margin: 0 auto;">
      <p style="margin-top: 10px; font-style: italic; text-align: center;">Caption</p>
    </td>
  </tr>
</table>
```

## Why the Table-Based Approach Works Best

### 1. **Universal Support**
- Tables are supported by all PDF renderers
- Cell alignment (`text-align: center`) is more reliable than CSS margins
- Less likely to be affected by CSS stripping

### 2. **Explicit Control**
- Table cells provide a clear container with predictable behavior
- Padding and border controls are more reliable
- Width declarations work consistently

### 3. **Renderer Compatibility**
- Works with WeasyPrint, wkhtmltopdf, and other PDF tools
- Less susceptible to differences between rendering engines
- Maintains consistency across different PDF viewers

## Technical Implementation Details

### Image Optimization
- Resize images to 800px width while maintaining aspect ratio
- Use high-quality resampling (LANCZOS) for best results
- Preserve transparency and quality with PNG format

### CSS Strategy
- Use `!important` declarations to ensure styles aren't overridden
- Provide fallback methods for different properties
- Minimize reliance on complex CSS features

### HTML Structure
- Create explicit containers with defined dimensions
- Use semantic markup that's friendly to PDF renderers
- Avoid complex nested structures that might be simplified

## Results

Our solutions have successfully addressed the image centering issue:

1. **Improved Approach**: Better than original but may still have issues in some PDF viewers
2. **Exact Approach**: Table-based method that works reliably across all platforms
3. **Final Solution**: Comprehensive approach combining image optimization with table-based centering

## Recommendation

Use the **table-based approach** (Exact Centering) for maximum compatibility:

- Most reliable across different PDF renderers
- Consistent results in all PDF viewers
- Easiest to debug and maintain

The table-based method may seem like a step back from modern CSS, but it's actually the most pragmatic solution for PDF generation where CSS support is limited.