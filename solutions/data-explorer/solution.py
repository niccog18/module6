"""
L10 — Data Explorer  (Solution)
=================================
Run with:
    streamlit run solution.py

Key concepts:
    • @st.cache_data        — caches the function's return value; re-runs only when inputs change
                              or the ttl (time-to-live) expires
    • ttl=300               — cache expires after 300 seconds (5 minutes)
    • st.dataframe()        — interactive scrollable table (sortable columns)
    • st.table()            — static non-interactive table (use for small, fixed data)
    • st.bar_chart()        — quick bar chart from a dict or DataFrame
    • st.metric(delta_color)— "normal" (green up / red down), "inverse", or "off"
"""

import streamlit as st
import requests

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="User Data Explorer",
    page_icon="🔍",
    layout="wide",
)

# ══════════════════════════════════════════════════════════════════════════════
# @st.cache_data
# ──────────────────────────────────────────────────────────────────────────────
# Streamlit re-runs the entire script on every interaction. Without caching,
# this function would call the API on EVERY click, slider move, or keystroke —
# slow and wasteful.
#
# @st.cache_data stores the return value.
# On subsequent re-runs, Streamlit returns the cached value instantly without
# calling the API again.
#
# ttl=300 means the cache is cleared after 300 seconds, forcing a fresh
# fetch to pick up new data from the API.
#
# st.cache_data vs st.cache_resource:
#   cache_data     → for data (lists, dicts, DataFrames) — creates a copy per caller
#   cache_resource → for shared connections (DB engines, ML models) — single shared object
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data(ttl=300)
def fetch_users() -> list[dict]:
    """Fetch all users from JSONPlaceholder. Cached for 5 minutes."""
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    response.raise_for_status()   # raises an exception for 4xx/5xx responses
    return response.json()


# ── Load data ─────────────────────────────────────────────────────────────────
with st.spinner("Loading users…"):
    users = fetch_users()

# ── Derived data ───────────────────────────────────────────────────────────────
total_users = len(users)

# Count users per city
city_counts: dict[str, int] = {}
for user in users:
    city = user["address"]["city"]
    city_counts[city] = city_counts.get(city, 0) + 1

most_common_city = max(city_counts, key=city_counts.get)

# Average latitude (geo.lat is a string in the API response)
avg_lat = sum(float(user["geo"]["lat"]) for user in users) / total_users

# ── Page title ─────────────────────────────────────────────────────────────────
st.title("🔍 User Data Explorer")
st.caption("Data sourced from JSONPlaceholder · Cached for 5 minutes")

# ── Metrics row ────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="👥 Total Users",
        value=total_users,
        delta=None,              # no delta — just a static count
    )

with col2:
    st.metric(
        label="🏙️ Most Common City",
        value=most_common_city,
        delta=f"{city_counts[most_common_city]} users",
        delta_color="off",       # "off" shows delta in neutral grey (no colour coding)
    )

with col3:
    st.metric(
        label="🌍 Avg. Latitude",
        value=f"{avg_lat:.2f}°",
        # delta_color="inverse" — positive delta shown in RED, negative in GREEN
        # Useful when "higher is worse" (e.g. avg response time)
        delta="N/A",
        delta_color="off",
    )

st.divider()

# ── Sidebar filter ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔎 Filter")
    name_filter = st.text_input(
        "Filter by name:",
        placeholder="Type part of a name…",
    )
    st.caption(f"Showing filtered users from a total of {total_users}")

# Apply filter
if name_filter:
    filtered_users = [u for u in users if name_filter.lower() in u["name"].lower()]
else:
    filtered_users = users

# ── Data table ─────────────────────────────────────────────────────────────────
st.subheader(f"User Table  ({len(filtered_users)} of {total_users})")

# Flatten nested dict into rows for display
table_rows = [
    {
        "Name":     u["name"],
        "Email":    u["email"],
        "City":     u["address"]["city"],
        "Company":  u["company"]["name"],
        "Lat":      u["geo"]["lat"],
        "Lng":      u["geo"]["lng"],
    }
    for u in filtered_users
]

# st.dataframe() — interactive: sortable, scrollable, searchable
# st.table()     — static: renders the whole table, no interaction
# Use dataframe for large or dynamic data; table for small summary data
st.dataframe(
    table_rows,
    use_container_width=True,   # fill the full column width
    hide_index=True,
)

st.divider()

# ── Bar chart: users per city ─────────────────────────────────────────────────
st.subheader("Users per City")
st.bar_chart(city_counts)
st.caption("Each user's city is taken from their address.city field.")
