const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function convertMarkdownToPDF() {
  // Read the markdown file
  const markdownPath = path.join(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Reduced_Tables.md');
  const markdownContent = fs.readFileSync(markdownPath, 'utf8');
  
  // Convert markdown to HTML (simplified conversion)
  let htmlContent = `
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="UTF-8">
    <title>GK & A Logistics Services Ltd - Emergency Response Plan</title>
    <style>
      @media print {
        @page {
          margin: 1cm;
        }
      }
      
      body {
        font-family: Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.5;
        margin: 2cm;
      }
      
      h1 {
        font-size: 24pt;
        font-weight: bold;
        margin: 24pt 0 16pt 0;
        padding-bottom: 10pt;
        border-bottom: 1pt solid #ddd;
      }
      
      h2 {
        font-size: 18pt;
        font-weight: bold;
        margin: 20pt 0 14pt 0;
        padding-bottom: 8pt;
        border-bottom: 1pt solid #eee;
      }
      
      h3 {
        font-size: 14pt;
        font-weight: bold;
        margin: 16pt 0 12pt 0;
      }
      
      h4 {
        font-size: 12pt;
        font-weight: bold;
        margin: 14pt 0 10pt 0;
      }
      
      h5 {
        font-size: 11pt;
        font-weight: bold;
        margin: 12pt 0 8pt 0;
      }
      
      h6 {
        font-size: 10pt;
        font-weight: bold;
        margin: 10pt 0 6pt 0;
      }
      
      p {
        margin: 8pt 0;
        text-align: justify;
      }
      
      ul, ol {
        margin: 12pt 0;
        padding-left: 24pt;
      }
      
      li {
        margin: 4pt 0;
      }
      
      strong {
        font-weight: bold;
      }
      
      em {
        font-style: italic;
      }
      
      code {
        font-family: monospace;
        background-color: #f8f9fa;
        padding: 2pt 4pt;
        border-radius: 3pt;
      }
      
      pre {
        font-family: monospace;
        background-color: #f8f9fa;
        padding: 12pt;
        border-radius: 5pt;
        overflow-x: auto;
        margin: 16pt 0;
      }
      
      blockquote {
        border-left: 4pt solid #3498db;
        padding-left: 16pt;
        margin: 16pt 0;
        color: #7f8c8d;
      }
      
      table {
        width: 100%;
        border-collapse: collapse;
        margin: 16pt 0;
        font-size: 10pt;
      }
      
      th {
        background-color: #f2f2f2;
        border: 1pt solid #ddd;
        padding: 8pt 12pt;
        text-align: left;
        font-weight: bold;
      }
      
      td {
        border: 1pt solid #ddd;
        padding: 8pt 12pt;
        text-align: left;
      }
      
      tr:nth-child(even) {
        background-color: #f9f9f9;
      }
      
      hr {
        border: 0;
        height: 1pt;
        background-color: #ddd;
        margin: 24pt 0;
      }
      
      .page-break {
        page-break-after: always;
      }
      
      @media print {
        body {
          margin: 1cm;
        }
        
        .page-break {
          page-break-after: always;
        }
      }
    </style>
  </head>
  <body>
  `;
  
  // Simple markdown to HTML conversion
  const lines = markdownContent.split('\n');
  let inList = false;
  let listType = '';
  
  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];
    
    // Skip empty lines
    if (line.trim() === '') {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      continue;
    }
    
    // Headings
    if (line.startsWith('# ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h1>${line.substring(2)}</h1>`;
    } else if (line.startsWith('## ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h2>${line.substring(3)}</h2>`;
    } else if (line.startsWith('### ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h3>${line.substring(4)}</h3>`;
    } else if (line.startsWith('#### ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h4>${line.substring(5)}</h4>`;
    } else if (line.startsWith('##### ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h5>${line.substring(6)}</h5>`;
    } else if (line.startsWith('###### ')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<h6>${line.substring(7)}</h6>`;
    }
    // Horizontal rule
    else if (line.startsWith('---')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += '<hr>';
    }
    // Page break
    else if (line.includes('<div style="page-break-after: always;"></div>')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += '<div class="page-break"></div>';
    }
    // Tables
    else if (line.startsWith('|')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      
      // Simple table parsing
      if (line.includes('---')) {
        // Skip separator line
        continue;
      } else {
        // Parse table row
        const cells = line.split('|').filter(cell => cell.trim() !== '');
        if (cells.length > 0) {
          // Check if it's a header row (based on position or content)
          const isHeader = i > 0 && lines[i-1] && lines[i-1].includes('---');
          
          if (isHeader) {
            htmlContent += '<thead><tr>';
            cells.forEach(cell => {
              htmlContent += `<th>${cell.trim()}</th>`;
            });
            htmlContent += '</tr></thead><tbody>';
          } else {
            htmlContent += '<tr>';
            cells.forEach(cell => {
              htmlContent += `<td>${cell.trim()}</td>`;
            });
            htmlContent += '</tr>';
          }
        }
      }
    }
    // Lists
    else if (line.trim().startsWith('- ')) {
      if (!inList || listType !== 'ul') {
        if (inList) {
          htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        }
        htmlContent += '<ul>';
        inList = true;
        listType = 'ul';
      }
      htmlContent += `<li>${line.substring(2)}</li>`;
    } else if (line.trim().match(/^\d+\. /)) {
      if (!inList || listType !== 'ol') {
        if (inList) {
          htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        }
        htmlContent += '<ol>';
        inList = true;
        listType = 'ol';
      }
      htmlContent += `<li>${line.replace(/^\d+\. /, '')}</li>`;
    }
    // Bold text
    else if (line.includes('**')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      // Remove markdown bold formatting
      let cleanLine = line.replace(/\*\*/g, '');
      htmlContent += `<p>${cleanLine}</p>`;
    }
    // Italic text
    else if (line.includes('*') && !line.includes('---')) {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      // Remove markdown italic formatting
      let cleanLine = line.replace(/\*/g, '');
      htmlContent += `<p>${cleanLine}</p>`;
    }
    // Regular paragraph
    else {
      if (inList) {
        htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
        inList = false;
        listType = '';
      }
      htmlContent += `<p>${line}</p>`;
    }
  }
  
  // Close any open list or table
  if (inList) {
    htmlContent += listType === 'ul' ? '</ul>' : '</ol>';
  }
  
  htmlContent += '</body></html>';
  
  // Write intermediate HTML file
  const htmlPath = path.join(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Reduced_Tables.html');
  fs.writeFileSync(htmlPath, htmlContent);
  console.log(`Created intermediate HTML file: ${htmlPath}`);
  
  // Convert HTML to PDF using Puppeteer
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.setContent(htmlContent, { waitUntil: 'domcontentloaded' });
  
  const pdfPath = path.join(__dirname, 'GK_and_A_Logistics_Services_Ltd_Emergency_Response_Plan_Reduced_Tables.pdf');
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    margin: {
      top: '1cm',
      right: '1cm',
      bottom: '1cm',
      left: '1cm'
    },
    printBackground: true
  });
  
  await browser.close();
  
  console.log(`Successfully created Emergency Response Plan PDF with reduced tables: ${pdfPath}`);
}

convertMarkdownToPDF().catch(console.error);