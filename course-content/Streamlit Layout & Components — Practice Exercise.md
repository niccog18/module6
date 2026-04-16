# Streamlit Layout & Components — Practice Exercise

## Personal Stats Dashboard

**Objective:** Build a Streamlit dashboard with a professional layout structure, practicing columns, sidebar, tabs, expanders, and metrics.

**Time:** 35 minutes

**What you’ll build:**

Create `my_dashboard.py` — a personal stats dashboard about any topic: study progress, fitness goals, reading list, project tracker, or anything with numbers you can display.

**Requirements:**

1. **`st.set_page_config()`** with `layout="wide"` and a relevant title/icon
2. **Sidebar** with at least 2 controls (selectbox, slider, radio, checkbox) that affect the main content
3. **Metrics row** — at least 3 `st.metric()` cards in a `st.columns()` row, with delta values
4. **2 tabs** with different content in each (e.g., "Overview" and "Details")
5. **1 expander** with supplementary information
6. Data can be hardcoded — the focus is on layout, not data fetching

**Deliverable:** A running Streamlit app (`my_dashboard.py`) with professional dashboard layout.

**Why this exercise?** This dashboard pattern — sidebar controls, metrics row, tabbed content — is the exact structure you’ll use for the module project. Building it now with simple data means you can focus on the layout without worrying about API calls.