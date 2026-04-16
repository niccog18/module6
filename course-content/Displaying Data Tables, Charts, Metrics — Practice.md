# Displaying Data: Tables, Charts, Metrics — Practice Exercise

## Data Explorer

**Objective:** Build a Streamlit app that fetches data from an API, displays it with metrics and charts, and uses caching to avoid re-fetching.

**Time:** 35 minutes

**What you’ll build:**

Create `data_explorer.py` that fetches user data from JSONPlaceholder and displays it interactively.

**Requirements:**

1. **Fetch users** from `https://jsonplaceholder.typicode.com/users` using `requests.get()`
2. **Cache the fetch** with `@st.cache_data` so it doesn’t re-fetch on every re-run
3. **3 metrics** in a `st.columns()` row: total users, unique cities, unique companies
4. **Interactive dataframe** (`st.dataframe()`) displaying users — with a sidebar name filter (text input that filters the displayed users)
5. **Bar chart** showing the number of users per city

**Data extraction hints:**

- User name: `user["name"]`
- User city: `user["address"]["city"]`
- User company: `user["company"]["name"]`
- Convert to a DataFrame for easy display: `pd.DataFrame(rows)`

**Deliverable:** A running Streamlit app that displays JSONPlaceholder user data with metrics, a filterable table, and a chart.

**Why this exercise?** This is a miniature version of what your module project will look like: fetch data, display metrics, show a table, create a chart. The only difference is the data source.