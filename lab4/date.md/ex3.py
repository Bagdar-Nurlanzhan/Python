# микросекундсыз уақытты көрсету
from datetime import datetime
now = datetime.now()
new_now = now.replace(hour=12)
print("date and time without microsecond:", new_now)