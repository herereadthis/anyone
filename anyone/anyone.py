"""Create the Poem class."""

import json
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'data.json')) as json_data:
    data = json.load(json_data)


class Poem:
    """Make Poem class."""

    def __init__(self):
        """Initialize stuff."""
        self.title = data['title']
        self.author = data['author']
        self.publication = data['publication']
        self.verses = data['verses']

    def get_author(self):
        """Very redundant. You can do instance.author. It's just a demo."""
        return self.author

    def get_publication(self):
        """Very redundant. You can do instance.publication."""
        return self.publication

    def get_title(self):
        """Very redundant. You can do instance.title."""
        return self.title

    def get_verse(self, v=0):
        """Get a specific verse."""
        verse_count = len(self.verses)
        if v < verse_count:
            return self.verses[v]

    def get_line_in_verse(self, v=0, l=0):
        """Return a specific line from a specific verse."""
        return 123

    def print_poem(self):
        """Print all the verses."""
        for index, verse in enumerate(self.verses):
            for line in verse:
                print(line)
            if index != len(self.verses) - 1:
                print('')
