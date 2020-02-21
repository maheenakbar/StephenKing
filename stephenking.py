import unittest
import requests
import re
import urllib
from bs4 import BeautifulSoup
import pandas as pd

website_url = "https://en.wikipedia.org/wiki/Stephen_King_bibliography"
req = urllib.request.urlopen(website_url)
soup = BeautifulSoup(req, "html.parser")

tables = soup.findAll('table', {'class': 'wikitable sortable'})
href_tags = soup.findAll(href=True)

list_names = list()
for tags in href_tags:
	list_names.append(tags.find('title'))

print (list_names)
	