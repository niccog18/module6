# Connecting Streamlit to FastAPI — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Structure a project with separate backend and frontend folders
2. Centralize API calls in an `api_client.py` module
3. Store JWT tokens in `st.session_state` and implement the auth gate pattern
4. Handle connection errors and 401 responses gracefully

---

`[VIDEO PLACEHOLDER: 8 min — "Connect Streamlit to FastAPI: show the full flow from login form to authenticated API calls. Demonstrate the auth gate pattern, token storage in session state, and graceful error handling for connection failures and expired tokens."]`

You’ve built APIs (Module 5). You’ve built Streamlit interfaces (this week). Now it’s time to connect them — the frontend calling the backend, with proper authentication and error handling.

This is the moment your stack comes together. The pattern you learn here carries through every remaining module: Streamlit frontend → FastAPI backend → database/AI model.

---

## Project Structure

For any project with a Streamlit frontend and FastAPI backend, use this structure:

```
my-app/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── requirements.txt
├── frontend/
│   ├── app.py           # Streamlit app
│   ├── api_client.py    # Centralized API calls
│   └── requirements.txt
└── README.md
```

Keeping backend and frontend separate makes deployment cleaner and lets you work on either side independently.

---

## The `api_client.py` Pattern

Instead of scattering `requests.get()` and `requests.post()` calls throughout your Streamlit code, centralize them in one file:

```python
# frontend/api_client.py
import requests

API_URL = "http://localhost:8000"  # Your FastAPI backend

def login(username: str, password: str):
    """Authenticate and return a JWT token."""
    response = requests.post(f"{API_URL}/auth/token",
        data={"username": username, "password": password})
    if response.status_code == 200:
        return response.json()["access_token"]
    return None

def get_tasks(token: str):
    """Fetch all tasks for the authenticated user."""
    response = requests.get(f"{API_URL}/tasks",
        headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 401:
        return "unauthorized"  # Signal that the token expired
    if response.ok:
        return response.json()
    return None

def create_task(token: str, title: str, description: str = ""):
    """Create a new task."""
    response = requests.post(f"{API_URL}/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": title, "description": description})
    return response.ok
```

This gives you one place to update if the API URL changes, consistent error handling, and a clean separation between UI logic and API communication.

---

## The Auth Gate Pattern

The most common Streamlit authentication pattern: show the login form if there’s no token, show the app if there is one.

```python
# frontend/app.py
import streamlit as st
from api_client import login, get_tasks

if "token" not in st.session_state:
    st.session_state["token"] = None
    st.session_state["username"] = None

# --- Auth Gate ---
if st.session_state["token"] is None:
    # Show login form
    st.title("🔐 Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            token = login(username, password)
            if token:
                st.session_state["token"] = token
                st.session_state["username"] = username
                st.rerun()
            else:
                st.error("Invalid credentials")
else:
    # Show the actual app
    st.title("My Dashboard")
    # ... dashboard content using st.session_state["token"] ...
```

The gate is a simple `if/else` on the token. No token? Show login. Token exists? Show app. Logout is just clearing the session state.

---

## Handling Errors Gracefully

Three error scenarios to handle:

**Connection error** — The backend isn’t running:

```python
try:
    tasks = get_tasks(st.session_state["token"])
except requests.exceptions.ConnectionError:
    st.error("❌ Cannot connect to the API. Is the backend running?")
    st.stop()  # Stop script execution here
```

**401 Unauthorized** — Token expired or invalid:

```python
if tasks == "unauthorized":
    st.warning("Session expired. Please log in again.")
    st.session_state["token"] = None
    st.rerun()  # Re-run to show the login form
```

**General API error** — Something else went wrong:

```python
if tasks is None:
    st.error("Failed to load tasks. Please try again.")
```

`st.stop()` is useful for fatal errors — it halts the script so no further content renders below the error message.