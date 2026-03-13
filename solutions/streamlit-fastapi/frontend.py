"""
L11 — Streamlit + FastAPI: Frontend  (Solution)
================================================
Run with (after starting the backend):
    streamlit run frontend.py

Key patterns demonstrated:
    • Auth gate       — show login form if no token; show app if token exists
    • Centralized API client — all requests go through api_call() with automatic
                               auth header injection and 401 handling
    • JWT in session state  — token is stored once at login; re-used on every
                               request without asking the user to log in again
    • Error handling        — connection errors vs 401 unauthorized vs other errors
"""

import streamlit as st
import requests

# ── Configuration ─────────────────────────────────────────────────────────────
API_BASE = "http://localhost:8000"

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Task Manager",
    page_icon="✅",
    layout="wide",
)

# ── Session state initialisation ──────────────────────────────────────────────
if "token"    not in st.session_state: st.session_state.token    = None
if "username" not in st.session_state: st.session_state.username = None

# ══════════════════════════════════════════════════════════════════════════════
# CENTRALISED API CLIENT
# ──────────────────────────────────────────────────────────────────────────────
# Instead of scattering requests.get / requests.post calls throughout the app,
# every API call goes through this function. Benefits:
#   • Auth header is injected automatically
#   • 401 handling is in one place (log the user out)
#   • Connection errors are caught once
# ══════════════════════════════════════════════════════════════════════════════
def api_call(method: str, path: str, **kwargs) -> tuple[dict | list | None, str | None]:
    """
    Make an authenticated API request.
    Returns (data, error_message). One of them will be None.
    """
    headers = kwargs.pop("headers", {})
    if st.session_state.token:
        # Attach the JWT as a Bearer token in the Authorization header
        headers["Authorization"] = f"Bearer {st.session_state.token}"

    try:
        response = requests.request(
            method,
            f"{API_BASE}{path}",
            headers=headers,
            timeout=5,
            **kwargs,
        )

        if response.status_code == 401:
            # Token expired or invalid — force re-login
            st.session_state.token    = None
            st.session_state.username = None
            return None, "Session expired. Please log in again."

        if not response.ok:
            return None, f"API error {response.status_code}: {response.text}"

        # 204 No Content — successful but no body
        if response.status_code == 204:
            return {}, None

        return response.json(), None

    except requests.ConnectionError:
        return None, "Cannot connect to the API. Is the FastAPI backend running?"
    except Exception as e:
        return None, str(e)


# ══════════════════════════════════════════════════════════════════════════════
# AUTH GATE
# If no token in session state → show login form.
# Otherwise → show the main app.
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.token is None:
    # ── Login Screen ─────────────────────────────────────────────────────────
    st.title("✅ Task Manager")
    st.subheader("Log In")
    st.info("Demo credentials: **demo / demo**  (or try alice / password123)")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log In")

    if submitted:
        if not username or not password:
            st.error("Please enter both username and password.")
        else:
            data, error = api_call(
                "POST",
                "/auth/token",
                json={"username": username, "password": password},
            )
            if error:
                st.error(error)
            else:
                # Store the token and username — available on every re-run
                st.session_state.token    = data["access_token"]
                st.session_state.username = data["username"]
                st.rerun()   # re-run to show the main app

    st.stop()  # stop rendering here — don't show the app below

# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP  (only reached when logged in)
# ══════════════════════════════════════════════════════════════════════════════

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("✅ Task Manager")
    st.divider()
    st.markdown(f"👤 Logged in as **{st.session_state.username}**")
    if st.button("🚪 Log Out", use_container_width=True):
        st.session_state.token    = None
        st.session_state.username = None
        st.rerun()
    st.divider()
    st.caption("Backend: FastAPI · http://localhost:8000")

# ── Load tasks ────────────────────────────────────────────────────────────────
tasks, load_error = api_call("GET", "/tasks")

if load_error:
    st.error(load_error)
    tasks = []

# ── Metrics ───────────────────────────────────────────────────────────────────
st.title(f"Welcome, {st.session_state.username}! 👋")

total   = len(tasks)
done    = sum(1 for t in tasks if t["done"])
pending = total - done

m1, m2, m3 = st.columns(3)
m1.metric("📋 Total Tasks",   total)
m2.metric("✅ Completed",     done,    delta=f"+{done} done")
m3.metric("⏳ Pending",       pending, delta=f"{pending} remaining", delta_color="inverse")

st.divider()

# ── Add task form ─────────────────────────────────────────────────────────────
st.subheader("➕ Add New Task")
with st.form("add_task_form", clear_on_submit=True):
    new_title = st.text_input("Task title", placeholder="What needs to be done?")
    add_btn   = st.form_submit_button("Add Task")

if add_btn:
    if not new_title.strip():
        st.warning("Please enter a task title.")
    else:
        data, error = api_call("POST", "/tasks", json={"title": new_title.strip()})
        if error:
            st.error(error)
        else:
            st.success(f"Task added: **{data['title']}**")
            st.rerun()

# ── Task list ─────────────────────────────────────────────────────────────────
st.subheader("📋 Your Tasks")

if not tasks:
    st.info("No tasks yet — add one above!")
else:
    for task in tasks:
        col_title, col_status, col_btn = st.columns([4, 2, 1])

        # Strikethrough for completed tasks using markdown
        title_display = f"~~{task['title']}~~" if task["done"] else task["title"]
        col_title.markdown(title_display)

        if task["done"]:
            col_status.success("✅ Done")
        else:
            col_status.warning("⏳ Pending")
            if col_btn.button("Complete", key=f"complete_{task['id']}"):
                _, error = api_call("PATCH", f"/tasks/{task['id']}/complete")
                if error:
                    st.error(error)
                else:
                    st.rerun()
