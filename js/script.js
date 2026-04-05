/* ==========================================
   Personal Portfolio Website - Custom JavaScript
   ========================================== */

// ==========================================
// Set Active Navigation Link
// ==========================================

document.addEventListener('DOMContentLoaded', function () {
  // Get the current page filename
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  
  // Get all navigation links
  const navLinks = document.querySelectorAll('.nav-link');
  
  // Remove active class from all links and add to current page link
  navLinks.forEach(link => {
    link.classList.remove('active');
    
    // Get href attribute
    const href = link.getAttribute('href');
    
    // Check if link matches current page
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
  
  // Close navbar when link is clicked (mobile)
  const navbarToggler = document.querySelector('.navbar-toggler');
  navLinks.forEach(link => {
    link.addEventListener('click', function () {
      if (window.innerWidth < 992) {
        navbarToggler.click();
      }
    });
  });
});

// ==========================================
// Form Validation
// ==========================================

// Get all forms with the needs-validation class
const forms = document.querySelectorAll('.needs-validation');

Array.from(forms).forEach(form => {
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopPropagation();

    // Validate the form
    if (!validateForm(form)) {
      event.preventDefault();
      return false;
    }

    // If validation passes
    if (form.checkValidity() === false) {
      event.preventDefault();
    } else {
      // Show success message
      showAlert('success', 'Form submitted successfully! We will get back to you soon.');
      form.reset();
      form.classList.remove('was-validated');
    }

    form.classList.add('was-validated');
  }, false);
});

// ==========================================
// Custom Validation Function
// ==========================================

function validateForm(form) {
  let isValid = true;
  
  // Get form fields
  const fields = form.querySelectorAll('input, textarea, select');
  
  fields.forEach(field => {
    // Remove previous error message
    const errorMsg = field.parentElement.querySelector('.invalid-feedback');
    if (errorMsg) {
      errorMsg.remove();
    }

    // Check if field is empty
    if (!field.value.trim()) {
      showFieldError(field, 'This field is required.');
      isValid = false;
      return;
    }

    // Email validation
    if (field.type === 'email') {
      if (!isValidEmail(field.value)) {
        showFieldError(field, 'Please enter a valid email address.');
        isValid = false;
      }
    }

    // Phone number validation (10 digits)
    if (field.type === 'tel' || field.name === 'phone') {
      const phoneValue = field.value.replace(/\D/g, '');
      if (phoneValue.length !== 10) {
        showFieldError(field, 'Phone number must be 10 digits.');
        isValid = false;
      }
    }

    // Message field minimum length
    if (field.name === 'message' && field.value.trim().length < 10) {
      showFieldError(field, 'Message must be at least 10 characters long.');
      isValid = false;
    }
  });

  return isValid;
}

// ==========================================
// Email Validation
// ==========================================

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// ==========================================
// Show Field Error
// ==========================================

function showFieldError(field, message) {
  field.classList.add('is-invalid');
  
  // Create error message element
  const errorMsg = document.createElement('div');
  errorMsg.className = 'invalid-feedback d-block';
  errorMsg.textContent = message;
  
  // Insert after field
  field.parentNode.insertBefore(errorMsg, field.nextSibling);
}

// ==========================================
// Show Alert Message
// ==========================================

function showAlert(type, message) {
  // Create alert container if it doesn't exist
  let alertContainer = document.getElementById('alert-container');
  
  if (!alertContainer) {
    alertContainer = document.createElement('div');
    alertContainer.id = 'alert-container';
    alertContainer.style.position = 'fixed';
    alertContainer.style.top = '80px';
    alertContainer.style.right = '20px';
    alertContainer.style.zIndex = '9999';
    alertContainer.style.maxWidth = '400px';
    document.body.appendChild(alertContainer);
  }

  // Create alert element
  const alert = document.createElement('div');
  alert.className = `alert alert-${type} alert-dismissible fade show`;
  alert.role = 'alert';
  alert.innerHTML = `
    ${message}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  `;

  // Add to container
  alertContainer.appendChild(alert);

  // Auto close after 5 seconds
  setTimeout(() => {
    alert.remove();
  }, 5000);
}

// ==========================================
// Format Phone Number Input
// ==========================================

document.querySelectorAll('input[type="tel"]').forEach(input => {
  input.addEventListener('input', function (e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length > 10) {
      value = value.slice(0, 10);
    }
    e.target.value = value;
  });
});

// ==========================================
// Smooth Scroll for Anchor Links
// ==========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// ==========================================
// Scroll Animation for Elements
// ==========================================

const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function (entries) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in-up');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe all cards, skill items, and other elements
document.querySelectorAll('.card, .skill-item, .qualification-item, .certification-card').forEach(el => {
  observer.observe(el);
});

// ==========================================
// Modal Certificate Preview
// ==========================================

document.querySelectorAll('[data-certificate]').forEach(button => {
  button.addEventListener('click', function () {
    const certImage = this.getAttribute('data-certificate');
    const certName = this.getAttribute('data-cert-name');
    
    // Create modal content
    const modalBody = document.querySelector('#certificateModal .modal-body');
    if (modalBody) {
      modalBody.innerHTML = `
        <img src="${certImage}" alt="${certName}" class="img-fluid rounded">
        <p class="mt-3 text-center"><strong>${certName}</strong></p>
      `;
    }
  });
});

// ==========================================
// Update Progress Bar on Scroll
// ==========================================

document.querySelectorAll('.progress-bar').forEach(bar => {
  const targetWidth = bar.getAttribute('aria-valuenow');
  bar.style.width = '0%';
  
  const updateProgress = () => {
    const rect = bar.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
      bar.style.width = targetWidth + '%';
    }
  };
  
  window.addEventListener('scroll', updateProgress);
  updateProgress();
});

// ==========================================
// Navbar Scroll Effect
// ========== ===============================

let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function () {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  
  if (scrollTop > 100) {
    navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.2)';
  } else {
    navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
  }
  
  lastScrollTop = scrollTop;
});

// ==========================================
// Counter Animation
// ==========================================

function animateCounter(element, target) {
  let current = 0;
  const increment = target / 50;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      element.textContent = target;
      clearInterval(timer);
    } else {
      element.textContent = Math.floor(current);
    }
  }, 20);
}

// Animate counters when they become visible
document.querySelectorAll('[data-counter]').forEach(counter => {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.getAttribute('data-counter'));
        animateCounter(entry.target, target);
        observer.unobserve(entry.target);
      }
    });
  });
  observer.observe(counter);
});

// ==========================================
// Initialize Tooltips
// ========================================== 

document.addEventListener('DOMContentLoaded', function () {
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

// ==========================================
// Hamburger Menu Animation
// ========================================== 

const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler) {
  navbarToggler.addEventListener('click', function () {
    this.classList.toggle('active');
  });
}

// Close menu when clicking outside
document.addEventListener('click', function (event) {
  const isClickInside = navbarToggler?.contains(event.target) || navbarCollapse?.contains(event.target);
  
  if (!isClickInside && navbarCollapse?.classList.contains('show')) {
    navbarToggler.click();
  }
});

console.log('Portfolio JavaScript loaded successfully!');
