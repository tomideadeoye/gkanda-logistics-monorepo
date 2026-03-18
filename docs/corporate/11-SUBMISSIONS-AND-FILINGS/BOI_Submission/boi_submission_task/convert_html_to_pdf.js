const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

async function convertHTMLtoPDF(inputPath, outputPath) {
  // Check if input file exists
  try {
    await fs.access(inputPath);
  } catch (error) {
    console.error(`Input file not found: ${inputPath}`);
    return;
  }

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Load the HTML file
  const fileUrl = `file://${path.resolve(inputPath)}`;
  await page.goto(fileUrl, { waitUntil: 'networkidle0' });
  
  // Generate PDF
  await page.pdf({
    path: outputPath,
    format: 'A4',
    printBackground: true,
    margin: {
      top: '0.5in',
      right: '0.5in',
      bottom: '0.5in',
      left: '0.5in'
    }
  });
  
  await browser.close();
  console.log(`PDF generated: ${outputPath}`);
}

async function convertMultipleHTMLtoPDF() {
  const coverPages = [
    { input: 'emergency_response_plan_cover.html', output: 'Emergency_Response_Plan_Cover.pdf' },
    { input: 'safety_management_system_cover.html', output: 'Safety_Management_System_Cover.pdf' },
    { input: 'quality_assurance_manual_cover.html', output: 'Quality_Assurance_Manual_Cover.pdf' }
  ];

  for (const cover of coverPages) {
    try {
      await convertHTMLtoPDF(cover.input, cover.output);
    } catch (error) {
      console.error(`Error converting ${cover.input}:`, error);
    }
  }
}

// If this script is run directly
if (require.main === module) {
  // Check if command line arguments are provided
  const args = process.argv.slice(2);
  
  if (args.length === 2) {
    // Convert specific files provided as arguments
    convertHTMLtoPDF(args[0], args[1]);
  } else {
    // Convert the default set of cover pages
    convertMultipleHTMLtoPDF();
  }
}

module.exports = { convertHTMLtoPDF, convertMultipleHTMLtoPDF };