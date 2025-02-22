# а дан кейін б тұра ма 
import re
text = input()
pattern = r"ab*"
print(bool(re.fullmatch(pattern, text)))