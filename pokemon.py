#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(f"{pokeapi['name']} image- {pokeapi['sprites']['front_default']}")
    imgurl= pokeapi['sprites']['front_default']

    print(f"{pokeapi['name']} has appeared in {len(pokeapi['game_indices'])} games!")

    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1

    print('This pokemon has appeared in', game_indices, 'video games')

main()
