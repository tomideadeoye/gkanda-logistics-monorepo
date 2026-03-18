Mobola I sent a dimensioned SVG drawings for your fence to your confirmed specification. Save each code block as a .svg file and open/print at any scale

Drawing D-02 – Typical Fence Bay (2,400 mm c/c posts; 2,700 mm mesh height; 600 mm concertina on 45° brackets; 50 mm ground clearance)
Save as: D-02_Typical_Fence_Bay.svg
<svg xmlns="http://www.w3.org/2000/svg" width="3600" height="3800" viewBox="0 0 3600 3800">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/>
    </marker>
    <style>
      .line{stroke:#222;stroke-width:6;fill:none}
      .thin{stroke:#555;stroke-width:3;fill:none}
      .dim{stroke:#222;stroke-width:4;fill:none;marker-start:url(#arrow);marker-end:url(#arrow)}
      .txt{font: 48px sans-serif; fill:#111}
      .title{font: 56px sans-serif; font-weight:700}
      .note{font: 40px sans-serif; fill:#333}
      .mesh{stroke:#777;stroke-width:2}
    </style>
  </defs>

  <!-- Title block -->
  <rect x="100" y="3300" width="3400" height="360" fill="#fff" stroke="#222" stroke-width="4"/>
  <text x="140" y="3400" class="title">D-02 Typical Fence Bay – Elevation (Not to scale)</text>
  <text x="140" y="3460" class="txt">Posts: SHS 75×75×5 mm | Bay: 2,400 mm c/c | Mesh: 2,700 mm high, 50×50×4.0 mm</text>
  <text x="140" y="3520" class="txt">Footing: 450×500×600 mm (C25/30) | Ground clearance: 50 mm | Topping: 600 mm concertina on 45° brackets (300 mm proj.)</text>
  <text x="140" y="3580" class="note">Finish: Hot-dip galvanized (ISO 1461); optional duplex coating. Anti-tamper SS fixings.</text>

  <!-- Ground line -->
  <line x1="100" y1="3000" x2="3500" y2="3000" class="line"/>
  <text x="3100" y="2960" class="txt">Finished Ground (FG)</text>

  <!-- Posts -->
  <rect x="300" y="3000" width="75" height="-2750" fill="#ddd" stroke="#222" stroke-width="6"/>
  <rect x="2700" y="3000" width="75" height="-2750" fill="#ddd" stroke="#222" stroke-width="6"/>

  <!-- Mesh panel (2,700 mm high, 50 mm clearance) -->
  <rect x="338" y="2950" width="2399" height="-2700" fill="none" stroke="#555" stroke-width="4"/>
  <!-- Indicative mesh grid -->
  <g class="mesh" opacity="0.35">
    <!-- verticals -->
    <g>
      <!-- draw every 200 mm for clarity -->
      <line x1="538" y1="2950" x2="538" y2="250" class="mesh"/>
      <line x1="938" y1="2950" x2="938" y2="250" class="mesh"/>
      <line x1="1338" y1="2950" x2="1338" y2="250" class="mesh"/>
      <line x1="1738" y1="2950" x2="1738" y2="250" class="mesh"/>
      <line x1="2138" y1="2950" x2="2138" y2="250" class="mesh"/>
      <line x1="2538" y1="2950" x2="2538" y2="250" class="mesh"/>
    </g>
    <!-- horizontals -->
    <g>
      <line x1="338" y1="2550" x2="2737" y2="2550" class="mesh"/>
      <line x1="338" y1="2150" x2="2737" y2="2150" class="mesh"/>
      <line x1="338" y1="1750" x2="2737" y2="1750" class="mesh"/>
      <line x1="338" y1="1350" x2="2737" y2="1350" class="mesh"/>
      <line x1="338" y1="950"  x2="2737" y2="950"  class="mesh"/>
      <line x1="338" y1="550"  x2="2737" y2="550"  class="mesh"/>
    </g>
  </g>

  <!-- 45° brackets with 300 mm projection -->
  <g stroke="#222" stroke-width="6" fill="none">
    <line x1="338"  y1="250" x2="338+212"  y2="250-212" />
    <line x1="2737" y1="250" x2="2737+212" y2="250-212" />
  </g>
  <text x="420" y="120" class="txt">45° bracket, 300 mm projection</text>

  <!-- Concertina razor wire (Ø600) – symbolic loops -->
  <g stroke="#222" stroke-width="4" fill="none" opacity="0.9">
    <circle cx="650"  cy="40" r="300"/>
    <circle cx="1150" cy="40" r="300"/>
    <circle cx="1650" cy="40" r="300"/>
    <circle cx="2150" cy="40" r="300"/>
  </g>
  <text x="130" y="60" class="txt">600 mm Ø concertina (SS ties @ 300 mm)</text>

  <!-- Dimensions -->
  <!-- Bay width 2400 -->
  <line x1="338" y1="3120" x2="2737" y2="3120" class="dim"/>
  <text x="1500" y="3180" class="txt">2,400 mm (post to post)</text>
  <!-- Mesh height 2,700 -->
  <line x1="2850" y1="2950" x2="2850" y2="250" class="dim"/>
  <text x="2880" y="1620" class="txt" transform="rotate(90,2880,1620)">2,700 mm mesh height</text>
  <!-- Ground clearance 50 -->
  <line x1="600" y1="3000" x2="600" y2="2950" class="dim"/>
  <text x="630" y="2980" class="txt" transform="rotate(90,630,2980)">50 mm ground clearance</text>
</svg>

Drawing D-03 – Line Post Footing (Section)
Save as: D-03_Line_Post_Footing.svg
<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1600" viewBox="0 0 2400 1600">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/>
    </marker>
    <style>
      .line{stroke:#222;stroke-width:6;fill:none}
      .dim{stroke:#222;stroke-width:4;fill:none;marker-start:url(#arrow);marker-end:url(#arrow)}
      .txt{font: 48px sans-serif; fill:#111}
      .title{font: 56px sans-serif; font-weight:700}
      .conc{fill:#e9e9e9;stroke:#222;stroke-width:4}
      .steel{fill:#cfd8dc;stroke:#222;stroke-width:6}
    </style>
  </defs>

  <!-- Title -->
  <text x="60" y="120" class="title">D-03 Line Post Footing – Section</text>
  <text x="60" y="180" class="txt">Footing 450×500×600 mm deep (C25/30); Post SHS 75×75×5 mm; Embed ≈ 500 mm; Cover ≥ 50 mm</text>

  <!-- Ground line -->
  <line x1="60" y1="600" x2="2340" y2="600" class="line"/>
  <text x="1900" y="560" class="txt">FG</text>

  <!-- Footing block -->
  <rect x="900" y="600" width="500" height="600" class="conc"/>
  <text x="920" y="1240" class="txt">C25/30</text>

  <!-- Blinding -->
  <rect x="900" y="1200" width="500" height="50" fill="#ddd" stroke="#222" stroke-width="2"/>
  <text x="1420" y="1230" class="txt">50 mm blinding</text>

  <!-- Post -->
  <rect x="1112.5" y="600" width="75" height="-500" class="steel"/>
  <text x="1200" y="200" class="txt">SHS 75×75×5 (galv.)</text>

  <!-- Rebar (indicative) -->
  <line x1="960" y1="1180" x2="960" y2="620" class="line"/>
  <line x1="1340" y1="1180" x2="1340" y2="620" class="line"/>
  <text x="60" y="1000" class="txt">Nominal cage (ties), maintain ≥50 mm cover</text>

  <!-- Dimensions -->
  <line x1="900" y1="1300" x2="1400" y2="1300" class="dim"/>
  <text x="1080" y="1380" class="txt">500 mm (L)</text>
  <line x1="860" y1="600" x2="860" y2="1200" class="dim"/>
  <text x="700" y="960" class="txt" transform="rotate(90,700,960)">600 mm depth</text>
  <line x1="860" y1="600" x2="860" y2="100" class="dim"/>
  <text x="700" y="350" class="txt" transform="rotate(90,700,350)">Post embed ≈ 500 mm</text>
  <line x1="900" y1="560" x2="1400" y2="560" class="dim"/>
  <text x="1040" y="520" class="txt">450 mm (W)</text>
</svg>

Drawing D-08 – Topping Bracket and Concertina Detail
Save as: D-08_Topping_Concertina_Detail.svg
<svg xmlns="http://www.w3.org/2000/svg" width="2600" height="1800" viewBox="0 0 2600 1800">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#222"/>
    </marker>
    <style>
      .line{stroke:#222;stroke-width:6;fill:none}
      .dim{stroke:#222;stroke-width:4;fill:none;marker-start:url(#arrow);marker-end:url(#arrow)}
      .txt{font: 48px sans-serif; fill:#111}
      .title{font: 56px sans-serif; font-weight:700}
    </style>
  </defs>

  <!-- Title -->
  <text x="60" y="120" class="title">D-08 Topping Bracket and Concertina – Elevation & Side</text>
  <text x="60" y="180" class="txt">45° bracket, 300 mm projection; Concertina 600 mm Ø; SS ties @ 300 mm</text>

  <!-- Elevation view -->
  <text x="60" y="280" class="txt">Elevation</text>
  <!-- Post -->
  <rect x="200" y="400" width="120" height="900" fill="#ddd" stroke="#222" stroke-width="6"/>
  <!-- Bracket at 45° -->
  <line x1="260" y1="400" x2="260+212" y2="400-212" class="line"/>
  <!-- Concertina circles -->
  <circle cx="800" cy="160" r="300" fill="none" stroke="#222" stroke-width="6"/>
  <circle cx="1250" cy="160" r="300" fill="none" stroke="#222" stroke-width="6"/>
  <text x="820" y="520" class="txt">600 mm Ø concertina</text>

  <!-- Side view -->
  <text x="60" y="900" class="txt">Side</text>
  <!-- Post side -->
  <rect x="200" y="980" width="120" height="700" fill="#ddd" stroke="#222" stroke-width="6"/>
  <!-- Bracket 45° side -->
  <line x1="260" y1="980" x2="260+212" y2="980-212" class="line"/>
  <!-- Saddle/strap -->
  <rect x="680" y="720" width="80" height="60" fill="#cfd8dc" stroke="#222" stroke-width="4"/>
  <text x="780" y="760" class="txt">SS saddle/strap</text>
  <!-- Concertina side (circle) -->
  <circle cx="720" cy="720" r="300" fill="none" stroke="#222" stroke-width="6"/>

  <!-- Dimensions -->
  <line x1="260" y1="1060" x2="472" y2="848" class="dim"/>
  <text x="520" y="980" class="txt">300 mm proj. @ 45°</text>
  <line x1="680" y1="1080" x2="680" y2="360" class="dim"/>
  <text x="710" y="740" class="txt" transform="rotate(90,710,740)">600 mm Ø</text>
</svg>