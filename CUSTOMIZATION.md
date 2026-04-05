# Portfolio Customization Guide

This guide helps you quickly customize the portfolio template with your personal information.

## 📝 STEP-BY-STEP CUSTOMIZATION

### STEP 1: Personal Information

Update these files with your details:

#### 1.1 index.html (Home Page)
```html
<!-- Update hero section -->
<h1>Your Name Here</h1>
<p>Your Job Title | Your Specialization | Your Focus</p>

<!-- Update feature descriptions -->
<h4>Your Expertise</h4>
<p>Your description</p>

<!-- Update project cards -->
<h5>Your Project Name</h5>
<p>Your project description</p>

<!-- Update statistics -->
<div class="stat-number" data-counter="YOUR_NUMBER">0</div>
<div class="stat-label">Your Label</div>
```

#### 1.2 about.html (About Page)
```html
<!-- Update profile -->
<h2 class="display-5 fw-bold mb-4">Your Full Name</h2>
<p class="fs-5 mb-4">Your bio and professional summary...</p>

<!-- Update contact info -->
<p>your.email@example.com</p>
<p>+1 (555) 123-4567</p>
<p>Your City, State</p>
<p>Your Professional Title</p>

<!-- Update timeline -->
<h5>Your Achievement</h5>
<p>Description of what you accomplished...</p>

<!-- Update interests -->
<p>Your Interest 1</p>
<p>Your Interest 2</p>
```

#### 1.3 qualifications.html (Qualifications)
```html
<!-- Update education -->
<h4>Your Degree Name</h4>
<p>Your University</p>
<p>GPA: Your GPA</p>

<!-- Update experience -->
<strong>Your Job Title</strong>
<td>Your Company Name</td>
<td>Your Duration</td>

<!-- Update technologies -->
<div class="qualification-badge">Your Tech/Skill</div>
```

#### 1.4 skills.html (Skills)
```html
<!-- Update skill name and level -->
<span class="skill-name-label">Your Skill Name</span>
<span class="skill-level">85%</span>
<div class="progress-bar" style="width: 85%"></div>

<!-- Update soft skills -->
<div class="expertise-badge">Your Skill</div>
```

#### 1.5 certifications.html (Certifications)
```html
<!-- Update certification -->
<h4>Your Certification Name</h4>
<div class="cert-issuer">Issuing Organization</div>

<div class="cert-date">
  <i class="fas fa-calendar"></i> Month Year
</div>

<p class="cert-description">
  Description of what you learned...
</p>

<!-- Update skills covered -->
<span class="skill-badge">Skill 1</span>
<span class="skill-badge">Skill 2</span>
```

#### 1.6 contact.html (Contact)
```html
<!-- Update contact info -->
<a href="mailto:your.email@example.com">your.email@example.com</a>
<a href="tel:+15551234567">+1 (555) 123-4567</a>
<p>Your City, State</p>

<!-- Update FAQ -->
<h5>Your Question</h5>
<div>Your answer to the question</div>
```

### STEP 2: Color Customization

Edit `css/style.css` - Find the `:root` section:

```css
:root {
  --primary-color: #667eea;        /* Your primary color - HEX code */
  --secondary-color: #764ba2;      /* Your secondary color - HEX code */
  --accent-color: #f093fb;         /* Your accent color - HEX code */
  --dark-color: #2d3436;           /* Dark text color */
  --light-color: #f5f6fa;          /* Light background color */
  --success-color: #10b981;        /* Green for success */
  --danger-color: #ef4444;         /* Red for errors */
  --warning-color: #f59e0b;        /* Orange for warnings */
}
```

**Popular Color Combinations:**

1. **Blue Theme:**
   - Primary: #3498db, Secondary: #2980b9, Accent: #1abc9c

2. **Purple Theme:**
   - Primary: #9b59b6, Secondary: #8e44ad, Accent: #e74c3c

3. **Modern Tech:**
   - Primary: #00d4ff, Secondary: #0099cc, Accent: #ff006e

4. **Professional:**
   - Primary: #34495e, Secondary: #2c3e50, Accent: #e74c3c

### STEP 3: Add Your Images

1. **Profile Picture:**
   - Create an image (200x200px recommended)
   - Save as: `assets/profile.jpg`
   - In about.html, replace the placeholder image reference

2. **Project Images:**
   - Create screenshots/images of your projects
   - Save in `assets/` folder
   - Update references in index.html

3. **Favicon:**
   - Create favicon.ico (16x16px)
   - Save in root folder
   - Add to HTML head: `<link rel="icon" href="favicon.ico">`

### STEP 4: Social Media Links

Update all pages' navigation footer and contact page:

Change from: `<a href="#">`
To: `<a href="https://github.com/yourusername">`

**Common profiles to update:**
- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile
- Twitter: https://twitter.com/yourhandle
- Instagram: https://instagram.com/yourhandle
- Email: mailto:your.email@example.com

### STEP 5: Form Configuration

In contact.html, update form submission:

```html
<!-- Add your form handling service -->
<!-- Option 1: Formspree (recommended) -->
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">

<!-- Option 2: EmailJS -->
<!-- Add EmailJS script in <head> -->
<script type="text/javascript"
  src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/index.min.js"></script>
```

**Setup Formspree (Easy option):**
1. Go to https://formspree.io/
2. Sign up with email
3. Create new form
4. Update form action in contact.html with your form ID

### STEP 6: Favicon Setup

```html
<!-- Add in <head> section of all HTML files -->
<link rel="icon" type="image/x-icon" href="favicon.ico">
```

## 🎨 TEXT CUSTOMIZATION

### Change Navbar Brand Text
```html
<a class="navbar-brand" href="index.html">
  <i class="fas fa-user-circle"></i> Your Name
</a>
```

### Change Page Titles
```html
<title>Your Name - Portfolio</title>
<meta name="description" content="Your professional description">
<meta name="author" content="Your Name">
```

### Footer Content
```html
<p>&copy; 2024 Your Name. All rights reserved.</p>
```

## 🔗 SEO OPTIMIZATION

Update meta tags in all HTML files (in `<head>`):

```html
<meta name="title" content="Your Name - Full Stack Developer">
<meta name="description" content="Professional portfolio showcasing my projects">
<meta name="keywords" content="developer, portfolio, web development, yourname">
<meta name="author" content="Your Name">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## 📊 ANALYTICS (Optional)

Add Google Analytics to all pages in `<head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 💾 BEFORE DEPLOYMENT

Checklist before pushing to GitHub Pages:

- [ ] All personal info updated
- [ ] Colors customized
- [ ] Images added to assets/
- [ ] Social links updated
- [ ] Form setup (if using)
- [ ] Links tested (all internal links work)
- [ ] Mobile responsiveness tested
- [ ] Spelling and grammar checked
- [ ] SEO meta tags updated
- [ ] Footer copyright year updated

## 🚀 QUICK FIND & REPLACE

Use Ctrl+H (Find and Replace) in your code editor:

| Find | Replace |
|------|---------|
| john.developer@example.com | your.email@email.com |
| +1 (555) 123-4567 | your phone number |
| San Francisco, California | your city, state |
| Full Stack Developer | your title |
| YYYY | current year |

## 📱 MOBILE TESTING

After customization, test on:
- Mobile phones (iPhone, Android)
- Tablets (iPad, Android tablet)
- Desktop browsers
- Different screen sizes (use browser DevTools)

## 🐛 COMMON ISSUES

**Problem:** Links show as 404
**Solution:** Verify all href paths are correct relative paths

**Problem:** Images not showing
**Solution:** Check image file names match exactly in src attribute

**Problem:** Styles broken on mobile
**Solution:** Check Bootstrap classes and ensure no CSS conflicts

**Problem:** Forms not working
**Solution:** Verify form action URL and all input names are correct

## 📞 FORM FIELD NAMES

Don't change these in contact form:
- `name` - User's full name
- `email` - User's email
- `phone` - User's phone number
- `subject` - Subject selection
- `message` - Message content
- `budget` - Budget range
- `agree` - Agreement checkbox

---

**Ready to customize? Start with STEP 1 and work through each section!**

Good luck with your portfolio! 🎉
