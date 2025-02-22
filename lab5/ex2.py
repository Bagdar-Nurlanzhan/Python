#а дан кейін 2 3 b
import re
text = input()
pattern = r"ab{2,3}$" 
print(bool(re.fullmatch(pattern, text)))