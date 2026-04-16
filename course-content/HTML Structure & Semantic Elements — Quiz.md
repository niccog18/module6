# HTML Structure & Semantic Elements — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What is the purpose of semantic HTML elements like `<header>`, `<main>`, and `<footer>`?

- A) They make the page load faster
- B) They describe the meaning and role of content, not just its position
- C) They automatically add styling to the page
- D) They are required for the page to display in a browser

> **Answer: B** — Semantic elements tell browsers, screen readers, and search engines *what* the content is, not just that it exists. A `<nav>` says "this is navigation," while a `<div>` just says "this is a container." They don't add speed (A), don't add styling on their own beyond default browser styles (C), and aren't strictly required for rendering — you could build a page entirely with `<div>` tags and it would display, just without meaningful structure (D).
> 

---

**Question 2:** What is the `<main>` element used for, and how many can appear on a page?

- A) It wraps all content including headers and footers; you can have multiple per page
- B) It wraps the dominant, unique content of the page; there should be only one per page
- C) It wraps the navigation menu; there should be only one per page
- D) It's interchangeable with `<section>` and you can have as many as you need

> **Answer: B** — `<main>` identifies the primary content of the page — the content that is unique to this page and not repeated across other pages (unlike headers, footers, or nav bars). The HTML spec says there should be only one `<main>` per page. If you picked D, `<section>` is for thematic groupings *within* the main content — you can have many sections, but they serve a different role than `<main>`.
> 

---

**Question 3:** Why should images always include an `alt` attribute?

- A) It makes the image load faster
- B) It changes the image's appearance
- C) It provides a text description for screen readers and displays when the image fails to load
- D) It's required for the image to display at all

> **Answer: C** — The `alt` attribute serves two critical purposes: it provides a text alternative for users who rely on screen readers (accessibility), and it displays as fallback text when the image can't be loaded (broken link, slow connection). It doesn't affect loading speed (A) or appearance (B), and images will still display without it (D) — they'll just be inaccessible to screen reader users.
> 

---

**Question 4:** Which section of the HTML document skeleton contains metadata that is NOT visible on the page itself?

- A) `<body>`
- B) `<main>`
- C) `<head>`
- D) `<footer>`

> **Answer: C** — The `<head>` section contains metadata like the page title (shown in the browser tab, not on the page), character encoding, viewport settings, and links to CSS files. None of this content is directly visible to the user on the page. The `<body>` (A) is where all visible content lives. `<main>` (B) and `<footer>` (D) are both inside `<body>` and are visible.
>