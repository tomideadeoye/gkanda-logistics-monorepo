const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function generateDiagramScreenshots() {
  // Read the markdown file to extract mermaid diagrams
  const mdFilePath = '/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/GK_and_A_Logistics_Services_Ltd_ESMS_Handbook_Enhanced.md';
  const mdContent = fs.readFileSync(mdFilePath, 'utf-8');
  
  // Extract mermaid diagrams using regex
  const mermaidRegex = /```mermaid\s*([\s\S]*?)\s*```/g;
  const diagrams = [];
  let match;
  
  while ((match = mermaidRegex.exec(mdContent)) !== null) {
    diagrams.push(match[1]);
  }
  
  console.log(`Found ${diagrams.length} mermaid diagrams`);
  
  // Launch browser
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  // Set viewport for consistent sizing
  await page.setViewport({ width: 1200, height: 800 });
  
  // Generate screenshots for each diagram
  for (let i = 0; i < diagrams.length; i++) {
    const diagramCode = diagrams[i];
    
    // Create HTML with the mermaid diagram
    const htmlContent = `
    <!DOCTYPE html>
    <html>
    <head>
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({ 
                startOnLoad: true,
                theme: 'default',
                securityLevel: 'loose',
                fontFamily: 'Arial, sans-serif'
            });
        </script>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .mermaid {
                text-align: center;
                margin: 20px auto;
                max-width: 1000px;
            }
            .diagram-container {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="diagram-container">
            <div class="mermaid">
                ${diagramCode}
            </div>
        </div>
    </body>
    </html>
    `;
    
    // Create temporary HTML file
    const tempHtmlPath = path.join('/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task', `temp_diagram_${i+1}.html`);
    fs.writeFileSync(tempHtmlPath, htmlContent);
    
    // Navigate to the page
    await page.goto(`file://${tempHtmlPath}`, { waitUntil: 'networkidle0' });
    
    // Wait for mermaid to render
    await page.waitForSelector('.mermaid svg', { timeout: 10000 });
    
    // Take screenshot
    const screenshotPath = path.join('/Users/mac/Documents/GitHub/gkalogistics/boi_submission_task/diagrams', `diagram_${i+1}_screenshot.png`);
    await page.screenshot({ 
      path: screenshotPath, 
      fullPage: true,
      type: 'png'
    });
    
    console.log(`Generated screenshot: diagram_${i+1}_screenshot.png`);
    
    // Clean up temp file
    fs.unlinkSync(tempHtmlPath);
  }
  
  await browser.close();
  console.log('All diagram screenshots generated successfully!');
}

// Run the function
generateDiagramScreenshots().catch(console.error);