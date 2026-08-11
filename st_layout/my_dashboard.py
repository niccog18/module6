import streamlit as st


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Watch Collection Dashboard",
    page_icon="⌚",
    layout="wide"
)


# --------------------------------------------------
# Hardcoded watch data
# --------------------------------------------------

watches = {
    "Rolex": {
        "count": 3,
        "value": 27000,
        "favorite": "Submariner"
    },
    "Omega": {
        "count": 4,
        "value": 24000,
        "favorite": "Speedmaster"
    },
    "Seiko": {
        "count": 6,
        "value": 4500,
        "favorite": "Prospex"
    },
    "Tudor": {
        "count": 2,
        "value": 8000,
        "favorite": "Black Bay"
    }
}


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("⌚ Dashboard Controls")

brand = st.sidebar.selectbox(
    "Choose a brand:",
    ["All Brands"] + list(watches.keys())
)

minimum_watches = st.sidebar.slider(
    "Minimum number of watches:",
    min_value=1,
    max_value=10,
    value=1
)

show_values = st.sidebar.checkbox(
    "Show collection values",
    value=True
)


# --------------------------------------------------
# Calculate dashboard values
# --------------------------------------------------

if brand == "All Brands":
    selected_watches = watches
else:
    selected_watches = {
        brand: watches[brand]
    }


# Filter based on minimum watch count
filtered_watches = {
    name: data
    for name, data in selected_watches.items()
    if data["count"] >= minimum_watches
}


total_watches = sum(
    data["count"]
    for data in filtered_watches.values()
)

total_value = sum(
    data["value"]
    for data in filtered_watches.values()
)

number_of_brands = len(filtered_watches)

average_value = (
    total_value / total_watches
    if total_watches > 0
    else 0
)


# --------------------------------------------------
# Main dashboard
# --------------------------------------------------

st.title("⌚ Personal Watch Collection Dashboard")

st.write(
    "A quick overview of my watch collection, favorite brands, "
    "and collection statistics."
)


# --------------------------------------------------
# Metrics row
# --------------------------------------------------

st.subheader("Collection Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Watches",
        total_watches,
        delta="+2 this year"
    )

with col2:
    if show_values:
        st.metric(
            "Collection Value",
            f"${total_value:,.0f}",
            delta="+8.5%"
        )
    else:
        st.metric(
            "Collection Value",
            "Hidden",
            delta="Private"
        )

with col3:
    st.metric(
        "Brands",
        number_of_brands,
        delta="+1"
    )

with col4:
    if show_values:
        st.metric(
            "Average Value",
            f"${average_value:,.0f}",
            delta="+5%"
        )
    else:
        st.metric(
            "Average Value",
            "Hidden",
            delta="Private"
        )


# --------------------------------------------------
# Tabs
# --------------------------------------------------

tab1, tab2 = st.tabs(
    ["📊 Overview", "⌚ Watch Details"]
)


# --------------------------------------------------
# Overview tab
# --------------------------------------------------

with tab1:

    st.header("Collection Overview")

    if filtered_watches:

        for name, data in filtered_watches.items():

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(f"### {name}")

            with col2:
                st.write(f"**Watches:** {data['count']}")

            with col3:
                if show_values:
                    st.write(
                        f"**Value:** ${data['value']:,.0f}"
                    )
                else:
                    st.write("**Value:** Hidden")

    else:

        st.warning(
            "No brands match your current filters."
        )


# --------------------------------------------------
# Details tab
# --------------------------------------------------

with tab2:

    st.header("Collection Details")

    if filtered_watches:

        for name, data in filtered_watches.items():

            st.write(f"### {name}")

            st.write(
                f"Number of watches: **{data['count']}**"
            )

            st.write(
                f"Favorite watch: **{data['favorite']}**"
            )

            if show_values:
                st.write(
                    f"Estimated collection value: "
                    f"**${data['value']:,.0f}**"
                )

            st.divider()

    else:

        st.info(
            "Try lowering the minimum watch count in the sidebar."
        )


# --------------------------------------------------
# Expander
# --------------------------------------------------

with st.expander("ℹ️ About this dashboard"):

    st.write(
        """
        This dashboard uses hardcoded data to demonstrate
        Streamlit's layout features.

        The sidebar controls change which brands appear in
        the dashboard and whether collection values are shown.

        The metrics, tabs, columns, and expander demonstrate
        common patterns used in larger Streamlit applications.
        """
    )