# frequent words used inside the web site

import urllib.request
from bs4 import BeautifulSoup
import csv
import re
import nltk
from nltk.corpus import stopwords

# specify the url
# static web page
urlpage =  'https://www.tutorialspoint.com/python/python_basic_syntax.htm'
print(urlpage)

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# all texts
text = soup.get_text()

# strip text
text = soup.get_text(strip = True)

# remove non alphanumerics
text = re.sub('[^A-Za-z0-9]+', ' ', text)

# lowercase all text
text = text.lower()

# tokenize the text
tokens = [t for t in text.split()]

# remove stopwords in English and calculate the frequecy of text
# first 20 frequent words
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':-------->' + str(val))
freq.plot(20, cumulative=False)
