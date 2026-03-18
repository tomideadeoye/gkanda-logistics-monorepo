#!/bin/bash

# Setup script for Mermaid diagram support

echo "Setting up Mermaid diagram support..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "npm is not installed. Please install npm first."
    exit 1
fi

# Install mermaid CLI globally
echo "Installing mermaid CLI..."
npm install -g @mermaid-js/mermaid-cli

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "pandoc is not installed. Installing pandoc..."
    # On macOS, use brew if available
    if command -v brew &> /dev/null; then
        brew install pandoc
    else
        echo "Please install pandoc manually: https://pandoc.org/installing.html"
        exit 1
    fi
fi

# Install Python dependencies if not already installed
echo "Checking Python dependencies..."
python3 -c "import weasyprint" 2>/dev/null || pip3 install weasyprint
python3 -c "import markdown" 2>/dev/null || pip3 install markdown

echo "Setup completed successfully!"
echo ""
echo "To use the diagram generation scripts:"
echo "1. Run 'python3 generate_md_with_svgs.py' to convert mermaid diagrams to SVG images"
echo "2. Run 'python3 convert_and_merge_v3.py' to convert markdown to PDF with diagram support"