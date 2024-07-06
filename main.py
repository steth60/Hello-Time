import time
from datetime import datetime

last_minute = -1

while True:
    now = datetime.now()
    current_minute = now.minute
    
    if current_minute != last_minute:
        current_time = now.strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        last_minute = current_minute
    
    time.sleep(1)
