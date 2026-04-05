#!/usr/bin/env python3
"""
Create 5-page PDF with important code using ReportLab
"""
import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Paths
website_dir = r"c:\Users\POLEBOINA SAIKUMAR\OneDrive\Desktop\website"
pdf_file = os.path.join(website_dir, "CODE_DOCUMENTATION.pdf")

# Create PDF
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
story = []
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#667eea'),
    spaceAfter=20,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#2d3436'),
    spaceAfter=10,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

code_style = ParagraphStyle(
    'CodeStyle',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=8,
    textColor=colors.HexColor('#212529'),
    backColor=colors.HexColor('#f8f9fa'),
    leftIndent=10,
    rightIndent=10,
    borderPadding=8,
)

normal_style = ParagraphStyle(
    'NormalStyle',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#333333'),
    alignment=TA_JUSTIFY
)

# ============ PAGE 1 ============
story.append(Paragraph("📄 PAGE 1: HTML STRUCTURE & NAVIGATION", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Navigation Bar HTML Structure", heading_style))
code_text = """<nav class="navbar navbar-expand-lg navbar-dark sticky-top">
  <div class="container-fluid px-lg-5">
    <a class="navbar-brand" href="index.html">
      <i class="fas fa-user-circle"></i> Portfolio
    </a>
    <button class="navbar-toggler" type="button" 
            data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <a class="nav-link active" href="index.html">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="about.html">About</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown">
            Expertise
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="skills.html">Skills</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Hero Section", heading_style))
code_text = """<section class="hero">
  <div class="hero-content">
    <h1 class="display-3 fw-bold">JADI VIJAY KUMAR</h1>
    <p class="lead">Information Technology Student | Web Developer</p>
    <div class="d-flex flex-wrap justify-content-center gap-3">
      <a href="about.html" class="btn btn-primary btn-lg">Learn More</a>
      <a href="contact.html" class="btn btn-outline-light btn-lg">Get In Touch</a>
    </div>
    <div class="social-links mt-5">
      <a href="#" title="GitHub"><i class="fab fa-github"></i></a>
      <a href="#" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
    </div>
  </div>
</section>"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Key Features:", heading_style))
features = """✓ Bootstrap 5 framework for responsive layout
✓ Font Awesome icons for social links
✓ Sticky navigation with smooth scrolling
✓ Mobile-responsive hamburger menu"""
story.append(Paragraph(features, normal_style))

story.append(PageBreak())

# ============ PAGE 2 ============
story.append(Paragraph("🎨 PAGE 2: CSS - DESIGN SYSTEM & NAVBAR", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("CSS Custom Properties (Design System)", heading_style))
code_text = """:root {
  --primary-color: #667eea;      /* Purple Blue */
  --secondary-color: #764ba2;    /* Deep Purple */
  --accent-color: #f093fb;       /* Pink */
  --dark-color: #2d3436;         /* Dark Gray */
  --light-color: #f5f6fa;        /* Light Gray */
  --success-color: #10b981;      /* Green */
  --danger-color: #ef4444;       /* Red */
  --warning-color: #f59e0b;      /* Yellow */
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Navbar Styling", heading_style))
code_text = """.navbar {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem 2rem;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent-color);
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Dropdown Menu", heading_style))
code_text = """.dropdown-menu {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.dropdown-item:hover {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding-left: 2rem;
}"""
story.append(Preformatted(code_text, code_style))

story.append(PageBreak())

# ============ PAGE 3 ============
story.append(Paragraph("🎯 PAGE 3: CSS - HERO & CARD COMPONENTS", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Hero Section Styling", heading_style))
code_text = """.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 120px 20px;
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero h1 {
  font-size: 4rem;
  font-weight: 700;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
  animation: fadeInUp 1s ease;
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Card Components", heading_style))
code_text = """.card {
  border: none;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.card-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px 30px;
  font-weight: 600;
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Button Styling", heading_style))
code_text = """.btn {
  font-weight: 600;
  padding: 12px 35px;
  border-radius: 50px;
  transition: all 0.3s ease;
}

.btn-primary {
  background: var(--accent-color);
  border: none;
}

.btn-primary:hover {
  background: #ff77eb;
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(240, 147, 251, 0.4);
}"""
story.append(Preformatted(code_text, code_style))

story.append(PageBreak())

# ============ PAGE 4 ============
story.append(Paragraph("⚙️ PAGE 4: JAVASCRIPT - NAVIGATION & FORMS", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Active Navigation Link Handler", heading_style))
code_text = """document.addEventListener('DOMContentLoaded', function () {
  const currentPage = window.location.pathname.split('/').pop() 
    || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    
    if (href === currentPage || 
        (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
  
  const navbarToggler = document.querySelector('.navbar-toggler');
  navLinks.forEach(link => {
    link.addEventListener('click', function () {
      if (window.innerWidth < 992) {
        navbarToggler.click();
      }
    });
  });
});"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Form Submission Handler", heading_style))
code_text = """const forms = document.querySelectorAll('.needs-validation');

Array.from(forms).forEach(form => {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopPropagation();

    if (!validateForm(form)) {
      event.preventDefault();
      return false;
    }

    if (form.checkValidity() === false) {
      event.preventDefault();
    } else {
      showAlert('success', 'Form submitted successfully!');
      form.reset();
      form.classList.remove('was-validated');
    }

    form.classList.add('was-validated');
  }, false);
});"""
story.append(Preformatted(code_text, code_style))

story.append(PageBreak())

# ============ PAGE 5 ============
story.append(Paragraph("🔒 PAGE 5: JAVASCRIPT - VALIDATION & ERROR HANDLING", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("Custom Form Validation Function", heading_style))
code_text = """function validateForm(form) {
  let isValid = true;
  const fields = form.querySelectorAll('input, textarea, select');
  
  fields.forEach(field => {
    if (!field.value.trim()) {
      showFieldError(field, 'This field is required.');
      isValid = false;
      return;
    }

    if (field.type === 'email') {
      if (!isValidEmail(field.value)) {
        showFieldError(field, 'Invalid email address.');
        isValid = false;
      }
    }

    if (field.type === 'tel') {
      const phoneValue = field.value.replace(/\\D/g, '');
      if (phoneValue.length !== 10) {
        showFieldError(field, 'Phone must be 10 digits.');
        isValid = false;
      }
    }
  });

  return isValid;
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Email Validation & Error Display", heading_style))
code_text = """function isValidEmail(email) {
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  return emailRegex.test(email);
}

function showFieldError(field, message) {
  field.classList.add('is-invalid');
  const errorMsg = document.createElement('div');
  errorMsg.className = 'invalid-feedback d-block';
  errorMsg.textContent = message;
  field.parentNode.insertBefore(errorMsg, field.nextSibling);
}

function showAlert(type, message) {
  let alertContainer = document.getElementById('alert-container');
  if (!alertContainer) {
    alertContainer = document.createElement('div');
    alertContainer.id = 'alert-container';
    alertContainer.style.position = 'fixed';
    alertContainer.style.top = '80px';
    alertContainer.style.right = '20px';
    alertContainer.style.zIndex = '9999';
    document.body.appendChild(alertContainer);
  }

  const alert = document.createElement('div');
  alert.className = `alert alert-${type} alert-dismissible fade show`;
  alert.innerHTML = `${message}<button class="btn-close" data-bs-dismiss="alert"></button>`;
  alertContainer.appendChild(alert);

  setTimeout(() => { alert.remove(); }, 5000);
}"""
story.append(Preformatted(code_text, code_style))
story.append(Spacer(1, 15))

story.append(Paragraph("Summary", heading_style))
summary = """<b>Technology Stack:</b> HTML5 • CSS3 • Bootstrap 5 • JavaScript • Font Awesome

<b>Key Features:</b> Responsive design, form validation, smooth animations, error handling, accessible navigation"""
story.append(Paragraph(summary, normal_style))

# Build PDF
doc.build(story)
print(f"✓ PDF created: {pdf_file}")
print(f"  File size: {os.path.getsize(pdf_file):,} bytes")
