# Diagrams

Prompt: 

The placeholders for Diagrams are missing from the module 6 notion content [https://www.notion.so/codingtemple/Module-6-Web-Essentials-Streamlit-31ad15b03f0a8133a0c2f216e597fa24](../Module%206%20Web%20Essentials%20&%20Streamlit%2031ad15b03f0a8133a0c2f216e597fa24.md)

please help me make complete prompts for the diagrams to add into an AI image generator (Nano Banana) [add asset list]

---

**Status across all 12 concept pages:**

- ✅ Has image already: How the Web Works (2), JavaScript Basics (2), Streamlit Layout, State Management, Displaying Data
- ⚠️ Has `[DIAGRAM PLACEHOLDER]` text + image: HTML Semantic Elements (placeholder was never cleaned up)
- ❌ Has `[DIAGRAM PLACEHOLDER]` text, **no image**: Connecting Frontend to Backend
- ❌ Has `<empty-block/>` where image should be: CSS Essentials (box model section)
- ❌ No placeholder, no image (diagrams clearly needed): Fetch API & Async/Await, What is Streamlit?, Connecting Streamlit to FastAPI, Building an AI-Powered Interface

That's **6 diagrams needed** (I'm including the HTML Semantic one since the placeholder text is still sitting there and you may want to verify the embedded image is good). Here are the complete prompts:

---

## Module 6 — AI Image Generation Prompts

---

### DIAGRAM 1

**Lesson:** HTML Structure & Semantic Elements — Concept
**Placement:** After the semantic elements list (header, nav, main, article, aside, footer)
**Note:** A placeholder tag is still visible in Notion — verify the existing embedded image is sufficient or replace with this.

**Prompt:**

> Flat design educational diagram showing the layout of an HTML webpage using semantic elements. Clean white background with light gray section boxes. Show the full page as a tall rectangle. At the very top, a wide box labeled `<header>` in dark text with a smaller `<nav>` box nested inside it. Below that, a horizontal row with a large center box labeled `<main>` (containing two boxes inside labeled `<section>` and `<article>`) and a narrower box on the right labeled `<aside>`. At the bottom of the page, a wide box labeled `<footer>`. Each element label uses monospace font with angle brackets. Color code each element type with a distinct pastel color: header/nav = navy blue tones, main/section/article = teal tones, aside = amber/orange tones, footer = purple tones. Include a small legend in the bottom right corner. Style: developer education, minimalist, no shadows, sans-serif font, technical illustration.
> 

---

### DIAGRAM 2

**Lesson:** CSS Essentials — Concept
**Placement:** After the box model explanation (content, padding, border, margin), in the empty block where the image should be

**Prompt:**

> Flat design educational diagram of the CSS box model. Show four perfectly centered concentric rectangles, each labeled clearly. Outermost rectangle labeled "MARGIN" in light gray with a dashed gray border and very light gray fill. Next rectangle inward labeled "BORDER" in medium gray with a solid dark gray border. Next rectangle labeled "PADDING" in soft blue with a blue fill. Innermost rectangle labeled "CONTENT" in a medium blue with white text. Each layer is evenly spaced with visible gap showing the space between layers. Arrows on the left side pointing to each layer with the label name. Below the diagram, small text showing example CSS: `padding: 20px`, `border: 1px solid #ddd`, `margin: 16px`. Clean white background. Style: developer education, flat design, no decorative elements, monospace font for code, sans-serif for labels.
> 

---

### DIAGRAM 3

**Lesson:** Connecting Frontend to Backend — Concept
**Placement:** After the CORS introduction, before the "Sending Auth Headers" section — this is the one with the `[DIAGRAM PLACEHOLDER]` tag that has NO image

**Prompt:**

> Flat design technical flow diagram showing the full browser-to-database communication chain with JWT authentication. Horizontal flow left to right across the image. Show these labeled steps as connected boxes with arrows between them: 1) A browser icon labeled "Browser / User" → 2) A box labeled `fetch()` with a JWT token icon and text "Authorization: Bearer token" → 3) A green box labeled "FastAPI" with a small lock icon labeled "CORS check" → 4) A yellow box labeled "JWT Validation" with a checkmark → 5) A teal box labeled "SQLAlchemy" → 6) A blue cylinder labeled "Database" → then an arrow turning back left showing the return path → labeled "JSON Response" → back to the Browser box. Return arrows are shown in orange below the forward arrows. Label the top row "REQUEST →" and the bottom row "← RESPONSE". Clean white background, monospace font for code snippets, sans-serif for labels. Style: developer education, minimalist flow diagram, flat design.
> 

---

### DIAGRAM 4

**Lesson:** Fetch API & Async/Await — Concept
**Placement:** After the "restaurant" analogy (blocking vs non-blocking), before the `fetch()` code example

**Prompt:**

> Flat design educational diagram comparing synchronous (blocking) vs asynchronous (non-blocking) execution. Split the image into two columns with a clear dividing line. Left column header: "❌ Synchronous (Blocking)" — show a vertical timeline with events stacked: a user icon at top → a box labeled "Send request" → a long gray bar labeled "⏳ WAITING... (page frozen)" → a box labeled "Response arrives" → a box labeled "Continue". Right column header: "✓ Asynchronous (Non-Blocking)" — show a vertical timeline: a user icon → "Send request" → shorter bar labeled "Request sent" → multiple parallel boxes showing "User scrolls", "User clicks", "Page stays interactive" → then a box labeled "Response arrives" → "Handle response". Use red/orange tones for the blocking side and green/teal tones for the async side. Timeline arrows are vertical. Caption at bottom: "fetch() is non-blocking — the page stays responsive while waiting." Clean white background, sans-serif font. Style: developer education, flat design, timeline diagram.
> 

---

### DIAGRAM 5

**Lesson:** What is Streamlit? — Concept
**Placement:** After the re-run model explanation (the `count = count + 1` section), before Installation

**Prompt:**

> Flat design educational diagram illustrating the Streamlit re-run model. Show a circular loop. At the top of the circle, a box labeled "Script runs top to bottom" with a down arrow. On the right side, a box showing a simplified code snippet with a slider widget. Below that on the right, a box labeled "User moves slider" with a cursor/hand icon. At the bottom, a box labeled "Widget interaction detected" with a lightning bolt icon. On the left side, a box labeled "Streamlit triggers re-run" with a refresh/circular arrow icon. An arrow connecting back to the top. In the center of the circle, bold text: "EVERY interaction = full re-run". Color the cycle boxes in a consistent teal/blue palette. Below the main diagram, show a small "Key insight" callout box in yellow: "Widget functions always return their current value — no event listeners needed." Clean white background, sans-serif font. Style: developer education, circular flow diagram, flat design.
> 

---

### DIAGRAM 6

**Lesson:** Connecting Streamlit to FastAPI — Concept
**Placement:** After the project structure code block, before the `api_client.py` section

**Prompt:**

> Flat design educational diagram showing the Streamlit + FastAPI authentication gate pattern. Show a vertical flowchart with decision logic. Start at the top with a box: "App loads / User interacts". Arrow down to a diamond decision shape: "Token in session_state?" Left branch labeled "No" leads to a box: "Show Login Form" with a simple form mockup (username + password fields, Login button). An arrow from Login form to a box: "Call /auth/token endpoint" → decision diamond: "Valid credentials?" → "Yes" arrow leads to a box: "Store token in session_state" → dotted arrow looping back up to the decision. Right branch labeled "Yes" from the main decision leads to a box: "Show App Dashboard" with a small dashboard mockup (sidebar + main content). At the bottom, an "X" path from "Valid credentials? No" leads to "Show error message". Color: decision diamonds in amber/yellow, action boxes in teal/blue, login state in orange, dashboard state in green. Clean white background, sans-serif font, monospace for code references. Style: developer education, flowchart, flat design.
> 

---

### DIAGRAM 7

**Lesson:** Building an AI-Powered Interface — Concept
**Placement:** After the "Chat History Pattern" code block explanation, before the Streaming section

**Prompt:**

> Flat design educational diagram showing how Streamlit chat history works across re-runs. Show three side-by-side panels labeled "Run 1", "Run 2", "Run 3" with a right-pointing arrow between each labeled "User sends message / Re-run triggers". In Run 1 panel: session_state messages list shows 1 item (human bubble: "What is Python?") — script renders it — AI bubble appears below. In Run 2 panel: session_state messages list shows 2 items — script re-renders both bubbles from history — plus a new user message being added. In Run 3 panel: session_state messages list shows 3+ items — all previous bubbles shown — AI response being streamed in. Below the three panels, a caption box: "Each re-run: (1) render full history from session_state, (2) display new message, (3) append to session_state." Use alternating blue (user) and gray (assistant) message bubble colors. The session_state list is shown as a small stack/array icon on the left of each panel. Clean white background, sans-serif font. Style: developer education, panel sequence diagram, flat design.
> 

---

**Quick reference — where each goes in Notion:**

| # | Diagram | Notion Page | Status |
| --- | --- | --- | --- |
| 1 | HTML Semantic Elements Layout | HTML Structure & Semantic Elements — Concept | Placeholder tag still present; existing image may be sufficient |
| 2 | CSS Box Model | CSS Essentials — Concept | Empty block — image never added |
| 3 | Frontend-Backend JWT Flow | Connecting Frontend to Backend — Concept | Placeholder tag present, no image |
| 4 | Sync vs Async Blocking | Fetch API & Async/Await — Concept | No placeholder, no image |
| 5 | Streamlit Re-Run Model | What is Streamlit? — Concept | No placeholder, no image |
| 6 | Auth Gate Flowchart | Connecting Streamlit to FastAPI — Concept | No placeholder, no image |
| 7 | Chat History Pattern | Building an AI-Powered Interface — Concept | No placeholder, no image |