# RTF Formatting Fix

This script fixes the issue where RTF formatting codes like `{\fonttbl{\f0 Times New Roman;}{\f1 Arial;}}` were appearing in the physical print PDFs.

## Problem
The original RTF to PDF conversion was not properly stripping RTF formatting codes, causing them to appear in the printed documents.

## Solution
The `fix_rtf_formatting.py` script:
1. Extracts RTF files from the ZIP package
2. Uses the `striprtf` library to completely remove all RTF formatting codes
3. Converts the clean text to properly formatted PDFs using ReportLab
4. Outputs clean PDFs to `NPA_Submission_Package/Physical_Prints_A4_Clean/`

## Usage
```bash
python fix_rtf_formatting.py
```

## Dependencies
- striprtf (installed via pip)
- reportlab (already in requirements.txt)

The clean PDFs in the `Physical_Prints_A4_Clean` directory no longer contain any RTF formatting codes and are suitable for professional printing.