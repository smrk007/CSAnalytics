# Logging functionalities
import time
import datetime

class Logger:
    def __init__ (self, log_path="csanalytics.log"):
        self.log_path = log_path
        self.log_file = open(log_path, "a")

    def __del__ (self):
        self.log_file.close()

    def log (self, message):
        real_time = time.time()
        time_stamp = datetime.datetime.fromtimestamp(real_time).strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(time_stamp+": "+message+"\n")
