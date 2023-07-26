Json Schema Generator
=====================

Installation
============

To install the Json Schema Generator, use pip:

.. code-block:: bash

    pip install generate-json-schema

Usage
=====

To use the Json Schema Generator, import the module and utilize the function `generate_json_schema`:

.. code-block:: python

    # Use the path of the directory already within your project
    from json_schema_converter.generate_schema import generate_json_schema
    schema = generate_json_schema("/pytests/schemas/teste.json")