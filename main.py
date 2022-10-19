from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import re
import nltk

# working url
url = "https://www.w3.org/DesignIssues/TimBook-old/History.html"
# load site code
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
# get text from html
text = bs.getText()
# clear text
# get text tokens
tokens = nltk.word_tokenize(text)
# pos tokens
tagged = nltk.pos_tag(tokens)
print(tagged)
# get list of tags
tags_list = []
for tag in tagged:
    raw_tag = tag[1]
    # get first letter of tag type
    tags_list.append(raw_tag[0])
# print result(using counter to count tags usage)
print(Counter(tags_list))