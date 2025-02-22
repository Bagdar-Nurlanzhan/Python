# Бос орын, , немесе . таңбасын : таңбасына ауыстыру
import re
text = input()
pattern = r"[ ,.]"
print(re.sub(pattern, ":", text))