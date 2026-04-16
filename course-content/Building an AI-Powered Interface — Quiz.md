# Building an AI-Powered Interface — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What does the walrus operator (`:=`) do in this line?

```python
if prompt := st.chat_input("Ask me anything..."):
```

- A) It compares `prompt` to `st.chat_input()`
- B) It assigns the return value of `st.chat_input()` to `prompt` AND checks if it’s truthy, all in one expression
- C) It creates a constant that cannot be changed
- D) It’s a Streamlit-specific operator

> **Answer: B** — The walrus operator (`:=`) combines assignment and evaluation. It assigns the value to `prompt` and then the `if` checks whether that value is truthy (not `None`, not empty string). Without it, you’d need two lines: `prompt = st.chat_input(...)` followed by `if prompt:`. It’s standard Python 3.8+, not Streamlit-specific.
> 

---

**Question 2:** Why must you re-render the entire chat history on every script run?

- A) Streamlit has a bug that clears the display
- B) Because Streamlit re-runs the entire script, the display is rebuilt from scratch each time — previous messages disappear unless explicitly re-displayed
- C) Chat messages expire after 10 seconds
- D) The browser cache clears on every interaction

> **Answer: B** — Streamlit’s re-run model means every `st.write()` and `st.chat_message()` call from the previous run is gone. The messages are safely stored in `st.session_state["messages"]`, but they must be actively re-displayed by looping through the history list. This `for message in history: display(message)` pattern is fundamental to all stateful Streamlit apps.
> 

---

**Question 3:** What does `st.write_stream()` accept as input?

- A) A string
- B) A generator (an object that yields text chunks one at a time)
- C) A URL to an API endpoint
- D) A pandas DataFrame

> **Answer: B** — `st.write_stream()` takes a generator — any function that uses `yield` to produce text chunks sequentially. It displays each chunk as it arrives, creating the typing effect. Both mock generators (using `yield` with `time.sleep()`) and real API streams work. The function returns the complete concatenated text when the generator is exhausted.
>