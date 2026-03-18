# NPA Site Plan Submission - Requirements Summary

## Task Overview
**Task ID:** 8  
**Title:** NPA Site Plan Submission  
**Description:** Prepare and submit complete documentation package for perimeter security fence and gates installation at NPA Lighter Terminal, Ikorodu (Lease Reg 007/2025)  
**Status:** In-progress (20% complete)  
**Deadline:** October 15, 2025  

## Overall Project Scope
- **Client**: GK & A Logistics Services Ltd
- **Location**: NPA Lighter Terminal, Ikorodu
- **System**: Perimeter security fence (2.44m high wire-mesh with barbed-wire topping) and sliding gates
- **Engineering**: Prepared by RYT-Coxt Logics Limited
- **Submission Date**: 26 September 2025
- **Status**: As-Built - Issued for Approval

## Key Technical Specifications
- **Wind Loading**: V=30 m/s, net pressure p=331 N/m²
- **Post Capacity**: SHS 60×60×3.0 mm S355, MRd≈4.4-4.5 kNm
- **Foundations**: Line posts 350×350×900 mm C25/30, ends/corners 450×450×1000 mm
- **Coatings**: HDG ≥85 μm + duplex topcoat ≥160-200 μm DFT
- **Earthing**: 16 mm² bonds, 2.4 m rods at ≤100 m intervals

## Already Implemented Conversions and Files

### Generated PDF Files
- **Technical Drawings** (in [pdf_outputs](file:///Users/mac/Documents/GitHub/gkalogistics/pdf_outputs) directory):
  - D-02_Typical_Fence_Bay.pdf
  - D-03_Line_Post_Footing.pdf
  - D-08_Topping_Concertina_Detail.pdf

- **Site Plan Documents** (in site_plan_submisssion_task directory):
  - Site_Plan_GKA_Ikorodu (1).pdf (site plan drawing)
  - GK_A_Fence_AsBuilt.pdf (typical wire-mesh panel)
  - STRUCTURAL DESIGN REPORT.pdf

### Generated Submission Package
- **ZIP File**: GKAL_As-Built_Submission_2025-09-26.zip (contains all 19 RTF documents)
- **Base64 Version**: GKAL_As-Built_Submission_2025-09-26_base64.txt (for secure transfer)

### SVG Source Files
- D-02_Typical_Fence_Bay.svg
- D-03_Line_Post_Footing.svg
- D-08_Topping_Concertina_Detail.svg

## Key Tasks to Complete

### 1. Generate the Main Submission ZIP Package
- **Script to Create**: `build_gkal_submission_zip.py` (already run, files exist)
- **Purpose**: Creates `GKAL_As-Built_Submission_2025-09-26.zip` containing all RTF documents
- **Output**: ZIP file + base64 encoded version for transfer
- **Contents**: 19 RTF documents (letters, statements, logs, covers) + README

### 2. Create Technical Drawings PDFs
- **Drawing D-01**: Site Plan (SVG provided in `siteplan.md`, PDF already generated)
- **Drawing D-02**: Typical Fence Bay Elevation (SVG in `task5.md`, PDF already generated)
- **Drawing D-03**: Line Post Footing Section (SVG in `task5.md`, PDF already generated) 
- **Drawing D-08**: Topping Bracket and Concertina Detail (SVG in `task5.md`, PDF already generated)
- **Additional Drawing**: Typical Wire-Mesh Panel (Python script in `task2.md`, PDF already generated)

**Conversion Methods** (already implemented using CairoSVG):
- Python: `python -c "import cairosvg; cairosvg.svg2pdf(url='filename.svg', write_to='filename.pdf')"`

### 3. Generate As-Built Survey Summary
- Includes coordinate table, alignment details, tolerances, and photo references

## Document Organization Structure

### Volume 1: Report and Records (A4 Binder)
**00 Cover Letters**
- Cover Letter (introduction and compliance declaration)
- Transmittal/Index (submission details)
- Site Acceptance Request

**01 Compliance Statement**
- Structural compliance declaration against Nigerian Building Code, BS EN standards, ISO standards

**02 Structural Calculations Summary**
- Design basis (wind loading, soil conditions)
- Analysis summary (post bending moments, foundation stability)
- Materials specifications

**03 Materials & Certificates**
- Mesh and panels certificates
- Steel posts/rails MTRs
- Gates and hardware CoCs
- Concrete delivery tickets and cube results
- Coatings (HDG and duplex DFT logs)
- Anchors/bolts/fixings certificates

**04 QA/QC Logs**
- Concrete cube tests (7/28-day results)
- Coating DFT readings
- HDG thickness measurements
- Bolt torque checks
- Anchor pull tests

**05 HSE**
- Method statements, risk assessments, permits

**06 As-Built Survey & Photos**
- Survey summary with coordinates
- Photo documentation

**07 O&M and Warranty**
- Maintenance plan (inspections, lubrication, corrosion control)
- Warranty letter (12-24 months coverage)

**08 Permits/Approvals**
- Construction permits, NPA clearances

**09 Transmittal/Register**
- Final submission register

### Volume 2: Drawings (A3 Binder)
- D-01: General Layout Plan and Key Plan
- D-02: Fence Elevations and Typical Bay  
- D-03: Line Post and Mesh Fixing Details
- D-04: End/Corner/Strainer Post Details and Bracing
- D-05: Gate GA and Foundations/Plinth Details
- D-06: Gate Hardware (Receivers/Guides/Stops)
- D-07: Foundation Schedules and Reinforcement (Gate Bases)
- D-08: Earthing and Bonding Details
- D-09: Notes and Schedules (Materials/Hardware)
- D-10: Typical Sections at Drainage/Crossings
- D-11: As-Built Survey Alignment and Coordinates

## Subtasks Progress

1. **Prepare Site Plan Drawing** - COMPLETED
   - Convert SVG site plan to PDF format
   - Verify all dimensions and gate locations

2. **Convert Technical Drawings** - COMPLETED
   - Convert 3 SVG technical drawings to PDF format

3. **Create Submission Package** - COMPLETED
   - Package all RTF documents into ZIP file using build_gkal_submission_zip.py script

4. **Review Compliance Documents** - PENDING
   - Verify all compliance statements, structural calculations, and QA records

5. **Submit to NPA** - PENDING
   - Submit completed ZIP package to Nigerian Ports Authority

## Submission Organization Steps

1. **Compile All Documents**
   - Run the ZIP generation script to create the complete RTF package
   - Convert all SVG drawings to PDF format
   - Gather QA/QC records, survey data, and certificates

2. **Physical Organization**
   - **Binder 1 (A4)**: Report documents with colored divider tabs
   - **Binder 2 (A3)**: Drawing set with cover sheet
   - Include binder covers, spines, and spine labels as provided in the RTF templates

3. **Digital Submission**
   - Submit the ZIP file containing all RTFs
   - Provide PDFs of drawings separately or included in ZIP
   - Include base64 encoded version for secure transfer if needed

4. **Quality Checks**
   - Verify all signatures and dates (26 September 2025)
   - Ensure compliance with NPA Lands & Asset Department requirements
   - Cross-reference drawing numbers and titles
   - Confirm QA/QC logs are complete with actual test results

## Contacts
- Omobola Abiru (omobola@gkalogistics.com)
- Mr. Temidayo (temidayo@rytcoxt.com)

## File References
- Site plan submission directory: `site_plan_submisssion_task/`
- Sample content directory: `site_plan_submisssion_task/content to submit sample/`

## Submission Process
1. Submit to NPA Executive Director, Engineering and Technical Services
2. Attention: General Manager, Lands & Asset Department; Physical Planning
3. Request joint site inspection for acceptance
4. Provide contact details for inspection coordination