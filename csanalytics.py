# Python file to test batch scripts

##################################################
# Preliminary Actions
##################################################
# Logging
import time
import datetime
import csv
from logger import Logger
logger = Logger()
# Web Scraping
from bs4 import BeautifulSoup
from collections import Counter
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from ws_test import *
##################################################

logger.log("Starting program")
# Timestamp for date
real_time = time.time()
time_stamp = datetime.datetime.fromtimestamp(real_time).strftime("%Y-%m-%d")

# Load a list of the words in recent ArXiv titles on some topic machine learning
titles = []
raw_html = simple_get("https://arxiv.org/list/cs.LG/pastweek?show=1000")
html = BeautifulSoup(raw_html, 'html.parser')
for elem in html.select('div'):
    if 'class' in elem.attrs:
        if 'list-title' in elem['class']:
            titles += elem.contents[2].split()
titles = [title.lower() for title in titles]
word_counts = Counter(titles)

# Save to CSV
with open("data/ArXiv_MachineLearning_"+time_stamp+".csv","w") as f:
    for key in word_counts.keys():
        f.write("%s,%s\n"%(key,word_counts[key]))
    

