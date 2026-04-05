#!/usr/bin/env python3
"""
Convert HTML documentation to PDF
"""
import os
import sys
import subprocess

# Add the website directory to path
website_dir = r"c:\Users\POLEBOINA SAIKUMAR\OneDrive\Desktop\website"
html_file = os.path.join(website_dir, "CODE_DOCUMENTATION.html")
pdf_file = os.path.join(website_dir, "CODE_DOCUMENTATION.pdf")

print("Converting HTML to PDF...")
print(f"Input: {html_file}")
print(f"Output: {pdf_file}")

try:
    import pdfkit
    
    # Try using pdfkit with wkhtmltopdf
    try:
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None,
            'enable-local-file-access': None,
        }
        
        pdfkit.from_file(html_file, pdf_file, options=options)
        print(f"✓ PDF created successfully: {pdf_file}")
        sys.exit(0)
        
    except Exception as e:
        print(f"! pdfkit/wkhtmltopdf not available: {e}")
        print("  Trying alternative method...")

except ImportError:
    print("! pdfkit not installed")

# Fallback: Use reportlab to create PDF from HTML
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from html.parser import HTMLParser
    
    class HTMLToElements(HTMLParser):
        def __init__(self):
            super().__init__()
            self.elements = []
            self.current_text = ""
            self.styles = getSampleStyleSheet()
            self.in_code = False
            self.code_content = ""
            
        def handle_starttag(self, tag, attrs):
            if tag == 'code' or tag == 'pre':
                self.in_code = True
            elif tag in ['h1', 'h2', 'h3', 'h4', 'div', 'p']:
                if self.current_text:
                    self.elements.append(self.current_text)
                    self.current_text = ""
                    
        def handle_data(self, data):
            if self.in_code:
                self.code_content += data
            else:
                self.current_text += data.strip() + " "
                
        def handle_endtag(self, tag):
            if tag == 'code' or tag == 'pre':
                if self.code_content:
                    self.elements.append(("CODE", self.code_content))
                    self.code_content = ""
                self.in_code = False
    
    print("✓ Using reportlab for PDF generation...")
    
    # For now, just create a simple text-based PDF
    # This is a fallback and won't preserve the exact formatting
    from reportlab.pdfgen import canvas
    
    c = canvas.Canvas(pdf_file, pagesize=A4)
    width, height = A4
    y = height - 40
    
    # Read and parse HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple extraction of text content
    from re import sub
    text = sub('<[^<]+?>', '', content)
    
    # Draw title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Website Code Documentation - 5 Pages")
    y -= 20
    
    c.setFont("Helvetica", 10)
    c.drawString(40, y, "This PDF contains important code sections from your portfolio website")
    y -= 30
    
    # Add text content
    from textwrap import wrap
    for line in text.split('\n'):
        if line.strip():
            for wrapped_line in wrap(line, 90):
                if y < 40:
                    c.showPage()
                    y = height - 40
                c.drawString(40, y, wrapped_line)
                y -= 12
    
    c.save()
    print(f"✓ PDF created successfully: {pdf_file}")
    
except Exception as e:
    print(f"✗ Error creating PDF: {e}")
    print("\nPlease open the HTML file in your browser and use:")
    print("  1. Right-click → Print")
    print("  2. Select 'Save as PDF'")
    print(f"  3. Save to: {pdf_file}")
    sys.exit(1)
