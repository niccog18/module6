"""
Module 6 Project — AI Dashboard  (Solution)
API Client — centralised backend communication
================================================
All network calls go through this module so:
  • Auth header is added in one place
  • Error handling is consistent
  • The Streamlit app stays clean
"""

import requests

API_BASE = "http://localhost:8000"
TIMEOUT  = 5  # seconds


def _headers(token: str | None) -> dict:
    """Build the Authorization header dict."""
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}


def login(username: str, password: str) -> tuple[dict | None, str | None]:
    """POST /auth/token. Returns (response_dict, error)."""
    try:
        r = requests.post(
            f"{API_BASE}/auth/token",
            json={"username": username, "password": password},
            timeout=TIMEOUT,
        )
        if not r.ok:
            return None, f"Login failed ({r.status_code}): {r.json().get('detail', r.text)}"
        return r.json(), None
    except requests.ConnectionError:
        return None, "Cannot connect to the backend. Is it running? (uvicorn backend:app --reload)"
    except Exception as e:
        return None, str(e)


def get_tasks(token: str) -> tuple[list | None, str | None]:
    """GET /tasks. Returns (task_list, error)."""
    try:
        r = requests.get(f"{API_BASE}/tasks", headers=_headers(token), timeout=TIMEOUT)
        if r.status_code == 401:
            return None, "401"
        if not r.ok:
            return None, f"API error {r.status_code}"
        return r.json(), None
    except requests.ConnectionError:
        return None, "Cannot connect to the backend."
    except Exception as e:
        return None, str(e)


def create_task(token: str, title: str) -> tuple[dict | None, str | None]:
    """POST /tasks. Returns (new_task, error)."""
    try:
        r = requests.post(
            f"{API_BASE}/tasks",
            json={"title": title},
            headers=_headers(token),
            timeout=TIMEOUT,
        )
        if r.status_code == 401:
            return None, "401"
        if not r.ok:
            return None, f"API error {r.status_code}"
        return r.json(), None
    except requests.ConnectionError:
        return None, "Cannot connect to the backend."
    except Exception as e:
        return None, str(e)


def complete_task(token: str, task_id: int) -> tuple[dict | None, str | None]:
    """PATCH /tasks/{id}/complete. Returns (updated_task, error)."""
    try:
        r = requests.patch(
            f"{API_BASE}/tasks/{task_id}/complete",
            headers=_headers(token),
            timeout=TIMEOUT,
        )
        if r.status_code == 401:
            return None, "401"
        if not r.ok:
            return None, f"API error {r.status_code}"
        return r.json(), None
    except requests.ConnectionError:
        return None, "Cannot connect to the backend."
    except Exception as e:
        return None, str(e)
