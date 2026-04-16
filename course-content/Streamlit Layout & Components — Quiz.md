# Streamlit Layout & Components — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What is the recommended approach for creating a row of 3-4 metrics across the top of a Streamlit dashboard?

- A) Use `st.metric()` three times in a row — they automatically arrange horizontally
- B) Use `st.columns(3)` or `st.columns(4)` and place one `st.metric()` inside each column
- C) Use `st.tabs()` with one metric per tab
- D) Use HTML and CSS within `st.markdown()`

> **Answer: B** — Streamlit renders content top-to-bottom by default. To place metrics side-by-side, you need `st.columns()` to create horizontal containers, then use `with col:` to place one metric in each. If you just call `st.metric()` three times (A), they’d stack vertically.
> 

---

**Question 2:** What is the sidebar best used for in a Streamlit dashboard?

- A) Displaying the main data tables and charts
- B) Filters, controls, settings, and navigation that affect the main content
- C) Error messages and warnings
- D) Chat interfaces

> **Answer: B** — The sidebar is the standard location for controls that modify what’s shown in the main content area. This follows the same UI pattern used by virtually every analytics dashboard: controls on the side, results in the center. Main data display (A) should be in the main area where there’s more space.
> 

---

**Question 3:** When should you use `st.tabs()` versus `st.expander()`?

- A) Tabs and expanders are identical — use whichever you prefer
- B) Tabs are for switching between different full-page views; expanders are for hiding optional content within a view
- C) Expanders should only be used in the sidebar
- D) Tabs are only for charts; expanders are only for text

> **Answer: B** — Tabs organize content into mutually exclusive views (show Overview OR Details OR Raw Data). Expanders toggle visibility of supplementary content within a view (click to expand additional details). Use tabs for top-level navigation between sections; use expanders for optional drill-down information within a section.
>