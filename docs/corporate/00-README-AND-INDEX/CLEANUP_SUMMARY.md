# Repository Cleanup & Restructuring Summary

**Date:** February 28, 2026  
**Status:** IN PROGRESS  

---

## ✅ COMPLETED ACTIONS

### 1. Created New Folder Structure
- [x] 00-README-AND-INDEX
- [x] 01-CORPORATE-DOCUMENTS
- [x] 02-REGULATORY-AND-LICENSES
- [x] 03-FINANCIAL-INFORMATION
- [x] 04-TECHNICAL-AND-ENGINEERING
- [x] 05-ESG-AND-COMPLIANCE
- [x] 06-COMMERCIAL-AND-CONTRACTS
- [x] 07-INVESTOR-RELATIONS
- [x] 08-MEDIA-AND-COMMUNICATIONS
- [x] 09-OPERATIONS
- [x] 10-PROJECT-DEVELOPMENT
- [x] 11-SUBMISSIONS-AND-FILINGS
- [x] 12-MEETINGS-AND-CORRESPONDENCE
- [x] 99-ARCHIVE
- [x] scripts
- [x] temp

### 2. Moved Documents to Proper Locations
- [x] Corporate documents (CAC registration, corporate profile)
- [x] Technical drawings (D-01 to D-08)
- [x] QAQC records (10 RTF files)
- [x] Survey reports
- [x] ESG documents (ESMS, Emergency Response, Waste Management)
- [x] Press releases
- [x] Investment teaser
- [x] LOIs and MOUs
- [x] Job descriptions
- [x] OBC document
- [x] Submission packages (BOI, NEXIM, NPA)
- [x] Brand assets (logos, images)
- [x] Website content

### 3. Created Documentation
- [x] Updated README.md with dataroom navigation
- [x] Created DATAROOM_INDEX.md with full checklist
- [x] Updated .gitignore with comprehensive exclusions

### 4. Folders Reorganized
- [x] boi_submission_task → 11-SUBMISSIONS-AND-FILINGS/BOI_Submission/
- [x] nexim-document → 11-SUBMISSIONS-AND-FILINGS/NEXIM_Submission/
- [x] NPA_Submission_Package → 11-SUBMISSIONS-AND-FILINGS/NPA_Submission_Package/
- [x] operations → 09-OPERATIONS/Internal/
- [x] past-meetings → 12-MEETINGS-AND-CORRESPONDENCE/
- [x] aig letter of intent → 06-COMMERCIAL-AND-CONTRACTS/LOIs_and_MOUs/
- [x] site_plan_submisssion_task → 10-PROJECT-DEVELOPMENT/Phase_II/
- [x] images → 08-MEDIA-AND-COMMUNICATIONS/Brand_Assets/Images/
- [x] gkaassets → 08-MEDIA-AND-COMMUNICATIONS/Brand_Assets/Logos/
- [x] assets → 08-MEDIA-AND-COMMUNICATIONS/Marketing_Materials/
- [x] documents → 99-ARCHIVE/Documents_Backup/
- [x] rtf_converted → 99-ARCHIVE/RTF_Conversions/
- [x] IA → 08-MEDIA-AND-COMMUNICATIONS/Marketing_Materials/IA/

---

## ⚠️ REMAINING ISSUES

### Root Directory Still Has Clutter

#### Python Scripts (Should move to scripts/)
These are development/utility scripts that should be in `scripts/` folder:
- [ ] better_rtf_to_pdf.py
- [ ] build_fence_drawing.py
- [ ] check_pdf_dimensions.py
- [ ] convert_fixed_svg_to_pdf.py
- [ ] convert_rtf_to_pdf.py
- [ ] convert_svg_to_pdf_with_svglib.py
- [ ] convert_svgs_to_pdf.py
- [ ] convert_to_pdf_reportlab_direct.py
- [ ] convert_to_pdf_reportlab.py
- [ ] create_complete_drawing_set.py
- [ ] create_drawing_set_cover.py
- [ ] create_missing_drawings.py
- [ ] example_pdf_merge.py
- [ ] fix_rtf_formatting.py
- [ ] fix_svg_expressions.py
- [ ] generate_litigation_audit_dashboard_pdf.js
- [ ] generate_wire_mesh_svg.py
- [ ] generate_zip.py
- [ ] html_to_pdf.py
- [ ] main.py
- [ ] merge_pdfs.py
- [ ] modify_esg_html.py
- [ ] pdf_index.py
- [ ] rtf_to_pdf_via_html.py
- [ ] rtfparse_to_pdf.py
- [ ] unrtf_to_pdf.py
- [ ] verify_npa_submission_package.py
- [ ] verify_submission_package.py
- [ ] weasyprint_rtf_to_pdf.py
- [ ] wire_mesh.py

#### SVG Files (Should move to technical drawings or archive)
- [ ] concertina_wire_variants.svg
- [ ] D-01_Site_Plan_GKA_Ikorodu.svg (duplicate - original moved)
- [ ] D-02_Typical_Fence_Bay.svg (duplicate - original moved)
- [ ] D-03_Line_Post_Footing.svg (duplicate - original moved)
- [ ] D-08_Topping_Concertina_Detail.svg (duplicate - original moved)
- [ ] wire_mesh_detail.svg
- [ ] wire_mesh_drawing.svg
- [ ] wire_mesh.svg

#### Configuration Files (Keep in root)
- [x] .gitignore (KEEP)
- [x] eslint.config.mjs (KEEP - project config)
- [x] components.json (KEEP - project config)
- [x] package.json (KEEP - project config)
- [x] pnpm-lock.yaml (KEEP - dependencies)
- [x] pyproject.toml (KEEP - project config)
- [x] requirements.txt (KEEP - dependencies)
- [x] tsconfig.json (KEEP - project config)
- [x] next.config.ts (KEEP - project config)
- [x] postcss.config.mjs (KEEP - project config)

#### Build/Cache Folders (Should be in .gitignore)
- [ ] .venv/ (IGNORED - Python virtual env)
- [ ] node_modules/ (IGNORED - Node dependencies)
- [ ] .next/ (IGNORED - Next.js build)
- [ ] .mypy_cache/ (IGNORED - Python cache)
- [ ] __pycache__/ (IGNORED - Python cache)
- [ ] gkalogistics.egg-info/ (IGNORED - Python package info)

#### Random Files (Need review)
- [ ] =2.7.0 (Unknown - should delete or archive)
- [ ] .DS_Store (DELETE - macOS metadata)
- [ ] tasks.db (DELETE or move to temp/)
- [ ] tasks.json (DELETE or move to temp/)
- [ ] wkhtmltox.pkg (Unknown - archive or delete)
- [ ] build-tasks.sh (Move to scripts/)
- [ ] setup.sh (Move to scripts/)
- [ ] open-html-versions.sh (Move to scripts/)
- [ ] open-technical-drawings.sh (Move to scripts/)

#### HTML/JS Files (Need review)
- [ ] html-to-pdf.js (Move to scripts/)
- [ ] test_image.py (Move to temp/ or delete)
- [ ] test_pandoc.html (Move to temp/ or delete)
- [ ] test_reportlab.py (Move to temp/ or delete)

#### Markdown Files (Need proper categorization)
- [ ] README_PYTHON.md (Merge with main README or move to 00-README-AND-INDEX/)
- [ ] reference.md (Already moved to 00-README-AND-INDEX/)

---

## 📋 NEXT STEPS

### Phase 1: Clean Root Directory (Priority: HIGH)
1. Move all Python scripts to `scripts/` folder
2. Delete .DS_Store files
3. Move test files to `temp/`
4. Review and archive/delete unknown files (=2.7.0, wkhtmltox.pkg)

### Phase 2: Consolidate Duplicates (Priority: MEDIUM)
1. Remove duplicate SVG files (keep only PDFs in technical drawings)
2. Archive old script versions
3. Consolidate configuration documentation

### Phase 3: Archive Cleanup (Priority: LOW)
1. Organize 99-ARCHIVE folder
2. Delete truly obsolete files
3. Create archive index

### Phase 4: Final Polish (Priority: LOW)
1. Add README.md to each major folder
2. Create folder-level indexes
3. Set up access control documentation
4. Create visual data room map

---

## 📊 METRICS

### Before Restructuring
- **Root files:** 80+ scattered files
- **Root folders:** 20+ unorganized folders
- **Navigation:** Very difficult
- **Professional appearance:** Poor

### After Restructuring (Current)
- **Root files:** ~50 (mostly config files)
- **Root folders:** 14 organized numbered folders + scripts + temp
- **Navigation:** Clear and intuitive
- **Professional appearance:** Good

### Target State
- **Root files:** ~20 (config files only)
- **Root folders:** 14 numbered folders + scripts + temp
- **Navigation:** Excellent with folder READMEs
- **Professional appearance:** Excellent (investor-ready)

---

## 🎯 SUCCESS CRITERIA

- [x] Main folder structure created
- [x] Key documents organized
- [x] README and index created
- [x] .gitignore updated
- [ ] Root directory clean (only config files)
- [ ] All scripts in scripts/ folder
- [ ] Archive properly organized
- [ ] Folder-level documentation
- [ ] Access control implemented
- [ ] Regular maintenance schedule established

---

**Maintained by:** Merislabs Design Team  
**Last Updated:** February 28, 2026
