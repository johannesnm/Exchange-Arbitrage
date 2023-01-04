
from findArb import find_arbitrage_opportunities_for_trading_pairs
from time import sleep

exchanges = ['alpaca','bigone','bitforex', 'coinmate','cryptocom', 'kraken',
'kuna', 'hitbtc','hollaex', 'huobi', 'kucoin','latoken','lykke','mexc','ndax','poloniex','probit']

pairs = ["AVAX/USDT", "BTC/USDT", "SOL/USDT", "ETH/USDT", "LINK/USDT"]

while True:
        find_arbitrage_opportunities_for_trading_pairs(pairs,exchanges)
        sleep(1)


