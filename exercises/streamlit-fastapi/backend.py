"""
L11 — Streamlit + FastAPI: Backend  (STARTER)
===============================================
Run with (once implemented):
    uvicorn backend:app --reload --port 8000

Your goal: build an authenticated task API.

Endpoints to implement:
    POST /auth/token           — accept username+password, return {"access_token": ..., "username": ...}
    GET  /tasks                — return the current user's tasks (auth required)
    POST /tasks                — create a task for the current user (auth required)
    PATCH /tasks/{id}/complete — mark a task as done (auth required)

Authentication scheme:
    • For simplicity, encode the token as base64-encoded JSON:
        import base64, json
        payload = json.dumps({"sub": username})
        token = base64.b64encode(payload.encode()).decode()
    • Clients send: Authorization: Bearer <token>
    • Use FastAPI's HTTPBearer security scheme to extract the token

Data storage:
    • In-memory dicts: TASKS (username → list of tasks), NEXT_IDS (username → int)
    • No database needed
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
import base64, json

app = FastAPI(title="Task API with Auth")

# TODO: Add CORSMiddleware with allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]

security = HTTPBearer()

# ── In-memory data ────────────────────────────────────────────────────────────
# TODO: Create a USERS dict: {username: password} with at least "demo": "demo"
USERS = {}

# TODO: Create TASKS dict: {username: [list of task dicts]}
# TODO: Create NEXT_IDS dict: {username: int} for auto-increment IDs
TASKS: dict[str, list] = {}
NEXT_IDS: dict[str, int] = {}

# ── Request body models ───────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    username: str
    password: str

class TaskCreate(BaseModel):
    title: str

# ── Token helpers ─────────────────────────────────────────────────────────────
# TODO: Implement make_token(username) → str
#   Encode {"sub": username} as base64 JSON
def make_token(username: str) -> str:
    pass  # TODO

# TODO: Implement decode_token(token) → str
#   Decode base64 JSON → return username, raise HTTPException(401) if invalid
def decode_token(token: str) -> str:
    pass  # TODO

# ── Auth dependency ───────────────────────────────────────────────────────────
# TODO: Implement get_current_user(credentials) → str
#   Use decode_token on credentials.credentials
#   Raise 401 if username not in USERS
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    pass  # TODO

# ── Routes ────────────────────────────────────────────────────────────────────

# TODO: POST /auth/token
#   - Check username + password against USERS
#   - Raise HTTPException(401) if wrong
#   - Call TASKS.setdefault and NEXT_IDS.setdefault to initialise data for new users
#   - Return {"access_token": make_token(username), "token_type": "bearer", "username": username}
@app.post("/auth/token")
def login(body: LoginRequest):
    pass  # TODO


# TODO: GET /tasks — protected with Depends(get_current_user)
#   Return TASKS.get(username, [])
@app.get("/tasks")
def get_tasks(username: str = Depends(get_current_user)):
    pass  # TODO


# TODO: POST /tasks — protected
#   Create a task dict {id, title, done: False, created_at}
#   Append to TASKS[username], increment NEXT_IDS[username], return the task
@app.post("/tasks", status_code=201)
def create_task(body: TaskCreate, username: str = Depends(get_current_user)):
    pass  # TODO


# TODO: PATCH /tasks/{task_id}/complete — protected
#   Find the task, set done=True, return it
#   Raise HTTPException(404) if not found
@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int, username: str = Depends(get_current_user)):
    pass  # TODO


@app.get("/")
def root():
    return {"message": "Backend is running. Visit /docs for interactive API docs."}
