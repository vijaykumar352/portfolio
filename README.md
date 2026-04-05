# Personal Portfolio Website - Bootstrap 5

A fully responsive, modern personal portfolio website built with **Bootstrap 5**, featuring multiple interconnected pages and rich Bootstrap components.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Pages Included](#pages-included)
- [Bootstrap Components Used](#bootstrap-components-used)
- [Setup Instructions](#setup-instructions)
- [Deployment on GitHub Pages](#deployment-on-github-pages)
- [Customization Guide](#customization-guide)

## ✨ Features

### ✅ Responsive Design
- Mobile-first responsive layout
- Works perfectly on all devices (mobile, tablet, desktop)
- Bootstrap Grid system for flexible layouts

### ✅ Interactive Navigation
- Sticky navbar with active link highlighting
- Dropdown menus for Expertise section
- Collapsible mobile menu
- Smooth navigation

### ✅ Form Validation
- HTML5 validation
- JavaScript custom validation
- Mobile number validation (10 digits)
- Email format validation
- Real-time error messaging

### ✅ Beautiful Components
- Animated cards with hover effects
- Progress bars for skill levels
- Interactive tables with striped rows
- Badges and badges styling
- Material icons throughout
- Smooth animations and transitions

### ✅ Modern UI/UX
- Gradient backgrounds and styling
- Consistent color scheme
- Professional typography
- Accessible form inputs with icons
- Tooltip support
- Modal windows for certificate preview

## 📁 Project Structure

```
portfolio/
├── index.html                 # Home page
├── about.html                 # About page
├── qualifications.html        # Qualifications page
├── skills.html                # Skills page
├── certifications.html        # Certifications page
├── contact.html               # Contact page
│
├── css/
│   └── style.css             # Custom CSS with Bootstrap customization
│
├── js/
│   └── script.js             # Custom JavaScript for validation & interactivity
│
├── assets/                    # Folder for images and media
│
└── README.md                 # This file
```

## 📄 Pages Included

### 1. **Home (index.html)**
- Hero section with call-to-action buttons
- Feature showcase
- Recent projects/work samples
- Statistics counter section
- Social media links

**Components Used:** Jumbotron, Buttons, Cards, Badges, Carousel (optional), Counters

### 2. **About (about.html)**
- Profile card with image
- Personal information
- Timeline of journey/experience
- Interests and hobbies
- Contact call-to-action

**Components Used:** Cards, Responsive images, Timeline, Grid system

### 3. **Qualifications (qualifications.html)**
- Education details with cards
- Professional experience table
- Achievements section
- Technical keywords display
- GPA and honors badges

**Components Used:** Tables (striped, bordered, hover), Badges, Cards, Grid system

### 4. **Skills (skills.html)**
- Organized skill categories
- Progress bars with percentages
- Tool and technology list groups
- Soft skills display
- Statistics section

**Components Used:** Progress bars, List groups, Badges, Grid system, Cards

### 5. **Certifications (certifications.html)**
- Certificate cards with details
- Category filtering (Web, Cloud, Tools)
- Modal preview functionality
- Download buttons
- Status badges (Active/Expired)

**Components Used:** Cards, Badges, Buttons, Modals, Dropdowns, Filter functionality

### 6. **Contact (contact.html)**
- Contact information sidebar
- Contact form with validation
- Input groups with icons
- Subject selection dropdown
- Budget range selector
- FAQ Accordion section
- Social media connection options

**Components Used:** Forms, Input groups, Textareas, Select dropdowns, Checkboxes, Accordions, Buttons

## 🎨 Bootstrap Components Used

✅ **Navigation & Layout**
- Navbar (responsive, sticky)
- Grid system (rows, columns, responsive)
- Responsive containers

✅ **Content**
- Cards
- Jumbotron-style sections
- Tables (striped, bordered, hover)
- Lists & List groups
- Badges
- Alerts
- Breadcrumbs (optional)

✅ **Forms**
- Form controls (input, textarea, select)
- Input groups with icons
- Form validation
- Checkboxes & radio buttons
- Labels
- Help text

✅ **Components**
- Buttons (primary, outline, sizes)
- Dropdowns & dropdown menus
- Accordions
- Modals
- Progress bars
- Spinners (optional)
- Tooltips

✅ **Utilities**
- Spacing (margins, padding)
- Colors & backgrounds
- Typography
- Display utilities
- Flexbox utilities
- Alignment utilities

## 🚀 Setup Instructions

### Local Setup (Testing)

1. **Download/Clone the project:**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Open in browser:**
   - Simply open `index.html` in any modern web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     ```
   - Then visit `http://localhost:8000`

3. **Customize content:**
   - Edit HTML files to add your information
   - Replace placeholder text with your details
   - Update social media links
   - Modify images and assets

## 📤 Deployment on GitHub Pages

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click "**+**" > "**New repository**"
3. Name it: `portfolio` (or any name)
4. Add description: "Personal Portfolio Website"
5. Choose **Public** repository
6. Click "**Create repository**"

### Step 2: Push Code to GitHub

```bash
# Navigate to your project folder
cd portfolio

# Initialize git (if not already initialized)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Portfolio website"

# Add remote repository
git remote add origin https://github.com/yourusername/portfolio.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "**Settings**" (usually at the top right)
3. Scroll down to "**Pages**" section
4. Under "**Source**", select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click "**Save**"
6. Wait 1-2 minutes for deployment
7. Your site will be available at: `https://yourusername.github.io/portfolio/`

### Step 4: Verify Deployment

- Check the "Deploy from a branch" section for status
- Look for "Your site is live at..." message
- Visit the provided URL to see your portfolio live

## 🔴 Troubleshooting GitHub Pages

| Issue | Solution |
|-------|----------|
| Pages not showing | Check Settings > Pages > Source is set to `main` |
| Old content showing | Hard refresh (Ctrl+Shift+R) or clear cache |
| Styles not loading | Check CSS paths are relative (not absolute) |
| Images not showing | Verify image paths in HTML files |
| 404 Page not found | Ensure index.html is in root folder |

## 🎨 Customization Guide

### Change Color Scheme

Edit `css/style.css`:
```css
:root {
  --primary-color: #667eea;      /* Change primary color */
  --secondary-color: #764ba2;     /* Change secondary color */
  --accent-color: #f093fb;        /* Change accent color */
  --dark-color: #2d3436;
  --light-color: #f5f6fa;
}
```

### Update Personal Information

1. **Home Page (index.html)**
   - Change title and subtitle
   - Update feature descriptions
   - Modify project cards

2. **About Page (about.html)**
   - Update profile name
   - Change bio and contacts
   - Edit timeline entries
   - Modify interests

3. **Skills Page (skills.html)**
   - Update skill names
   - Change progress percentages
   - Add/remove skills

4. **Contact Page (contact.html)**
   - Update email, phone, location
   - Change subject options
   - Modify FAQ content

### Add Custom Images

1. Place images in `assets/` folder
2. Reference in HTML: `<img src="assets/image-name.jpg" alt="Description">`

### Modify Bootstrap Theme

Override Bootstrap variables in `css/style.css`:
```css
/* Override Bootstrap defaults */
$primary: #667eea;
$secondary: #764ba2;
```

## 📱 Responsive Breakpoints

The site is optimized for:
- **Mobile:** 320px - 576px
- **Tablet:** 576px - 992px
- **Desktop:** 992px and above

## ✅ Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📧 Form Validation Rules

- **Name:** Required, any text
- **Email:** Required, valid email format
- **Phone:** Required, exactly 10 digits
- **Subject:** Required, dropdown selection
- **Message:** Required, minimum 10 characters
- **Budget:** Optional, dropdown selection

## 🔗 Live Features

- Smooth scrolling navigation
- Active page highlighting
- Form validation feedback
- Animated skill progress bars
- Hover effects on cards
- Responsive navbar collapse
- Modal certificate preview
- Accordion FAQ section
- Tooltip support

## 🎯 Best Practices Implemented

✅ Semantic HTML5
✅ Mobile-first responsive design
✅ Accessibility (ARIA labels, semantic tags)
✅ Clean, modular CSS
✅ DRY (Don't Repeat Yourself) principles
✅ Performance optimized
✅ Cross-browser compatible
✅ SEO friendly structure

## 📚 Resources

- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Font Awesome Icons](https://fontawesome.com/)
- [GitHub Pages Guide](https://pages.github.com/)
- [Git Documentation](https://git-scm.com/doc)

## 💡 Tips for Success

1. **Update content regularly** - Keep your portfolio fresh
2. **Add real projects** - Show actual work samples
3. **Optimize images** - Use compressed images for faster loading
4. **Test on multiple devices** - Ensure responsive design works
5. **Update skills frequently** - Add new skills as you learn them
6. **Stay active on social media** - Link your social profiles
7. **Get feedback** - Ask friends and colleagues to review

## 🤝 Contributing

Feel free to fork, modify, and customize this template for your own portfolio!

## 📄 License

This project is free to use for personal and commercial purposes.

## 👨‍💻 Author

Created as a complete Bootstrap 5 responsive portfolio template.

---

## Quick Start Checklist

- [ ] Customize all HTML content with your information
- [ ] Update color scheme if desired
- [ ] Add your profile image
- [ ] Update social media links
- [ ] Test all forms and validations
- [ ] Test responsive design on mobile
- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Enable GitHub Pages
- [ ] Share your portfolio URL!

---

**Happy coding! 🚀 Your portfolio is ready to impress!**

For questions or support, refer to the official Bootstrap documentation or GitHub Pages help.
