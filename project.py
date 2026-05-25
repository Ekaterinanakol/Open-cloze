import re

def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return words
