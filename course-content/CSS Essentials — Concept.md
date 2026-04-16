# CSS Essentials — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 35 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what CSS does and how it connects to HTML
2. Write CSS selectors to target elements by type, class, and ID
3. Describe the box model (content, padding, border, margin) and how it affects layout
4. Use Flexbox to create basic layouts

---

`[VIDEO PLACEHOLDER: 6 min — "CSS in action: take the unstyled profile page from Lesson 2 and add CSS step by step. Show how selectors, box model, and Flexbox transform the page from plain HTML into a styled layout."]`

Remember that house analogy from the HTML lesson? HTML is the frame — the walls, the roof, the rooms. CSS is everything that makes it look like a home: the paint, the flooring, the furniture arrangement, the lighting.

**CSS** stands for **Cascading Style Sheets**. It's the language that controls how HTML elements look — colors, fonts, spacing, sizes, and layout. Without CSS, every website would look like the plain, unstyled HTML page you built in the last lesson. With CSS, you can make that same content look professional, modern, and polished.

The word "cascading" is key: CSS rules can overlap and override each other in a predictable order, flowing down like a waterfall. We'll get to that shortly.

---

## How CSS Connects to HTML

There are three ways to add CSS to an HTML page. For this course, we'll use the most common and cleanest approach: an **external stylesheet**.

You create a separate `.css` file and link it in your HTML's `<head>`:

```html
<head>
    <link rel="stylesheet" href="styles.css">  <!-- Connect the CSS file -->
</head>
```

This keeps your structure (HTML) and your styling (CSS) in separate files — a practice called **separation of concerns**. You can change the look of your entire site by editing one CSS file without touching the HTML.

---

## Selectors: Targeting Elements

A CSS rule has two parts: a **selector** (what to style) and a **declaration block** (how to style it):

```css
h1 {
    color: navy;        /* Change the text color */
    font-size: 2rem;    /* Set the font size */
}
```

Here, `h1` is the selector (targets all `<h1>` elements), and the declarations inside the curly braces are the styles to apply.

There are several types of selectors:

**Element selectors** target all elements of a type:

```css
p { color: #333; }           /* ALL paragraphs */
```

**Class selectors** target elements with a specific `class` attribute. Classes start with a dot:

```css
.highlight { background-color: yellow; }   /* Any element with class="highlight" */
```

**ID selectors** target one specific element with a unique `id`. IDs start with a hash:

```css
#about { padding: 20px; }    /* The element with id="about" */
```

**Descendant selectors** target elements inside other elements:

```css
nav a { color: white; }      /* Only <a> tags that are inside <nav> */
```

A quick specificity rule: if two rules conflict, **ID beats class beats element**. This is the "cascading" part — more specific selectors win.

---

## The Box Model: Every Element Is a Box

This is one of the most important concepts in CSS. **Every HTML element is a rectangular box**, and that box has four layers:

- **Content** — The actual stuff inside the element (text, images)
- **Padding** — Space between the content and the border. Think of it as the cushion inside a picture frame.
- **Border** — A line around the padding (can be invisible, solid, dashed, etc.)
- **Margin** — Space *outside* the border, between this element and its neighbors. Think of it as the gap between picture frames on a wall.

```css
.card {
    padding: 20px;           /* 20px cushion inside the box */
    border: 1px solid #ddd;  /* 1px light gray border */
    margin: 16px;            /* 16px gap around the outside */
}
```

A common gotcha: by default, `width` only sets the *content* width. Padding and border are added on top of that, making the total box wider than you expect. To fix this, most developers add this rule at the top of their CSS:

```css
* {
    box-sizing: border-box;  /* Make width include padding and border */
}
```

---

## Flexbox: Laying Out Elements Side by Side

By default, HTML elements stack vertically — each one goes below the previous one. But what if you want elements side by side, like project cards in a row or a navigation menu across the top?

That's what **Flexbox** does. You apply it to a *container* element, and it controls how the *children* inside that container are arranged:

```css
.project-grid {
    display: flex;            /* Activate Flexbox on this container */
    gap: 20px;                /* Space between each child element */
    flex-wrap: wrap;          /* Wrap to the next line if no room */
}

.project-grid article {
    flex: 1;                  /* Each card takes equal width */
    min-width: 250px;         /* But never narrower than 250px */
}
```

With just those few lines, your project cards arrange themselves in a responsive row that wraps gracefully when the screen gets narrow.

Flexbox has many options (`justify-content`, `align-items`, `flex-direction`), but for this crash course, `display: flex`, `gap`, and `flex-wrap: wrap` will handle 90% of what you need.

---

## Common CSS Properties Quick Reference

Here are the properties you'll use most often:

- `color` — Text color
- `background-color` — Background color of the element
- `font-size` — Text size (use `rem` for relative sizing)
- `font-family` — Which font to use
- `padding` — Inside spacing
- `margin` — Outside spacing
- `border` — Border around the element
- `border-radius` — Rounded corners
- `max-width` — Maximum width (great for centering content)
- `text-align` — Align text (left, center, right)
- `display` — How the element behaves (block, flex, inline)

---

## Why This Matters (Even Though You'll Use Streamlit)

You might be thinking: "I'm going to use Streamlit in Python. Why learn CSS at all?"

Fair question. Here's why: Streamlit generates HTML and CSS under the hood. When your Streamlit layout doesn't look right, understanding the box model and Flexbox helps you debug it. When you need to customize Streamlit's appearance (and you will), you'll write CSS. And when you read web content — documentation, Stack Overflow answers, colleague's code — CSS literacy means you can follow along instead of being lost.

This isn't about becoming a CSS expert. It's about building just enough understanding to be effective in the tools you'll actually use.