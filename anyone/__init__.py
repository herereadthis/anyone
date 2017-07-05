"""Initiate stuff."""

import json
from pprint import pprint

json_data = open('./data.json')
data = json.load(json_data)


def poem():
    """Spit out the poem."""
    verses = data['verses']
    # Here is an example of enumerate, which helps to get index and value.
    # It is kind of like myArray.forEach((v, k) =>{}) in JavaScript
    for index, verse in enumerate(verses):
        for line in verse:
            print(line)
        if index != len(verses) - 1:
            print('')
