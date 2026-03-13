"""
L8 — Personal Stats Dashboard  (Solution)
===========================================
Run with:
    streamlit run solution.py

Layout concepts demonstrated:
    • st.set_page_config(layout="wide")  — expands the app to fill the browser window
    • st.sidebar.*                       — widgets in the left sidebar act as controls
    • st.columns([...])                  — horizontal layout; pass weights for widths
    • st.metric()                        — big number display with optional delta
    • st.tabs()                          — tabbed content areas
    • st.expander()                      — collapsible section

When to use tabs vs expanders:
    Tabs      → mutually exclusive sections (user sees one at a time)
                Good for: Overview vs Details, different data views
    Expanders → optional detail that most users won't need
                Good for: methodology notes, raw data dumps, advanced settings
"""

import streamlit as st
import random

# ── Page config ───────────────────────────────────────────────────────────────
# layout="wide" makes the content span the full browser width.
# This is the first call that must happen in a Streamlit script.
st.set_page_config(
    page_title="Personal Stats Dashboard",
    page_icon="📊",
    layout="wide",
)

# ── Hardcoded data ────────────────────────────────────────────────────────────
# Real apps would load from a DB or API; we hardcode for the demo.
WEEKLY_STUDY = {
    "Mon": 1.5, "Tue": 2.0, "Wed": 0.5, "Thu": 2.5,
    "Fri": 1.0, "Sat": 3.0, "Sun": 0.0,
}
MODULES_DATA = {
    "Module 1: AI Fundamentals":       {"score": 88, "exercises": 6,  "status": "Complete"},
    "Module 2: Advanced Python":       {"score": 92, "exercises": 8,  "status": "Complete"},
    "Module 3: Databases & SQL":       {"score": 79, "exercises": 7,  "status": "Complete"},
    "Module 4: REST API Fundamentals": {"score": 85, "exercises": 6,  "status": "Complete"},
    "Module 5: FastAPI":               {"score": 90, "exercises": 7,  "status": "Complete"},
    "Module 6: Web & Streamlit":       {"score": 0,  "exercises": 12, "status": "In Progress"},
}
SKILLS = ["Python", "SQL", "HTML/CSS", "APIs", "Data Analysis", "FastAPI", "Streamlit"]
SKILL_SCORES = [90, 75, 65, 80, 70, 85, 60]

# ── Sidebar controls ──────────────────────────────────────────────────────────
# The sidebar is a great place for controls that affect the whole dashboard.
# It stays visible while the user scrolls through main content.
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    st.divider()

    # Sidebar widget 1 — selectbox
    selected_module = st.selectbox(
        "Focus Module",
        options=list(MODULES_DATA.keys()),
        index=0,
    )

    # Sidebar widget 2 — radio
    chart_type = st.radio(
        "Study Hours Chart Style",
        options=["Bar", "Line", "Area"],
    )

    st.divider()
    st.caption("Data is hardcoded for this demo.")

# ── Page title (main area) ────────────────────────────────────────────────────
st.title("📊 Personal Stats Dashboard")
st.caption(f"Focused on: {selected_module}")

# ── Metrics row — 3 columns ───────────────────────────────────────────────────
# st.columns([1, 1, 1]) creates three equal-width columns.
# Use fractional weights like [2, 1, 1] for different widths.
col1, col2, col3 = st.columns(3)

total_study_hours = sum(WEEKLY_STUDY.values())
completed_modules = sum(1 for m in MODULES_DATA.values() if m["status"] == "Complete")
avg_score         = sum(m["score"] for m in MODULES_DATA.values() if m["score"] > 0) / completed_modules

with col1:
    # st.metric(label, value, delta)
    # delta > 0  → green arrow up
    # delta < 0  → red arrow down
    # delta_color="inverse" flips the colour logic
    st.metric(
        label="📚 Study Hours This Week",
        value=f"{total_study_hours:.1f} hrs",
        delta="+1.5 hrs vs last week",
    )

with col2:
    st.metric(
        label="✅ Modules Completed",
        value=f"{completed_modules} / {len(MODULES_DATA)}",
        delta="+1 this week",
    )

with col3:
    st.metric(
        label="⭐ Average Score",
        value=f"{avg_score:.0f}%",
        delta="+3% vs last month",
    )

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
# st.tabs() returns a list of tab context managers.
# Use `with tab:` to add content to each tab.
# Users see only the active tab at a time.
tab_overview, tab_details = st.tabs(["📈 Overview", "📋 Details"])

with tab_overview:
    st.subheader("Study Hours by Day")

    # Show different chart types based on sidebar selection
    if chart_type == "Bar":
        st.bar_chart(WEEKLY_STUDY)
    elif chart_type == "Line":
        st.line_chart(WEEKLY_STUDY)
    else:  # Area
        st.area_chart(WEEKLY_STUDY)

    st.subheader("Skill Scores")
    # Build a simple dict for the chart
    skill_chart_data = dict(zip(SKILLS, SKILL_SCORES))
    st.bar_chart(skill_chart_data)

with tab_details:
    st.subheader("Module Progress")

    # Show module table
    for module_name, data in MODULES_DATA.items():
        icon = "✅" if data["status"] == "Complete" else "🔄"
        col_a, col_b, col_c, col_d = st.columns([3, 1, 1, 1])
        col_a.write(f"{icon} {module_name}")
        col_b.write(f"Score: {data['score']}%" if data["score"] else "In Progress")
        col_c.write(f"{data['exercises']} exercises")
        col_d.write(data["status"])

    st.divider()

    # ── Expander — collapsible section ───────────────────────────────────
    # Use expanders for content that's useful but not primary.
    # expanded=False means it starts collapsed.
    with st.expander("📊 Raw Data & Methodology", expanded=False):
        st.subheader("Weekly Study Data")
        st.json(WEEKLY_STUDY)

        st.subheader("How Scores Are Calculated")
        st.markdown("""
        - **Exercise score**: average of all submitted exercises
        - **Module score**: weighted average (exercises 60%, project 40%)
        - **Overall average**: mean of all completed module scores
        - Scores are self-reported for this demo
        """)

# ── Selected module detail ────────────────────────────────────────────────────
st.divider()
st.subheader(f"Deep Dive: {selected_module}")

module_info = MODULES_DATA[selected_module]
d_col1, d_col2, d_col3 = st.columns(3)
d_col1.metric("Score", f"{module_info['score']}%" if module_info["score"] else "N/A")
d_col2.metric("Exercises", module_info["exercises"])
d_col3.metric("Status", module_info["status"])

if module_info["status"] == "In Progress":
    st.info("This module is currently in progress. Keep going! 🎯")
else:
    st.success(f"Module completed with a score of {module_info['score']}%!")
