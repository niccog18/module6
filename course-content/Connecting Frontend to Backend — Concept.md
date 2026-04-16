# Connecting Frontend to Backend — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what CORS is, why it exists, and how to configure it in FastAPI
2. Describe the full communication chain from browser to database and back
3. Send authenticated requests with authorization headers using fetch
4. Implement error handling patterns for frontend-to-backend communication

---

`[VIDEO PLACEHOLDER: 6 min — "CORS explained simply: what happens when your browser blocks a request, why the error is so confusing, and the one-line FastAPI fix. Then show the full browser → FastAPI → DB chain."]`

You’ve built an API backend (Module 5). You’ve learned how to make HTTP requests from the browser (Lesson 5). Now it’s time to connect them. This is the moment where the frontend meets the backend, and it comes with a surprise that trips up almost every developer the first time.

Imagine you have two buildings next to each other. Building A is your frontend (an HTML page). Building B is your FastAPI server. You’d think they could just talk to each other freely — they’re right next to each other, after all.

But there’s a security guard between them. This guard has a strict policy: "Unless Building B explicitly says it’s okay, Building A is not allowed to request anything from it." This security guard is called **CORS**.

---

## CORS: The Security Guard You Didn’t Know About

**CORS** stands for **Cross-Origin Resource Sharing**. An "origin" is the combination of protocol + domain + port. So `http://localhost:8501` (where Streamlit runs) and `http://localhost:8000` (where FastAPI runs) are *different origins* — even though they’re on the same computer.

Browsers enforce the **Same-Origin Policy**: JavaScript on one origin cannot make requests to a different origin unless the target server explicitly permits it. This is a security feature that prevents malicious websites from making requests to your bank’s API using your logged-in session.

Here’s what the error looks like when CORS blocks your request:

```
Access to fetch at 'http://localhost:8000/tasks' from origin 
'http://localhost:8501' has been blocked by CORS policy
```

The fix is simple: tell your FastAPI server to accept requests from your frontend’s origin.

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://localhost:5500"],  # Your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers (including Authorization)
)
```

In production, you’d replace `"*"` with specific methods and headers, and list only your actual frontend domains. For development, this permissive configuration is fine.

---

## The Full Communication Chain

Let’s trace what happens when a user clicks a button in your frontend that loads their tasks:

`[DIAGRAM PLACEHOLDER: Flow diagram showing: User clicks button → JavaScript sends fetch() with JWT in header → FastAPI receives request → Validates JWT → Queries SQLAlchemy/Database → Returns JSON response → JavaScript receives response → Updates DOM to display tasks]`

1. User clicks "Load Tasks" in the browser
2. JavaScript sends a `fetch()` GET request to `http://localhost:8000/tasks` with an `Authorization: Bearer <token>` header
3. FastAPI’s CORS middleware checks if the request’s origin is allowed
4. FastAPI validates the JWT token in the Authorization header
5. The endpoint function queries the database via SQLAlchemy
6. FastAPI returns a JSON response with the tasks
7. JavaScript receives the response, checks `response.ok`, parses the JSON
8. JavaScript updates the DOM to display the tasks

This is the exact same chain that will happen when you connect Streamlit to FastAPI in Week 2. The only difference is that Streamlit uses Python’s `requests` library instead of JavaScript’s `fetch()`.

---

## Sending Auth Headers with Fetch

In Module 5, you built JWT authentication. To call protected endpoints from the frontend, you include the token in a header:

```jsx
const response = await fetch("http://localhost:8000/tasks", {
    headers: {
        "Authorization": `Bearer ${token}`,  // JWT from login
        "Content-Type": "application/json"
    }
});
```

The pattern is always: **log in → get a token → send the token with every subsequent request**.

If the token is expired or invalid, you’ll get a 401 (Unauthorized) response. Your frontend should handle this gracefully — typically by redirecting the user to a login form.

---

## Error Handling Patterns for Frontend-Backend Communication

Three types of errors can happen when your frontend talks to your backend:

**Network errors** — The server is unreachable (not running, wrong URL, network down). `fetch()` throws a real exception for these.

**HTTP errors** — The server responded, but with an error status (401 Unauthorized, 404 Not Found, 422 Validation Error, 500 Server Error). `fetch()` does NOT throw — you must check `response.ok`.

**Application errors** — The server returned 200, but the data isn’t what you expected (empty list, missing fields, unexpected format).

A robust error-handling pattern covers all three:

```jsx
async function fetchTasks(token) {
    try {
        const response = await fetch("http://localhost:8000/tasks", {
            headers: { "Authorization": `Bearer ${token}` }
        });

        if (response.status === 401) {
            // Token expired or invalid — redirect to login
            showLoginForm();
            return;
        }

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const tasks = await response.json();
        displayTasks(tasks);  // Update the DOM

    } catch (error) {
        // Network failure OR our thrown error
        showError("Could not connect to the server. Is it running?");
    }
}
```

Note the special handling for 401 — a 422 from FastAPI typically means Pydantic validation failed (you sent data in the wrong format). Your frontend should show a clear message, not a cryptic error.

---

## Looking Ahead: Streamlit Simplifies This

In Week 2, Streamlit replaces the JavaScript `fetch()` with Python’s `requests` library. The CORS concepts remain the same. The error handling patterns remain the same. The authentication flow remains the same. What changes is the language and the fact that Streamlit handles the DOM updates for you automatically.

That’s the payoff of this week: you now *understand the web*. Streamlit is about to make it much easier to *work with it*.