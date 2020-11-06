from os import path

from setuptools import find_packages, setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    install_requires=[
        'PyNaCl==1.4.0',
        'pycodestyle==2.6.0',
        'pytest-xdist==2.1.0',
        'pytest==6.1.2',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='thenewboston-python-client',
    packages=find_packages(
        exclude=['tests', 'tests.*']
    ),
    version='0.0.2',
)
