from time import sleep
from PyCryptsy import PyCryptsy
from subprocess import call

api=PyCryptsy('API KEY HERE', 'API SECRET HERE')




Coin_One = raw_input('Insert the coin you want to trade: ')
print ''
Coin_Two = raw_input('Insert BTC if you want the '+Coin_One+'/BTC market or LTC if you want the '+Coin_One+'/LTC market. Insert: ')
print ''

BuyPercentage = float(raw_input('Insert the multiplier of the current highest buy price: '))
SellPercentage  = float(raw_input('Insert the multiplier of the current lowest sell price: '))
print ''
print 'Insert the multiplier of the amount of your balance; should be lower than 1! Example: if you want to trade 70% of your available '+Coin_Two+' balance, then insert 0.7'
BtcPercentage = float(raw_input('Insert the multiplier of the amount of your balance: '))


while True:
    try:
        text_file = open('TradingLog.txt', "w")
        MyBTC = api.GetAvailableBalance(Coin_Two)
        SellPrice = api.GetSellPrice(Coin_One, Coin_Two)*SellPercentage
        BuyPrice = api.GetBuyPrice(Coin_One, Coin_Two)*BuyPercentage
        TradeAmount = MyBTC * BtcPercentage
        text_file.write('[OK] My BTC balance: '+str(MyBTC)+' \n')
        text_file.write('[OK] Buy price: '+str(BuyPrice)+' \n')
        text_file.write('[OK] prices decided \n')
 
        TradeAmount = TradeAmount / BuyPrice
        text_file.write('[OK] BUYORDER get \n')
        BuyOrder = api.CreateBuyOrder(Coin_One, Coin_Two, TradeAmount, BuyPrice)
        
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        SellAmount=MyOrders['return'][0]['orig_quantity']
        text_file.write('[OK] created buy order of market '+Coin_One+'/'+Coin_Two+' at price: '+str(BuyPrice)+' amount: '+str(TradeAmount)+' \n')
        text_file.write('')

        text_file.write('[OK] now buying.. \n')

        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        text_file.write('[OK] coin bought! \n')
        SellOrder = api.CreateSellOrder(Coin_One, Coin_Two, float(SellAmount), SellPrice)
        text_file.write('[OK] sell order sent \n')
        MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        text_file.write('[OK] SELLORDER get \n')
        text_file.write('[OK] now selling.. \n')

        try:
            while MyOrders['return'] != []:
                    sleep(1)
                    MyOrders = api.GetMyOrders(Coin_One, Coin_Two)
        except:
            pass

        
        text_file.write('[OK] trade-cycle completed! \n')
        text_file.close()
        print 'restarting cycle'
        sleep(5)

    except KeyboardInterrupt:
        text_file.close()
        print 'INTERRUPT'
        break 



    



        




