#!/usr/bin/env python3
"""
Convert HTML documentation to PDF using WeasyPrint
"""
import os
from weasyprint import HTML, CSS

# Define paths
website_dir = r"c:\Users\POLEBOINA SAIKUMAR\OneDrive\Desktop\website"
html_file = os.path.join(website_dir, "CODE_DOCUMENTATION.html")
pdf_file = os.path.join(website_dir, "CODE_DOCUMENTATION.pdf")

print("=" * 60)
print("Converting HTML to PDF")
print("=" * 60)
print(f"Source: {html_file}")
print(f"Destination: {pdf_file}")
print()

try:
    # Convert HTML to PDF
    HTML(filename=html_file).write_pdf(pdf_file)
    
    # Verify file was created
    if os.path.exists(pdf_file):
        size = os.path.getsize(pdf_file)
        print(f"✓ SUCCESS: PDF created successfully!")
        print(f"  File size: {size:,} bytes")
        print(f"  Location: {pdf_file}")
    else:
        print("✗ ERROR: PDF file was not created")
        
except Exception as e:
    print(f"✗ ERROR: {e}")
    print("\nFallback: Please open the HTML file manually")
    print(f"  {html_file}")
