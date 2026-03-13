"""
L6 — Mini Dashboard: FastAPI Backend  (STARTER)
=================================================
Run this server once implemented:
    uvicorn mini_api:app --reload --port 8000

Your goal: build a simple task API with an in-memory list.

Endpoints to implement:
    GET  /tasks              — return all tasks
    POST /tasks              — create a new task (body: {"title": "..."})
    PATCH /tasks/{id}/complete — mark a task as done

Rules:
    • Use CORSMiddleware with allow_origins=["*"] so the HTML frontend can call this API
    • Use a Python list as the "database" (no real DB needed)
    • Auto-increment IDs starting at 1
    • 404 if PATCH targets a non-existent ID

Key concepts:
    • CORSMiddleware — lets browsers on different origins (ports) call this API
    • In-memory store — a Python list; data resets on restart (fine for demos)
    • Pydantic BaseModel — validates the JSON request body automatically
    • HTTPException — raises an HTTP error response with a given status code
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Mini Task API")

# ── CORS ─────────────────────────────────────────────────────────────────────
# TODO: Add CORSMiddleware to `app` using app.add_middleware(...)
# Parameters to use:
#   CORSMiddleware,
#   allow_origins=["*"],
#   allow_methods=["*"],
#   allow_headers=["*"],
#
# WHY: Without this, browsers block JavaScript on http://localhost:5500 from
#      calling an API on http://localhost:8000 (different port = different origin).


# ── In-memory task list ───────────────────────────────────────────────────────
# TODO: Create a list called `tasks` with 2-3 sample task dicts.
# Each task should have: id (int), title (str), done (bool), created_at (str)
# Example: {"id": 1, "title": "Read the FastAPI docs", "done": False, "created_at": "2026-03-01"}
tasks = []

# TODO: Create a global `next_id` variable starting at the next available int
next_id = 1

# ── Request body schema ───────────────────────────────────────────────────────
# TODO: Define a Pydantic BaseModel called TaskCreate with one field:
#   title: str
class TaskCreate(BaseModel):
    pass  # replace with: title: str


# ── Routes ────────────────────────────────────────────────────────────────────

# TODO: Implement GET /tasks
# Should return the `tasks` list.
@app.get("/tasks")
def get_tasks():
    pass  # TODO


# TODO: Implement POST /tasks
# Should create a new task dict, append it to tasks, increment next_id, return the new task.
# Decorator: @app.post("/tasks", status_code=201)
@app.post("/tasks", status_code=201)
def create_task(body: TaskCreate):
    pass  # TODO


# TODO: Implement PATCH /tasks/{task_id}/complete
# Should find the task with the matching id, set done=True, return the task.
# Raise HTTPException(status_code=404, detail="...") if not found.
@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    pass  # TODO


@app.get("/")
def root():
    return {"message": "Mini Task API is running. Visit /docs for interactive docs."}
