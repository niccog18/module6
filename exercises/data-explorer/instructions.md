# Data Explorer

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 35 minutes

## Objective

Build a Streamlit app that fetches, caches, and visually explores user data from a public API.

## What You'll Build

A data exploration dashboard that fetches users from JSONPlaceholder and presents them interactively. The app uses `@st.cache_data(ttl=300)` to avoid redundant API calls. It displays three metrics (total users, most common city, average latitude), provides a sidebar text input to filter users by name, shows filtered results in an `st.dataframe()`, and renders a bar chart of users per city.

## Reference Code

The solution file (`solution.py`) is provided as a reference — try building it yourself first, then compare.

## Running

```bash
streamlit run solution.py
```

## Deliverable

A Streamlit app with cached API data, metric cards, a filterable data table, and a bar chart.
