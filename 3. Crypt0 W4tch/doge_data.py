import requests

def doge_info():
    # price of xrp
    print("*"*20)
    print("DOGE COIN PRICE INFORMATION (DOGE/USDT)")
    print("*"*20)
    web1='https://api.binance.com/api/v3/ticker/price?symbol='
    currency="DOGEUSDT"
    web_request1=requests.get(web1+currency)
    data1=web_request1.json()
    c_price=float(data1.get('price'))
    print(f"CURRENT PRICE:",round(c_price,2),"USD")
    print("")



        # 24 hour price change
    print("*"*20)
    print("24 HOUR CHANGES (DOGE/USDT)")
    print("*"*20)
    web2='https://api.binance.com/api/v3/ticker/24hr?symbol='
    web_request2=requests.get(web2+currency)
    data2=web_request2.json()
    h_price = float(data2.get('highPrice'))
    l_price = float(data2.get('lowPrice'))
    #v = float(data2.get('volume'))
    print(f"24 HOUR HIGH:",round(h_price,2),"USD")
    print(f"24 HOUR LOW:",round(l_price,2),"USD")
    print(f"PRICE CHANGE:",data2.get('priceChangePercent'),"%")
    xrp_volume=float(data2.get('volume'))
    xrp_million_conversion = xrp_volume/1000000
    print(f"TRADE VOLUME IN XRP:",round(xrp_million_conversion,2),"Million DOGE")
    #print(f"TRADE VOLUME IN XRP:",data2.get('volume'))
    #print(f"TRADE VOLUME IN USD:",data2.get('quoteVolume'))
    volume_usd=float(data2.get('quoteVolume'))
    million_conversion=volume_usd/1000000
    print(f"TRADE VOLUME IN USD (Rounded Figure):",round(million_conversion,2),"Million USD")
    print("")
    print("")
    #print(f"24 HOUR CHANGE",data1.get('symbol'))




