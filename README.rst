Json Schema Generator
====================
.. image:: https://img.shields.io/pypi/v/jsonschemagenerator
        :alt: Release Status

Installation
======================

.. code:: bash

    $ pip install jsonschemagenerator


Usage
======================

.. code:: python

    $ # use the path of the directory already within your project
    $ from json_schema_converter.generate_schema import generate_json_schema
    $ schema = generate_json_schema("/pytests/schemas/teste.json")