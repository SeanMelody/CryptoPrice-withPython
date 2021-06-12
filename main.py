from bs4 import BeautifulSoup
import inquirer
import requests
import time
# Import all the requirements

# Function to get the user selected coin price


def get_crypto_price(user_selected):

    # Inquirer returns a dictionary, so must get the value to search it
    coin = user_selected['crypto']
    # Set up the print so that the user knows that it is working, and will have more inforation on what is diplayed.
    print('One ' + coin + ' costs:')

# Get the Url to seach using Beautiful Soup and the selected coin
    url = 'https://coinmarketcap.com/currencies/' + coin

# Make the request
    HTML = requests.get(url)

# Parse the data with Beautiful soup, using the html parser
    soup = BeautifulSoup(HTML.text, 'html.parser')


# Get the price from the webpage, that is located in the <div class="priceValue___11gHJ">
    price = soup.find('div', attrs={'class': 'priceValue___11gHJ'}).text

 # Return the price
    return price


crypto_options = [inquirer.List('crypto',
                                message="What coin price would you like to check?: ",
                                choices=['Bitcoin', 'Ethereum', 'Tether', 'Cardano', 'Dogecoin',
                                         'XRP', 'Polkadot', 'Uniswap', 'Litecoin', 'Solana', 'Filecoin']
                                )
                  ]
user_selected = inquirer.prompt(crypto_options)
# print(user_selected)
print_price = get_crypto_price(user_selected)
print(print_price)
