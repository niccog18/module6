# API-Powered Live Search

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 30 minutes

## Objective

Build a live search interface that fetches data from a public API and filters results as the user types.

## What You'll Build

A single HTML page that fetches all users from JSONPlaceholder on load and displays them as cards showing each user's name, email, and city. A search input filters the user list by name or email on every keystroke using the `input` event. The page shows a result count ("Showing 3 of 10 users"), a loading state while fetching, and a friendly error message if the request fails. Key concepts include `async/await`, `response.ok`, `response.json()`, and `try/catch/finally`.

## Reference Code

The solution file (`live_search.html`) is provided as a reference — try building it yourself first, then compare.

## Running

Open `live_search.html` directly in your browser.

## Deliverable

A single HTML file with a live search UI that fetches users from an API and filters them in real time.
