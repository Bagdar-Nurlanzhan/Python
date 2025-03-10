import os
def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = sum(1 for _ in f)
    print(f"Файл '{file_path}' содержит {result} строк.")
    return result
