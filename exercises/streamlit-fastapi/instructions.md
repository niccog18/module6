# Streamlit + FastAPI Full-Stack App

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 50 minutes

## Objective

Build a full-stack authenticated task manager with a FastAPI backend and a Streamlit frontend.

## What You'll Build

**Backend (`backend.py`):** A FastAPI server with authentication. Endpoints include `POST /auth/token` (accept username and password, return an access token), `GET /tasks` (return the current user's tasks), `POST /tasks` (create a task), and `PATCH /tasks/{id}/complete` (mark done). Authentication uses base64-encoded JSON tokens with FastAPI's `HTTPBearer` security scheme. Tasks are stored in-memory per user.

**Frontend (`frontend.py`):** A Streamlit app that communicates with the backend. It includes a login form that stores the token in session state, a sidebar showing the logged-in user with a logout button, a metrics row (total/done/pending), a task list with a Complete button per pending task, an add-task form, and error handling for connection errors and 401 responses. An auth gate shows the login form when no token exists and the full app when authenticated.

## Reference Code

The solution files (`backend.py` and `frontend.py`) are provided as a reference — try building them yourself first, then compare.

## Running

Start the backend first, then launch the frontend:

```bash
# Terminal 1 — backend
uvicorn backend:app --reload --port 8000

# Terminal 2 — frontend
streamlit run frontend.py
```

## Deliverable

A working FastAPI backend with token authentication and a Streamlit frontend that handles login, task display, and task creation.
