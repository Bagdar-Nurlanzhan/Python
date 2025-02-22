# жолды бас әріптерден бөлу
import re
text = input()
print(' '.join(re.findall(r'[A-Z][a-z]*', text)))