import ccxt
import time
from datetime import datetime
import termcolor
import colorama

def find_arbitrage_opportunities(tradingPair,exchangesList):

    colorama.init()
    # Get a list of all available exchanges in ccxt
    exchanges = exchangesList

    # Convert the timestamp from seconds to a datetime object
    timestamp = time.time()
    datetime_object = datetime.fromtimestamp(timestamp)
    timestamp_string = datetime_object.strftime('%H:%M:%S')

    # Initialize a dictionary to store the bid and ask prices for each exchange
    prices = {}
    fees = {} # dictionary to store the fees for each exchange
    
    print(f"Searching for arbs... {tradingPair}")
    
    for exchange in exchanges:
        # Initialize the exchange using ccxt
        exchange = getattr(ccxt, exchange)()
        trading_pair = tradingPair


        # Check if the exchange supports the specified trading pair
        try:
            # Load the markets for the exchange
            exchange.load_markets()
            # Check if the exchange supports the specified trading pair
            if trading_pair not in exchange.markets:
            # Skip this exchange if it doesn't have the specified trading pair
                continue
                # Fetch the order book data for the trading pair    
            order_book = exchange.fetch_order_book(trading_pair)
            
            # fetch the fees for this exchange
            fees[exchange.id] = exchange.fetch_fees()
            
        except (ccxt.BadSymbol, ccxt.RequestTimeout, ccxt.NetworkError,ccxt.AuthenticationError):
                # Skip this exchange if it doesn't have the specified trading pair or if there is a network issue
                continue
        try:
                # Check if the order book data is valid
                if order_book is None or 'bids' not in order_book or 'asks' not in order_book:
                    continue

                # Store the current bid and ask prices for Bitcoin in USDT for this exchange
                prices[exchange.id] = {
                    'bid': order_book['bids'][0][0],
                    'ask': order_book['asks'][0][0]
                }
        except ccxt.RequestTimeout:
                continue

    # Find the exchange with the lowest ask price and the highest bid price
    lowest_ask = min(prices, key=lambda x: prices[x]['ask'])
    highest_bid = max(prices, key=lambda x: prices[x]['bid'])

    # Calculate the difference between the lowest ask price and the highest bid price
    price_difference = prices[highest_bid]['bid'] - prices[lowest_ask]['ask']
    
    # Calculate the total cost of the arbitrage by adding the maker and taker fees for the ask exchange
    # and the withdraw fee for the ask exchange
    total_cost = 0
    if 'taker' in fees[lowest_ask]:
        total_cost += fees[lowest_ask]['taker']
    if 'maker' in fees[lowest_ask]:
        total_cost += fees[lowest_ask]['maker']
    if 'withdraw' in fees[lowest_ask]:
        total_cost += fees[lowest_ask]['withdraw']

    
    # Subtract the total cost of the arbitrage from the original price difference
    arbitrage_cost = price_difference - total_cost
    
    # Use the termcolor library to print the arbitrage cost in red if it is negative,
    # or green if it is positive
    if arbitrage_cost > 0:
        # Open the text file in append mode
        with open('arbitrage_opportunities.txt', 'a') as f:
            # Write the arbitrage information to the text file
            f.write(f'[{timestamp_string}] Lowest ask: {lowest_ask} ({prices[lowest_ask]["ask"]}) Highest bid: {highest_bid} ({prices[highest_bid]["bid"]}) Arbitrage cost: {arbitrage_cost:.5f}\n')
        text = f'[{timestamp_string}] Lowest ask: {lowest_ask} ({prices[lowest_ask]["ask"]}) Highest bid: {highest_bid} ({prices[highest_bid]["bid"]}) Arbitrage cost: {arbitrage_cost:.5f}'
        print(termcolor.colored(text, 'green'))

    else:
        text = f'[{timestamp_string}] Lowest ask: {lowest_ask} ({prices[lowest_ask]["ask"]}) Highest bid: {highest_bid} ({prices[highest_bid]["bid"]}) Arbitrage cost: {arbitrage_cost:.5f}'
        print(termcolor.colored(text, 'red'))


def find_arbitrage_opportunities_for_trading_pairs(tradingPairs, exchangesList):
    for tradingPair in tradingPairs:
        find_arbitrage_opportunities(tradingPair, exchangesList)