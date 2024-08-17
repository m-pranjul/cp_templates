import time
from plyer import notification

# hour = int(input("Optional message to Display: "))

Title = input("Enter Reminder name: ")
try:
    Message = input("Enter Message With Reminder: ")
except:
    Message = None

# while True:
#     time.sleep(hour)
notification.notify(title = Title, message = Message, timeout = 2)


    