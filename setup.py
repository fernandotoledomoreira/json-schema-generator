# setup.py - Packaging configuration for jsonschemagenerator
#
# Copyright (C) 2023 Your Name <fernandotoledomoreira@gmail.com>

import os
from setuptools import setup

# Library Information
NAME = 'jsonschemagenerator'
VERSION = '0.1.0'
DESCRIPTION = 'A Python library for generating JSON schemas from JSON data.'
AUTHOR = 'Fernando Toledo Moreira'
AUTHOR_EMAIL = 'fernandotoledomoreira@gmail.com'
URL = 'https://github.com/fernandotoledomoreira/json-schema-generator'

# Minimum Python version required for the library
PYTHON_REQUIRES = '>=3.6'

# Read the README.rst file to use as long description
def get_readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Configuration of the package using setuptools' setup()
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=get_readme('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=["json_schema_converter"],   # List of packages for the project
    package_dir={"json_schema_converter": "src"},   # Directories of the packages
    classifiers=[   # Classifications for the library
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='json schema generator development',   # Keywords related to the library
    python_requires=PYTHON_REQUIRES,   # Minimum required Python version
)