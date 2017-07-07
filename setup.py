from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.srt'), encoding='utf-8') as f:
#    long_description = f.read()

with open('README.srt') as readme_data:
    readme = readme_data.read()


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
    version='0.1.8',

    description='anyone lived in a pretty how town - the poem',
    long_description=readme,
    
    url='https://github.com/herereadthis/anyone',

    # Author details
    author='herereadthis',
    author_email='herereadthis@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
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
