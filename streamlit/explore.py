import streamlit as st
from datetime import date


# Title
st.title("⌚ Watch Collection Explorer")

st.write("Explore different watches, complications, and estimate your collection value.")

# Header
st.header("Build Your Watch Profile")


# Widget 1: Text input
owner = st.text_input("Enter your name:")

# Widget 2: Selectbox
watch_type = st.selectbox(
    "Choose your favorite watch style:",
    ["Dress Watch", "Dive Watch", "Chronograph", "Field Watch", "Smart Watch"]
)

# Widget 3: Multiselect
complications = st.multiselect(
    "Select watch complications you enjoy:",
    [
        "Date Display",
        "Moon Phase",
        "Chronograph",
        "Tourbillon",
        "Power Reserve",
        "GMT"
    ]
)

# Widget 4: Slider
collection_size = st.slider(
    "How many watches are in your collection?",
    min_value=1,
    max_value=50,
    value=5
)

# Widget 5: Number input
average_price = st.number_input(
    "Average price per watch ($):",
    min_value=100,
    max_value=100000,
    value=2000
)

# Widget 6: Radio
experience = st.radio(
    "How experienced are you with watches?",
    ["Beginner", "Intermediate", "Expert"]
)

# Widget 7: Checkbox
include_insurance = st.checkbox(
    "Include estimated insurance cost"
)

# Widget 8: Date input
purchase_date = st.date_input(
    "Date you started collecting watches:",
    date.today()
)

# Widget 9: Text area
notes = st.text_area(
    "Describe your dream watch:"
)


# Calculation section
st.header("Collection Analysis")

# Calculate collection value
collection_value = collection_size * average_price

if include_insurance:
    insurance_cost = collection_value * 0.02
    total_value = collection_value + insurance_cost
else:
    insurance_cost = 0
    total_value = collection_value


# Display metrics
st.metric(
    "Estimated Collection Value",
    f"${collection_value:,.2f}"
)

if include_insurance:
    st.warning(
        f"Estimated yearly insurance cost: ${insurance_cost:,.2f}"
    )


# Conditional content
st.subheader("Personalized Watch Recommendation")

if watch_type == "Dive Watch":
    st.info(
        "You might enjoy watches with high water resistance, rotating bezels, and strong lume."
    )

elif watch_type == "Chronograph":
    st.info(
        "Chronographs are great if you enjoy mechanical complexity and timing functions."
    )

elif watch_type == "Dress Watch":
    st.info(
        "Consider watches with elegant designs, thin cases, and classic complications."
    )

elif watch_type == "Smart Watch":
    st.info(
        "Smart watches are ideal if you prefer fitness tracking and digital features."
    )

else:
    st.info(
        "Field watches are practical, durable, and inspired by military designs."
    )


# Experience-based logic
if experience == "Beginner":
    st.success(
        "Recommended starting point: learn about basic movements like automatic and quartz."
    )

elif experience == "Intermediate":
    st.success(
        "You may enjoy exploring complications like GMTs and chronographs."
    )

else:
    st.success(
        "You might appreciate advanced complications like perpetual calendars and tourbillons."
    )


# Progress tracker
progress = min(collection_size / 50, 1.0)

st.subheader("Collection Progress")
st.progress(progress)


# Show selected complications
if complications:
    st.write("Your favorite complications:")
    st.code(", ".join(complications))
else:
    st.write("You haven't selected any complications yet.")


# User notes
if notes:
    st.write("Your dream watch:")
    st.write(notes)


st.write(
    f"{owner if owner else 'Collector'}, you started your collection on {purchase_date}."
)