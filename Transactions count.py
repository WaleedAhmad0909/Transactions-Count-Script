import urllib.request
import json

with urllib.request.urlopen("https://safe-transaction-mainnet.safe.global/api/v1/safes/0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8/multisig-transactions/") as url:
    dict = json.loads(url.read())
walletConnect_Total=0
for x in dict['results']:
    if x['origin']=='{}':
        continue
    else: 
        origin = eval(x['origin'])  # changing string to dictionary (origin variable is dictionary)
        if origin['name']=='WalletConnect':
            walletConnect_Total +=1

print(walletConnect_Total) 