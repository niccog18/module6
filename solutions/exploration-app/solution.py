"""
L7 — Streamlit Exploration App: Python Learning Journey  (Solution)
=====================================================================
Run with:
    streamlit run solution.py

KEY CONCEPT — the re-run model:
    Every time a user interacts with a widget (moves a slider, selects an
    option, types in a text box), Streamlit re-executes the ENTIRE script
    from top to bottom.

    This means:
      • Widget calls (st.slider, st.selectbox, etc.) both RENDER the widget
        AND RETURN the current value.
      • You use the returned value immediately in the same run.
      • There is no event loop or callback to register — just write
        top-to-bottom Python.

Session state (st.session_state) is needed only when you want values to
PERSIST across re-runs or be shared between widgets. For simple reactive
displays, the return values are enough.
"""

import streamlit as st

# ── Page configuration ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="Python Learning Journey",
    page_icon="🐍",
    layout="centered",
)

st.title("🐍 Python Learning Journey")
st.caption("Adjust the widgets to explore your progress and learning path.")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 1 — slider
# Returns an int (or float). Triggers a re-run every time value changes.
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("1. Experience Level")
weeks = st.slider(
    label="How many weeks have you been coding?",
    min_value=0,
    max_value=52,
    value=8,      # default value
    step=1,
    help="Drag to adjust your experience level",
)

# Immediate use of the returned value — this line re-evaluates every run
if weeks == 0:
    level_label = "Absolute Beginner"
elif weeks < 4:
    level_label = "Newcomer"
elif weeks < 12:
    level_label = "Beginner"
elif weeks < 26:
    level_label = "Intermediate"
else:
    level_label = "Advanced"

st.metric(label="Experience Level", value=level_label, delta=f"{weeks} weeks")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 2 — selectbox
# Displays a dropdown; returns the selected item from the options list.
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("2. Current Topic")
topic = st.selectbox(
    label="Which Python topic are you working on?",
    options=[
        "Variables & Data Types",
        "Control Flow (if/for/while)",
        "Functions & Scope",
        "Object-Oriented Programming",
        "File I/O & Exceptions",
        "Data Structures (lists, dicts, sets)",
        "APIs & requests library",
        "Web Frameworks (FastAPI, Streamlit)",
    ],
)

# Show a topic-specific tip
tips = {
    "Variables & Data Types": "💡 Python is dynamically typed — you don't need to declare types.",
    "Control Flow (if/for/while)": "💡 Use `enumerate()` to get index AND value in a for loop.",
    "Functions & Scope": "💡 Functions are first-class objects in Python — you can pass them around!",
    "Object-Oriented Programming": "💡 `__init__` is the constructor, `self` refers to the instance.",
    "File I/O & Exceptions": "💡 Always use a `with` statement when opening files — it auto-closes.",
    "Data Structures (lists, dicts, sets)": "💡 Dict comprehensions: `{k: v for k, v in items.items()}`",
    "APIs & requests library": "💡 Always check `response.ok` before calling `response.json()`.",
    "Web Frameworks (FastAPI, Streamlit)": "💡 Streamlit re-runs your script top-to-bottom on every interaction!",
}
st.info(tips.get(topic, "Keep practising!"))

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 3 — radio buttons
# Returns one value from the options list.
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("3. Learning Style")
style = st.radio(
    label="How do you learn best?",
    options=["Reading docs", "Watching videos", "Building projects", "Pair programming"],
    horizontal=True,   # display options side by side
)

resources = {
    "Reading docs":      "📚 Bookmark: [Python Docs](https://docs.python.org/3/) and [Real Python](https://realpython.com/)",
    "Watching videos":   "📺 Check out Corey Schafer's Python tutorials on YouTube.",
    "Building projects": "🔨 Clone a repo, break it, fix it. Building > reading.",
    "Pair programming":  "👥 Ask a classmate to review your code — teaching is the best learning.",
}
st.markdown(resources[style])

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 4 — multiselect
# Returns a list of selected items (can be empty).
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("4. Tools & Libraries You Use")
selected_tools = st.multiselect(
    label="Select all that apply:",
    options=["pandas", "requests", "FastAPI", "Streamlit", "SQLite", "matplotlib", "plotly", "pytest"],
    default=["requests", "Streamlit"],
)

if selected_tools:
    st.write(f"You are working with **{len(selected_tools)}** tools:")
    for tool in selected_tools:
        st.write(f"  ✅ {tool}")
else:
    st.warning("Select at least one tool to see your toolkit summary.")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 5 — text_input
# Returns a string. Empty string ("") if nothing is typed yet.
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("5. Project Idea Generator")
project_keyword = st.text_input(
    label="Enter a keyword for a project idea:",
    placeholder="e.g. weather, fitness, recipes…",
)

if project_keyword:
    # Calculation based on user input — simple string manipulation demo
    keyword_clean = project_keyword.strip().lower()
    ideas = [
        f"A {keyword_clean} tracker that stores data in SQLite",
        f"A FastAPI backend that serves {keyword_clean} data as JSON",
        f"A Streamlit dashboard visualising {keyword_clean} trends",
        f"A CLI tool that fetches {keyword_clean} info from a public API",
    ]
    st.markdown("**Project ideas based on your keyword:**")
    for idea in ideas:
        st.write(f"  💡 {idea}")
else:
    st.write("Type a keyword above to generate project ideas.")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 6 — checkbox
# Returns True (checked) or False (unchecked).
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("6. Progress Summary")
show_summary = st.checkbox("Show my personalised learning summary", value=True)

if show_summary:
    # All widget values are available here in the SAME run
    st.success(
        f"**Summary for a {level_label} learner ({weeks} weeks in):**\n\n"
        f"- Currently studying: **{topic}**\n"
        f"- Learning style: **{style}**\n"
        f"- Tools in use: **{', '.join(selected_tools) if selected_tools else 'none selected'}**\n"
        f"- Project keyword: **{project_keyword if project_keyword else 'not set'}**"
    )
    st.caption("This summary updates instantly as you change any widget above — no Submit button needed!")
