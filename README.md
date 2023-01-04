# Exchange-Arbitrage-Project

This is a script that searches for arbitrage opportunities in the cryptocurrency market using the ccxt library.
It takes in a trading pair and a list of exchanges as input and fetches the order book data for the trading pair from each exchange.
It then calculates the difference between the lowest ask price and the highest bid price, and subtracts the total cost of the arbitrage,
including maker and taker fees and withdraw fees, from the original price difference.
If the resulting arbitrage cost is positive, the script prints the arbitrage information in green, otherwise it prints it in red.
The script also writes the arbitrage information to a text file.
