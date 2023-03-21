import time
import schedule
from SendMessage import SendMessage


schedule.every().day.at("07:00").do(SendMessage().send_message)
while True:
    schedule.run_pending()
    time.sleep(1)
