from urllib.request import urlopen
from bs4 import BeautifulSoup
import nltk
import csv
nltk.download('averaged_perceptron_tagger')
# working url
url = "https://www.w3.org/DesignIssues/TimBook-old/History.html"
# load site code
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
# get text from html
text = bs.getText()
# get text tokens
tokens = nltk.word_tokenize(text)
# pos tokens
tagged = nltk.pos_tag(tokens)
print(tagged)