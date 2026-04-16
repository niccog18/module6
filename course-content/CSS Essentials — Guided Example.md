# CSS Essentials — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Style the profile page: step-by-step CSS transformation from unstyled HTML to a polished, Flexbox-based layout with dark header, hover effects, and card grid."]`

Let's take the profile page from the HTML lesson and make it look professional. We'll create a separate CSS file and build up the styles step by step.

---

## Step 1: Create the CSS File and Link It

Create a new file called `styles.css` in the same folder as your `profile.html`.

Open `profile.html` and add this line inside the `<head>` section (below the `<title>` tag):

```html
<link rel="stylesheet" href="styles.css">
```

Now open `styles.css` and start with the universal box-sizing reset and some base styles:

```css
/* --- Reset and Base Styles --- */
* {
    box-sizing: border-box;  /* Padding and border included in width */
    margin: 0;               /* Remove default margins */
    padding: 0;              /* Remove default padding */
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;          /* Space between lines of text */
    color: #333;               /* Dark gray text */
    background-color: #f5f5f5; /* Light gray background */
}
```

Save both files and refresh the browser. You should see the fonts change and the background turn light gray. The default spacing around elements disappears because of our reset.

---

## Step 2: Style the Header

Let's make the header dark with white text:

```css
/* --- Header --- */
header {
    background-color: #1a1a2e;  /* Dark navy background */
    color: white;               /* White text */
    padding: 40px 20px;         /* 40px top/bottom, 20px left/right */
    text-align: center;         /* Center all text in the header */
}

header h1 {
    font-size: 2.5rem;          /* Large heading */
    margin-bottom: 8px;         /* Small gap below the name */
}

header p {
    font-size: 1.1rem;          /* Slightly larger than body text */
    opacity: 0.85;              /* Slightly transparent for a subtitle feel */
}
```

Save and refresh. The header should now be a dark navy bar with your name centered in large white text.

---

## Step 3: Style the Navigation Links

Let's make the nav links look like a proper menu:

```css
/* --- Navigation --- */
nav {
    margin-top: 20px;  /* Gap between subtitle and nav */
}

nav a {
    color: #e0e0e0;             /* Light gray link color */
    text-decoration: none;       /* Remove underline */
    margin: 0 12px;             /* 12px gap on each side of each link */
    font-weight: 500;           /* Slightly bolder than normal */
    transition: color 0.2s;      /* Smooth color change on hover */
}

nav a:hover {
    color: #00d4ff;  /* Bright blue when hovering */
}
```

Save and refresh. Hover over the nav links — they should smoothly transition to bright blue. The `transition` property creates that smooth animation instead of an abrupt color change.

---

## Step 4: Center the Main Content

Let's constrain the main content to a readable width and center it:

```css
/* --- Main Content --- */
main {
    max-width: 900px;      /* Never wider than 900px */
    margin: 40px auto;     /* Center horizontally with auto left/right margins */
    padding: 0 20px;       /* 20px padding on left and right for small screens */
}

section {
    margin-bottom: 40px;   /* Space between sections */
}

section h2 {
    font-size: 1.8rem;
    margin-bottom: 16px;
    color: #1a1a2e;        /* Match the header color */
    border-bottom: 2px solid #00d4ff;  /* Blue underline */
    padding-bottom: 8px;
}
```

Save and refresh. The content should now be centered with a max width, and section headings should have a blue underline accent.

---

## Step 5: Create a Flexbox Card Grid for Projects

First, add a `class` attribute to the projects section in your HTML. Open `profile.html` and change:

```html
<section id="projects">
    <h2>Projects</h2>
```

to:

```html
<section id="projects">
    <h2>Projects</h2>
    <div class="project-grid">  <!-- Add this wrapper -->
```

And add the closing `</div>` after the last `</article>` but before `</section>`.

Now add the Flexbox styles in `styles.css`:

```css
/* --- Project Cards with Flexbox --- */
.project-grid {
    display: flex;              /* Arrange children in a row */
    gap: 20px;                  /* 20px space between cards */
    flex-wrap: wrap;            /* Wrap to next line if needed */
}

.project-grid article {
    flex: 1;                    /* Each card takes equal width */
    min-width: 250px;           /* Never narrower than 250px */
    background-color: white;    /* White card background */
    padding: 24px;              /* Padding inside each card */
    border-radius: 8px;         /* Rounded corners */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    transition: transform 0.2s; /* Smooth hover animation */
}

.project-grid article:hover {
    transform: translateY(-4px);  /* Lift the card slightly on hover */
}

.project-grid article h3 {
    color: #1a1a2e;
    margin-bottom: 8px;
}
```

Save and refresh. Your three project entries should now appear as white cards in a row, with rounded corners and subtle shadows. Hover over one — it should lift up slightly.

---

## Step 6: Style the Footer

```css
/* --- Footer --- */
footer {
    background-color: #1a1a2e;  /* Match header */
    color: white;
    text-align: center;
    padding: 30px 20px;
    margin-top: 40px;
}

footer a {
    color: #00d4ff;             /* Blue links in footer */
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;  /* Underline on hover */
}
```

Save and refresh. Your page should now have a cohesive, professional look: dark header and footer bookending centered content with card-style project entries.

`[DIAGRAM PLACEHOLDER: Before/after screenshot showing the unstyled HTML page on the left and the fully styled page on the right]`

[https://www.notion.so](https://www.notion.so)