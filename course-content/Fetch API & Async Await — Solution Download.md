# Fetch API & Async/Await — Solution Download

**GitHub:** `module-06-web-streamlit/solutions/exercises/live-search/`

Compare your solution to the reference. Key things to check:

- Are you fetching users once on page load and storing them, rather than re-fetching on every keystroke?
- Is the search case-insensitive (using `.toLowerCase()` on both the search term and the user fields)?
- Does the result count update correctly as you type?
- Did you check `response.ok` before parsing the JSON?

Differences in card styling, layout, and variable names are fine. The core pattern should be: fetch once → store → filter on input → re-render.