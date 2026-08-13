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