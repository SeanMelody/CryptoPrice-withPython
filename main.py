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


def get_crypto_price(coin):

    # Get the URLS's
    # etherium = 'http://google.com/search?q=etherium+price'
    # url = 'http://google.com/search?q=bitcoin+' + coin + 'price'
    url = 'https://coinmarketcap.com/currencies/' + coin

    # Make  a request
    HTML = requests.get(url)

    #   Parse!
    soup = BeautifulSoup(HTML.text, 'html.parser')

    # Print
    # print(soup.prettify())

    # Find the current price
    text = soup.find('div', attrs={'class': 'priceValue___11gHJ'}).text

    # print(text)

    return text


# get the pice with a function
# price = get_crypto_price('bitcoin')
# print(price + ' US Dollars')

users_coin = input("Which coin price would you like?: ")
print_price = get_crypto_price(users_coin)
print(print_price)
# Create Function to show the price when it changes


def loop():
    last_price = -1
    # Loop to continulously show the price
    # while True:
    # pick a coin:
