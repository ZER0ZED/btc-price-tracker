import requests

def get_btc_price():
    try:
        response = requests.get("https://api.coinlore.net/api/ticker/?id=90")
        data = response.json()
        price = data[0]['price_usd']
        return price
    except Exception as e:
        print(f"Error fetching BTC price: {e}")
        return None
