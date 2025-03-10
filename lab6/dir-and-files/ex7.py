import shutil
import os

def copy_file(src, dest):
    if not os.path.exists(src):
        print(f"Ошибка: Файл '{src}' не существует.")
        return
    shutil.copy(src, dest)
    print(f"Файл '{src}' скопирован в '{dest}'")

# Пример вызова
copy_file("example.txt", "example_copy.txt")
