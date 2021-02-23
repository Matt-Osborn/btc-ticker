from win10toast import ToastNotifier
import requests
import json
import time, threading

#initialize win10toast

toaster = ToastNotifier()

#initialize global variables

temp = 0

High = input("Set High Value: ")

Low = input("Set Low Value: ")


def fetch_data():
    global High
    global Low
    global temp

## make request to coinbase API:

    r = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")


##get data:

    t = r.text

    d = json.loads(t)

    data = d['data']


##print raw data:

    print(data)


##print formatted BTC price in USD:

    a = data['amount']

    print("BTC: $", a)

    if float(a) < int(Low) and float(temp) > int(Low):        
        toaster.show_toast("BITCOIN FELL TO " + "$" + a)
        Low = int(Low) -100
        High = int(High) - 100


    elif float(a) > int(High) and float(temp) < int(High):
        toaster.show_toast("BITCOIN ROSE TO " + "$" + a)
        Low = int(Low) + 100
        High = int(High) + 100
        ##print("High Value is now " + High)
        ##print("Low Value is now " + Low)

    temp = a
        
##delay:
    
    threading.Timer(10, fetch_data).start()

fetch_data()
