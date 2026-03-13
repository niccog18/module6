"""
Module 6 Project — AI Dashboard  (Solution)
Streamlit Frontend
====================
Run with (after starting the backend):
    uvicorn backend:app --reload --port 8000
    streamlit run frontend.py

Features:
    • Authentication — login form, JWT in session state, logout
    • Dashboard tab — metrics row, task dataframe, chart
    • Tasks tab — add/complete tasks with live API calls
    • AI Chat tab — chat history, mock + optional real OpenAI streaming
    • Wide layout, sidebar controls, error messages, loading states
"""

import streamlit as st
import time
import api_client

# ── Mock data for offline testing ─────────────────────────────────────────────
MOCK_TOKEN = "mock-offline"
MOCK_USER  = "demo_user"
MOCK_TASKS = [
    {"id": 1, "title": "Complete Module 6 project",  "done": False, "created_at": "2026-03-10"},
    {"id": 2, "title": "Review FastAPI auth docs",   "done": True,  "created_at": "2026-03-09"},
    {"id": 3, "title": "Practice CSS Flexbox",       "done": False, "created_at": "2026-03-08"},
    {"id": 4, "title": "Build Streamlit dashboard",  "done": True,  "created_at": "2026-03-07"},
]
# Use a dict wrapper so we can mutate these from inside with-blocks without `global`
_mock_state = {
    "tasks":   [t.copy() for t in MOCK_TASKS],
    "next_id": len(MOCK_TASKS) + 1,
}

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Dashboard",
    page_icon="🤖",
    layout="wide",
)

# ── Session state ─────────────────────────────────────────────────────────────
if "token"    not in st.session_state: st.session_state.token    = None
if "username" not in st.session_state: st.session_state.username = None
if "use_mock" not in st.session_state: st.session_state.use_mock = False
if "messages" not in st.session_state: st.session_state.messages = []
if "api_key"  not in st.session_state: st.session_state.api_key  = ""

# ── Helpers ───────────────────────────────────────────────────────────────────
def handle_401():
    """Log out if the backend returns 401."""
    st.session_state.token    = None
    st.session_state.username = None
    st.warning("Session expired — please log in again.")
    st.rerun()


def load_tasks() -> list:
    """Load tasks from mock data or the real API."""
    if st.session_state.use_mock:
        return [t.copy() for t in _mock_state["tasks"]]
    tasks, error = api_client.get_tasks(st.session_state.token)
    if error == "401":
        handle_401()
    if error:
        st.error(f"Could not load tasks: {error}")
        return []
    return tasks or []


# ══════════════════════════════════════════════════════════════════════════════
# AUTH GATE
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.token is None:
    st.title("🤖 AI Dashboard")
    st.subheader("Log In")

    with st.form("login_form"):
        username    = st.text_input("Username")
        password    = st.text_input("Password", type="password")
        use_mock    = st.checkbox("Use mock data (no backend needed)", value=True)
        submit      = st.form_submit_button("Log In")

    st.info("Real credentials: **demo / demo** · or enable mock data above")

    if submit:
        if use_mock:
            st.session_state.token    = MOCK_TOKEN
            st.session_state.username = username or MOCK_USER
            st.session_state.use_mock = True
            st.rerun()
        elif not username or not password:
            st.error("Enter both username and password.")
        else:
            data, error = api_client.login(username, password)
            if error:
                st.error(error)
            else:
                st.session_state.token    = data["access_token"]
                st.session_state.username = data["username"]
                st.session_state.use_mock = False
                st.rerun()

    st.stop()

# ══════════════════════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════════════════════

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🤖 AI Dashboard")
    st.divider()

    mode_label = "🟡 Mock Mode" if st.session_state.use_mock else "🟢 Live API"
    st.markdown(f"**{mode_label}**")
    st.markdown(f"👤 {st.session_state.username}")

    if st.button("🚪 Log Out", use_container_width=True):
        for key in ["token", "username", "use_mock", "messages"]:
            st.session_state[key] = None if key != "messages" else []
        st.rerun()

    st.divider()
    st.subheader("🤖 AI Chat Settings")
    st.session_state.api_key = st.text_input(
        "OpenAI API Key (optional)", type="password", placeholder="sk-..."
    )
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful assistant for an AI engineering bootcamp.",
        height=80,
    )
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Backend: FastAPI · http://localhost:8000")

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_dash, tab_tasks, tab_chat = st.tabs(["📊 Dashboard", "✅ Tasks", "🤖 AI Chat"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
with tab_dash:
    st.header(f"Welcome, {st.session_state.username}! 👋")

    tasks = load_tasks()
    total   = len(tasks)
    done    = sum(1 for t in tasks if t["done"])
    pending = total - done

    # Metrics row
    m1, m2, m3 = st.columns(3)
    m1.metric("📋 Total Tasks", total)
    m2.metric("✅ Completed",   done,    delta=f"{done} done",    delta_color="off")
    m3.metric("⏳ Pending",     pending, delta=f"{pending} left", delta_color="inverse")

    st.divider()

    # Task dataframe
    st.subheader("All Tasks")
    if tasks:
        rows = [{"Title": t["title"], "Status": "✅ Done" if t["done"] else "⏳ Pending",
                 "Created": t["created_at"]} for t in tasks]
        st.dataframe(rows, use_container_width=True, hide_index=True)
    else:
        st.info("No tasks yet.")

    st.divider()

    # Chart: done vs pending
    st.subheader("Progress Overview")
    st.bar_chart({"Done": done, "Pending": pending})

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — TASKS
# ══════════════════════════════════════════════════════════════════════════════
with tab_tasks:
    st.header("Task Manager")

    # Add task
    with st.form("add_task", clear_on_submit=True):
        new_title = st.text_input("New task title", placeholder="What needs to be done?")
        if st.form_submit_button("➕ Add Task"):
            if not new_title.strip():
                st.warning("Enter a title.")
            elif st.session_state.use_mock:
                _mock_state["tasks"].append({"id": _mock_state["next_id"], "title": new_title.strip(),
                                             "done": False, "created_at": "2026-03-13"})
                _mock_state["next_id"] += 1
                st.success(f"Task added: {new_title}")
                st.rerun()
            else:
                data, error = api_client.create_task(st.session_state.token, new_title.strip())
                if error == "401":
                    handle_401()
                elif error:
                    st.error(f"Could not add task: {error}")
                else:
                    st.success(f"Task added: {data['title']}")
                    st.rerun()

    st.divider()

    # Task list
    tasks = load_tasks()
    if not tasks:
        st.info("No tasks yet — add one above!")
    else:
        for task in tasks:
            col_title, col_status, col_btn = st.columns([4, 2, 1])
            title_md = f"~~{task['title']}~~" if task["done"] else task["title"]
            col_title.markdown(title_md)

            if task["done"]:
                col_status.success("✅ Done")
            else:
                col_status.warning("⏳ Pending")
                if col_btn.button("Complete", key=f"done_{task['id']}"):
                    if st.session_state.use_mock:
                        for t in _mock_state["tasks"]:
                            if t["id"] == task["id"]:
                                t["done"] = True
                        st.rerun()
                    else:
                        _, error = api_client.complete_task(st.session_state.token, task["id"])
                        if error == "401":
                            handle_401()
                        elif error:
                            st.error(f"Could not complete task: {error}")
                        else:
                            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — AI CHAT
# ══════════════════════════════════════════════════════════════════════════════
def mock_stream(text: str):
    """Mock streaming generator — yields one word at a time."""
    responses = {
        "fastapi":   "FastAPI is a modern Python web framework. It uses type hints and Pydantic to automatically validate request bodies.",
        "streamlit": "Streamlit re-runs your entire script on every user interaction. Session state persists values across re-runs.",
        "session":   "Use `if 'key' not in st.session_state:` to initialise session state safely.",
        "auth":      "JWT authentication: the server returns a token on login; the client sends it as `Authorization: Bearer <token>` on every request.",
        "cors":      "CORS (Cross-Origin Resource Sharing) lets browsers call APIs on different origins/ports. Add CORSMiddleware in FastAPI.",
    }
    lower    = text.lower()
    response = next((v for k, v in responses.items() if k in lower),
                    f"Good question about '{text}'! Add an OpenAI API key in the sidebar for real AI answers.")
    for word in response.split():
        yield word + " "
        time.sleep(0.03)


with tab_chat:
    st.header("AI Chat")

    # Render history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    if prompt := st.chat_input("Ask about APIs, Streamlit, Python…"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if st.session_state.api_key:
                try:
                    from openai import OpenAI
                    client = OpenAI(api_key=st.session_state.api_key)
                    stream = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "system", "content": system_prompt}]
                                  + st.session_state.messages,
                        stream=True,
                    )
                    def real_gen():
                        for chunk in stream:
                            delta = chunk.choices[0].delta.content
                            if delta:
                                yield delta
                    full = st.write_stream(real_gen())
                except Exception as e:
                    full = f"OpenAI error: {e}"
                    st.error(full)
            else:
                full = st.write_stream(mock_stream(prompt))

        st.session_state.messages.append({"role": "assistant", "content": full})
