# HTML Structure & Semantic Elements — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 8 min — "Build a semantic profile page from scratch. Show the unstyled HTML result in the browser and explain what each semantic element contributes."]`

Let's build a real HTML page from scratch. We'll create a simple profile page using semantic elements. By the end, you'll have a file you can open in your browser and see a structured (if unstyled) webpage.

---

## Step 1: Create the File

Create a new file called `profile.html` in your project folder. You can use VS Code or any text editor.

Start with the document skeleton:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Developer Profile</title>  <!-- This text shows in the browser tab -->
</head>
<body>
    <!-- We'll build everything in here -->
</body>
</html>
```

Save and open the file in your browser (double-click the file, or in VS Code right-click → "Open with Live Server" if you have that extension). You should see a blank page with "Developer Profile" in the browser tab.

---

## Step 2: Add the Header

Inside the `<body>` tag, add a header with your name and a navigation menu:

```html
<body>
    <header>
        <h1>Alex Johnson</h1>  <!-- The main heading of the page -->
        <p>AI Engineering Student | Coding Temple</p>

        <nav>  <!-- Navigation section -->
            <a href="#about">About</a> |
            <a href="#projects">Projects</a> |
            <a href="#skills">Skills</a> |
            <a href="#contact">Contact</a>
        </nav>
    </header>
```

Save and refresh your browser. You should see a heading, a subtitle, and four links in a row. The links use `#about`, `#projects`, etc. — these are **anchor links** that will jump to sections on the same page (once we add those sections with matching `id` attributes).

---

## Step 3: Add the Main Content

Below the `</header>` tag, add the `<main>` section with an About section and a Projects section:

```html
<main>
    <!-- About Section -->
    <section id="about">  <!-- id="about" lets the nav link jump here -->
        <h2>About Me</h2>
        <p>I'm a career changer transitioning into AI engineering. Previously, I worked in hospitality management for 8 years, where I developed strong problem-solving and communication skills. Now I'm building the technical foundation to create AI-powered applications.</p>
        <p>Currently working through the <strong>AI Engineering Foundations</strong> program at Coding Temple, where I've already built Python applications, designed databases with SQLAlchemy, and created REST APIs with FastAPI.</p>
    </section>

    <!-- Projects Section -->
    <section id="projects">
        <h2>Projects</h2>

        <article>  <!-- Each project is a self-contained article -->
            <h3>Student Grade Tracker</h3>
            <p>A command-line Python application that reads student data from CSV files, calculates averages, and generates summary reports. Built with proper error handling and virtual environment management.</p>
        </article>

        <article>
            <h3>Data Processing Pipeline</h3>
            <p>An OOP-based data pipeline that cleans messy datasets using pandas, performs analysis with grouping and aggregation, and generates visualizations with matplotlib.</p>
        </article>

        <article>
            <h3>AI-Ready Task Manager API</h3>
            <p>A FastAPI backend with JWT authentication, full CRUD operations, SQLAlchemy database integration, and automated testing with pytest.</p>
        </article>
    </section>

    <!-- Skills Section -->
    <section id="skills">
        <h2>Skills</h2>
        <ul>  <!-- Unordered list for skills -->
            <li>Python (pandas, matplotlib, requests)</li>
            <li>SQL & SQLAlchemy ORM</li>
            <li>FastAPI & REST API Design</li>
            <li>Git & GitHub</li>
            <li>Testing with pytest</li>
        </ul>
    </section>
</main>
```

Save and refresh. You should see three sections with headings, paragraphs, project descriptions, and a bulleted skills list. Notice how each `<article>` is a self-contained project description — you could lift any one of them out and it would still make sense on its own.

---

## Step 4: Add the Footer

Finally, add a footer below the closing `</main>` tag:

```html
    <footer id="contact">
        <h2>Contact</h2>
        <p>Email: <a href="mailto:alex@example.com">alex@example.com</a></p>
        <p>GitHub: <a href="https://github.com/alexjohnson" target="_blank">github.com/alexjohnson</a></p>
        <p>&copy; 2026 Alex Johnson</p>  <!-- &copy; displays the © symbol -->
    </footer>
</body>
</html>
```

Save and refresh. Your complete page now has a clear structure: header with navigation, main content with about/projects/skills sections, and a footer with contact info.

---

## What You Should See

The page looks plain — no colors, default fonts, everything left-aligned. That's by design. HTML gives you structure. In the next lesson, you'll add CSS to make it look polished.

But right-click on the page and choose "Inspect." In the Elements panel, you'll see the semantic hierarchy clearly: `<header>`, `<main>` with nested `<section>` and `<article>` elements, and `<footer>`. A screen reader could navigate this page effortlessly because the structure has *meaning*, not just layout.

`[DIAGRAM PLACEHOLDER: Side-by-side showing the plain rendered HTML page on the left, and the semantic element tree structure (header > nav, main > section > article, footer) on the right]`