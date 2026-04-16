# CSS Essentials — Practice Exercise

## Style Your Portfolio Page

**Objective:** Apply CSS styling to the HTML portfolio page you built in the previous lesson, practicing selectors, the box model, and Flexbox layout.

**Time:** 30 minutes

**What you'll do:**

1. Create a `portfolio-styles.css` file and link it to your `portfolio.html`
2. Apply styling that meets these requirements:

**Header:**

- Dark background color (your choice) with light-colored text
- Your name should be larger than the default `<h1>` size
- Navigation links should be styled (no underline, light color, hover effect)

**Main content:**

- Max width of 900px or similar, centered on the page with `margin: auto`
- Section headings should have a visible accent (underline, border-bottom, or color)

**Project cards:**

- Wrap your project `<article>` elements in a `<div class="project-grid">`
- Use Flexbox (`display: flex`, `gap`, `flex-wrap: wrap`) to arrange them in a row
- Each card should have: white background, padding, rounded corners (`border-radius`), and a subtle shadow (`box-shadow`)

**Footer:**

- Should visually match the header (same background color)
- Links should be a contrasting color

**Deliverable:** A styled `portfolio.html` page that looks cohesive and professional when opened in a browser. Your project cards should sit side by side on wide screens.

**Hints:**

- Start with the universal reset: `* { box-sizing: border-box; margin: 0; padding: 0; }`
- Use `rem` units for font sizes (e.g., `2rem`, `1.1rem`) for better scalability
- The `transition` property on `:hover` effects makes your page feel polished

**Why this exercise?** You're combining every CSS concept from this lesson into one cohesive design. The card grid pattern you're building is the same pattern used in dashboards, product listings, and data displays — you'll see it again when you build Streamlit dashboards in Week 2.