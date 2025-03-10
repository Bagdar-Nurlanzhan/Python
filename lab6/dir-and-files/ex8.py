import os

def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"Файл '{path}' удалён")
        except PermissionError:
            print(f"Ошибка: Нет прав на удаление '{path}'")
        except Exception as e:
            print(f"Ошибка при удалении '{path}': {e}")
    else:
        print(f"Ошибка: Файл '{path}' не существует")

# Пример вызова
delete_file("example_copy.txt")
