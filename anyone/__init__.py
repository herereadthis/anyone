"""Initiate stuff."""

import json
from os import path
from pprint import pprint

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'data.json')) as json_data:
    data = json.load(json_data)


def main():
    """Spit out the poem."""
    verses = data['verses']
    # Here is an example of enumerate, which helps to get index and value.
    # It is kind of like myArray.forEach((v, k) =>{}) in JavaScript
    for index, verse in enumerate(verses):
        for line in verse:
            print(line)
        if index != len(verses) - 1:
            print('')
