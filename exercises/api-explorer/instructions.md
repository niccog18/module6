# API Explorer

**Module:** 6 — Web Essentials & Streamlit
**Estimated time:** 20 minutes

## Objective

Use the `requests` library to fetch data from a public REST API and display formatted results in the terminal.

## What You'll Build

A Python script that calls the PokeAPI to retrieve Pokemon data. You will implement a `fetch_pokemon()` function that sends GET requests, checks status codes, parses JSON responses, and prints each Pokemon's name, height, weight, and types. The script should handle 404 errors gracefully (e.g., a misspelled name like "pikacu") without crashing.

## Reference Code

The solution file (`solution.py`) is provided as a reference — try building it yourself first, then compare.

## Running

```bash
python solution.py
```

## Deliverable

A Python script that fetches and displays Pokemon info from the PokeAPI with proper error handling for invalid names.
