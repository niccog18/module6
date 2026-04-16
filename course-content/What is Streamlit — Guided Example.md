# What is Streamlit? — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Build execution_demo.py: live timestamp proving re-runs happen, widgets returning current values, radio buttons changing rendered content, multiselect driving calculations. Show the re-run model in action."]`

Let’s build a small app that demonstrates Streamlit’s execution model and widget system. By the end, you’ll *see* the re-run model happening in real time.

Create a file called `execution_demo.py`:

---

## Step 1: Prove the Re-Run Model

```python
import streamlit as st
from datetime import datetime

st.title("Streamlit Execution Demo")

# This runs on EVERY re-run — so the timestamp changes each time
st.write(f"Script ran at: **{datetime.now().strftime('%H:%M:%S')}**")
```

Run it:

```bash
streamlit run execution_demo.py
```

You should see the app with a title and a timestamp. Now press `R` on your keyboard (Streamlit’s shortcut to re-run). Notice the timestamp changes — proof that the entire script just executed again.

---

## Step 2: Widgets Return Current Values

Add this below the timestamp:

```python
st.divider()  # Visual separator line

st.header("Widget Values")

# Each widget returns its current value
name = st.text_input("What's your name?", placeholder="Type here...")
volume = st.slider("Volume", min_value=0, max_value=100, value=50)
color = st.selectbox("Favorite color", ["Red", "Blue", "Green", "Purple"])

# Display the current values
st.write(f"Name: **{name or '(empty)'}**")
st.write(f"Volume: **{volume}**")
st.write(f"Color: **{color}**")
```

Save the file. Streamlit will detect the change and prompt you to re-run (or click "Always rerun" to enable auto-refresh).

Type in the name field. Move the slider. Change the selectbox. After *each* interaction, check the timestamp at the top — it updates every time, proving the script re-ran.

---

## Step 3: Conditional Rendering with Radio Buttons

Add this:

```python
st.divider()
st.header("Conditional Content")

# Radio button returns the selected option as a string
topic = st.radio(
    "What would you like to learn about?",
    ["Python", "JavaScript", "SQL", "FastAPI"]
)

# Different content renders based on the selection
if topic == "Python":
    st.info("Python is a versatile language used in AI, data science, web development, and automation.")
    st.code('print("Hello from Python!")', language="python")
elif topic == "JavaScript":
    st.info("JavaScript makes web pages interactive. It runs in the browser.")
    st.code('console.log("Hello from JS!");', language="javascript")
elif topic == "SQL":
    st.info("SQL queries and manages data in relational databases.")
    st.code('SELECT * FROM users WHERE active = true;', language="sql")
elif topic == "FastAPI":
    st.info("FastAPI builds high-performance Python APIs with auto-validation.")
    st.code('@app.get("/hello")\ndef hello():\n    return {"message": "Hello!"}', language="python")
```

Save and interact. Click different radio options — the content below changes instantly. There are no event listeners, no callback functions, no DOM updates. You just wrote `if/elif` logic, and Streamlit handles the rest.

---

## Step 4: Multiselect Driving Calculations

Add this:

```python
st.divider()
st.header("Dynamic Calculations")

# Multiselect returns a list of selected options
modules = st.multiselect(
    "Which modules have you completed?",
    ["Pre-work: Python", "Module 1: AI Fundamentals", "Module 2: Advanced Python",
     "Module 3: Databases", "Module 4: REST APIs", "Module 5: FastAPI"],
    default=["Pre-work: Python"]  # Pre-selected
)

# Calculate and display progress
total_modules = 9  # Total in the course
completed = len(modules)
progress = completed / total_modules

st.write(f"Completed: **{completed}** of **{total_modules}** modules")
st.progress(progress)  # Built-in progress bar widget

if progress == 1.0:
    st.balloons()  # Fun celebration animation!
    st.success("Congratulations! You've completed the course!")
elif progress >= 0.5:
    st.write("More than halfway there! Keep going!")
else:
    st.write("Great start! Every module builds on the last.")
```

Save and try it. Select and deselect modules — the progress bar, count, and message update instantly.

Notice how natural this feels: you’re writing Python `if/elif` logic, using `len()` on a list, and doing basic math. No web framework knowledge needed. That’s the Streamlit promise.

---

## What You Should See

Your final app has four sections: a live timestamp proving re-runs, interactive widgets displaying their current values, a radio button switching between different content blocks, and a multiselect driving a progress calculation. Every interaction triggers a re-run, and every section updates based on the current widget values.

![image.png](What%20is%20Streamlit%20%E2%80%94%20Guided%20Example/image.png)