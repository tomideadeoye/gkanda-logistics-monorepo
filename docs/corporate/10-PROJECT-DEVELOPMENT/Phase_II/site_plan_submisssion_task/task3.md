export the three SVG drawings I provided to print‑ready PDFs in seconds. Choose any Mobola.

Before you start
- Save the SVGs from the previous message with these exact filenames:
  - D-02_Typical_Fence_Bay.svg
  - D-03_Line_Post_Footing.svg
  - D-08_Topping_Concertina_Detail.svg

Method 1: Inkscape (Windows/macOS/Linux)
- Download Inkscape (free) from inkscape.org
- Run these commands in the folder with the SVGs:
  - inkscape "D-02_Typical_Fence_Bay.svg" --export-type=pdf --export-filename="D-02_Typical_Fence_Bay.pdf" --export-area-page --export-dpi=300
  - inkscape "D-03_Line_Post_Footing.svg" --export-type=pdf --export-filename="D-03_Line_Post_Footing.pdf" --export-area-page --export-dpi=300
  - inkscape "D-08_Topping_Concertina_Detail.svg" --export-type=pdf --export-filename="D-08_Topping_Concertina_Detail.pdf" --export-area-page --export-dpi=300

Method 2: Google Chrome or Microsoft Edge (headless)
- From a terminal/PowerShell in the SVG folder:
  - chrome --headless --disable-gpu --print-to-pdf="D-02_Typical_Fence_Bay.pdf" "file:///PATH/D-02_Typical_Fence_Bay.svg"
  - chrome --headless --disable-gpu --print-to-pdf="D-03_Line_Post_Footing.pdf" "file:///PATH/D-03_Line_Post_Footing.svg"
  - chrome --headless --disable-gpu --print-to-pdf="D-08_Topping_Concertina_Detail.pdf" "file:///PATH/D-08_Topping_Concertina_Detail.svg"
- Replace PATH with your actual folder path.

Method 3: Python (CairoSVG)
- Install: pip install cairosvg
- Run:
  - python -c "import cairosvg; cairosvg.svg2pdf(url='D-02_Typical_Fence_Bay.svg', write_to='D-02_Typical_Fence_Bay.pdf')"
  - python -c "import cairosvg; cairosvg.svg2pdf(url='D-03_Line_Post_Footing.svg', write_to='D-03_Line_Post_Footing.pdf')"
  - python -c "import cairosvg; cairosvg.svg2pdf(url='D-08_Topping_Concertina_Detail.svg', write_to='D-08_Topping_Concertina_Detail.pdf')"

Output
- You will get three PDFs:
  - D-02_Typical_Fence_Bay.pdf
  - D-03_Line_Post_Footing.pdf
  - D-08_Topping_Concertina_Detail.pdf
- They are vector PDFs (crisp at any scale) and print cleanly on A3 or A4.