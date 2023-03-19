# Cryptocurrency exchanges arbitrage (I.e Binance and Coinbase)

Features:

- Searches for arbitrage opportunities in the cryptocurrency market using the ccxt library.

- Takes in a trading pair and a list of exchanges as input and fetches the order book data for the trading pair from each exchange.

- Calculates the difference between the lowest ask price and the highest bid price, and subtracts the total cost of the arbitrage,
including maker and taker fees and withdraw fees, from the original price difference.

- If the resulting arbitrage cost is positive, the script prints the arbitrage information in green, otherwise it prints it in red.

- Writes the possible arbitrages to a text file.


