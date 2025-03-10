import os
def write_list_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines("\n".join(data))
    print(f"Список записан в файл '{file_path}'")

