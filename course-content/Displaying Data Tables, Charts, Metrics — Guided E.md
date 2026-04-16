# Displaying Data: Tables, Charts, Metrics — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Build data_display.py: sidebar filters, 4-column metrics row with deltas, tabs for chart view / Plotly scatter / raw data, chart type radio button, styled dataframe."]`

Create `data_display.py` — a data explorer that demonstrates every display technique:

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(page_title="Data Display Demo", page_icon="📊", layout="wide")

# --- Generate sample data ---
@st.cache_data  # Cache so it doesn't regenerate on every re-run
def load_data():
    categories = ["Electronics", "Clothing", "Food", "Books", "Home"]
    data = []
    for i in range(50):
        data.append({
            "Product": f"Product {i+1}",
            "Category": random.choice(categories),
            "Price": round(random.uniform(5, 200), 2),
            "Rating": round(random.uniform(1, 5), 1),
            "Sales": random.randint(10, 500)
        })
    return pd.DataFrame(data)

df = load_data()

# --- Sidebar Filters ---
with st.sidebar:
    st.title("🔍 Filters")
    selected_categories = st.multiselect(
        "Categories", df["Category"].unique().tolist(),
        default=df["Category"].unique().tolist()  # All selected by default
    )
    price_range = st.slider(
        "Price Range", float(df["Price"].min()), float(df["Price"].max()),
        (float(df["Price"].min()), float(df["Price"].max()))  # Default: full range
    )

# Apply filters
filtered = df[
    (df["Category"].isin(selected_categories)) &
    (df["Price"].between(price_range[0], price_range[1]))
]

# --- Title and Metrics ---
st.title("📊 Product Data Explorer")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Products", len(filtered),
              f"{len(filtered) - len(df)}" if len(filtered) != len(df) else "All")
with col2:
    st.metric("Avg Price", f"${filtered['Price'].mean():.2f}")
with col3:
    st.metric("Avg Rating", f"{filtered['Rating'].mean():.1f} ⭐")
with col4:
    st.metric("Total Sales", f"{filtered['Sales'].sum():,}")

st.divider()

# --- Tabbed Content ---
tab_charts, tab_scatter, tab_raw = st.tabs(
    ["📊 Charts", "🔵 Product Scatter", "🗑️ Raw Data"]
)

with tab_charts:
    chart_type = st.radio(
        "Chart type", ["Bar", "Line", "Area"], horizontal=True
    )

    # Group data for charting
    chart_data = filtered.groupby("Category")["Sales"].sum().reset_index()

    if chart_type == "Bar":
        st.bar_chart(chart_data, x="Category", y="Sales")
    elif chart_type == "Line":
        st.line_chart(chart_data, x="Category", y="Sales")
    else:
        st.area_chart(chart_data, x="Category", y="Sales")

with tab_scatter:
    fig = px.scatter(
        filtered, x="Price", y="Rating", color="Category",
        size="Sales", hover_name="Product",
        title="Price vs Rating by Category"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab_raw:
    st.subheader(f"Filtered Data ({len(filtered)} products)")
    st.dataframe(
        filtered.style.highlight_max(subset=["Sales", "Rating"], color="#d4edda"),
        use_container_width=True
    )
```

Run it:

```bash
pip install plotly  # If not already installed
streamlit run data_display.py
```

---

## What You Should See

A full dashboard with sidebar filters (multiselect for categories, slider for price range), a 4-metric row updating with filter changes, and three tabs: Charts (with a radio button to switch chart types), Product Scatter (interactive Plotly scatter plot), and Raw Data (sortable dataframe with highlighted max values).

`[DIAGRAM PLACEHOLDER: Screenshot of the completed data_display.py showing the metrics row, Plotly scatter chart, and filtered dataframe]`