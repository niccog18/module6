# Displaying Data: Tables, Charts, Metrics — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What is the key difference between `st.dataframe()` and `st.table()`?

- A) `st.dataframe()` only works with pandas DataFrames; `st.table()` works with any data
- B) `st.dataframe()` is interactive (sortable, scrollable, searchable); `st.table()` is static
- C) `st.table()` is faster for large datasets
- D) There is no difference

> **Answer: B** — `st.dataframe()` renders an interactive table where users can sort columns, resize them, and scroll through data. `st.table()` renders a simple, static table with no interactivity. Both accept pandas DataFrames, lists of dictionaries, and other data formats. For most use cases, `st.dataframe()` is the better choice.
> 

---

**Question 2:** What does `@st.cache_data` do?

- A) It saves data to a file permanently
- B) It caches the return value of a function so it doesn’t re-execute on every Streamlit re-run, until the cache expires
- C) It compresses the data for faster display
- D) It makes the function run asynchronously

> **Answer: B** — `@st.cache_data` is a decorator that stores the function’s return value. On subsequent re-runs, if the function is called with the same arguments, Streamlit returns the cached result instead of re-executing the function. The `ttl` parameter controls how long the cache stays valid. This is critical for functions that fetch data from APIs or databases — without caching, every widget click would re-fetch the data.
> 

---

**Question 3:** When should you use `delta_color="inverse"` in `st.metric()`?

- A) When you want the delta text to be invisible
- B) When a negative change is good (e.g., fewer bugs, lower costs, faster response times)
- C) When the metric value is negative
- D) When you want red to always be used

> **Answer: B** — By default, `st.metric()` shows positive deltas in green and negative in red. But for metrics like "Bug Count" or "Response Time," a *decrease* is good. `delta_color="inverse"` flips the colors so negative deltas show green and positive show red, matching the actual meaning.
>