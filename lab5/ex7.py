# Преобразовать snake_case в CamelCase
import re
text = input()
print(''.join(word.capitalize() for word in text.split('_')))