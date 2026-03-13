"""
L11 — Streamlit + FastAPI: Frontend  (STARTER)
================================================
Run with (after starting the backend):
    streamlit run frontend.py

Your goal: build a Streamlit frontend for the task API.

Required features:
    1. Login form (stores JWT in session state on success)
    2. Sidebar showing logged-in user + logout button
    3. Metrics row (total / done / pending tasks)
    4. Task list with Complete button per pending task
    5. Add task form (POST to API)
    6. Error handling for connection errors and 401s
    7. Auth gate: show login if no token, app if token exists

Key patterns:
    Auth gate:
        if st.session_state.token is None:
            # show login form
            st.stop()
        # rest of app (only reached when logged in)

    Centralised api_call(method, path, **kwargs):
        • Adds Authorization: Bearer <token> header automatically
        • Returns (data, error_string) — one of them is None
        • Handles 401 → clears token → returns error message
        • Handles ConnectionError → returns helpful error message
"""

import streamlit as st
import requests

API_BASE = "http://localhost:8000"

# ── Page config ────────────────────────────────────────────────────────────
# TODO: st.set_page_config

# ── Session state ──────────────────────────────────────────────────────────
# TODO: Initialise "token" to None
# TODO: Initialise "username" to None

# ══════════════════════════════════════════════════════════════════════════
# CENTRALISED API CLIENT
# ══════════════════════════════════════════════════════════════════════════
# TODO: Implement api_call(method, path, **kwargs)
#   - Inject Authorization header if token exists
#   - Call requests.request(method, API_BASE + path, headers=headers, ...)
#   - If 401: clear token and username, return (None, "Session expired...")
#   - If not response.ok: return (None, f"API error {status}: {text}")
#   - If 204: return ({}, None)
#   - Otherwise: return (response.json(), None)
#   - Catch ConnectionError: return (None, "Cannot connect to the API...")
def api_call(method: str, path: str, **kwargs):
    pass  # TODO — return (data, error)


# ══════════════════════════════════════════════════════════════════════════
# AUTH GATE
# ══════════════════════════════════════════════════════════════════════════
# TODO: if st.session_state.token is None:
#   - Show login form (st.form)
#   - On submit: call api_call("POST", "/auth/token", json={...})
#   - On success: store token + username in session state, st.rerun()
#   - On error: st.error(error_message)
#   - Call st.stop() so the app below doesn't render


# ══════════════════════════════════════════════════════════════════════════
# MAIN APP
# ══════════════════════════════════════════════════════════════════════════

# ── Sidebar ────────────────────────────────────────────────────────────────
# TODO: with st.sidebar:
#   - App title + divider
#   - Show "Logged in as [username]"
#   - Logout button → clear token + username + st.rerun()

# ── Load tasks ─────────────────────────────────────────────────────────────
# TODO: tasks, error = api_call("GET", "/tasks")
# TODO: If error: st.error(error); tasks = []

# ── Metrics ────────────────────────────────────────────────────────────────
# TODO: Calculate total, done, pending
# TODO: Display 3 st.metric() in 3 columns

# ── Add task form ──────────────────────────────────────────────────────────
# TODO: st.form with a text_input and submit button
# TODO: On submit: api_call("POST", "/tasks", json={"title": ...})
#       → st.success / st.error, then st.rerun()

# ── Task list ──────────────────────────────────────────────────────────────
# TODO: For each task:
#   - Show title (strikethrough if done: f"~~{title}~~" in markdown)
#   - Show status (st.success for done, st.warning for pending)
#   - For pending tasks: Complete button → api_call("PATCH", f"/tasks/{id}/complete")
#     → st.rerun() on success
