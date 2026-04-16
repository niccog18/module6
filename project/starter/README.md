# Module 6 Project — AI Dashboard (Starter)

## Overview

Build a full-featured Streamlit dashboard that integrates everything from Module 6:
authentication, task management, data visualisation, and an AI chat interface.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Start the FastAPI backend:
   ```bash
   pip install fastapi uvicorn
   uvicorn backend:app --reload --port 8000
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit app — your primary work file |
| `api_client.py` | Stub functions for backend communication |
| `mock_data.py` | Sample data for offline development |
| `requirements.txt` | Python dependencies |

## Requirements

Your project is graded using the FIT rubric described below.
Key sections to implement:

1. **Authentication** — login form, JWT stored in session state, logout
2. **Dashboard** — metrics row (st.metric), dataframe, chart
3. **Task management** — add task form, complete task buttons
4. **AI Chat** — chat history, mock responses, streaming with st.write_stream
5. **Layout** — wide layout, sidebar controls, multiple tabs

## Tips

- Use `mock_data.py` to build and test the UI before the backend is ready.
- All API calls should go through `api_client.py`, not inline `requests` calls.
- Follow the session state pattern: initialise all keys before reading them.

---

## Detailed Requirements

### 1. Authentication
- Login form with username/password fields
- JWT token stored in `st.session_state`
- Logout button that clears session
- Protected pages that redirect to login if not authenticated

### 2. Dashboard
- Metrics row using `st.metric` (e.g., total tasks, completed, pending)
- Data displayed in `st.dataframe`
- At least one chart (bar, line, or pie) using Streamlit's built-in charting

### 3. Task Management
- Form to add new tasks (title, description, priority)
- Display task list with status
- Complete/delete task buttons
- Tasks persist in session state (or via API)

### 4. AI Chat Interface
- Chat history displayed with `st.chat_message`
- User input via `st.chat_input`
- Mock AI responses (or real if you have an API key)
- Streaming display using `st.write_stream`

### 5. Layout & Polish
- Wide layout (`st.set_page_config(layout="wide")`)
- Sidebar with navigation/controls
- Multiple tabs or pages for different sections
- Clean, professional appearance

---

## Presentation (5 minutes)

1. **App walkthrough** (2 min) — Demo the full app: login, dashboard, task management, AI chat
2. **Architecture** (1.5 min) — Explain how components connect (session state, API client, mock data)
3. **Interesting feature** (1 min) — Highlight one feature you're proud of or found challenging
4. **Challenge** (0.5 min) — What was hardest? How did you solve it?

---

## Grading — FIT Framework

9 dimensions across three categories, each scored 1–5, for a **total of 45 points**. A score of 3 ("Minimally Career-Ready") on every dimension is the passing bar.

### Functional

| Dimension | What We're Looking For |
|-----------|----------------------|
| **Value/Impact** | Working dashboard that integrates auth, data display, task management, and AI chat |
| **Requirements** | All 5 sections implemented: auth, dashboard, tasks, AI chat, layout |
| **Timelines** | Delivered on time with working demo |

### Interpersonal

| Dimension | What We're Looking For |
|-----------|----------------------|
| **Professionalism** | Clean code, proper session state management, organized file structure |
| **Presentation** | 5-minute demo covering app walkthrough, architecture, interesting feature, challenge |
| **Feedback** | Evidence of iteration — UI refinements, debugging, testing different layouts |

### Technical

| Dimension | What We're Looking For |
|-----------|----------------------|
| **Complexity** | Session state auth, API integration, streaming chat, data visualization |
| **Design** | API calls through `api_client.py`, not inline. Clean separation of concerns |
| **Reliability** | Handles missing data, failed API calls, unauthenticated access gracefully |

> **Scoring Scale:** 5 = Exemplary · 4 = Proficient · 3 = Minimally Career-Ready · 2 = Needs Improvement · 1 = Incomplete
