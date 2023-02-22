#!/usr/bin/env pyhton3
marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").lower()

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()

value = marvelchars[char_name.capitalize()][char_stat]

if char_stat == "real name":
    value = value.title()

print(f"{char_name.capitalize()}'s {char_stat} is: {value}")
