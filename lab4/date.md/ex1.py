# 5 күн бұрынғы күнді есептеу
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date + timedelta(minutes=5)
print("date 5 days ago:", new_date.date())