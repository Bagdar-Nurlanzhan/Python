import os
def generate_text_files():
    for letter in range(65, 91):
        with open(f"{chr(letter)}.txt", 'w') as f:
            f.write(f"This is file {chr(letter)}.txt")
    print("Созданы файлы A.txt - Z.txt")
