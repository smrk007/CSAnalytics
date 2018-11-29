# Python file to test batch scripts

##################################################
# Preliminary Actions
##################################################
# Logging
import time
import datetime
log_file = open("csanalytics.log","a")
##################################################

# Current timestamp
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

log_file.write(st+": File executed")
