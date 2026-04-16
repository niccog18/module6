# What is Streamlit? — Practice Exercise

## Topic Exploration App

**Objective:** Build a Streamlit app that demonstrates at least 5 different widget types, with content that changes based on widget values and at least one calculation.

**Time:** 30 minutes

**What you’ll build:**

Create a file called `explore.py` — a Streamlit app about a topic you know well (cooking, fitness, music, travel, gaming, a hobby — anything). The topic is your choice, which makes this more fun and gives you creative freedom.

**Requirements:**

1. Use **at least 5 different widget types** from this list:
    - `st.text_input()`, `st.number_input()`, `st.slider()`, `st.selectbox()`, `st.multiselect()`, `st.radio()`, `st.checkbox()`, `st.text_area()`, `st.date_input()`
2. **Content that changes** based on widget values (use `if/elif` or conditional logic)
3. **At least one calculation** that uses widget values (e.g., a cost calculator, a rating average, a progress tracker)
4. Use at least two of these display elements: `st.write()`, `st.info()`, `st.success()`, `st.warning()`, `st.metric()`, `st.code()`, `st.progress()`
5. A `st.title()` and at least one `st.header()` or `st.subheader()`

**Example ideas:**

- **Recipe calculator:** Select ingredients with multiselect, set servings with a slider, calculate total calories
- **Workout planner:** Radio buttons for workout type, slider for duration, checkbox for warm-up, calculate estimated calories burned
- **Trip planner:** Selectbox for destination, date_input for travel dates, number_input for budget, calculate daily budget

**Deliverable:** A running Streamlit app (`explore.py`) that demonstrates at least 5 widget types with interactive content.

**Why this exercise?** You’re cementing the core Streamlit pattern: widgets return values, values drive logic, logic determines what’s displayed. This is the same pattern behind every AI dashboard and tool you’ll build.