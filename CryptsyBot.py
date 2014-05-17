from time import sleep
from PyCryptsy import PyCryptsy
from subprocess import call

api=PyCryptsy('API KEY', 'API SECRET KEY')



# setting parameters
Coin_One = raw_input('Insert the coin you want to trade: ')
print ''
Coin_Two = raw_input('Insert BTC if you want the '+Coin_One+'/BTC market or LTC if you want the '+Coin_One+'/LTC market. Insert: ')
print ''

BuyPercentage = float(raw_input('Insert the multiplier of the current highest buy price: '))
SellPercentage  = float(raw_input('Insert the multiplier of the current lowest sell price: '))
print ''
print 'Insert the multiplier of the amount of your balance; should be lower than 1! Example: if you want to trade 70% of your available '+Coin_Two+' balance, then insert 0.7'
BtcPercentage = float(raw_input('Insert the multiplier of the amount of your balance: '))
print 'Working....'


while True:
    try:
        #defining orders
        MyBTC = api.GetAvailableBalance(Coin_Two)
        SellPrice = api.GetSellPrice(Coin_One, Coin_Two)*SellPercentage
        BuyPrice = api.GetBuyPrice(Coin_One, Coin_Two)*BuyPercentage
        TradeAmount = MyBTC * BtcPercentage
        TradeAmount = TradeAmount / BuyPrice        
        BuyOrder = api.CreateBuyOrder(Coin_One, Coin_Two, TradeAmount, BuyPrice)
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        print 'testing orders'
        print MyOrders

        # checking if the currency is bought
        if MyOrders['return'] == []:
            SellAmount = api.GetAvailableBalance(Coin_One)
        else:
            SellAmount = MyOrders['return'][0]['orig_quantity']
        
        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        # currency bought, creating sell order        
        SellOrder = api.CreateSellOrder(Coin_One, Coin_Two, float(SellAmount), SellPrice)
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)

        #checking if currency sold
        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        #end of the job, restarting
        print 'restarting cycle'
        sleep(5)

    except KeyboardInterrupt:
        print 'INTERRUPT'
        break 

