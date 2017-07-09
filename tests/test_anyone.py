"""Unit tests for anyone."""

import pytest
from anyone import anyone


@pytest.fixture
def response():
    """Test fixture."""
    import requests
    return requests.get('https://github.com/herereadthis/anyone.git')


def test_author():
    """Test getting author."""
    poem = anyone.Poem()
    assert poem.author == poem.get_author()


def test_publication():
    """Test getting publication."""
    poem = anyone.Poem()
    assert poem.publication == poem.get_publication()


def test_title():
    """Test getting title."""
    poem = anyone.Poem()
    assert poem.title == poem.get_title()


def test_verse():
    """Test getting specific verse."""
    poem = anyone.Poem()
    assert poem.get_verse() == poem.verses[0]
    assert poem.get_verse(1) == poem.verses[1]
    assert poem.publication == poem.get_publication()
