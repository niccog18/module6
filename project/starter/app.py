"""
Module 6 Project — AI Dashboard
================================

Run with:

    # Start the backend:
    uvicorn backend:app --reload --port 8000

    # Start the Streamlit app:
    streamlit run app.py
"""

import time

import streamlit as st

from mock_data import (
    MOCK_TASKS,
    MOCK_STATS,
    MOCK_USER,
    MOCK_TOKEN,
    MOCK_CHAT_HISTORY,
)

import api_client


# ── Step 1: Page configuration ─────────────────────────────────────────────

st.set_page_config(
    layout="wide",
    page_title="AI Dashboard",
    page_icon="🤖",
)


# ── Step 2: Session state initialisation ───────────────────────────────────

if "token" not in st.session_state:
    st.session_state.token = None

if "username" not in st.session_state:
    st.session_state.username = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "use_mock" not in st.session_state:
    st.session_state.use_mock = False


# ════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ════════════════════════════════════════════════════════════════════════════

def logout():
    """Clear the user's session and return to the login screen."""

    st.session_state.token = None
    st.session_state.username = None
    st.session_state.messages = []
    st.session_state.use_mock = False

    st.rerun()


def get_tasks():
    """Get tasks from mock data or the real API."""

    if st.session_state.use_mock:
        return MOCK_TASKS, None

    tasks, error = api_client.get_tasks(
        st.session_state.token
    )

    return tasks, error


def get_task_stats(tasks):
    """Calculate task statistics."""

    if st.session_state.use_mock:
        return MOCK_STATS

    total = len(tasks)

    done = sum(
        1
        for task in tasks
        if task.get("completed", False)
    )

    pending = total - done

    return {
        "total_tasks": total,
        "done_tasks": done,
        "pending_tasks": pending,
    }


def mock_ai_response(message):
    """Generate a simple mock AI response."""

    responses = [
        (
            "FastAPI is a modern Python framework for building APIs. "
            "It uses Python type hints and Pydantic for validation."
        ),
        (
            "A good approach is to break large tasks into smaller "
            "steps and complete the highest-priority items first."
        ),
        (
            "Streamlit lets you build interactive Python web "
            "applications without needing to write frontend "
            "JavaScript."
        ),
        (
            "JWT authentication allows the client to prove that "
            "the user has successfully logged in when making "
            "protected API requests."
        ),
    ]

    index = len(message) % len(responses)

    return responses[index]


def stream_response(response):
    """Simulate a streaming AI response."""

    for word in response.split():
        yield word + " "
        time.sleep(0.04)


# ════════════════════════════════════════════════════════════════════════════
# SECTION A — AUTHENTICATION
# ════════════════════════════════════════════════════════════════════════════

if not st.session_state.token:

    st.title("🤖 AI Dashboard")

    st.subheader("Login")

    st.write(
        "Log in to access your task dashboard."
    )

    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter your username",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
        )

        use_mock = st.checkbox(
            "Use Mock Data",
            help=(
                "Use the instructor-provided mock data "
                "without starting the FastAPI backend."
            ),
        )

        submitted = st.form_submit_button(
            "Login",
            use_container_width=True,
        )

        if submitted:

            # Mock login
            if use_mock:

                st.session_state.token = MOCK_TOKEN
                st.session_state.username = MOCK_USER
                st.session_state.use_mock = True
                st.session_state.messages = MOCK_CHAT_HISTORY.copy()

                st.rerun()

            # Real API login
            if not username or not password:

                st.error(
                    "Please enter both username and password."
                )

            else:

                token, error = api_client.login(
                    username,
                    password,
                )

                if error:

                    st.error(error)

                else:

                    st.session_state.token = token
                    st.session_state.username = username
                    st.session_state.use_mock = False

                    st.rerun()

    st.stop()


# ════════════════════════════════════════════════════════════════════════════
# SECTION B — SIDEBAR
# ════════════════════════════════════════════════════════════════════════════

with st.sidebar:

    st.title("🤖 AI Dashboard")

    st.divider()

    st.subheader("👤 Account")

    st.write(
        f"Logged in as **{st.session_state.username}**"
    )

    if st.session_state.use_mock:
        st.caption("🧪 Mock data mode")
    else:
        st.caption("🔗 Connected to FastAPI")

    if st.button(
        "🚪 Logout",
        use_container_width=True,
    ):
        logout()

    st.divider()

    st.subheader("🤖 AI Chat Settings")

    ai_api_key = st.text_input(
        "AI API Key",
        type="password",
        help="Optional. Current version uses mock AI responses.",
    )

    system_prompt = st.text_area(
        "System Prompt",
        value=(
            "You are a helpful AI assistant that helps "
            "the user manage and prioritize tasks."
        ),
    )

    st.divider()

    st.caption(
        "Module 6 — Web Essentials / Streamlit"
    )


# ════════════════════════════════════════════════════════════════════════════
# SECTION C — MAIN CONTENT
# ════════════════════════════════════════════════════════════════════════════

st.title("📋 Task Management Dashboard")

st.write(
    "Manage tasks, monitor progress, and use the AI assistant "
    "to help organize your work."
)


tab_dash, tab_tasks, tab_chat = st.tabs(
    [
        "📊 Dashboard",
        "✅ Tasks",
        "🤖 AI Chat",
    ]
)


# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — DASHBOARD
# ════════════════════════════════════════════════════════════════════════════

with tab_dash:

    st.header("📊 Dashboard")

    with st.spinner("Loading task data..."):

        tasks, error = get_tasks()

    if error:

        st.error(error)
        tasks = []

    stats = get_task_stats(tasks)

    # Metrics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Tasks",
            stats["total_tasks"],
        )

    with col2:
        st.metric(
            "Completed",
            stats["done_tasks"],
        )

    with col3:
        st.metric(
            "Pending",
            stats["pending_tasks"],
        )

    st.divider()

    # Task dataframe

    st.subheader("Task List")

    if tasks:

        st.dataframe(
            tasks,
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.info(
            "No tasks found."
        )

    # Chart

    st.subheader("Task Completion")

    chart_data = {
        "Status": [
            "Completed",
            "Pending",
        ],
        "Tasks": [
            stats["done_tasks"],
            stats["pending_tasks"],
        ],
    }

    st.bar_chart(
        chart_data,
        x="Status",
        y="Tasks",
    )


# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — TASKS
# ════════════════════════════════════════════════════════════════════════════

with tab_tasks:

    st.header("✅ Task Management")

    # Add Task Form

    st.subheader("➕ Add a Task")

    with st.form("add_task_form"):

        title = st.text_input(
            "Task Title",
            placeholder="Enter a task title...",
        )

        submitted = st.form_submit_button(
            "Add Task",
            use_container_width=True,
        )

        if submitted:

            if not title.strip():

                st.error(
                    "Task title cannot be empty."
                )

            elif st.session_state.use_mock:

                new_id = (
                    max(
                        task["id"]
                        for task in MOCK_TASKS
                    ) + 1
                    if MOCK_TASKS
                    else 1
                )

                MOCK_TASKS.append(
                    {
                        "id": new_id,
                        "title": title,
                        "done": False,
                        "created_at": "2026-08-13",
                    }
                )

                st.success(
                    "Task added successfully!"
                )

                st.rerun()

            else:

                task, error = api_client.create_task(
                    st.session_state.token,
                    title,
                )

                if error:

                    st.error(error)

                else:

                    st.success(
                        "Task added successfully!"
                    )

                    st.rerun()

    st.divider()

    # Existing Tasks

    st.subheader("Existing Tasks")

    with st.spinner("Loading tasks..."):

        tasks, error = get_tasks()

    if error:

        st.error(error)

    elif not tasks:

        st.info(
            "No tasks available."
        )

    else:

        for task in tasks:

            task_id = task.get("id")

            task_title = task.get(
                "title",
                "Untitled Task",
            )

            # Mock data uses "done".
            # Real API data uses "completed".
            is_done = task.get(
                "done",
                task.get("completed", False),
            )

            col1, col2 = st.columns(
                [5, 1]
            )

            with col1:

                if is_done:

                    st.write(
                        f"~~{task_title}~~"
                    )

                else:

                    st.write(
                        f"**{task_title}**"
                    )

            with col2:

                if is_done:

                    st.success("Done")

                else:

                    if st.button(
                        "Complete",
                        key=f"complete_{task_id}",
                    ):

                        # Mock complete
                        if st.session_state.use_mock:

                            task["done"] = True

                            st.success(
                                "Task completed!"
                            )

                            st.rerun()

                        # Real API complete
                        else:

                            updated_task, error = (
                                api_client.complete_task(
                                    st.session_state.token,
                                    task_id,
                                )
                            )

                            if error:

                                st.error(error)

                            else:

                                st.success(
                                    "Task completed!"
                                )

                                st.rerun()


# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — AI CHAT
# ════════════════════════════════════════════════════════════════════════════

with tab_chat:

    st.header("🤖 AI Task Assistant")

    st.write(
        "Ask the AI assistant questions about your tasks, "
        "priorities, or study workflow."
    )

    # Scrollable chat history area
    chat_container = st.container(height=500)

    with chat_container:

        # Display existing chat history
        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

    # Chat input stays below the chat history
    prompt = st.chat_input(
        "Ask the AI assistant something..."
    )

    if prompt:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        # Display user message
        with chat_container:

            with st.chat_message("user"):

                st.markdown(prompt)

        # Generate AI response
        with chat_container:

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    response = mock_ai_response(prompt)

                streamed_response = st.write_stream(
                    stream_response(response)
                )

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": streamed_response,
            }
        )