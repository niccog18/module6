import streamlit as st
import requests

# Module 5 FastAPI backend
API = "http://localhost:8000"

st.set_page_config(
    page_title="Task Manager",
    page_icon="✅",
    layout="wide"
)


# --- Session State Init ---
if "token" not in st.session_state:
    st.session_state["token"] = None

if "username" not in st.session_state:
    st.session_state["username"] = None


# --- Helper Functions ---
def api_get(endpoint, token):
    """Send an authenticated GET request."""
    try:
        response = requests.get(
            f"{API}{endpoint}",
            headers={"Authorization": f"Bearer {token}"}
        )

        if response.status_code == 401:
            return "unauthorized"

        if response.ok:
            return response.json()

        return None

    except requests.exceptions.ConnectionError:
        return "connection_error"


def api_post(endpoint, token, data=None):
    """Send an authenticated POST request."""
    try:
        response = requests.post(
            f"{API}{endpoint}",
            headers={"Authorization": f"Bearer {token}"},
            json=data
        )

        if response.status_code == 401:
            return "unauthorized"

        if response.ok:
            return response.json()

        return None

    except requests.exceptions.ConnectionError:
        return "connection_error"


def api_patch(endpoint, token, data=None):
    """Send an authenticated PATCH request."""
    try:
        response = requests.patch(
            f"{API}{endpoint}",
            headers={"Authorization": f"Bearer {token}"},
            json=data
        )

        if response.status_code == 401:
            return "unauthorized"

        if response.ok:
            return response.json()

        return None

    except requests.exceptions.ConnectionError:
        return "connection_error"


# --- Auth Gate ---
if st.session_state["token"] is None:

    st.title("🔐 Task Manager — Login")
    st.write("Log in with your Module 5 Task Manager account.")

    with st.form("login"):

        email = st.text_input(
            "Email",
            placeholder="you@example.com"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        submitted = st.form_submit_button("Login")

        if submitted:

            if not email or not password:
                st.warning("Please enter your email and password.")

            else:
                try:
                    # Module 5 API uses /auth/login
                    # and expects JSON credentials.
                    response = requests.post(
                        f"{API}/auth/login",
                        json={
                            "email": email,
                            "password": password
                        }
                    )

                    if response.status_code == 200:
                        data = response.json()

                        # Store JWT in Streamlit session state
                        st.session_state["token"] = data["access_token"]

                        # Store email temporarily for sidebar display
                        st.session_state["username"] = email

                        st.rerun()

                    elif response.status_code == 401:
                        st.error("Invalid email or password.")

                    else:
                        st.error(
                            f"Login failed. API returned "
                            f"status code {response.status_code}."
                        )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "❌ Cannot connect to the API. "
                        "Is the FastAPI backend running?"
                    )

    st.stop()


# --- Sidebar ---
with st.sidebar:

    st.write(
        f"Logged in as **{st.session_state['username']}**"
    )

    st.divider()

    if st.button("Logout"):

        st.session_state["token"] = None
        st.session_state["username"] = None

        st.rerun()


# --- Authentication Token ---
token = st.session_state["token"]


# --- Get Current User ---
current_user = api_get("/users/me", token)

if current_user == "connection_error":
    st.error(
        "❌ Cannot connect to the API. "
        "Is the FastAPI backend running?"
    )
    st.stop()

if current_user == "unauthorized":
    st.warning("Your session has expired. Please log in again.")

    st.session_state["token"] = None
    st.session_state["username"] = None

    st.rerun()


# --- Load Tasks ---
task_list = api_get("/tasks", token)


# --- Handle Task API Errors ---
if task_list == "connection_error":
    st.error(
        "❌ Cannot connect to the API. "
        "Is the FastAPI backend running?"
    )
    st.stop()

if task_list == "unauthorized":
    st.warning("Your session has expired. Please log in again.")

    st.session_state["token"] = None
    st.session_state["username"] = None

    st.rerun()

if task_list is None:
    st.error("❌ Could not load tasks from the API.")
    st.stop()


# --- Dashboard ---
st.title("✅ Task Manager")

if current_user:
    st.write(
        f"Welcome, **{current_user.get('name', st.session_state['username'])}**!"
    )


# --- Metrics ---
total_tasks = len(task_list)

completed_tasks = sum(
    1 for task in task_list
    if task.get("completed", False)
)

pending_tasks = total_tasks - completed_tasks


c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Tasks",
    total_tasks
)

c2.metric(
    "Completed Tasks",
    completed_tasks
)

c3.metric(
    "Pending Tasks",
    pending_tasks
)


st.divider()


# --- Task List ---
st.subheader("📋 Tasks")

if not task_list:

    st.info("No tasks found. Add your first task below.")

else:

    for task in task_list:

        col_text, col_btn = st.columns([4, 1])

        with col_text:

            status = (
                "✅ Completed"
                if task.get("completed", False)
                else "⬜ Pending"
            )

            st.write(
                f"**{task.get('title', 'Untitled Task')}** — {status}"
            )

            if task.get("description"):
                st.caption(task["description"])

            if task.get("priority"):
                st.caption(
                    f"Priority: {task['priority']}"
                )

        with col_btn:

            if task.get("completed", False):
                button_label = "Undo"
            else:
                button_label = "Complete"

            if st.button(
                button_label,
                key=f"toggle_{task['id']}"
            ):

                result = api_patch(
                    f"/tasks/{task['id']}",
                    token,
                    {
                        "completed": not task.get(
                            "completed",
                            False
                        )
                    }
                )

                if result == "connection_error":
                    st.error(
                        "❌ Cannot connect to the API."
                    )

                elif result == "unauthorized":
                    st.session_state["token"] = None
                    st.session_state["username"] = None
                    st.rerun()

                elif result is None:
                    st.error(
                        "❌ Could not update the task."
                    )

                else:
                    st.rerun()


st.divider()


# --- Add Task Form ---
st.subheader("➕ Add a Task")

with st.form(
    "add_task",
    clear_on_submit=True
):

    new_title = st.text_input(
        "Task title",
        placeholder="Enter a task..."
    )

    new_description = st.text_area(
        "Description",
        placeholder="Optional description"
    )

    new_priority = st.selectbox(
        "Priority",
        ["low", "medium", "high"]
    )

    submitted = st.form_submit_button(
        "➕ Add Task"
    )

    if submitted:

        if not new_title.strip():

            st.warning(
                "Please enter a task title."
            )

        else:

            result = api_post(
                "/tasks",
                token,
                {
                    "title": new_title.strip(),
                    "description": new_description.strip(),
                    "priority": new_priority
                }
            )

            if result == "connection_error":

                st.error(
                    "❌ Cannot connect to the API. "
                    "Is the FastAPI backend running?"
                )

            elif result == "unauthorized":

                st.session_state["token"] = None
                st.session_state["username"] = None

                st.rerun()

            elif result is None:

                st.error(
                    "❌ Could not create the task."
                )

            else:

                st.success(
                    "✅ Task added successfully!"
                )

                st.rerun()
