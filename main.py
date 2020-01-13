import requests
import json

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

]
total_pl = 0

for x in range(0, 5):
    for coin in coins:
        if coin['symbol'] == api[x]['symbol']:
            total_paid = coin['amount_owned'] * coin ['price_per_coin']
            current_value = coin['amount_owned'] * float(api[x]['price_usd'])
            pl_percoin = float(api[x]['price_usd']) - coin['price_per_coin']
            total_pl_coin = pl_percoin * coin['amount_owned']
            total_pl += total_pl_coin

            print(api[x]['name'] + ' - ' + api[x]['symbol'])
            print("Price: {0:.2f}".format(float(api[x]['price_usd'])))
            print(f'Number of coins: {coin["amount_owned"]}')
            print('Total amount paid: {0:.2f}'.format(total_paid))
            print('Current value: {0:.2f}'.format(current_value))
            print('P/L per coin: {0:.2f}'.format(pl_percoin))
            print('Total P/L: {0:.2f}'.format(total_pl_coin))

            print("--------------------------------")

print('Net profit or loss: {0:.2f}'.format(total_pl))
