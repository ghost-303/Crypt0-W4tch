import requests

def eth_info():
    # price of etherium
    print("*"*20)
    print("ETHEREUM PRICE INFORMATION (ETH/USDT)")
    print("*"*20)
    web1='https://api.binance.com/api/v3/ticker/price?symbol='
    currency="ETHUSDT"
    web_request1=requests.get(web1+currency)
    data1=web_request1.json()
    c_price=float(data1.get('price'))
    print(f"CURRENT PRICE:",round(c_price,2),"USD")
    print("")



        # 24 hour price change
    print("*"*20)
    print("24 HOUR CHANGES (ETH/USDT)")
    print("*"*20)
    web2='https://api.binance.com/api/v3/ticker/24hr?symbol='
    web_request2=requests.get(web2+currency)
    data2=web_request2.json()
    h_price = float(data2.get('highPrice'))
    l_price = float(data2.get('lowPrice'))
    v = float(data2.get('volume'))
    print(f"24 HOUR HIGH:", round(h_price, 2), "USD")
    print(f"24 HOUR LOW:", round(l_price, 2), "USD")
    print(f"PRICE CHANGE:", data2.get('priceChangePercent'), "%")
    print(f"TRADE VOLUME IN ETH:",round(v,2), "ETH")
    volume_usd=float(data2.get('quoteVolume'))
    billion_conversion=volume_usd/1000000000
    print(f"TRADE VOLUME IN USD (Rounded Figure):",round(billion_conversion,2),"Billion")
    print("")
    print("")





