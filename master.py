import json
import urllib.request

with urllib.request.urlopen("https://www.coinspot.com.au/pubapi/latest") as url:
    data = json.loads(url.read().decode())

    def check_status(x):
        if data['status'] == 'ok':
            try:
                print(f"BID  -> {data['prices'][str(x)]['bid']}\nASK  -> {data['prices'][str(x)]['ask']}\nLAST -> {data['prices'][str(x)]['last']}")

            except KeyError:
                print(f"That coin doesnt exist in Coinspot\nCan't retrieve any Information on '{x}'")
    check_status(input().lower())
