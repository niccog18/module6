# Mini Dashboard

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 40 minutes

## Objective

Build a full-stack task management dashboard with a FastAPI backend and an HTML/JavaScript frontend.

## What You'll Build

**Backend (`mini_api.py`):** A FastAPI server with three endpoints — `GET /tasks` (return all tasks), `POST /tasks` (create a task from a JSON body), and `PATCH /tasks/{id}/complete` (mark a task as done). Tasks are stored in an in-memory list. CORS middleware is required so the HTML frontend can call the API.

**Frontend (`dashboard.html`):** An HTML page that communicates with the API using `fetch()`. It displays a stats bar (total/done/pending counts), loads the task list on page open, provides an "Add task" form, a "Mark Done" button per task, a refresh button, a last-fetched timestamp, and error handling if the API is unreachable.

## Reference Code

The solution files (`mini_api.py` and `dashboard.html`) are provided as a reference — try building them yourself first, then compare.

## Running

Start the backend first, then open the frontend:

```bash
uvicorn mini_api:app --reload --port 8000
```

Then open `dashboard.html` in your browser.

## Deliverable

A working FastAPI backend and HTML frontend that together provide a task management dashboard.
