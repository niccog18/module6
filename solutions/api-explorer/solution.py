"""
L1 — API Explorer
=================
Demonstrates how to make HTTP requests using the `requests` library.

Key concepts covered:
- requests.get(url)          : sends an HTTP GET request to a URL
- response.status_code       : the HTTP status code (200 = OK, 404 = Not Found, etc.)
- response.json()            : parses the JSON body of a response into a Python dict/list
- Graceful error handling    : checking status before trying to use the data
"""

import requests

# ── Base URL for the PokeAPI ──────────────────────────────────────────────────
# The PokeAPI is a free, public REST API. No authentication required.
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def fetch_pokemon(name: str) -> None:
    """Fetch and print details for a single Pokémon by name."""

    print(f"\n{'=' * 40}")
    print(f"  Fetching: {name}")
    print(f"{'=' * 40}")

    # requests.get() sends an HTTP GET request.
    # The return value is a Response object containing status code, headers, and body.
    url = BASE_URL + name.lower()
    response = requests.get(url)

    # Every HTTP response includes a 3-digit status code:
    #   2xx = success   (200 OK, 201 Created, …)
    #   4xx = client error (400 Bad Request, 404 Not Found, …)
    #   5xx = server error
    print(f"  Status code: {response.status_code}")

    if response.status_code == 404:
        # Handle the "not found" case without crashing the program
        print(f"  ERROR: '{name}' was not found. Check the spelling!")
        return

    if response.status_code != 200:
        # Catch any other unexpected status codes
        print(f"  ERROR: Unexpected status code {response.status_code}")
        return

    # response.json() decodes the response body from JSON text into a Python dict.
    # This only works if the server returned valid JSON (it always does here).
    data = response.json()

    # Extract the fields we care about from the nested dictionary
    pokemon_name = data["name"].capitalize()
    height       = data["height"]        # in decimetres (divide by 10 for metres)
    weight       = data["weight"]        # in hectograms  (divide by 10 for kg)

    # "types" is a list of dicts; each has a nested "type" dict with a "name" key
    # Example structure: [{"slot": 1, "type": {"name": "electric", "url": "..."}}]
    types = [entry["type"]["name"].capitalize() for entry in data["types"]]

    print(f"  Name   : {pokemon_name}")
    print(f"  Height : {height / 10:.1f} m  ({height} decimetres)")
    print(f"  Weight : {weight / 10:.1f} kg ({weight} hectograms)")
    print(f"  Types  : {', '.join(types)}")


def main():
    print("=" * 40)
    print("  Pokémon API Explorer")
    print("=" * 40)

    # ── Fetch three valid Pokémon ─────────────────────────────────────────────
    for name in ["pikachu", "charizard", "bulbasaur"]:
        fetch_pokemon(name)

    # ── Demonstrate graceful 404 handling ────────────────────────────────────
    # "pikacu" is intentionally misspelled — the API will return a 404.
    fetch_pokemon("pikacu")

    print("\nDone!\n")


if __name__ == "__main__":
    main()
