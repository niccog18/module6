# How the Web Works — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 8 min — "Browser DevTools Network Tab walkthrough + making HTTP requests with Python requests library. Show the request/response cycle live."]`

In this guided example, we'll do two things: peek behind the curtain using your browser's built-in developer tools, and then make HTTP requests with Python's `requests` library — a tool you'll use throughout this course.

---

## Part 1: Browser DevTools — Seeing the Web in Action

Every modern browser has developer tools built in. Let's use them to watch the request/response cycle happen in real time.

**Step 1: Open DevTools**

Open Google Chrome (or any Chromium-based browser). Navigate to any website — let's use `https://jsonplaceholder.typicode.com/` (a free test API you'll use throughout this module).

Now open DevTools:

- **Mac:** `Cmd + Option + I`
- **Windows/Linux:** `Ctrl + Shift + I`
- **Or:** Right-click anywhere on the page → "Inspect"

You should see a panel open on the right side (or bottom) of your browser.

**Step 2: Go to the Network Tab**

Click the **Network** tab at the top of DevTools. This tab shows every HTTP request your browser makes.

Now refresh the page (`Cmd + R` or `Ctrl + R`). You should see a list of requests appear — the HTML page itself, CSS files, JavaScript files, maybe some images. Each row is one HTTP request.

**Step 3: Inspect a Request**

Click on the very first request in the list (it should be the HTML document). You'll see several sub-tabs:

- **Headers** — Shows the request method (GET), the URL, status code (200), and all request/response headers
- **Preview** — Shows a rendered preview of the response
- **Response** — Shows the raw response body (the actual HTML)

This is the request/response cycle from the Concept lesson, happening right in front of you. Every website you visit triggers dozens or hundreds of these requests.

![image.png](How%20the%20Web%20Works%20%E2%80%94%20Guided%20Example/image.png)

---

## Part 2: Making HTTP Requests with Python

Now let's do the same thing from Python. You've already used the `requests` library in Module 4 — here we'll connect it to the web concepts you just learned.

Create a new file called `web_explorer.py`:

```python
import requests  # The HTTP library you installed in Module 4

# --- GET Request: Fetching data ---
# This is exactly what your browser does when you visit a URL
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# The status code tells us if the request succeeded
print(f"Status Code: {response.status_code}")  # Should print 200

# Response headers contain metadata about the response
print(f"Content-Type: {response.headers['Content-Type']}")

# The response body contains the actual data
data = response.json()  # Parse the JSON response into a Python dictionary
print(f"Post Title: {data['title']}")
print(f"Post Body: {data['body'][:80]}...")  # First 80 characters
```

Run it:

```bash
python web_explorer.py
```

You should see:

```
Status Code: 200
Content-Type: application/json; charset=utf-8
Post Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Post Body: quia et suscipit
suscipit recusandae consequuntur expedita et cum
reprehenderit...
```

That 200 status code means the server successfully returned the data. Now let's see what happens when things go wrong:

```python
# --- Handling Errors: What happens with bad requests ---

# Request a post that doesn't exist
response_404 = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
print(f"\nBad Post Status: {response_404.status_code}")  # 404 — Not Found

# Request a URL that doesn't exist at all
try:
    response_bad = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    print(f"Bad URL Status: {response_bad.status_code}")  # Still returns a status code
except requests.exceptions.ConnectionError:
    # This happens when the server can't be reached at all
    print("Could not connect to the server!")
```

You should see:

```
Bad Post Status: 404
Bad URL Status: 404
```

Now let's make a POST request — sending data *to* a server:

```python
# --- POST Request: Sending data ---
# This is what happens when you submit a form or create a new record
new_post = {
    "title": "My First Post from Python",
    "body": "This was sent using the requests library!",
    "userId": 1  # Required by this API
}

response_post = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # 'json=' automatically sets Content-Type header
)

print(f"\nPOST Status: {response_post.status_code}")  # 201 — Created
print(f"Created Post: {response_post.json()}")
```

You should see:

```
POST Status: 201
Created Post: {'title': 'My First Post from Python', 'body': 'This was sent using the requests library!', 'userId': 1, 'id': 101}
```

Notice the **201** status code — that's "Created," meaning the server successfully created a new resource. The response includes an `id` that the server assigned to our new post.

---

## Connecting It All Together

What you just did with Python is exactly what your browser does — but your browser also takes the response and renders it visually. When you build a Streamlit app later in this module, Streamlit will handle the rendering for you. Your job will be to make the right HTTP requests to the right endpoints and display the responses in a useful way.

The pattern is always the same: **build a request → send it → check the status → use the response**. That pattern works whether you're fetching a webpage, calling a REST API, or querying an AI model.