"""
L11 — Streamlit + FastAPI: Backend  (Solution)
================================================
Run with:
    uvicorn backend:app --reload --port 8000

Then run the frontend separately:
    streamlit run frontend.py

Endpoints:
    POST /auth/token           — fake login; returns JWT for any username/password
    GET  /tasks                — list all tasks (requires Authorization header)
    POST /tasks                — create a task
    PATCH /tasks/{id}/complete — mark a task done

Authentication flow:
    1. Client sends username + password to POST /auth/token
    2. Server returns {"access_token": "...", "token_type": "bearer"}
    3. Client includes the token in subsequent requests:
         Authorization: Bearer <token>
    4. Server decodes the token to identify the user

Note: This uses FAKE JWTs (just base64-encoded JSON) for simplicity.
      A production app would use python-jose or PyJWT with a secret key.
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
import base64, json

# ── App setup ─────────────────────────────────────────────────────────────────
app = FastAPI(title="Task API with Auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # allow all origins — fine for local dev
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

# ── In-memory data ────────────────────────────────────────────────────────────
# Users (username → hashed password in production; plain text here for demo)
USERS = {
    "alice": "password123",
    "bob":   "pass456",
    "demo":  "demo",
}

# Tasks store: username → list of tasks
TASKS: dict[str, list] = {
    "alice": [
        {"id": 1, "title": "Learn FastAPI",    "done": False, "created_at": "2026-03-01"},
        {"id": 2, "title": "Build a REST API", "done": True,  "created_at": "2026-03-02"},
    ],
    "bob": [
        {"id": 1, "title": "Study Streamlit", "done": False, "created_at": "2026-03-01"},
    ],
    "demo": [
        {"id": 1, "title": "Try the demo app",  "done": False, "created_at": "2026-03-01"},
        {"id": 2, "title": "Add a task",        "done": False, "created_at": "2026-03-01"},
        {"id": 3, "title": "Complete a task",   "done": True,  "created_at": "2026-03-01"},
    ],
}
NEXT_IDS: dict[str, int] = {"alice": 3, "bob": 2, "demo": 4}

# ── Helper: fake JWT ──────────────────────────────────────────────────────────
def make_token(username: str) -> str:
    """Encode a username as a base64 token (demo only — not secure)."""
    payload = json.dumps({"sub": username, "type": "fake-jwt"})
    return base64.b64encode(payload.encode()).decode()


def decode_token(token: str) -> str:
    """Decode the fake token and return the username. Raises 401 if invalid."""
    try:
        payload = json.loads(base64.b64decode(token).decode())
        return payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")


# ── Dependency: get current user from token ───────────────────────────────────
def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Extract and validate the Bearer token; return the username."""
    username = decode_token(credentials.credentials)
    if username not in USERS:
        raise HTTPException(status_code=401, detail="Unknown user")
    return username


# ── Request body models ───────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    username: str
    password: str

class TaskCreate(BaseModel):
    title: str


# ── Routes ────────────────────────────────────────────────────────────────────

@app.post("/auth/token")
def login(body: LoginRequest):
    """
    Accept any username/password that exists in USERS.
    Returns a fake JWT — replace with python-jose in production.
    """
    if body.username not in USERS or USERS[body.username] != body.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Ensure the user has a task list
    TASKS.setdefault(body.username, [])
    NEXT_IDS.setdefault(body.username, 1)

    return {
        "access_token": make_token(body.username),
        "token_type": "bearer",
        "username": body.username,
    }


@app.get("/tasks")
def get_tasks(username: str = Depends(get_current_user)):
    return TASKS.get(username, [])


@app.post("/tasks", status_code=201)
def create_task(body: TaskCreate, username: str = Depends(get_current_user)):
    task = {
        "id":         NEXT_IDS[username],
        "title":      body.title.strip(),
        "done":       False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    TASKS[username].append(task)
    NEXT_IDS[username] += 1
    return task


@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int, username: str = Depends(get_current_user)):
    for task in TASKS.get(username, []):
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.get("/")
def root():
    return {
        "message": "Task API with Auth is running.",
        "demo_credentials": {"username": "demo", "password": "demo"},
    }
