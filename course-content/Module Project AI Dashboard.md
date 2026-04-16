# Module Project: AI Dashboard

**Module 6 — Web Essentials & Streamlit**

---

## Project Overview

Build a **Streamlit application** that connects to a real API backend and includes at least one AI-powered feature. This project integrates everything from Module 6 — layout, state management, data display, API connection, and AI interfaces — into one cohesive application.

**Time:** 10–15 hours

**Presentation:** 5 minutes (live demo + architecture walkthrough)

---

## Project Structure

```
ai-dashboard/
├── backend.py           # FastAPI backend (or use your Module 5 API)
├── app.py               # Streamlit frontend
├── api_client.py        # Centralized API call functions
├── requirements.txt     # Dependencies (streamlit, requests, plotly, etc.)
└── .streamlit/
    └── secrets.toml     # API keys (not committed to Git)
```

---

## Requirements & Rubric

### 1. Authentication (15 points)

- Login form with username and password fields
- JWT token stored in `st.session_state`
- Logged-in user displayed in the sidebar
- Working logout button that clears session state

### 2. Dashboard View (20 points)

- At least 3 `st.metric()` cards in a `st.columns()` row
- At least one `st.dataframe()` displaying data from the API
- At least one chart (Streamlit built-in or Plotly)

### 3. Data Interaction (20 points)

- One create/add form that POSTs data to the API
- One action on existing data (complete a task, delete an item, update a record)

### 4. AI Feature (20 points)

Implement ONE of the following:

- **AI suggestion endpoint** — Call a `/suggest` or similar endpoint that returns an AI-generated suggestion based on data
- **Chat interface** — A chat tab with `st.chat_message()`, history in session state, and streaming responses (real API or mock)
- **AI summary** — A button that sends data to an AI endpoint and displays a summary

### 5. Layout & UX (15 points)

- `st.set_page_config()` with layout, title, and icon
- Sidebar for controls and settings
- At least 2 tabs organizing content
- Error messages for API failures (connection errors, 401s)
- Loading states where appropriate (`st.spinner()` or `st.status()`)

### 6. Code Quality (10 points)

- Centralized API calls (not scattered `requests.get()` everywhere)
- Proper `st.session_state` initialization with the `if "key" not in` pattern
- Organized code with functions (not one giant script)
- Working `requirements.txt`

---

## Grading Rubric

| Category | Points | Criteria |
| --- | --- | --- |
| Authentication | 15 | Login form, JWT in state, user in sidebar, logout works |
| Dashboard View | 20 | 3+ metrics, 1 dataframe, 1 chart, data from API |
| Data Interaction | 20 | 1 create form (POST), 1 action on existing data |
| AI Feature | 20 | Working AI suggestion, chat, or summary feature |
| Layout & UX | 15 | Page config, sidebar, 2+ tabs, error handling, loading |
| Code Quality | 10 | Centralized API calls, state init, functions, requirements.txt |
| **Total** | **100** |  |

---

## Backend Options

**Option A (Recommended):** Your **Module 5 AI-Ready Task Manager API**. It already has auth, CRUD, and you can add a `/suggest` endpoint for the AI feature.

**Option B:** The **demo backend from Lesson 11**. Simpler, but fully functional for this project.

**Option C:** A **public API** (JSONPlaceholder, OpenWeather, etc.) with direct AI calls for the AI feature. No auth component needed if the API doesn’t require it — but you’d need to implement a mock auth gate for the authentication points.

---

## Suggested App Ideas

1. **Task Dashboard** — Connected to your Module 5 API. Metrics (total/done/pending), task list with complete/delete, add form, AI suggestion for task descriptions or priorities.
2. **Study Tracker** — Track modules completed, hours spent, quiz scores. AI feature: ask the AI to suggest study focus areas based on your weakest scores.
3. **Weather Dashboard** — Connect to OpenWeather API. Show current weather metrics, 5-day forecast chart, location search. AI feature: "What should I wear today?" chat based on weather data.
4. **Recipe Finder** — Connect to a recipe API. Browse recipes, filter by category, save favorites. AI feature: chat with an AI chef that suggests recipes based on ingredients.
5. **Personal Finance Tracker** — Track expenses/income with your own API. Metrics (total spent, budget remaining), charts by category, add expense form. AI feature: spending summary or budget advice.

---

## Recommended Build Order

1. **Set up the project structure** — Create files, install dependencies, get the backend running
2. **Build the auth gate** — Login form → token in session state → sidebar user display + logout
3. **Add the dashboard view** — Metrics row, one dataframe, one chart (hardcoded data is fine initially)
4. **Connect to the API** — Replace hardcoded data with real API calls via `api_client.py`
5. **Add data interaction** — Create/add form and one action on existing data
6. **Add the AI feature** — Chat interface, suggestion endpoint, or summary
7. **Polish** — Layout, tabs, error handling, loading states, code cleanup

---

## 5-Minute Presentation

Your presentation should include:

1. **Live demo** (2 min) — Log in, show the dashboard, add data, interact with existing data, use the AI feature
2. **Architecture** (1 min) — Briefly explain: "My Streamlit frontend talks to this FastAPI backend. Here’s how auth works."
3. **One challenge** (1 min) — What was the hardest part? How did you solve it?
4. **What you’d improve** (1 min) — If you had another week, what would you add or change?

---

## Starter Code

**GitHub:** `module-06-web-streamlit/project/starter/`

The starter includes the project folder structure, a `requirements.txt` with pinned versions, an `api_client.py` skeleton with function stubs, and a basic `app.py` with `set_page_config` and session state initialization.

You are expected to build the actual implementation. The starter just saves you the setup time.