# Displaying Data: Tables, Charts, Metrics — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Choose between `st.dataframe()` and `st.table()` for displaying tabular data
2. Create line, bar, and area charts with Streamlit’s built-in charting and Plotly
3. Use `st.metric()` with delta values and `delta_color` for KPI dashboards
4. Apply `@st.cache_data` to avoid re-fetching data on every script re-run

---

`[VIDEO PLACEHOLDER: 7 min — "Streamlit Data Display: dataframes with sorting/filtering, built-in charts, Plotly for more control, metrics with deltas, and caching. Show the performance difference with and without @st.cache_data."]`

You’ve learned how to lay out a page and manage state. Now let’s fill it with data. Streamlit was built for data-heavy applications, and it shows — displaying tables, charts, and metrics takes remarkably little code.

![image.png](Displaying%20Data%20Tables,%20Charts,%20Metrics%20%E2%80%94%20Concept/image.png)

Think of this lesson as stocking the shelves of your dashboard. The layout is the store (from Lesson 8). Now you’re putting products on display in the most effective way.

---

## Tables: `st.dataframe()` vs `st.table()`

Streamlit has two ways to display tabular data:

**`st.dataframe()`** renders an interactive table. Users can sort columns, resize them, search, and scroll. It handles large datasets efficiently.

**`st.table()`** renders a static table. No sorting, no interactivity. Good for small, fixed data that doesn’t need interaction.

```python
import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Score": [92, 85, 78]})

st.dataframe(df, use_container_width=True)  # Interactive — sortable, scrollable
st.table(df)                                 # Static — simple display
```

Rule of thumb: use `st.dataframe()` for most cases. Use `st.table()` only when you want a simple, non-interactive display.

---

## Charts: Built-In and Plotly

Streamlit has simple built-in charts for quick visualization:

```python
st.line_chart(df, x="Day", y="Sales")     # Line chart
st.bar_chart(df, x="Category", y="Count")  # Bar chart
st.area_chart(df, x="Month", y="Revenue")  # Area chart
```

These are great for quick, simple visualizations. For more control (custom colors, multiple axes, scatter plots, annotations), use **Plotly**:

```python
import plotly.express as px

fig = px.scatter(df, x="price", y="rating", color="category",
                 title="Price vs Rating")
st.plotly_chart(fig, use_container_width=True)
```

Plotly charts are interactive by default — users can hover for details, zoom, and pan.

---

## Metrics: KPI Dashboard Cards

`st.metric()` displays a label, value, and delta (change indicator):

```python
st.metric("Revenue", "$45,678", "+12%")          # Green delta (positive is good)
st.metric("Bugs", "23", "-5", delta_color="inverse") # Green delta because FEWER bugs is good
st.metric("Users", "1,234", "0")                  # Gray delta (no change)
```

The `delta_color="inverse"` parameter flips the color logic — negative deltas show green and positive show red. Use this for metrics where *decreasing* is good (bugs, costs, response times).

---

## Caching: Don’t Re-Fetch on Every Re-Run

Remember: every widget interaction triggers a re-run. If your script fetches data from an API or database, that fetch happens on every single re-run. For a function that takes 3 seconds, every button click means a 3-second wait.

`@st.cache_data` solves this:

```python
@st.cache_data(ttl=300)  # Cache for 300 seconds (5 minutes)
def fetch_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()

users = fetch_users()  # First call: fetches from API. Subsequent calls: uses cache.
```

The first time `fetch_users()` is called, it runs normally and caches the result. On subsequent re-runs (within the TTL), Streamlit returns the cached result instantly without calling the function again.

`ttl` (time to live) controls how long the cache stays valid. After 300 seconds, the next call fetches fresh data.

---

## Other Useful Display Elements

```python
st.code("print('hello')", language="python")  # Syntax-highlighted code block
st.json({"name": "Alice", "age": 30})          # Formatted JSON display

st.info("Informational message")               # Blue info box
st.success("Operation completed!")             # Green success box
st.warning("Proceed with caution")             # Yellow warning box
st.error("Something went wrong")               # Red error box
```

These status elements are essential for user feedback — confirming actions, showing warnings, and displaying errors clearly.