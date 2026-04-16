# HTML Structure & Semantic Elements — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what HTML is and how it provides structure to web pages
2. Write a valid HTML document skeleton with `<!DOCTYPE>`, `<html>`, `<head>`, and `<body>`
3. Use semantic HTML elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`) to create meaningful page structure
4. Explain the difference between semantic and generic HTML elements

---

`[VIDEO PLACEHOLDER: 5 min — "What HTML is: show a webpage, then view source to reveal the HTML underneath. Demonstrate how HTML provides structure that CSS styles and JS makes interactive."]`

Imagine you're building a house. Before you pick paint colors or install smart light switches, you need a frame — walls, a roof, rooms, a foundation. Without the frame, there's nothing to paint and nowhere to install switches.

HTML is the frame of every webpage. It defines the structure: "This is a heading. This is a paragraph. This is a navigation menu. This is an image." It doesn't say anything about colors, fonts, or what happens when you click something — that's CSS and JavaScript, which you'll learn in the next two lessons. HTML just says *what's there* and *how it's organized*.

Every single webpage you've ever visited — Google, YouTube, your bank's website, your FastAPI docs at `/docs` — is built on HTML. It's the foundation of the web.

---

## How HTML Works: Tags and Elements

HTML uses **tags** to mark up content. A tag is a keyword wrapped in angle brackets:

```html
<p>This is a paragraph.</p>
```

Most tags come in pairs: an **opening tag** (`<p>`) and a **closing tag** (`</p>` — notice the forward slash). Everything between them is the *content* of that element. The whole unit — opening tag + content + closing tag — is called an **element**.

Some tags are **self-closing** because they don't wrap around content:

```html
<img src="photo.jpg" alt="A description of the photo">
<br>  <!-- Line break — no closing tag needed -->
```

Tags can also have **attributes** — extra information inside the opening tag. In the `<img>` example above, `src` tells the browser where to find the image, and `alt` provides a text description for screen readers and for when the image fails to load.

---

## The HTML Document Skeleton

Every HTML page starts with the same basic structure. Think of it as the blueprint every house needs before you add rooms:

```html
<!DOCTYPE html>       <!-- Tells the browser: "This is modern HTML" -->
<html lang="en">      <!-- The root element. lang="en" says it's in English -->
<head>
    <!-- Metadata that doesn't appear on the page itself -->
    <meta charset="UTF-8">                 <!-- Character encoding -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page Title</title>           <!-- Shows in the browser tab -->
</head>
<body>
    <!-- Everything visible on the page goes here -->
    <h1>Hello, World!</h1>
    <p>This is my first webpage.</p>
</body>
</html>
```

The `<head>` section is like the paperwork for a house — the deed, the building permit, the address. It's important but you don't *see* it when you walk inside. The `<body>` is the house itself — everything the visitor sees and interacts with.  

---

## Semantic HTML: Giving Your Structure Meaning

Here's where HTML gets interesting — and where most beginners miss a crucial concept.

You *could* build an entire webpage using just `<div>` tags (a generic container with no inherent meaning):

```html
<div>Navigation here</div>
<div>Main content here</div>
<div>Footer here</div>
```

This works visually, but it's like labeling every room in your house "Room." A person walking through can figure out which room is the kitchen by looking inside, but it would be much easier if the doors were labeled "Kitchen," "Bedroom," "Bathroom."

**Semantic HTML** elements are those labeled doors. They describe *what the content is*, not just that content exists:

```html
<header>Navigation and branding here</header>
<main>The primary content of the page</main>
<footer>Contact info and legal notices here</footer>
```

Here are the key semantic elements you should know:

- `<header>` — Introductory content, often containing a logo and navigation
- `<nav>` — A section of navigation links
- `<main>` — The dominant content of the page (only one per page)
- `<section>` — A thematic grouping of content, usually with a heading
- `<article>` — A self-contained piece of content (a blog post, a product card, a news story)
- `<aside>` — Content tangentially related to the main content (a sidebar)
- `<footer>` — Footer content, usually contact info, copyright, or navigation

`[DIAGRAM PLACEHOLDER: Visual showing a typical webpage layout with semantic elements labeled — header at top, nav inside header, main in the center with article and section inside it, aside on the right, footer at bottom]`

![image.png](HTML%20Structure%20&%20Semantic%20Elements%20%E2%80%94%20Concept/image.png)

---

## Why Semantic HTML Matters

Using semantic elements isn't just good practice — it has real consequences:

**Accessibility.** Screen readers (software that reads webpages aloud for visually impaired users) use semantic tags to navigate. A screen reader can jump directly to `<main>` to skip the navigation, or list all `<nav>` elements for quick orientation. With only `<div>` tags, a screen reader sees a flat wall of unlabeled content.

**SEO (Search Engine Optimization).** Search engines like Google use semantic structure to understand your page. Content inside `<article>` is treated as the primary content; `<nav>` is understood as navigation. This helps search engines rank your page more accurately.

**Developer experience.** When you (or a teammate) come back to your code in six months, `<header>` and `<footer>` are instantly clear. Forty nested `<div>` tags are not.

For this course, the most practical reason is **understanding structure**. When you build Streamlit apps in Week 2, Streamlit generates HTML under the hood. Understanding what it's generating helps you debug layout issues and write better applications.

---

## Common HTML Elements for Content

Beyond the structural elements, here are the content elements you'll encounter most often:

- `<h1>` through `<h6>` — Headings (h1 is the biggest/most important, h6 is the smallest)
- `<p>` — Paragraphs
- `<a href="url">` — Links ("anchor" tags)
- `<img src="url" alt="description">` — Images
- `<ul>` and `<ol>` — Unordered (bulleted) and ordered (numbered) lists
- `<li>` — A list item inside `<ul>` or `<ol>`
- `<strong>` — Bold text (semantically: important text)
- `<em>` — Italic text (semantically: emphasized text)

Notice how each element describes *what the content is*, not how it looks. An `<h1>` is the main heading — the browser happens to make it big and bold by default, but that's just the default styling. You could style a `<p>` to look identical to an `<h1>`, but a screen reader would still know the difference. Structure and style are separate concerns.