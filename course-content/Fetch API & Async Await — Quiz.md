# Fetch API & Async/Await — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** Why does a `fetch()` call need TWO `await` keywords?

```jsx
const response = await fetch(url);    // First await
const data = await response.json();   // Second await
```

- A) The first `await` is optional; only the second one matters
- B) The first `await` waits for the server to respond; the second waits for the response body to be parsed into a JavaScript object
- C) One `await` is for GET requests and one is for POST requests
- D) It’s a JavaScript bug; you only need one `await`

> **Answer: B** — `fetch()` returns a Promise that resolves when the server sends back headers (the start of the response). But the response *body* (the actual data) arrives as a stream and needs to be parsed separately. `.json()` is also asynchronous because it needs to read and parse the entire body. Two separate asynchronous steps = two `await`s.
> 

---

**Question 2:** You fetch a URL that returns a 404 status. What happens?

- A) `fetch()` throws an error that your `catch` block handles
- B) `fetch()` succeeds normally — you must check `response.ok` yourself to detect the 404
- C) The browser shows a 404 error page automatically
- D) `fetch()` returns `null`

> **Answer: B** — This is the most important gotcha with `fetch()`. It only throws errors for *network failures* (server unreachable, DNS error). A 404 or 500 response is still a valid HTTP response from the server, so `fetch()` treats it as a success. You MUST check `response.ok` (which is `false` for 400+ status codes) to detect API errors. Forgetting this check is one of the most common web development bugs.
> 

---

**Question 3:** What does the `finally` block do in a `try/catch/finally` structure?

- A) It runs only if there was an error
- B) It runs only if there was no error
- C) It runs regardless of whether the `try` succeeded or the `catch` handled an error
- D) It replaces the `catch` block

> **Answer: C** — `finally` always runs, no matter what. If `try` succeeds: `finally` runs. If `catch` handles an error: `finally` still runs. This makes it perfect for cleanup tasks like hiding loading spinners, re-enabling buttons, or resetting state — things that should happen regardless of the outcome. It’s the JavaScript equivalent of Python’s `finally`.
> 

---

**Question 4:** What is the purpose of `JSON.stringify()` in a POST request?

```jsx
body: JSON.stringify({ title: "Hello", body: "World" })
```

- A) It encrypts the data for security
- B) It converts a JavaScript object into a JSON-formatted string that can be sent over HTTP
- C) It validates that the data is correct
- D) It compresses the data to make the request faster

> **Answer: B** — HTTP request bodies are sent as text. `JSON.stringify()` converts a JavaScript object (with key-value pairs) into a JSON string (`{"title":"Hello","body":"World"}`). This is the reverse of `response.json()`, which converts a JSON string back into a JavaScript object. The server (like your FastAPI backend) then parses this JSON string back into its native data structures.
>