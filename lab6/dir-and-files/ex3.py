import os
def path_info(path):
    if os.path.exists(path):
        info = (os.path.basename(path), os.path.dirname(path))
        print(f"Файл: {info[0]}, Директория: {info[1]}")
        return info
    print(f"Путь '{path}' не существует")
    return None
