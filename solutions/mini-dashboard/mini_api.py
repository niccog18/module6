"""
L6 — Mini Dashboard: FastAPI Backend  (Solution)
==================================================
Run this server:
    uvicorn mini_api:app --reload --port 8000

Then open dashboard.html in your browser and click "Refresh".

Key concepts:
    • FastAPI       — a modern Python web framework for building APIs
    • CORSMiddleware— allows browsers on a different origin to call this API
    • In-memory storage — a plain Python list (no database needed for this demo)
    • HTTP methods  — GET (read), POST (create), PATCH (partial update)
    • Path parameters — /tasks/{id} passes the task ID through the URL
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

# ── Create the FastAPI application ───────────────────────────────────────────
app = FastAPI(title="Mini Task API", version="1.0")

# ── CORS — Cross-Origin Resource Sharing ─────────────────────────────────────
# Browsers enforce a "same-origin policy": by default, JavaScript on
# http://localhost:5500 (where dashboard.html runs) CANNOT call an API on
# http://localhost:8000. CORSMiddleware tells the browser "this API is safe
# to call from any origin", lifting that restriction for local development.
#
# In production you would replace allow_origins=["*"] with your actual
# frontend URL (e.g. allow_origins=["https://myapp.com"]).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins (fine for local dev)
    allow_methods=["*"],        # allow GET, POST, PATCH, DELETE, etc.
    allow_headers=["*"],        # allow any headers (including Authorization)
)

# ── In-memory data store ──────────────────────────────────────────────────────
# A plain Python list acts as our "database". Data resets every time the
# server restarts — perfect for demos, not for production.
tasks: list[dict] = [
    {"id": 1, "title": "Read the FastAPI docs", "done": False, "created_at": "2026-03-01T10:00:00"},
    {"id": 2, "title": "Build a portfolio page", "done": True,  "created_at": "2026-03-02T09:30:00"},
    {"id": 3, "title": "Practice CSS Flexbox",   "done": False, "created_at": "2026-03-03T14:00:00"},
]
next_id = 4  # simple auto-increment counter

# ── Request body schema ───────────────────────────────────────────────────────
# Pydantic BaseModel validates and parses the JSON request body.
class TaskCreate(BaseModel):
    title: str

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/tasks")
def get_tasks():
    """Return all tasks."""
    return tasks


@app.post("/tasks", status_code=201)
def create_task(body: TaskCreate):
    """Create a new task. Returns the created task."""
    global next_id
    new_task = {
        "id": next_id,
        "title": body.title.strip(),
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    """Mark a task as done. Returns the updated task."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    # 404 if no task with that ID exists
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.get("/")
def root():
    return {"message": "Mini Task API is running. Visit /docs for interactive docs."}
