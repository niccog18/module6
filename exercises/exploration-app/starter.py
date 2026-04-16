"""
L7 — Streamlit Exploration App  (STARTER)
===========================================
Run with:
    streamlit run starter.py

Your goal: build an interactive app called "Python Learning Journey" that
uses 5+ widget types and shows content that changes based on widget values.

KEY CONCEPT — The re-run model:
    Every time a user interacts with a widget, Streamlit re-executes the
    ENTIRE script from top to bottom. This means:
      • Widget functions (st.slider, st.selectbox, etc.) both RENDER the
        widget AND RETURN the current value in the same call.
      • Just use the returned value immediately — no event handlers needed.
      • Write code like a normal top-to-bottom Python script.

Widgets to use (at least 5):
    st.slider()       — returns a number (int or float)
    st.selectbox()    — returns one item from a list
    st.radio()        — returns one item from a list (shown as radio buttons)
    st.multiselect()  — returns a list of selected items
    st.text_input()   — returns a string
    st.checkbox()     — returns True or False
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
# Widget 1 — st.slider
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("1. Experience Level")
# TODO: Create a slider asking "How many weeks have you been coding?"
#       min_value=0, max_value=52, value=8, step=1
#       Store the result in `weeks`

# TODO: Use weeks to determine a level label (Beginner / Intermediate / Advanced)

# TODO: Display the level using st.metric()
# Hint: st.metric(label="...", value=level_label, delta=f"{weeks} weeks")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 2 — st.selectbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("2. Current Topic")
# TODO: Create a selectbox with at least 5 Python topics as options
#       Store the result in `topic`

# TODO: Show a topic-specific tip using st.info()
# Hint: use a dict to map topic → tip, then look up tips[topic]

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 3 — st.radio
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("3. Learning Style")
# TODO: Create radio buttons asking how the student learns best
#       Options: ["Reading docs", "Watching videos", "Building projects", "Pair programming"]
#       Use horizontal=True to display them in a row
#       Store the result in `style`

# TODO: Show a resource recommendation based on the selected style

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 4 — st.multiselect
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("4. Tools & Libraries You Use")
# TODO: Create a multiselect with tools: pandas, requests, FastAPI, Streamlit, SQLite, etc.
#       Set default=["requests", "Streamlit"]
#       Store the result in `selected_tools`

# TODO: If tools are selected, list them with checkmarks
# TODO: If no tools selected, show st.warning()

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 5 — st.text_input
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("5. Project Idea Generator")
# TODO: Create a text_input asking for a keyword (e.g. "weather", "fitness")
#       Store the result in `project_keyword`

# TODO: If a keyword is entered, generate 3-4 project ideas using that keyword
#       Hint: use an f-string like f"A {keyword} tracker that stores data in SQLite"

# TODO: If empty, show a prompt to enter a keyword

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# Widget 6 — st.checkbox
# ═══════════════════════════════════════════════════════════════════════════
st.subheader("6. Progress Summary")
# TODO: Create a checkbox labelled "Show my personalised learning summary"
#       Set value=True so it starts checked
#       Store the result in `show_summary`

# TODO: If show_summary is True, display a summary using all the widget values
#       collected above (weeks, topic, style, selected_tools, project_keyword)
# Hint: use st.success() with a multi-line f-string
