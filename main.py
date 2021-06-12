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

    # Return the price to be able to print it.
    return price

# Function to ask user if they want to get another coin price using Inquirer Confirm


def another():
    # Inquirer confrim letting the user select 'y' or 'n'
    pick_again = {inquirer.Confirm('again',
                                   message="Do you want to get the price of another coin?: ",
                                   default=True)
                  }

    # Set the response to a variable
    run_again = inquirer.prompt(pick_again)

    # print(run_again)

    # If statement to see if the user selected yes or no.
    # If yes, run the pick_a_coin function again
    if run_again['again'] == True:
        pick_a_coin()
    # Else make a silly crypto joke and say goodbye.
    else:
        print("HODL! Goodbye!")

# Main function to ask the user what coin they would like the price of


def pick_a_coin():

    # Using inquirer, give the user a list of coins to find the price of.
    # This is done to avoid user misspelling, or typing in something that is not a coin.
    crypto_options = [inquirer.List('crypto',
                                    message="What coin price would you like to check?: ",
                                    choices=['Bitcoin', 'Ethereum', 'Tether', 'Cardano', 'Dogecoin',
                                             'XRP', 'Polkadot', 'Uniswap', 'Litecoin', 'Solana', 'Filecoin']
                                    )
                      ]
    # Ask the question and set the response to a variable
    user_selected = inquirer.prompt(crypto_options)
    # Call the get_crypto_price function and send it the user selected coin.
    print_price = get_crypto_price(user_selected)
    # Print the results of the get_crypto_price function!
    print(print_price)
    # Call the another function to see if the user would like to ask another question
    another()


# Start the program by calling the pick_a_coin function!
pick_a_coin()
