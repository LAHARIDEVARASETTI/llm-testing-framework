import json

def load_dataset(path):

    with open(path, "r") as file:
        data = json.load(file)

    return data