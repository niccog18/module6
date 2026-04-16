# What is Streamlit? — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what Streamlit is and why it’s the right tool for AI interfaces
2. Describe Streamlit’s re-run execution model and why it’s the most important concept to understand
3. Install Streamlit and run a basic app from the terminal
4. Compare the effort required to build the same UI in HTML/CSS/JS versus Streamlit

---

`[VIDEO PLACEHOLDER: 5 min — "What is Streamlit? Build a simple app from zero in under 5 minutes. Show how little code is needed compared to the HTML/CSS/JS approach from Week 1. This is why we chose Streamlit — you stay in Python."]`

Last week you learned HTML, CSS, and JavaScript. You built pages, styled them, made them interactive, and connected them to an API. It worked — but it took a lot of code across multiple files in three different languages.

Now imagine you could do all of that in one Python file. No HTML. No CSS. No JavaScript. Just Python.

That’s **Streamlit**.

Streamlit is a Python library that turns Python scripts into interactive web applications. You write Python, and Streamlit converts it into a fully functional web app with widgets, charts, tables, and layouts — all rendered in the browser.

---

## The Same App, Two Ways

Let’s compare building a simple "Hello World" app:

**HTML/CSS/JS version** (3 files, ~40 lines):

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Hello!</h1>
    <input type="text" id="name-input" placeholder="Enter your name">
    <p id="greeting"></p>
    <script>
        document.querySelector("#name-input").addEventListener("input", (e) => {
            document.querySelector("#greeting").textContent = 
                e.target.value ? `Hello, ${e.target.value}!` : "";
        });
    </script>
</body>
</html>
```

**Streamlit version** (1 file, 4 lines):

```python
import streamlit as st

st.title("Hello!")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")
```

Four lines. One language. No event listeners, no DOM manipulation, no separate CSS file. Streamlit handles all the web rendering for you.

---

## The Re-Run Model (THE Most Important Concept)

Here’s the one thing you absolutely must understand about Streamlit, because everything else builds on it:

**Every time a user interacts with any widget, the entire Python script re-runs from top to bottom.**

Read that again. It’s not like Flask or FastAPI where specific functions handle specific requests. In Streamlit, *the whole script runs again*. Every time.

- User types in a text box? Script re-runs.
- User clicks a button? Script re-runs.
- User moves a slider? Script re-runs.

This is radically different from how JavaScript works. In JavaScript, you set up event listeners that run specific functions when specific things happen. In Streamlit, there are no event listeners — the entire script IS the event handler.

This design makes Streamlit incredibly simple to write. But it has one critical consequence:

**All variables reset to their initial values on every re-run.**

This means code like this does NOT work as a counter:

```python
count = 0  # Resets to 0 every time the script re-runs!
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")  # Always shows 0 or 1, never 2+
```

The solution is `st.session_state` — a dictionary that persists across re-runs. You’ll learn this in the State Management lesson.

---

## Installation and Running

Install Streamlit in your module’s virtual environment:

```bash
pip install streamlit
```

Create a file called `app.py` and add some code, then run it:

```bash
streamlit run app.py
```

Streamlit starts a local web server and opens your browser to `http://localhost:8501`. Every time you save the file, Streamlit detects the change and offers to re-run the app.

---

## Why Streamlit for AI Interfaces?

Streamlit was *designed* for data and AI applications. It has built-in support for displaying DataFrames and tables with sorting and filtering, rendering charts with one line of code, streaming text (critical for AI chat interfaces), managing file uploads, caching expensive computations (like model loading or API calls), and chat interface components (`st.chat_message`, `st.chat_input`).

For the rest of this course — building semantic search tools (Module 7), RAG chatbots (Module 8), and your capstone project (Module 9) — Streamlit will be your frontend. The web literacy from Week 1 helps you understand what Streamlit is doing under the hood. But from here forward, you stay in Python.

---

## Widget Basics: Every Widget Returns a Value

Streamlit widgets aren’t just visual elements — they’re **functions that return the current value of the widget**:

```python
name = st.text_input("Your name")     # Returns "" until the user types
age = st.slider("Age", 18, 100, 25)   # Returns the current slider value (default 25)
agreed = st.checkbox("I agree")        # Returns True or False
color = st.selectbox("Color", ["Red", "Blue", "Green"])  # Returns the selected option
```

Because the script re-runs on every interaction, these widgets always return their *current* value. You can use those values immediately in conditions, calculations, or API calls — no event listeners needed.

This is the power of Streamlit’s model: describe what you want to display, and Streamlit handles the interactivity.