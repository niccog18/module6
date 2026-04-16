# Fetch API & Async/Await — Guided Example

**Module 6 — Web Essentials & Streamlit**

`[VIDEO PLACEHOLDER: 10 min — "Build fetch_demo.html: fetch posts from JSONPlaceholder, display as cards with loading states, navigate between posts with a Next button. Show the try/catch/finally pattern live."]`

Let’s build a page that fetches data from an API and displays it dynamically. We’ll include loading states and error handling — the patterns every real application uses.

Create a file called `fetch_demo.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch API Demo</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 40px auto; padding: 0 20px; }
        .card { background: white; border: 1px solid #ddd; border-radius: 8px; padding: 24px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card h3 { margin-top: 0; color: #1a1a2e; }
        .loading { color: #888; font-style: italic; }
        .error { color: #e74c3c; font-weight: bold; }
        button { padding: 10px 20px; font-size: 1rem; cursor: pointer; margin-right: 8px; }
        #status { margin: 10px 0; font-size: 0.9rem; color: #666; }
    </style>
</head>
<body>
    <h1>Fetch API Demo</h1>
    <p id="status">Ready</p>
    <button id="load-btn">Load Post</button>
    <button id="next-btn">Next Post</button>
    <div id="content"></div>

    <script>
    // Track which post we're viewing (JSONPlaceholder has posts 1-100)
    let currentPostId = 1;

    // References to DOM elements we'll update
    const content = document.querySelector("#content");
    const status = document.querySelector("#status");
    const loadBtn = document.querySelector("#load-btn");
    const nextBtn = document.querySelector("#next-btn");

    async function loadPost(id) {
        // Show loading state
        content.innerHTML = '<p class="loading">Loading...</p>';
        status.textContent = `Fetching post ${id}...`;

        try {
            const response = await fetch(
                `https://jsonplaceholder.typicode.com/posts/${id}`
            );

            // CRITICAL: Check response.ok before parsing
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }

            const post = await response.json();

            // Build the card HTML using template literals
            content.innerHTML = `
                <div class="card">
                    <h3>Post #${post.id}: ${post.title}</h3>
                    <p>${post.body}</p>
                    <small>Author ID: ${post.userId}</small>
                </div>
            `;
            status.textContent = `Loaded post ${id} successfully`;

        } catch (error) {
            // Catches both network errors AND the error we throw on bad status
            content.innerHTML = `<p class="error">Failed to load: ${error.message}</p>`;
            status.textContent = "Error occurred";

        } finally {
            // Always runs — good place for cleanup
            console.log(`Fetch attempt for post ${id} complete.`);
        }
    }

    // Load the current post when clicking "Load Post"
    loadBtn.addEventListener("click", () => {
        loadPost(currentPostId);
    });

    // Move to next post and load it
    nextBtn.addEventListener("click", () => {
        currentPostId += 1;
        if (currentPostId > 100) currentPostId = 1;  // Loop back to start
        loadPost(currentPostId);
    });

    // Load the first post automatically when the page opens
    loadPost(1);
    </script>
</body>
</html>
```

Save and open in your browser.

---

## What You Should See

1. The page loads and immediately shows Post #1 in a styled card
2. Click "Next Post" — you briefly see "Loading..." then Post #2 appears
3. Keep clicking to browse through posts
4. The status bar shows the current state of each request

---

## Testing Error Handling

To test the error path, temporarily change the URL in the `loadPost` function to an invalid endpoint:

```jsx
// Change this line temporarily:
const response = await fetch(`https://jsonplaceholder.typicode.com/nonexistent/${id}`);
```

Refresh the page. You should see the red error message instead of a card. Change the URL back when you’re done.

---

## Key Patterns to Notice

**Loading state** — We show "Loading..." immediately before the request starts. This gives the user visual feedback that something is happening.

**`response.ok` check** — We throw an error if the status code indicates failure. Without this, a 404 response would silently try to parse an error page as JSON and produce confusing results.

**`try/catch/finally`** — The `catch` block handles both network failures and our manually thrown errors. The `finally` block runs regardless of outcome.

**Template literals** — We use backtick strings with `${variable}` to build HTML dynamically. This is JavaScript’s equivalent of Python’s f-strings.

These same patterns — loading states, error handling, dynamic DOM updates — appear in every web application, including the Streamlit apps you’ll build in Week 2.