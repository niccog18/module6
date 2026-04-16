# How the Web Works — Practice Exercise

## API Explorer

**Objective:** Practice making HTTP requests with Python and interpreting the responses — the same request/response cycle your browser uses every time you visit a website.

**Time:** 20 minutes

**What you'll do:**

1. Create a new file called `api_explorer.py`
2. Use the `requests` library to fetch data from the PokéAPI (`https://pokeapi.co/api/v2/`)
3. Fetch data for **3 different Pokémon** by name (e.g., `pikachu`, `charizard`, `bulbasaur`). The endpoint pattern is: `https://pokeapi.co/api/v2/pokemon/{name}`
4. For each Pokémon, extract and print:
    - Name
    - Height
    - Weight
    - Types (a Pokémon can have multiple types — look in the `types` field of the response)
5. Handle a **404 error gracefully**: also try fetching a Pokémon that doesn't exist (e.g., `"pikacu"` — a common misspelling). Your code should check the status code and print a helpful error message instead of crashing.

**Deliverable:** A working `api_explorer.py` file that fetches 3 Pokémon, displays their info in a clean format, and handles 404 errors without crashing.

**Expected output should look something like:**

```
--- pikachu ---
Height: 4
Weight: 60
Types: electric

--- charizard ---
Height: 17
Weight: 905
Types: fire, flying

--- bulbasaur ---
Height: 7
Weight: 69
Types: grass, poison

--- pikacu ---
Error: Pokémon 'pikacu' not found (Status 404). Check your spelling!
```

**Hints:**

- Use `response.status_code` to check if the request succeeded (200) before trying to parse the JSON
- The `types` field in the response is a list of dictionaries. Each one has a `type` key with a `name` inside it
- Use a loop or list to avoid repeating code for each Pokémon

**Why this exercise?** You're practicing the same request/response pattern that powers every web application. The PokéAPI is a real, well-documented API - and the skills transfer directly to calling FastAPI backends, AI model APIs, and any other HTTP service.