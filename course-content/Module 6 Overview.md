# Module 6 Overview

**Module 6 — Web Essentials & Streamlit**

**Duration:** 2 Weeks | **Hours:** 40 | **Prerequisites:** Modules 1–5

---

## Module Philosophy

**Week 1** gives students web literacy — just enough HTML, CSS, and JavaScript to understand the medium. This is a crash course, not a frontend development program. Students will not become JavaScript developers. They need to read it, understand what’s happening, and appreciate what Streamlit abstracts away.

**Week 2** gives students Streamlit — the Python-native UI tool they’ll use to build AI interfaces for the rest of the course. Because Streamlit replaces the need to write HTML/CSS/JS directly, students quickly see the payoff for the Week 1 literacy work.

By the end of Module 6, students have a running Streamlit app connected to their Module 5 FastAPI backend, with at least one AI-powered feature.

---

## Week Structure

### Week 1 — Web Literacy

1. **How the Web Works** — DNS, HTTP, client/server, request/response cycle
2. **HTML Structure & Semantic Elements** — Tags, document skeleton, semantic vs generic elements
3. **CSS Essentials** — Selectors, box model, Flexbox
4. **JavaScript Basics** — Variables, functions, the DOM, event listeners
5. **Fetch API & Async/Await** — Async requests, `response.ok` gotcha, error handling
6. **Connecting Frontend to Backend** — CORS, auth headers, full communication chain

### Knowledge Check: Web & UI Fundamentals (10 questions)

Covers Week 1 content plus preview of Streamlit’s execution model and session state.

### Week 2 — Streamlit

1. **What is Streamlit?** — Re-run model, installation, widgets returning values
2. **Streamlit Layout & Components** — Columns, sidebar, tabs, expanders, page config
3. **User Input, Forms & State Management** — `st.session_state`, `st.form()`, multi-step flows
4. **Displaying Data: Tables, Charts, Metrics** — DataFrames, Plotly, `@st.cache_data`
5. **Connecting Streamlit to FastAPI** — Auth gate pattern, centralized API calls, error handling
6. **Building an AI-Powered Interface** — Chat components, history pattern, streaming, API keys

### Module Project: AI Dashboard (100 points, 5-minute presentation)

---

## Assessment Summary

| Assessment | Type | Placement | Weight |
| --- | --- | --- | --- |
| Web & UI Fundamentals Check | Knowledge Check (10 questions) | End of Week 1 | Mid-module checkpoint |
| AI Dashboard | Module Project (5-min presentation) | End of Week 2 | Final module assessment |

---

## Dependencies

```
streamlit
requests
httpx
plotly
openai          # Optional — for AI chat feature
fastapi         # For the backend (already from Module 5)
uvicorn         # For running FastAPI
python-multipart # For form data in auth
```

---

## Stretch Challenges

Four lessons include optional stretch challenges for fast learners:

- **CSS Essentials** — Responsive media query
- **JavaScript Basics** — Keyboard navigation for flashcards
- **User Input, Forms & State** — Countdown timer using `st.empty()`
- **Building an AI Interface** — Conversation export/download

---

## Video Placeholders Summary

| Lesson | Placement | Length | Theme |
| --- | --- | --- | --- |
| How the Web Works | Concept | 5 min | Trace a URL from browser to server and back |
| How the Web Works | Guided Example | 8 min | DevTools Network tab + Python requests |
| HTML Structure | Concept | 5 min | View source to reveal HTML underneath |
| HTML Structure | Guided Example | 8 min | Build a semantic profile page |
| CSS Essentials | Concept | 6 min | Step-by-step CSS transformation |
| CSS Essentials | Guided Example | 10 min | Style profile page with Flexbox cards |
| JavaScript Basics | Concept | 7 min | JS vs Python, DOM manipulation demo |
| JavaScript Basics | Guided Example | 10 min | Dark mode, counter, dynamic list |
| Fetch API | Concept | 7 min | Live API calls, response.ok gotcha |
| Fetch API | Guided Example | 10 min | Fetch posts with loading/error states |
| Connecting FE to BE | Concept | 6 min | CORS explained + full chain diagram |
| Connecting FE to BE | Guided Example | 12 min | Mini API + HTML frontend |
| What is Streamlit? | Concept | 5 min | Same app in HTML vs Streamlit |
| What is Streamlit? | Guided Example | 10 min | Execution demo with live timestamp |
| Layout & Components | Concept | 6 min | Dashboard layout transformation |
| Layout & Components | Guided Example | 10 min | Full dashboard with sidebar/tabs |
| State Management | Concept | 7 min | Counter bug + session state fix |
| State Management | Guided Example | 10 min | Notes app with tags/delete |
| Data Display | Concept | 7 min | DataFrames, charts, metrics, caching |
| Data Display | Guided Example | 10 min | Product data explorer |
| Streamlit + FastAPI | Concept | 8 min | Auth gate + error handling |
| Streamlit + FastAPI | Guided Example | 12 min | Full login + task management |
| AI Interface | Concept | 8 min | Chat components + streaming |
| AI Interface | Guided Example | 12 min | Full AI chat with mock fallback |