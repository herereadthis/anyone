# Anyone

[![Build Status](https://travis-ci.org/herereadthis/anyone.svg?branch=master)](https://travis-ci.org/herereadthis/anyone)
[![PyPI version](https://badge.fury.io/py/anyone.svg)](https://badge.fury.io/py/anyone)

Anyone is a very simple Python Package which parses the poem, 'anyone lived in a pretty how town' by E. E. Cummings.

```bash
# Installation
sudo pip3 install anyone

# Run the package in terminal
anyone

# unit test
git clone https://github.com/herereadthis/anyone.git
cd anyone
sudo pip3 install pytest
pytest
```

## API

```python
from anyone import anyone

# new instance
poem = anyone.Poem()

# author
poem.author
poem.get_author()

# title
poem.title
poem.get_title()

# publication
poem.publication
poem.get_publication()

# get verse
poem.get_verse(2)

# get line
poem.get_line(25)
```


## About Python Packages

The real purpose of this package is build some solid Python foundations for future work.

So, it turns out nearly all of the documentation on building your own python package is either out of date or conflicting. Even the documentation on the [official Python documentation](https://packaging.python.org/tutorials/distributing-packages/) is wrong at times. There's also spotty documentation for the TestPyPi sandbox that is out of date too.

Anyway, I guess the best thing to do for now is to use this package as a starting template.

You must create an account. There are actually two pypi pages; I'm not really sure which i the definitive source of truth, though doing anything to one site will affect the other.

- [pypi.io](https://pypi.io)
- [pypi.python.org](https://pypi.python.org/pypi)

You must create a `.pypirc` file

```bash
cd ~
touch .pypirc

# copy + paste the following:
# change your username and password to pyp credentials
[distutils]
index-servers=
    pypi

[pypi]
username = myusername
password = mypassword
```

Once you made a template package like anyone, you must install `twine`, which is the service to upload packages

```bash
pip install twine
```

Then try to build your distribution. It might work.

```bash
# be sure to be in your package directory at its root
python setup.py sdist
```

Now cross your fingers and hopefully the rest will work

```bash
# upload
twine upload dist/*

# moment of truth
pip install mypackgename
```
