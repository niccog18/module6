import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name):
    """Fetch and display information about a Pokémon."""

    response = requests.get(f"{BASE_URL}{name}")

    if response.status_code == 200:
        data = response.json()

        pokemon_name = data["name"].title()
        height = data["height"]
        weight = data["weight"]
        types = [pokemon["type"]["name"].title() for pokemon in data["types"]]

        print("-" * 40)
        print(f"Name: {pokemon_name}")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print(f"Types: {', '.join(types)}")

    elif response.status_code == 404:
        print("-" * 40)
        print(f"Error: Pokémon '{name}' was not found (Status 404). Please check your spelling.")
    else:
        print("-" * 40)
        print(f"Request failed with status code {response.status_code}.")


pokemon_list = [
    "pikachu",
    "charizard",
    "bulbasaur",
    "pikacu",  # Intentional misspelling to test 404 handling
]

for pokemon in pokemon_list:
    get_pokemon(pokemon)