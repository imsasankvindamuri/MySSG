from typing import *
import pathlib
import json

def unpack_json(path: pathlib.Path) -> Dict:
    if not f"{path}".endswith(".json"):
        raise Exception(f"{path} is not a JSON file")
    
    with open(path,"r") as file:
        data = json.load(file)
    
    return data

if __name__ == "__main__":
    pass