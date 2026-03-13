"""
L1 — API Explorer  (STARTER)
=============================
Your goal: use the `requests` library to fetch data from the PokeAPI and
print nicely formatted Pokémon info.

Key concepts you will use:
- requests.get(url)       : sends an HTTP GET request
- response.status_code    : the HTTP status code (200 = OK, 404 = Not Found)
- response.json()         : parses the JSON response body into a Python dict

Run this file when you are done:
    python solution.py

Steps to complete:
  1. Fill in fetch_pokemon() to call the PokeAPI.
  2. Print name, height, weight, and types.
  3. Handle a 404 status code gracefully (print an error, don't crash).
  4. In main(), call fetch_pokemon() for the three valid names AND for "pikacu"
     (the misspelling) to test your error handling.
"""

import requests

# ── Base URL ──────────────────────────────────────────────────────────────────
# Append a Pokémon name to this URL to build the full endpoint.
# Example: BASE_URL + "pikachu"  →  "https://pokeapi.co/api/v2/pokemon/pikachu"
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_pokemon(name: str) -> None:
    """Fetch and print details for a single Pokémon by name."""

    print(f"\n{'=' * 40}")
    print(f"  Fetching: {name}")
    print(f"{'=' * 40}")

    # TODO: Build the full URL by combining BASE_URL and the pokemon name
    url = None  # replace None

    # TODO: Send a GET request using requests.get()
    #       Store the result in a variable called `response`

    # TODO: Print the status code so you can see what the API returned

    # TODO: If the status code is 404, print an error message and return early
    #       (use `return` to exit the function without crashing)

    # TODO: If the status code is not 200, print a generic error and return

    # TODO: Parse the JSON response body with response.json()
    #       Store the result in `data`

    # TODO: Extract name, height, and weight from `data`
    # Hint: data["name"], data["height"], data["weight"]

    # TODO: Extract the list of type names
    # Hint: data["types"] is a list of dicts. Each dict has a "type" key,
    #       which is itself a dict with a "name" key.
    # Example structure: [{"slot": 1, "type": {"name": "electric", "url": "..."}}]
    types = []  # replace with a list comprehension

    # TODO: Print name, height (in metres), weight (in kg), and types
    # Height unit: decimetres (divide by 10 for metres)
    # Weight unit: hectograms  (divide by 10 for kg)


def main():
    print("=" * 40)
    print("  Pokémon API Explorer")
    print("=" * 40)

    # TODO: Call fetch_pokemon() for "pikachu", "charizard", and "bulbasaur"

    # TODO: Call fetch_pokemon("pikacu") to test your 404 error handling

    print("\nDone!\n")


if __name__ == "__main__":
    main()
