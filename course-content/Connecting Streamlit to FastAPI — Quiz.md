# Connecting Streamlit to FastAPI — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** Where should you store the JWT token in a Streamlit application?

- A) In a regular Python variable at the top of the script
- B) In `st.session_state` so it persists across re-runs
- C) In a browser cookie using JavaScript
- D) In a file on the server

> **Answer: B** — `st.session_state` is the correct place to store tokens in Streamlit. A regular variable (A) would reset to `None` on every re-run, logging the user out on every interaction. Browser cookies (C) require JavaScript and aren’t accessible from Streamlit’s Python code. File storage (D) is insecure and wouldn’t distinguish between different users.
> 

---

**Question 2:** When your API returns a 401 status code, what should your Streamlit frontend do?

- A) Show an error message and crash the app
- B) Retry the request 5 times
- C) Clear the stored token and redirect the user to the login form
- D) Ignore it and show empty data

> **Answer: C** — A 401 means the token is invalid or expired. The right response is to clear `st.session_state["token"]` (setting it to `None`) and call `st.rerun()`. The auth gate pattern will then show the login form automatically. Retrying (B) would just get 401 again. Ignoring it (D) gives a confusing user experience.
>