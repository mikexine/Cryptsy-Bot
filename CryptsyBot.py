from time import sleep
from PyCryptsy import PyCryptsy
from subprocess import call

api=PyCryptsy('API KEY HERE', 'API SECRET HERE')



# setting parameters
Coin_One = raw_input('Insert the coin you want to trade: ')
print ''
Coin_Two = raw_input('Insert BTC if you want the '+Coin_One+'/BTC market or LTC if you want the '+Coin_One+'/LTC market. Insert: ')
print ''
BuyPercentage = float(raw_input('Insert the multiplier of the current highest buy price: '))
print ''
print 'Insert the multiplier of the amount of your balance; should be lower than 1! Example: if you want to trade 70% of your available '+Coin_Two+' balance, then insert 0.7'
BtcPercentage = float(raw_input('Insert the multiplier of the amount of your balance: '))
print 'Working....'


while True:
    try:
        #defining orders
        MyBTC = api.GetAvailableBalance(Coin_Two)
        TradeAmount = MyBTC * BtcPercentage
        
        BuyPrice = api.GetBuyPrice(Coin_One, Coin_Two)*BuyPercentage

        ## the multiplier here should be higher than 1.005015045, otherwise you are going to
        ## lose some money on fees - if I did all counts correctly. 1.01 is just an example
        SellPrice = 1.01 * BuyPrice
        
        TradeAmount = TradeAmount / BuyPrice
        
        BuyOrder = api.CreateBuyOrder(Coin_One, Coin_Two, TradeAmount, BuyPrice)
        print 'BUY: '+str(Coin_One)+'/'+str(Coin_Two)+' amount: '+str(TradeAmount)+' at price '+str(BuyPrice)
        sleep(1)
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        
        print 'BUY order'
        print MyOrders

        # checking if the currency is bought
        if MyOrders['return'] == []:
            SellAmount = api.GetAvailableBalance(Coin_One)
        else:
            SellAmount = MyOrders['return'][0]['orig_quantity']

        print 'buying',
                
        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    print '.',
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        print 'BOUGHT! \n'
        
        # currency bought, creating sell order        
        SellOrder = api.CreateSellOrder(Coin_One, Coin_Two, float(SellAmount), SellPrice)
        print 'SELL: '+str(Coin_One)+'/'+str(Coin_Two)+' amount: '+str(float(SellAmount))+' at price '+str(SellPrice)
        sleep(1)
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)

        print 'SELL order'
        print MyOrders
        print 'selling',

        #checking if currency sold
        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    print '.',
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        print 'SOLD! \n'

        #end of the job, restarting
        print 'restarting cycle \n'
        sleep(5)

    except KeyboardInterrupt:
        print 'INTERRUPT'
        break 

