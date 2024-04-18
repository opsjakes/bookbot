import os

global_filename = 'books/frankenstein.txt'

def sort_on(dict_list):
    new_dict_list = []
    for i in sorted(dict_list,key=dict_list.get,reverse=True):
        if i.isalpha():
            new_dict = {
                "letter": i,
                "count": dict_list[i]
            }
            new_dict_list.append(new_dict)
    return new_dict_list

    

def get_file():
    try:
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, global_filename)
        with open(filename) as file:
            text = file.read()
            data = text.split()
            return data
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found") from e

def count_characters(data):
    dataDict = {}
    lonSen = ''.join(data).lower()
    new = set(lonSen)
    total_count_words = len(data)
    for char in new:
            dataDict[char] = lonSen.count(char)
    return dataDict,total_count_words

def print_report(dict_list,total_count_words):
    print(f'-- Begin report of ${global_filename} ---')
    print(f'{total_count_words} words found in the document\n')
    for dict in dict_list:
        print(f"The '{dict['letter']}' was found {dict['count']} times")
    print('--- End report ---')


count_char,total_count_words = count_characters(get_file())
print_report(sort_on(count_char),total_count_words)
    