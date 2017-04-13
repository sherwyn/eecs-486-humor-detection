# coding: utf-8

import requests
import re
import os
import json
import csv
from sets import Set
from bs4 import BeautifulSoup

# with open('urls_sarcasm.txt') as f:
with open('urls_nonsarcasm.txt') as f:
    urls = f.readlines()
lines = [x.strip() for x in urls]

# csvname = 'goodreads_sarcasm.csv'
csvname = 'goodreads_nonsarcasm.csv'

with open(csvname, 'wb') as csvfile:

    csvwriter = csv.writer(csvfile)

    for l in lines:

        print l

        url = l
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html.parser')

        for div in soup.find_all('div', class_='quoteText'):

            quote = div.text.split(u'―')[0]

            if quote:
                csvwriter.writerow([quote.strip().encode('utf-8')])
