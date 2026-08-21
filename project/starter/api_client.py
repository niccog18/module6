"""
Module 6 Project — AI Dashboard
API Client
============
Centralised functions for all backend communication.

All API calls should go through these functions so that:
    • The Authorization header is added in one place
    • Error handling is consistent
    • The rest of the app stays clean
"""

import requests


# Module 5 FastAPI backend
API_BASE = "http://localhost:8000"


def login(username: str, password: str):
    """
    Log in to the FastAPI backend.

    Your Module 5 API uses:
        POST /auth/login

    and expects JSON:
        {
            "email": "...",
            "password": "..."
        }

    Returns:
        (access_token, None) on success
        (None, error_message) on failure
    """

    try:
        response = requests.post(
            f"{API_BASE}/auth/login",
            json={
                "email": username,
                "password": password,
            },
        )

        if not response.ok:
            try:
                detail = response.json().get(
                    "detail",
                    "Login failed.",
                )
            except ValueError:
                detail = "Login failed."

            return None, detail

        data = response.json()

        access_token = data.get("access_token")

        if not access_token:
            return None, "Login succeeded but no access token was returned."

        return access_token, None

    except requests.ConnectionError:
        return (
            None,
            "Could not connect to the API. "
            "Make sure the FastAPI backend is running.",
        )

    except requests.RequestException as e:
        return None, f"API request failed: {e}"


def get_tasks(token: str):
    """
    Get the logged-in user's tasks.

    Returns:
        (list_of_tasks, None) on success
        (None, error_message) on failure
    """

    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(
            f"{API_BASE}/tasks",
            headers=headers,
        )

        if response.status_code == 401:
            return None, "Authentication failed. Please log in again."

        if not response.ok:
            try:
                detail = response.json().get(
                    "detail",
                    "Unable to load tasks.",
                )
            except ValueError:
                detail = "Unable to load tasks."

            return None, detail

        return response.json(), None

    except requests.ConnectionError:
        return (
            None,
            "Could not connect to the API. "
            "Make sure the FastAPI backend is running.",
        )

    except requests.RequestException as e:
        return None, f"API request failed: {e}"


def create_task(token: str, title: str):
    """
    Create a new task.

    Your Module 5 API accepts a Task object.
    The minimum required field is title.

    Returns:
        (new_task_dict, None) on success
        (None, error_message) on failure
    """

    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.post(
            f"{API_BASE}/tasks",
            headers=headers,
            json={
                "title": title,
            },
        )

        if response.status_code == 401:
            return None, "Authentication failed. Please log in again."

        if not response.ok:
            try:
                detail = response.json().get(
                    "detail",
                    "Unable to create task.",
                )
            except ValueError:
                detail = "Unable to create task."

            return None, detail

        return response.json(), None

    except requests.ConnectionError:
        return (
            None,
            "Could not connect to the API. "
            "Make sure the FastAPI backend is running.",
        )

    except requests.RequestException as e:
        return None, f"API request failed: {e}"


def complete_task(token: str, task_id: int):
    """
    Complete an existing task.

    Your Module 5 API uses:
        PATCH /tasks/{task_id}

    with:
        {"completed": true}

    Returns:
        (updated_task_dict, None) on success
        (None, error_message) on failure
    """

    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.patch(
            f"{API_BASE}/tasks/{task_id}",
            headers=headers,
            json={
                "completed": True,
            },
        )

        if response.status_code == 401:
            return None, "Authentication failed. Please log in again."

        if not response.ok:
            try:
                detail = response.json().get(
                    "detail",
                    "Unable to complete task.",
                )
            except ValueError:
                detail = "Unable to complete task."

            return None, detail

        return response.json(), None

    except requests.ConnectionError:
        return (
            None,
            "Could not connect to the API. "
            "Make sure the FastAPI backend is running.",
        )

    except requests.RequestException as e:
        return None, f"API request failed: {e}"
