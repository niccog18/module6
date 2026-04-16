# User Input, Forms & State Management — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** Why does the following code never count past 1?

```python
count = 0
if st.button("Add"):
    count += 1
st.write(f"Count: {count}")
```

- A) `st.button()` only works once per session
- B) The script re-runs from top to bottom on each click, resetting `count = 0` before the button logic executes
- C) `count += 1` doesn’t work in Python
- D) You need to use `st.number_input()` instead

> **Answer: B** — Every time the button is clicked, the entire script re-runs. Line 1 (`count = 0`) executes first, resetting the counter. Then the button check increments it to 1. On the next click, it resets to 0 and increments to 1 again. The fix is to use `st.session_state` to store the count in a persistent dictionary that survives re-runs.
> 

---

**Question 2:** What is the benefit of wrapping inputs in `st.form()`?

- A) It makes the inputs look better
- B) It batches all input changes so the script only re-runs once when the form is submitted, instead of re-running on every individual widget change
- C) It automatically validates the input data
- D) It saves the inputs to a database

> **Answer: B** — Without `st.form()`, each widget interaction triggers a full script re-run. With 5 inputs, that’s 5+ re-runs while the user is still filling out the form. `st.form()` prevents re-runs until the submit button is clicked, making it ideal for forms that trigger expensive operations like API calls or database inserts.
> 

---

**Question 3:** Which is the correct way to initialize a session state variable?

- A) `st.session_state["key"] = 0` (on every run)
- B) `if "key" not in st.session_state: st.session_state["key"] = 0`
- C) `st.initialize("key", 0)`
- D) `session_state = {"key": 0}`

> **Answer: B** — The `if "key" not in st.session_state` check ensures the initial value is set only once (on the first run). On subsequent re-runs, the key already exists, so the initialization is skipped and the current value is preserved. Option A would reset the value to 0 on every run, defeating the purpose. Option C doesn’t exist. Option D creates a local variable, not Streamlit’s session state.
>