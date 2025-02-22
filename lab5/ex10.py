# Преобразовать CamelCase в snake_case
import re
text = input()
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower())