# author: jack lulich
# shaq
# testfile for playing with btc
# and btc xchange apis

import gdax
import asyncio

async def main():
	trader = gdax.trader.Trader(product_id="BTC-USD")
	res = await asyncio.gather(
		trader.get_products(),
		trader.get_product_ticker(),
		trader.get_time(),
		)
	print(res)
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
