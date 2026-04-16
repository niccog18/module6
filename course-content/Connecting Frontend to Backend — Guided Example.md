# Connecting Frontend to Backend — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 12 min — "Build a mini API + HTML frontend: FastAPI with in-memory tasks, then an HTML/JS frontend that loads tasks, adds tasks, and marks them complete — all via fetch(). Show CORS error first, then the fix."]`

Let’s build a complete frontend-to-backend connection. We’ll create a tiny FastAPI server with in-memory storage (no database setup needed) and an HTML frontend that communicates with it.

---

## Part 1: The Mini API (`mini_api.py`)

Create a file called `mini_api.py`:

```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS — allow our HTML frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow any origin (fine for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory task storage (resets when server restarts)
tasks = [
    {"id": 1, "title": "Learn HTML", "done": True},
    {"id": 2, "title": "Learn CSS", "done": True},
    {"id": 3, "title": "Learn JavaScript", "done": False},
    {"id": 4, "title": "Build Streamlit app", "done": False},
]
next_id = 5  # Track the next available ID

class TaskCreate(BaseModel):
    title: str

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id
    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.patch("/tasks/{task_id}")
def toggle_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]  # Toggle done/not done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/stats")
def get_stats():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    return {"total": total, "done": done, "pending": total - done}
```

Run it:

```bash
uvicorn mini_api:app --reload
```

Verify it works by visiting `http://localhost:8000/docs`. You should see the Swagger UI with your endpoints.

---

## Part 2: The HTML Frontend (`task_frontend.html`)

Create `task_frontend.html` in the same folder:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }
        .task { display: flex; justify-content: space-between; align-items: center;
                padding: 12px; margin: 8px 0; background: #f8f8f8; border-radius: 6px; }
        .task.done { text-decoration: line-through; opacity: 0.6; }
        .add-form { display: flex; gap: 8px; margin: 20px 0; }
        .add-form input { flex: 1; padding: 10px; font-size: 1rem; }
        button { padding: 8px 16px; cursor: pointer; }
        .error { color: #e74c3c; }
        .stats { display: flex; gap: 20px; margin: 16px 0; }
        .stat { background: #e8f4fd; padding: 12px 20px; border-radius: 6px; text-align: center; }
        .stat .number { font-size: 1.5rem; font-weight: bold; color: #1a1a2e; }
    </style>
</head>
<body>
    <h1>Task Manager</h1>
    <div class="stats" id="stats"></div>

    <div class="add-form">
        <input type="text" id="new-task" placeholder="Add a new task...">
        <button id="add-btn">Add</button>
    </div>

    <div id="task-list"></div>
    <p id="error" class="error"></p>

    <script>
    const API = "http://localhost:8000";  // Base URL for our FastAPI server

    // DOM element references
    const taskList = document.querySelector("#task-list");
    const statsDiv = document.querySelector("#stats");
    const newTaskInput = document.querySelector("#new-task");
    const addBtn = document.querySelector("#add-btn");
    const errorEl = document.querySelector("#error");

    // --- Load and display tasks ---
    async function loadTasks() {
        try {
            errorEl.textContent = "";  // Clear any previous errors
            const response = await fetch(`${API}/tasks`);
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const tasks = await response.json();

            // Build the task list HTML
            taskList.innerHTML = tasks.map(task => `
                <div class="task ${task.done ? 'done' : ''}" data-id="${task.id}">
                    <span>${task.title}</span>
                    <button onclick="toggleTask(${task.id})">
                        ${task.done ? 'Undo' : 'Complete'}
                    </button>
                </div>
            `).join("");  // .join("") combines the array of HTML strings

        } catch (error) {
            errorEl.textContent = "Could not load tasks. Is the API running?";
        }
    }

    // --- Load and display stats ---
    async function loadStats() {
        try {
            const response = await fetch(`${API}/stats`);
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();

            statsDiv.innerHTML = `
                <div class="stat"><div class="number">${data.total}</div>Total</div>
                <div class="stat"><div class="number">${data.done}</div>Done</div>
                <div class="stat"><div class="number">${data.pending}</div>Pending</div>
            `;
        } catch (error) {
            statsDiv.innerHTML = '<p class="error">Could not load stats</p>';
        }
    }

    // --- Add a new task ---
    async function addTask() {
        const title = newTaskInput.value.trim();
        if (!title) return;

        try {
            const response = await fetch(`${API}/tasks`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ title })
            });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);

            newTaskInput.value = "";   // Clear the input
            loadTasks();                // Refresh the task list
            loadStats();                // Refresh the stats
        } catch (error) {
            errorEl.textContent = "Failed to add task";
        }
    }

    // --- Toggle task complete/incomplete ---
    async function toggleTask(id) {
        try {
            const response = await fetch(`${API}/tasks/${id}`, { method: "PATCH" });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            loadTasks();   // Refresh
            loadStats();
        } catch (error) {
            errorEl.textContent = "Failed to update task";
        }
    }

    // --- Event listeners ---
    addBtn.addEventListener("click", addTask);
    newTaskInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") addTask();
    });

    // --- Initial load ---
    loadTasks();
    loadStats();
    </script>
</body>
</html>
```

---

## Running It

1. Make sure `mini_api.py` is running (`uvicorn mini_api:app --reload`)
2. Open `task_frontend.html` in your browser (double-click the file)
3. You should see the stats bar and task list loaded from the API
4. Add a task — it appears in the list and the stats update
5. Click "Complete" on a task — it gets crossed out, stats update

You just built a full frontend-to-backend application. The HTML/JS frontend communicates with the FastAPI backend over HTTP, just like any real web app.

`[DIAGRAM PLACEHOLDER: Screenshot of the working task frontend showing stats bar, task list, and add form, with arrows indicating which fetch() call each section triggers]`