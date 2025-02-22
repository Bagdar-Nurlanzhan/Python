# бас әріптерден бұрын бос орын қосу
import re
text = input()
print(re.sub(r'(?<!^)(?=[A-Z])', ' ' ,text))