"""
Module 6 Project — AI Dashboard  (Solution)
Backend: FastAPI Demo Server
==============================
Run with:
    uvicorn backend:app --reload --port 8000

Self-contained — no database needed. All data lives in memory.
Demo credentials: demo / demo  (or alice / password123)
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
import base64, json

app = FastAPI(title="AI Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

# ── Data ──────────────────────────────────────────────────────────────────────
USERS = {"demo": "demo", "alice": "password123", "bob": "pass456"}

TASKS: dict[str, list] = {
    "demo": [
        {"id": 1, "title": "Complete Module 6 project", "done": False, "created_at": "2026-03-10"},
        {"id": 2, "title": "Review FastAPI auth docs",   "done": True,  "created_at": "2026-03-09"},
        {"id": 3, "title": "Practice CSS Flexbox",       "done": False, "created_at": "2026-03-08"},
        {"id": 4, "title": "Build a Streamlit dashboard","done": True,  "created_at": "2026-03-07"},
    ],
    "alice": [
        {"id": 1, "title": "Read Python docs",       "done": True,  "created_at": "2026-03-01"},
        {"id": 2, "title": "Build a REST API",        "done": False, "created_at": "2026-03-05"},
    ],
    "bob": [
        {"id": 1, "title": "Learn Streamlit widgets", "done": False, "created_at": "2026-03-01"},
    ],
}
NEXT_IDS: dict[str, int] = {"demo": 5, "alice": 3, "bob": 2}

# ── Token helpers ─────────────────────────────────────────────────────────────
def make_token(username: str) -> str:
    return base64.b64encode(json.dumps({"sub": username}).encode()).decode()

def decode_token(token: str) -> str:
    try:
        return json.loads(base64.b64decode(token).decode())["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)) -> str:
    username = decode_token(creds.credentials)
    if username not in USERS:
        raise HTTPException(status_code=401, detail="Unknown user")
    return username

# ── Models ────────────────────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    username: str
    password: str

class TaskCreate(BaseModel):
    title: str

# ── Routes ────────────────────────────────────────────────────────────────────
@app.post("/auth/token")
def login(body: LoginRequest):
    if body.username not in USERS or USERS[body.username] != body.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    TASKS.setdefault(body.username, [])
    NEXT_IDS.setdefault(body.username, 1)
    return {"access_token": make_token(body.username), "token_type": "bearer", "username": body.username}

@app.get("/tasks")
def get_tasks(username: str = Depends(get_current_user)):
    return TASKS.get(username, [])

@app.post("/tasks", status_code=201)
def create_task(body: TaskCreate, username: str = Depends(get_current_user)):
    task = {"id": NEXT_IDS[username], "title": body.title.strip(), "done": False,
            "created_at": datetime.now().isoformat(timespec="seconds")}
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
    return {"message": "AI Dashboard API running", "demo": {"username": "demo", "password": "demo"}}
