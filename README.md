This is just a simple bot. 
This script does this:

- asks the user to insert the Cryptsy Coins to trade (ex: DRK and then BTC -> DRK/BTC market selected)
- asks the user to insert the Multiplier of the highest Buy Price (if the Multiplier is, for example, 0.9 the Buy Orders will be sent at the highest Buy Price * 0.9)
- asks the user to insert the Multiplier of the lowest Sell Price (if the Multiplier is, for example, 1.1 the Sell Orders will be sent at the lowest Sell Price * 1.1)
- asks the user to insert the Multiplier of his available balance (if the Multiplier is, for example, 0.5, and the market is DRK/BTC, the amount traded will be the half of the available BTC balance)


- enters a While cycle that stops just on CTRL-C

	- asks Cryptsy for the current Buy and Sell Prices.

	- creates a Buy Order with the above characteristics.

	- checks, every one second, if the Buy Order is fully executed. 

	- when the Buy Order is executed, creates a Sell Order with the above characteristics.

	- checks, every one second, if the Sell Order is fully executed.

	- when the Sell Order is fully executed, it restarts the While loop.


To use this you have to download also the PyCryptsy.py file (I added some lines to the one here: https://github.com/salfter/PyCryptsy - thank you @salfter for publishing this on GitHub!)

Be careful, the bot may not work or may cause losses of some kind. Do whatever you want with code; I am NOT responsible for how you use this.