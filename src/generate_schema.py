import json
import os

def generate_json_schema(json_path):
    """
    Generate a JSON schema by reading a JSON file from the specified path and inferring the data structure.

    Args:
        json_path (str): The path to the JSON file.

    Returns:
        dict: The JSON schema describing the data structure.
    """
    try:
        with open(f"{os.getcwd()}{json_path}") as file:
            json_data = json.load(file)
        schema = infer_schema(json_data)
        return schema
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

def infer_schema(data):
    """
    Infer the JSON schema from the provided data.

    Args:
        data: The data for which the schema needs to be inferred.

    Returns:
        dict: The JSON schema describing the data structure.
    """
    if isinstance(data, dict):
        # For dictionaries, infer the schema of each value recursively
        properties = {}
        required = []
        for key, value in data.items():
            properties[key] = infer_schema(value)
            required.append(key)
        
        return {"type": "object", "properties": properties, "required": required}
    elif isinstance(data, list):
        # For lists, infer the schema of each element recursively
        items = []
        for item in data:
            item_schema = infer_schema(item)
            items.append(item_schema)
        
        return {"type": "array", "items": items}
    elif isinstance(data, bool):
        # For booleans, return the corresponding JSON schema
        return {"type": "boolean"}
    elif isinstance(data, int):
        # For integers, return the corresponding JSON schema
        return {"type": "integer"}
    elif isinstance(data, float):
        # For floats, return the corresponding JSON schema
        return {"type": "number"}
    elif isinstance(data, str):
        # For strings, return the corresponding JSON schema
        return {"type": "string"}
    else:
        # For other data types, assume null
        return {"type": "null"}