const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

async function convertMarkdownToPdf() {
  try {
    // Read the markdown file
    const mdPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Complete.md');
    const markdownContent = await fs.readFile(mdPath, 'utf8');
    
    // Simple markdown to HTML conversion (basic)
    let htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Emergency Response Plan</title>
  <style>
    ${await fs.readFile(path.resolve(__dirname, 'enhanced_styling.css'), 'utf8')}
  </style>
</head>
<body>
`;
    
    // Simple conversion - this is a basic implementation
    // For a full implementation, you would use a proper markdown parser
    const lines = markdownContent.split('\n');
    let inTable = false;
    let listLevel = 0;
    
    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];
      
      // Handle page breaks
      if (line.includes('<div style="page-break-after: always;"></div>')) {
        htmlContent += '<div style="page-break-after: always;"></div>\n';
        continue;
      }
      
      // Headers
      if (line.startsWith('# ')) {
        htmlContent += `<h1>${line.substring(2)}</h1>\n`;
      } else if (line.startsWith('## ')) {
        htmlContent += `<h2>${line.substring(3)}</h2>\n`;
      } else if (line.startsWith('### ')) {
        htmlContent += `<h3>${line.substring(4)}</h3>\n`;
      } else if (line.startsWith('#### ')) {
        htmlContent += `<h4>${line.substring(5)}</h4>\n`;
      }
      // Tables (simplified)
      else if (line.startsWith('|') && line.endsWith('|')) {
        if (!inTable) {
          htmlContent += '<table>\n';
          inTable = true;
        }
        const cells = line.split('|').filter(cell => cell.trim() !== '');
        if (cells.length > 0) {
          // Check if it's a header row (next line is separator)
          if (i + 1 < lines.length && lines[i + 1].startsWith('|') && lines[i + 1].includes('---')) {
            htmlContent += '  <thead>\n';
            htmlContent += '    <tr>\n';
            cells.forEach(cell => {
              htmlContent += `      <th>${cell.trim()}</th>\n`;
            });
            htmlContent += '    </tr>\n';
            htmlContent += '  </thead>\n';
            htmlContent += '  <tbody>\n';
            i++; // Skip the separator line
          } else {
            htmlContent += '    <tr>\n';
            cells.forEach(cell => {
              htmlContent += `      <td>${cell.trim()}</td>\n`;
            });
            htmlContent += '    </tr>\n';
          }
        }
      } else if (inTable && (!line.startsWith('|') || !line.endsWith('|'))) {
        htmlContent += '  </tbody>\n';
        htmlContent += '</table>\n';
        inTable = false;
        // Process the current line normally
        processLine(line);
      }
      // Lists
      else if (line.startsWith('- ')) {
        if (listLevel === 0) {
          htmlContent += '<ul>\n';
          listLevel = 1;
        }
        htmlContent += `  <li>${line.substring(2)}</li>\n`;
      } else if (line.startsWith('  - ')) {
        if (listLevel < 2) {
          htmlContent += '  <ul>\n';
          listLevel = 2;
        }
        htmlContent += `    <li>${line.substring(4)}</li>\n`;
      } else if (listLevel > 0 && !line.startsWith('-') && !line.startsWith('  -')) {
        while (listLevel > 0) {
          htmlContent += listLevel === 1 ? '</ul>\n' : '  </ul>\n';
          listLevel--;
        }
        processLine(line);
      }
      // Paragraphs
      else {
        processLine(line);
      }
    }
    
    // Close any open lists
    while (listLevel > 0) {
      htmlContent += listLevel === 1 ? '</ul>\n' : '  </ul>\n';
      listLevel--;
    }
    
    // Close any open table
    if (inTable) {
      htmlContent += '  </tbody>\n';
      htmlContent += '</table>\n';
    }
    
    function processLine(line) {
      if (line.trim() === '') {
        htmlContent += '<br>\n';
      } else {
        htmlContent += `<p>${line}</p>\n`;
      }
    }
    
    htmlContent += `
</body>
</html>
`;
    
    // Write the HTML file for debugging
    const htmlPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Complete.html');
    await fs.writeFile(htmlPath, htmlContent);
    console.log(`Created intermediate HTML file: ${htmlPath}`);
    
    // Launch the browser
    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    // Create a new page
    const page = await browser.newPage();
    
    // Set the content
    await page.setContent(htmlContent, {
      waitUntil: 'networkidle0'
    });
    
    // Wait a bit for all resources to load
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Generate PDF
    const pdfPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Complete.pdf');
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '20mm',
        right: '20mm',
        bottom: '20mm',
        left: '20mm'
      }
    });
    
    console.log(`Successfully created complete Emergency Response Plan PDF: ${pdfPath}`);
    
    // Close the browser
    await browser.close();
    
    return true;
  } catch (error) {
    console.error('Error converting markdown to PDF:', error);
    return false;
  }
}

// Run the conversion
convertMarkdownToPdf().then(success => {
  if (success) {
    console.log('Complete Emergency Response Plan PDF created successfully!');
  } else {
    console.log('Failed to create complete Emergency Response Plan PDF');
  }
});