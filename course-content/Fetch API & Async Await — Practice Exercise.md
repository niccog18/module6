# Fetch API & Async/Await — Practice Exercise

## API-Powered Live Search

**Objective:** Build a search interface that fetches data from an API and filters it in real time as the user types — combining `fetch()`, DOM manipulation, and the `input` event.

**Time:** 25 minutes

**What you’ll build:**

A single HTML file (`live_search.html`) that loads user data from JSONPlaceholder and lets users search through it interactively.

**Requirements:**

1. When the page loads, fetch all users from `https://jsonplaceholder.typicode.com/users` (this returns 10 user objects)
2. Display all users as cards showing: name, email, company name (found in `user.company.name`)
3. Add a search input at the top of the page
4. As the user types in the search box, **filter the displayed cards in real time** — matching against both name and email (case-insensitive)
5. Show a **result count** below the search box: "Showing 3 of 10 users"
6. Handle the loading state: show "Loading users..." while the fetch is in progress
7. Handle errors: show an error message if the fetch fails

**Deliverable:** A working `live_search.html` file that loads user data, displays it as cards, and filters live as the user types.

**Hints:**

- Store the fetched users array in a variable so you can filter it without re-fetching
- Use the `.filter()` array method with `.toLowerCase()` for case-insensitive matching
- On each keystroke, clear the card container and re-render only the matching users
- Use `textContent` or `innerHTML` to rebuild the card list

**Why this exercise?** Live search is one of the most common UI patterns. Every dashboard, admin panel, and data explorer uses it. You’re combining fetch, DOM manipulation, and event handling in a realistic scenario.