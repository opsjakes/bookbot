import os

def sort_on(dict):
    return

def get_file():
    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "books/frankenstein.txt")
        with open(filename) as file:
            text = file.read()
            data = text.split()
            return data
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found") from e
    # Add an indented block of code here if needed

def count_characters(data):
    test = {}
    lonSen = ''.join(data).lower()
    new = set(lonSen)
    for char in new:
        test[char] = lonSen.count(char)
    return test


test = count_characters(get_file())
