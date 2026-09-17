import threading
from datetime import datetime

class Logger:
    __instance = None           # private — no instance created yet
    __lock = threading.Lock()   
    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
        return cls.__instance

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{timestamp} | {message}")


user_logger = Logger()
payment_logger = Logger()

print(user_logger is payment_logger)     # True

payment_logger.log("Payment failed")
user_logger.log("User login successful")