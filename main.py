import requests
import json
from tkinter import *

pycrypto = Tk()
pycrypto.title("Your Cryptofolio")



def my_portfolio():

    api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/')

    api = json.loads(api_request.content)


    coins = [
        {
          'symbol':'BTC',
          'amount_owned': 2,
          'price_per_coin': 3200
        },
        {
          'symbol':'ETH',
          'amount_owned': 100,
          'price_per_coin': 3200
        },
        {
          'symbol':'LTC',
          'amount_owned': 100,
          'price_per_coin': 50
        },
        {
          'symbol':'XMR',
          'amount_owned': 100,
          'price_per_coin': 10
        },

    ]
    total_pl = 0

    coin_row = 1

    total_current_value = 0

    for x in range(0,10):
        for coin in coins:
            if coin['symbol'] == api[x]['symbol']:
                total_paid = coin['amount_owned'] * coin ['price_per_coin']
                current_value = coin['amount_owned'] * float(api[x]['price_usd'])
                pl_percoin = float(api[x]['price_usd']) - coin['price_per_coin']
                total_pl_coin = pl_percoin * coin['amount_owned']
                total_pl += total_pl_coin
                total_current_value += current_value

                print(api[x]['name'] + ' - ' + api[x]['symbol'])
                print("Price: {0:.2f}".format(float(api[x]['price_usd'])))
                print(f'Number of coins: {coin["amount_owned"]}')
                print('Total amount paid: {0:.2f}'.format(total_paid))
                print('Current value: {0:.2f}'.format(current_value))
                print('P/L per coin: {0:.2f}'.format(pl_percoin))
                print('Total P/L: {0:.2f}'.format(total_pl_coin))

                print("--------------------------------")

                name = Label(pycrypto, text=api[x]['name'], bg="#F3F4F6", fg="black")
                name.grid(row=coin_row, column=0, sticky=N + S + E + W)

                price = Label(pycrypto, text="Price: {0:.2f}".format(float(api[x]['price_usd'])), bg="#F3F4F6", fg="black")
                price.grid(row=coin_row, column=1, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin["amount_owned"], bg="#F3F4F6", fg="black")
                no_coins.grid(row=coin_row, column=2, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text='{0:.2f}'.format(total_paid), bg="#F3F4F6", fg="black")
                amount_paid.grid(row=coin_row, column=3, sticky=N + S + E + W)

                current_val = Label(pycrypto, text='{0:.2f}'.format(current_value), bg="#F3F4F6", fg="black")
                current_val.grid(row=coin_row, column=4, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text='{0:.2f}'.format(pl_percoin), bg="#F3F4F6", fg="black")
                pl_coin.grid(row=coin_row, column=5, sticky=N + S + E + W)

                totalplcoin = Label(pycrypto, text='{0:.2f}'.format(total_pl_coin), bg="#F3F4F6", fg="black")
                totalplcoin.grid(row=coin_row, column=6, sticky=N + S + E + W)

                coin_row += 1
            totalcv = Label(pycrypto, text='{0:.2f}'.format(total_current_value), bg="#F3F4F6", fg="black")
            totalcv.grid(row=coin_row, column=4, sticky=N + S + E + W)
            totalpl = Label(pycrypto, text='{0:.2f}'.format(total_pl), bg="#F3F4F6", fg="black")
            totalpl.grid(row=coin_row, column=6, sticky=N + S + E + W)


    print('Net profit or loss: {0:.2f}'.format(total_pl))


name = Label(pycrypto, text='Coin name', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
name.grid(row=0, column=0, sticky=N + S + E + W)

price = Label(pycrypto, text='Price', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
price.grid(row=0, column=1, sticky=N + S + E + W)

no_coins = Label(pycrypto, text='Coins Owned', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
no_coins.grid(row=0, column=2, sticky=N + S + E + W)

amount_paid = Label(pycrypto, text='Total Amount Paid', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
amount_paid.grid(row=0, column=3, sticky=N + S + E + W)

current_val = Label(pycrypto, text='Current Value', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
current_val.grid(row=0, column=4, sticky=N + S + E + W)

pl_coin = Label(pycrypto, text='P/L Per Coin', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
pl_coin.grid(row=0, column=5, sticky=N + S + E + W)

totalpl = Label(pycrypto, text='Total P/L With Coin', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
totalpl.grid(row=0, column=6, sticky=N + S + E + W)

my_portfolio()

pycrypto.mainloop()

print('Program completed')
