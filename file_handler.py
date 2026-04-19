import json
from typing import *

FILE_NAME="data.json"

def load_expense()->List[Dict]:
    """
    Loads expense data from JSON file
    Returns empty list [] if file doesn't exist
    """
    try:
        with open(FILE_NAME,'r') as file:
            data = json.load(file)
            return data

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []



def save_expense(expenses: List[Dict]) -> None:
    """
    Save expense data to JSON file
    """
    with open("FILE_NAME",'w') as file:
        json.dump(expenses, file)
