# нижний пробел мен кіші әріптері бар сөздерді табу
import re
text = input()
pattern = r"\b[a-z]+_[a-z]+\b"
print(re.findall(pattern, text))