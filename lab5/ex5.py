# а басында б соңында
import re
text = input()
pattern = r"^a.*b$"
print(bool(re.fullmatch(pattern, text)))