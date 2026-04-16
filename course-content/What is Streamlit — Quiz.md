# What is Streamlit? — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** What happens when a user interacts with any Streamlit widget?

- A) Only the code related to that specific widget runs
- B) A JavaScript event listener fires in the browser
- C) The entire Python script re-runs from top to bottom
- D) Streamlit sends an API request to a separate backend

> **Answer: C** — This is Streamlit’s core execution model. Every widget interaction triggers a complete re-run of the script. There are no partial updates or targeted event handlers. This simplicity is what makes Streamlit so easy to write — but it means you need `st.session_state` to persist data between runs.
> 

---

**Question 2:** What does `st.button("Click me")` return when the button has NOT been clicked on the current run?

- A) `None`
- B) `True`
- C) `False`
- D) It doesn’t return anything

> **Answer: C** — `st.button()` returns `True` only during the re-run triggered by the click. On every other run, it returns `False`. This means code inside `if st.button("Click"):` only executes during that single run — it won’t persist. This is a common source of confusion and is why `st.session_state` exists for persistent actions.
> 

---

**Question 3:** What is the correct command to run a Streamlit app?

- A) `python app.py`
- B) `streamlit run app.py`
- C) `uvicorn app:main --reload`
- D) `flask run --app app.py`

> **Answer: B** — Streamlit has its own CLI command. `streamlit run app.py` starts a local web server and opens the app in your browser at `http://localhost:8501`. Using `python app.py` (A) would run the script but wouldn’t start the Streamlit server. The other commands (C, D) are for FastAPI and Flask respectively.
>