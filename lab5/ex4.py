# бір бас әріптерден кейін кіші әріптерді табу
import re
text = input()
pattern = r"[A-Z][a-z]+"
print(re.findall(pattern, text))