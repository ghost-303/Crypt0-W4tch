import requests

def btc_info():
    # price of bitcoin
    print("*"*20)
    print("BITCOIN PRICE INFORMATION (BTC/USDT)")
    print("*"*20)
    web1='https://api.binance.com/api/v3/ticker/price?symbol='
    currency="BTCUSDT"
    web_request1=requests.get(web1+currency)
    data1=web_request1.json()
    c_price=float(data1.get('price'))
    #print(f"CURRENT PRICE:",data1.get('price'))
    print(round(c_price,2),"USD")
    print("")



    # 24 hour price change
    print("*"*20)
    print("24 HOUR CHANGES (BTC/USDT)")
    print("*"*20)
    web2='https://api.binance.com/api/v3/ticker/24hr?symbol='
    web_request2=requests.get(web2+currency)
    data2=web_request2.json()
    h_price=float(data2.get('highPrice'))
    l_price=float(data2.get('lowPrice'))
    v=float(data2.get('volume'))
    print(f"24 HOUR HIGH:",round(h_price,2),"USD")
    print(f"24 HOUR LOW:", round(l_price, 2),"USD")
    print(f"PRICE CHANGE:", data2.get('priceChangePercent'),"%")
    print(f"TRADE VOLUME IN BTC:",round(v,2),"BTC")
    volume_usd=float(data2.get('quoteVolume'))
    billion_conversion=volume_usd/1000000000
    print(f"TRADE VOLUME IN USD (Rounded Figure):",round(billion_conversion,2),"Billion","USD")
    print("")
    print("")




