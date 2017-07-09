"""Setup Anyone package."""

from setuptools import setup, find_packages
# from codecs import open
# from os import path

# with open('README.srt', encoding='utf-8') as readme_rst:
#     long_description = readme_rst.read()

requirements = []

setup_requirements = [
    'pytest-runner'
]

test_requirements = [
    'pytest'
]

setup(
    name='anyone',

    # Version
    version='0.1.13',

    description='anyone lived in a pretty how town - the poem',
    long_description="""\
Anyone is a very simple Python Package which parses the poem, 'anyone lived in
a pretty how town' by E. E. Cummings.

The real purpose of this package is build some solid Python foundations for
future work.

Read the API and see a tutorial on Python packages on Github at
`herereadthis/anyone.git`_

Anyone requires Python 3.

.. _`herereadthis/anyone.git`: https://github.com/herereadthis/anyone.git
""",
    url='https://github.com/herereadthis/anyone',

    # Author details
    author='herereadthis',
    author_email='herereadthis@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='sample development poem',
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('/', ['anyone/data.json'])
    ],
    entry_points={
        'console_scripts': [
            'anyone=anyone:main'
        ]
    },
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    zip_safe=False
)
