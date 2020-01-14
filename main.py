import requests
import json
from tkinter import *
import sqlite3

pycrypto = Tk()
pycrypto.title("Your Cryptofolio")


con = sqlite3.connect('coin.db')
cursorObj = con.cursor()

# cursorObj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
# con.commit()

# cursorObj.execute("INSERT INTO coin VALUES(1, 'BTC', 2, 3250)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(2, 'ETH', 5, 120)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(3, 'LTC', 2, 50)")
# con.commit()
#
# cursorObj.execute("INSERT INTO coin VALUES(20, 'XMR', 2, 20)")
# con.commit()






def my_portfolio():

    api_request = requests.get('https://api.coinmarketcap.com/v1/ticker/')

    api = json.loads(api_request.content)

    def font_color(amount):
        if amount > 0:
            return "green"
        else:
            return 'red'

    def insert_coin():
        cursorObj.execute('INSERT INTO coin(symbol, price, amount) VALUES(?, ?, ?)', (symbol_txt.get(), price_txt.get(), amount_txt.get()))
        con.commit()


    # coins = [
    #     {
    #       'symbol':'BTC',
    #       'amount_owned': 2,
    #       'price_per_coin': 3200
    #     },
    #     {
    #       'symbol':'ETH',
    #       'amount_owned': 100,
    #       'price_per_coin': 3200
    #     },
    #     {
    #       'symbol':'LTC',
    #       'amount_owned': 100,
    #       'price_per_coin': 50
    #     },
    #     {
    #       'symbol':'XMR',
    #       'amount_owned': 100,
    #       'price_per_coin': 10
    #     },
    #
    # ]




    cursorObj.execute("SELECT * FROM coin")
    coins = cursorObj.fetchall()


    total_pl = 0

    coin_row = 1

    total_current_value = 0

    total_amount_paid = 0

    for x in range(0,10):
        for coin in coins:
            if coin[1] == api[x]['symbol']:
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * float(api[x]['price_usd'])
                pl_percoin = float(api[x]['price_usd']) - coin[3]
                total_pl_coin = pl_percoin * coin[2]
                total_pl += total_pl_coin
                total_current_value += current_value
                total_amount_paid += total_paid


                portfolio_id = Label(pycrypto, text=coin[0], bg="#F3F4F6", fg="black")
                portfolio_id.grid(row=coin_row, column=0, sticky=N + S + E + W)

                name = Label(pycrypto, text=api[x]['name'], bg="#F3F4F6", fg="black")
                name.grid(row=coin_row, column=1, sticky=N + S + E + W)

                price = Label(pycrypto, text="Price: {0:.2f}".format(float(api[x]['price_usd'])), bg="#F3F4F6", fg="black")
                price.grid(row=coin_row, column=2, sticky=N + S + E + W)

                no_coins = Label(pycrypto, text=coin[2], bg="#F3F4F6", fg="black")
                no_coins.grid(row=coin_row, column=3, sticky=N + S + E + W)

                amount_paid = Label(pycrypto, text='{0:.2f}'.format(total_paid), bg="#F3F4F6", fg="black")
                amount_paid.grid(row=coin_row, column=4, sticky=N + S + E + W)

                current_val = Label(pycrypto, text='{0:.2f}'.format(current_value), bg="#F3F4F6", fg='black')
                current_val.grid(row=coin_row, column=5, sticky=N + S + E + W)

                pl_coin = Label(pycrypto, text='{0:.2f}'.format(pl_percoin), bg="#F3F4F6", fg=font_color(float(pl_percoin)))
                pl_coin.grid(row=coin_row, column=6, sticky=N + S + E + W)

                totalplcoin = Label(pycrypto, text='{0:.2f}'.format(total_pl_coin), bg="#F3F4F6", fg=font_color(float(total_pl_coin)))
                totalplcoin.grid(row=coin_row, column=7, sticky=N + S + E + W)

                coin_row += 1

            # Insert Data:
            symbol_txt = Entry(pycrypto, borderwidth=2, relief='groove')
            symbol_txt.grid(row=coin_row, column = 1)

            price_txt = Entry(pycrypto, borderwidth=2, relief='groove')
            price_txt.grid(row=coin_row, column = 2)

            amount_txt = Entry(pycrypto, borderwidth=2, relief='groove')
            amount_txt.grid(row=coin_row, column = 3)

            add_coin = Button(pycrypto, text='Add Coin', bg='#142E54', fg='black', command=insert_coin, font='Lato 12', borderwidth=2, relief='groove')
            add_coin.grid(row=coin_row + 1, column = 3, sticky = N + S + E+ W)

            symbol_txt = Entry(pycrypto, borderwidth=2, relief='groove')
            symbol_txt.grid(row=coin_row, column = 4)

            totalamountpaid = Label(pycrypto, text='{0:.2f}'.format(total_amount_paid), bg="#F3F4F6", fg="black")
            totalamountpaid.grid(row=coin_row, column=4, sticky=N + S + E + W)

            totalcv = Label(pycrypto, text='{0:.2f}'.format(total_current_value), bg="#F3F4F6", fg="black")
            totalcv.grid(row=coin_row, column=5, sticky=N + S + E + W)

            totalpl = Label(pycrypto, text='{0:.2f}'.format(total_pl), bg="#F3F4F6", fg=font_color(float(total_pl)))
            totalpl.grid(row=coin_row, column=7, sticky=N + S + E + W)


            # api = ""

            # update = Button(pycrypto, text='Update', bg="#F3F4F6", fg="black", command = my_portfolio)
            # update.grid(row=coin_row + 1, column=6, sticky=N + S + E + W)


    print('Net profit or loss: {0:.2f}'.format(total_pl))


def app_header():
    portfolio_id = Label(pycrypto, text='Portfolio ID', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    portfolio_id.grid(row=0, column=0, sticky=N + S + E + W)

    name = Label(pycrypto, text='Coin name', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    name.grid(row=0, column=1, sticky=N + S + E + W)

    price = Label(pycrypto, text='Price', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    price.grid(row=0, column=2, sticky=N + S + E + W)

    no_coins = Label(pycrypto, text='Coins Owned', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    no_coins.grid(row=0, column=3, sticky=N + S + E + W)

    amount_paid = Label(pycrypto, text='Total Amount Paid', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    amount_paid.grid(row=0, column=4, sticky=N + S + E + W)

    current_val = Label(pycrypto, text='Current Value', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    current_val.grid(row=0, column=5, sticky=N + S + E + W)

    pl_coin = Label(pycrypto, text='P/L Per Coin', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    pl_coin.grid(row=0, column=6, sticky=N + S + E + W)

    totalpl = Label(pycrypto, text='Total P/L With Coin', bg="#142E54", fg="white", font='Lato 12 bold', padx='5', pady='5', borderwidth=2, relief='groove')
    totalpl.grid(row=0, column=7, sticky=N + S + E + W)
app_header()
my_portfolio()

pycrypto.mainloop()

print('Program completed')

cursorObj.close()
con.close()
