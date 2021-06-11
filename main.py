from bs4 import BeautifulSoup
import requests
import time

# Printing Test Start
# import string
# import random

# print("crypto")

# print(random.sample(string.ascii_letters, 10))
# Printing Test End

# BS4 TEST START
# with open("index.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

# soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

# print(BeautifulSoup(
#     "<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))
# BS4 TEST END

# Beautiful Soup Test
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# Get the URLS's
# etherium = 'http://google.com/search?q=etherium+price'
# url = 'http://google.com/search?q=bitcoin+' + coin + 'price'
url = 'http://google.com/search?q=bitcoin+price'

# Make  a request
HTML = requests.get(url)

# Parse!
soup = BeautifulSoup(HTML.text, 'html.parser')

# Print
print(soup.prettify())
