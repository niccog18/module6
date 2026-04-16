# Connecting Streamlit to FastAPI — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 12 min — "Full Streamlit + FastAPI integration: build a self-contained FastAPI demo backend and a Streamlit frontend with login, task management, and error handling. Show the complete flow from login to authenticated CRUD."]`

We’ll build a complete two-file application: a self-contained FastAPI backend and a Streamlit frontend that connects to it.

---

## The Backend: `backend.py`

This is a simplified FastAPI server with in-memory storage and basic auth (no database required):

```python
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import secrets

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Simple in-memory auth (for demo only — not production!)
USERS = {"admin": "password123", "student": "learn2026"}
tokens = {}  # token -> username mapping
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# In-memory tasks
tasks = [
    {"id": 1, "title": "Complete Module 5", "done": True, "user": "admin"},
    {"id": 2, "title": "Start Module 6", "done": True, "user": "admin"},
    {"id": 3, "title": "Build Streamlit app", "done": False, "user": "admin"},
]
next_id = 4

class TaskCreate(BaseModel):
    title: str

def get_current_user(token: str = Depends(oauth2_scheme)):
    username = tokens.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    return username

@app.post("/auth/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if USERS.get(form_data.username) != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = secrets.token_hex(32)
    tokens[token] = form_data.username
    return {"access_token": token, "token_type": "bearer"}

@app.get("/tasks")
def get_tasks(user: str = Depends(get_current_user)):
    return [t for t in tasks if t["user"] == user]

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, user: str = Depends(get_current_user)):
    global next_id
    new_task = {"id": next_id, "title": task.title, "done": False, "user": user}
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.patch("/tasks/{task_id}")
def toggle_task(task_id: int, user: str = Depends(get_current_user)):
    for task in tasks:
        if task["id"] == task_id and task["user"] == user:
            task["done"] = not task["done"]
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/stats")
def get_stats(user: str = Depends(get_current_user)):
    user_tasks = [t for t in tasks if t["user"] == user]
    total = len(user_tasks)
    done = sum(1 for t in user_tasks if t["done"])
    return {"total": total, "done": done, "pending": total - done}
```

Run it: `uvicorn backend:app --reload`

---

## The Frontend: `frontend.py`

```python
import streamlit as st
import requests

API = "http://localhost:8000"

st.set_page_config(page_title="Task Manager", page_icon="✅", layout="wide")

# --- Session State Init ---
if "token" not in st.session_state:
    st.session_state["token"] = None
    st.session_state["username"] = None

# --- Helper Functions ---
def api_get(endpoint, token):
    try:
        r = requests.get(f"{API}{endpoint}",
            headers={"Authorization": f"Bearer {token}"})
        if r.status_code == 401: return "unauthorized"
        return r.json() if r.ok else None
    except requests.exceptions.ConnectionError:
        return "connection_error"

def api_post(endpoint, token, data=None):
    try:
        r = requests.post(f"{API}{endpoint}",
            headers={"Authorization": f"Bearer {token}"}, json=data)
        return r.ok
    except requests.exceptions.ConnectionError:
        return False

# --- Auth Gate ---
if st.session_state["token"] is None:
    st.title("🔐 Task Manager — Login")
    with st.form("login"):
        username = st.text_input("Username", placeholder="admin or student")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            try:
                r = requests.post(f"{API}/auth/token",
                    data={"username": username, "password": password})
                if r.status_code == 200:
                    st.session_state["token"] = r.json()["access_token"]
                    st.session_state["username"] = username
                    st.rerun()
                else:
                    st.error("Invalid credentials")
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to API. Is the backend running?")
    st.stop()  # Don't render anything below the login form

# --- Sidebar ---
with st.sidebar:
    st.write(f"Logged in as **{st.session_state['username']}**")
    if st.button("Logout"):
        st.session_state["token"] = None
        st.session_state["username"] = None
        st.rerun()

# --- Load Data ---
token = st.session_state["token"]
stats = api_get("/stats", token)
task_list = api_get("/tasks", token)

# Handle errors
if stats == "connection_error" or task_list == "connection_error":
    st.error("❌ Cannot connect to the API. Is the backend running?")
    st.stop()
if stats == "unauthorized" or task_list == "unauthorized":
    st.warning("Session expired. Please log in again.")
    st.session_state["token"] = None
    st.rerun()

# --- Dashboard ---
st.title("✅ Task Manager")

# Metrics row
if stats:
    c1, c2, c3 = st.columns(3)
    c1.metric("Total", stats["total"])
    c2.metric("Done", stats["done"])
    c3.metric("Pending", stats["pending"])

st.divider()

# Task list
st.subheader("Tasks")
if task_list:
    for task in task_list:
        col_text, col_btn = st.columns([4, 1])
        with col_text:
            status = "✅" if task["done"] else "⬜"
            st.write(f"{status} {task['title']}")
        with col_btn:
            label = "Undo" if task["done"] else "Complete"
            if st.button(label, key=f"toggle_{task['id']}"):
                requests.patch(f"{API}/tasks/{task['id']}",
                    headers={"Authorization": f"Bearer {token}"})
                st.rerun()

st.divider()

# Add task form
with st.form("add_task", clear_on_submit=True):
    new_title = st.text_input("New task")
    if st.form_submit_button("➕ Add Task") and new_title.strip():
        api_post("/tasks", token, {"title": new_title.strip()})
        st.rerun()
```

Run it (in a separate terminal): `streamlit run frontend.py`

Log in with `admin` / `password123`. You should see your tasks, be able to add new ones, and toggle them complete.

`[DIAGRAM PLACEHOLDER: Screenshot of the working Streamlit task manager showing the login form, then the authenticated dashboard with metrics, task list, and add form]`