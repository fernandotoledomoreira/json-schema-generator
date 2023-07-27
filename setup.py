# setup.py - Packaging configuration for jsonschemagenerator
#
# Copyright (C) 2023 Your Name <fernandotoledomoreira@gmail.com>

import os
from setuptools import setup
import requests

# Library Information
NAME = 'generate-json-schema'
AUTHOR = 'Fernando Toledo Moreira'
AUTHOR_EMAIL = 'fernandotoledomoreira@gmail.com'
URL = 'https://github.com/fernandotoledomoreira/json-schema-generator'

# Minimum Python version required for the library
PYTHON_REQUIRES = '>=3.6'

# Get Tag from GitHub
def get_latest_version():
    try:
        url = 'https://api.github.com/repos/fernandotoledomoreira/json-schema-generator/releases/latest'
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta foi bem-sucedida
        data = response.json()
        return data['tag_name']
    except Exception as e:
        print(f"Erro ao obter a versão do GitHub: {e}")
        return VERSION

VERSION = get_latest_version()

# Read the README.rst file to use as long description
try:
    f = open("README.rst")
    readme = f.read()
    f.close()
except Exception:
    print("failed to read readme: ignoring...")
    readme = __doc__

# Configuration of the package using setuptools' setup()
setup(
    name=NAME,
    version=VERSION,
    description="Json Schema Generator",
    long_description="\n".join(readme.split("\n")[2:]).lstrip(),
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
