"""Unit tests for anyone."""

import pytest
import anyone


@pytest.fixture
def response():
    import requests
    return requests.get('https://github.com/herereadthis/anyone.git')

def func(x):
    return x + 1

def test_answer():
    bar = anyone.main()
    la = 'asdf'
    print(la)
    assert bar == 'bar'
    assert func(3) == 4

def test_content(response):
    assert func(3) == 4
