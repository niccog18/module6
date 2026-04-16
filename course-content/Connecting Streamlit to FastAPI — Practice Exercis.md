# Connecting Streamlit to FastAPI — Practice Exercise

## Connect to Your Module 5 Task Manager

**Objective:** Build a Streamlit frontend that connects to the FastAPI Task Manager API you built in Module 5, or use the demo backend from the Guided Example.

**Time:** 45 minutes

**What you’ll build:**

Create a Streamlit app (`my_frontend.py`) with the following features:

**Requirements:**

1. **Login/Logout** — Login form with username and password, JWT stored in session state, user displayed in sidebar, working logout button
2. **Metrics** — Display at least 2 `st.metric()` cards (total tasks, completed tasks)
3. **Task list** — Display all tasks with their status
4. **Add task form** — A form that POSTs a new task to the API
5. **Error handling** — Show a clear message if the backend is unreachable, and handle 401s by redirecting to login

**Backend options:**

- **Recommended:** Your Module 5 AI-Ready Task Manager API (start it with `uvicorn`)
- **Alternative:** The `backend.py` from this lesson’s Guided Example

**Deliverable:** A working Streamlit app that authenticates with your API, displays tasks, and allows adding new tasks.

**Hints:**

- Start with the auth gate pattern from the Concept lesson
- Use `try/except requests.exceptions.ConnectionError` around all API calls
- Test with the backend running, then stop it and verify your error handling works

**Why this exercise?** This is the pattern for the module project and every AI application you’ll build: a Streamlit frontend talking to a FastAPI backend with authentication. Getting it right here means the module project builds naturally.