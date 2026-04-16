# Connecting Frontend to Backend — Practice Exercise

## Mini Dashboard

**Objective:** Build a frontend dashboard that connects to the mini API from the Guided Example, practicing the full frontend-to-backend communication pattern.

**Time:** 30 minutes

**Prerequisites:** The `mini_api.py` from the Guided Example must be running.

**What you’ll build:**

Create a `dashboard.html` file that connects to the mini API and includes:

1. **Stats bar** — Display total, done, and pending task counts (fetch from `/stats`)
2. **Task list** — Display all tasks with their current status (fetch from `/tasks`)
3. **Add form** — An input field and button that POST a new task to `/tasks`
4. **Refresh button** — A button that re-fetches tasks and stats
5. **Last updated timestamp** — Show "Last updated: [time]" that updates whenever data is fetched. Use `new Date().toLocaleTimeString()` to get the current time.

**Deliverable:** A working `dashboard.html` that displays live data from the API, adds new tasks, and refreshes on demand.

**Hints:**

- Create a `refreshAll()` function that calls both `loadTasks()` and `loadStats()` — attach it to the Refresh button and call it on page load
- Update the timestamp inside the `refreshAll()` function
- Use the same `fetch()` + `response.ok` + `try/catch` pattern from the Guided Example

**Why this exercise?** You’re building the exact same type of interface you’ll build with Streamlit in Week 2 — a dashboard with stats, data display, forms, and API integration. The only difference will be the language.