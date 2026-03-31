# Reware - Sustainable Fashion Website

A professional website for your reware (rewear/secondhand) clothes business built with Flask, featuring modern design and responsive layout.

## Features

- **Modern Design**: Professional, clean interface with sustainable fashion theme
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Multiple Pages**: Home, Shop, About, and Contact pages
- **Interactive Elements**: Smooth scrolling, animations, and hover effects
- **Product Showcase**: Grid layout for displaying clothing items
- **Contact Form**: Professional contact form for customer inquiries
- **SEO Friendly**: Proper meta tags and semantic HTML structure

## Pages

1. **Home Page** (`/`): Hero section, features, about preview, and product categories
2. **Shop Page** (`/shop`): Product grid with filtering options
3. **About Page** (`/about`): Company story, mission, values, and team
4. **Contact Page** (`/contact`): Contact form, business information, and FAQ

## Installation & Setup

1. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

2. **Run the application**:
   ```bash
   cd REWARE
   python app.py
   ```

3. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

## File Structure

```
REWARE/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html        # Home page
│   ├── shop.html         # Shop page
│   ├── about.html        # About page
│   └── contact.html      # Contact page
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── images/           # Image assets (add your images here)
└── README.md             # This file
```

## Adding Images

To make your website complete, add the following images to the `static/images/` directory:

### Required Images:
- `hero-image.jpg` - Main hero section image
- `about-image.jpg` - About section image
- `women-category.jpg` - Women's clothing category
- `men-category.jpg` - Men's clothing category
- `accessories-category.jpg` - Accessories category
- `product1.jpg` to `product6.jpg` - Product images
- `team1.jpg` to `team3.jpg` - Team member photos
- `impact.jpg` - Environmental impact image

### Image Recommendations:
- Use high-quality images (at least 1200px wide for hero images)
- Optimize images for web (use tools like TinyPNG)
- Maintain consistent aspect ratios for product images
- Use professional photos that align with your brand

## Customization

### Colors
The website uses a green color scheme representing sustainability:
- Primary: `#2c5530` (Dark Green)
- Secondary: `#4a7c59` (Medium Green)
- Accent: `#f5f7fa` (Light Gray)

### Fonts
- Primary font: Poppins (Google Fonts)
- Fallback: Sans-serif system fonts

### Content
Update the following in the HTML templates:
- Company name and branding
- Contact information
- Product details
- Team member information
- Social media links

## Features to Add

Consider adding these features to enhance your website:
- Shopping cart functionality
- User authentication
- Payment integration
- Product search and filtering
- Customer reviews
- Newsletter signup
- Blog section
- Inventory management

## Browser Support

The website is compatible with:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Performance

The website is optimized for:
- Fast loading times
- Mobile responsiveness
- SEO best practices
- Accessibility standards

## Support

For questions or support, please contact the development team or refer to the Flask documentation at https://flask.palletsprojects.com/

---

**Built with ❤️ for sustainable fashion**
