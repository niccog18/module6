import streamlit as st
import requests
import pandas as pd


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="User Data Explorer",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Fetch user data
# --------------------------------------------------

@st.cache_data
def fetch_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# Get users
# --------------------------------------------------

users = fetch_users()


# --------------------------------------------------
# Convert API data into a DataFrame
# --------------------------------------------------

rows = []

for user in users:

    rows.append({
        "Name": user["name"],
        "Username": user["username"],
        "Email": user["email"],
        "City": user["address"]["city"],
        "Company": user["company"]["name"]
    })


df = pd.DataFrame(rows)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 JSONPlaceholder User Explorer")

st.write(
    "Explore user information retrieved from the "
    "JSONPlaceholder API."
)


# --------------------------------------------------
# Sidebar filter
# --------------------------------------------------

st.sidebar.header("🔎 Filters")

name_filter = st.sidebar.text_input(
    "Filter by name:",
    placeholder="Enter a name..."
)


# --------------------------------------------------
# Filter dataframe
# --------------------------------------------------

if name_filter:

    filtered_df = df[
        df["Name"].str.contains(
            name_filter,
            case=False,
            na=False
        )
    ]

else:

    filtered_df = df


# --------------------------------------------------
# Metrics
# --------------------------------------------------

st.subheader("User Statistics")

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Users",
        len(users)
    )


with col2:

    st.metric(
        "Unique Cities",
        df["City"].nunique()
    )


with col3:

    st.metric(
        "Unique Companies",
        df["Company"].nunique()
    )


# --------------------------------------------------
# User table
# --------------------------------------------------

st.subheader("Users")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True
)


# --------------------------------------------------
# Users per city
# --------------------------------------------------

st.subheader("Users by City")

city_counts = (
    df["City"]
    .value_counts()
    .reset_index()
)

city_counts.columns = ["City", "Users"]


st.bar_chart(
    city_counts.set_index("City")
)

