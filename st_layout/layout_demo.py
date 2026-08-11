import streamlit as st
import random

# --- Page Config (MUST be first Streamlit command) ---
st.set_page_config(
    page_title="Dashboard Demo",
    page_icon="📊",
    layout="wide"  # Use full browser width
)

# --- Sidebar: Controls ---
with st.sidebar:
    st.title("⚙️ Controls")

    time_period = st.selectbox(
        "Time Period",
        ["Today", "This Week", "This Month", "This Year"]
    )

    department = st.radio(
        "Department",
        ["All", "Engineering", "Marketing", "Sales"]
    )

    show_details = st.checkbox("Show detailed view", value=True)

    st.divider()
    st.caption(f"Viewing: {department} | {time_period}")

# --- Main Content ---
st.title("📊 Team Dashboard")
st.write(f"Showing data for **{department}** department — **{time_period}**")

# --- Metrics Row (4 columns) ---
col1, col2, col3, col4 = st.columns(4)

# Simulate different data based on sidebar selections
multiplier = {"Today": 1, "This Week": 7, "This Month": 30, "This Year": 365}
base = multiplier.get(time_period, 1)

with col1:
    st.metric("Total Tasks", f"{42 * base:,}", f"+{base}")
with col2:
    st.metric("Completed", f"{35 * base:,}", f"+{base - 1}")
with col3:
    st.metric("In Progress", f"{5 * base:,}", f"-{max(1, base//10)}")
with col4:
    completion = round(35 / 42 * 100, 1)
    st.metric("Completion Rate", f"{completion}%", "+2.3%")

st.divider()

# --- Tabbed Content ---
tab_overview, tab_details, tab_raw = st.tabs(
    ["📈 Overview", "🔍 Details", "🗑️ Raw Data"]
)

with tab_overview:
    st.subheader("Task Completion Trend")
    # Generate sample chart data
    chart_data = {"Day": list(range(1, 8)), "Tasks": [random.randint(3, 12) for _ in range(7)]}
    st.bar_chart(chart_data, x="Day", y="Tasks")

    with st.expander("💡 How to read this chart"):
        st.write("Each bar represents the number of tasks completed on that day. "
                 "Higher bars indicate more productive days. Look for patterns — "
                 "are certain days consistently more productive?")

with tab_details:
    if show_details:  # Controlled by sidebar checkbox
        st.subheader("Team Members")

        # Display team members in a 2-column layout
        left, right = st.columns(2)

        with left:
            st.write("**Engineering**")
            st.write("- Alice: 12 tasks completed")
            st.write("- Bob: 8 tasks completed")
            st.write("- Charlie: 15 tasks completed")

        with right:
            st.write("**Marketing**")
            st.write("- Diana: 10 tasks completed")
            st.write("- Eve: 7 tasks completed")
    else:
        st.info("Enable 'Show detailed view' in the sidebar to see team details.")

with tab_raw:
    st.subheader("Raw Task Data")
    # Sample data as a list of dictionaries
    sample_data = [
        {"Task": "Build API", "Assignee": "Alice", "Status": "Done", "Priority": "High"},
        {"Task": "Write tests", "Assignee": "Bob", "Status": "In Progress", "Priority": "Medium"},
        {"Task": "Update docs", "Assignee": "Charlie", "Status": "Done", "Priority": "Low"},
        {"Task": "Deploy v2", "Assignee": "Alice", "Status": "Pending", "Priority": "High"},
        {"Task": "Design mockups", "Assignee": "Diana", "Status": "Done", "Priority": "Medium"},
    ]
    st.dataframe(sample_data, use_container_width=True)  # Interactive table