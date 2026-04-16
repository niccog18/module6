# Connecting Frontend to Backend — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** Why does the browser block `fetch()` requests from `http://localhost:8501` to `http://localhost:8000`?

- A) Because they use different port numbers, making them different origins, and the browser’s Same-Origin Policy blocks cross-origin requests by default
- B) Because [localhost](http://localhost) can only run one server at a time
- C) Because fetch() doesn’t work with [localhost](http://localhost) URLs
- D) Because FastAPI doesn’t accept requests from browsers

> **Answer: A** — An "origin" is defined by protocol + domain + port. Even though both servers are on [localhost](http://localhost), different ports (8501 vs 8000) make them different origins. The browser’s Same-Origin Policy blocks JavaScript from making cross-origin requests unless the target server explicitly allows it via CORS headers. This is a security feature, not a bug. The fix is adding `CORSMiddleware` to your FastAPI app.
> 

---

**Question 2:** Your FastAPI endpoint expects a JSON body with a `title` field, but your frontend sends `{"name": "Test"}`. What status code does FastAPI return?

- A) 200 — it ignores the wrong field
- B) 404 — endpoint not found
- C) 422 — Unprocessable Entity (validation error)
- D) 500 — Server crashed

> **Answer: C** — FastAPI uses Pydantic validation. When the request body doesn’t match the expected schema (missing required `title` field, unexpected `name` field), Pydantic rejects it and FastAPI returns a 422 with a detailed error message explaining what’s wrong. This is one of FastAPI’s strengths — automatic validation with clear error messages.
> 

---

**Question 3:** Your frontend shows a "Could not connect to the server" error. Which of these should you check FIRST?

- A) Whether the CSS is correct
- B) Whether the API server is actually running and the URL in your fetch() is correct
- C) Whether the HTML is valid
- D) Whether the browser supports fetch()

> **Answer: B** — The most common cause of connection errors is that the server isn’t running or the URL is wrong. Check: Is `uvicorn` running? Is the port correct? Can you access `http://localhost:8000/docs` directly in the browser? Start with the simplest possible cause before investigating anything more complex. CSS and HTML issues (A, C) would not cause connection errors, and all modern browsers support fetch (D).
>