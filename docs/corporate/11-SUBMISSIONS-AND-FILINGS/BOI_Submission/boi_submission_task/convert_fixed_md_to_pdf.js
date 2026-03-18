const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

async function convertMarkdownToPdf() {
  try {
    // Read the markdown file
    const mdPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Fixed.md');
    const markdownContent = await fs.readFile(mdPath, 'utf8');
    
    // Convert markdown to HTML with better formatting
    let htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Emergency Response Plan</title>
  <style>
    ${await fs.readFile(path.resolve(__dirname, 'improved_styling.css'), 'utf8')}
  </style>
</head>
<body>
`;
    
    // Process markdown content line by line
    const lines = markdownContent.split('\n');
    let inTable = false;
    let listLevel = 0;
    
    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];
      
      // Skip empty lines that are just formatting
      if (line.trim() === '' && i > 0 && lines[i-1].trim() === '' && i < lines.length - 1 && lines[i+1].trim() === '') {
        continue;
      }
      
      // Handle page breaks
      if (line.includes('<div style="page-break-after: always;"></div>')) {
        htmlContent += '<div style="page-break-after: always;"></div>\n';
        continue;
      }
      
      // Headers
      if (line.startsWith('# ')) {
        htmlContent += `<h1>${line.substring(2).replace(/\*\*/g, '').replace(/__/g, '')}</h1>\n`;
      } else if (line.startsWith('## ')) {
        htmlContent += `<h2>${line.substring(3).replace(/\*\*/g, '').replace(/__/g, '')}</h2>\n`;
      } else if (line.startsWith('### ')) {
        htmlContent += `<h3>${line.substring(4).replace(/\*\*/g, '').replace(/__/g, '')}</h3>\n`;
      } else if (line.startsWith('#### ')) {
        htmlContent += `<h4>${line.substring(5).replace(/\*\*/g, '').replace(/__/g, '')}</h4>\n`;
      }
      // Tables
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
              htmlContent += `      <th>${cell.trim().replace(/\*\*/g, '').replace(/__/g, '')}</th>\n`;
            });
            htmlContent += '    </tr>\n';
            htmlContent += '  </thead>\n';
            htmlContent += '  <tbody>\n';
            i++; // Skip the separator line
          } else {
            htmlContent += '    <tr>\n';
            cells.forEach(cell => {
              htmlContent += `      <td>${cell.trim().replace(/\*\*/g, '').replace(/__/g, '')}</td>\n`;
            });
            htmlContent += '    </tr>\n';
          }
        }
      } else if (inTable && (!line.startsWith('|') || !line.endsWith('|'))) {
        htmlContent += '  </tbody>\n';
        htmlContent += '</table>\n';
        inTable = false;
        processLine(line);
      }
      // Horizontal rules
      else if (line.startsWith('---') || line.startsWith('***') || line.startsWith('___')) {
        // Skip horizontal rules for cleaner look
        htmlContent += '<br>\n';
      }
      // Lists
      else if (line.startsWith('- ')) {
        if (listLevel === 0) {
          htmlContent += '<ul>\n';
          listLevel = 1;
        }
        htmlContent += `  <li>${line.substring(2).replace(/\*\*/g, '').replace(/__/g, '')}</li>\n`;
      } else if (listLevel > 0 && !line.startsWith('-')) {
        while (listLevel > 0) {
          htmlContent += '</ul>\n';
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
      htmlContent += '</ul>\n';
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
        // Remove markdown formatting characters
        let cleanLine = line.replace(/\*\*/g, '').replace(/__/g, '').replace(/\*/g, '').replace(/_/g, '');
        htmlContent += `<p>${cleanLine}</p>\n`;
      }
    }
    
    htmlContent += `
</body>
</html>
`;
    
    // Write the HTML file for debugging
    const htmlPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Fixed.html');
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
    
    // Generate PDF with narrow margins
    const pdfPath = path.resolve(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Fixed.pdf');
    await page.pdf({
      path: pdfPath,
      format: 'A4',
      printBackground: true,
      margin: {
        top: '1cm',
        right: '1cm',
        bottom: '1cm',
        left: '1cm'
      }
    });
    
    console.log(`Successfully created fixed Emergency Response Plan PDF: ${pdfPath}`);
    
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
    console.log('Fixed Emergency Response Plan PDF created successfully!');
  } else {
    console.log('Failed to create fixed Emergency Response Plan PDF');
  }
});