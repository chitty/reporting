import csv
import json

# Constants
DEPOSIT = 0.07654199
BONUS = 0.00373599
SATOSHIS_TO_BTC = 100000000
WITHDRAWAL = 30000

FIRST_ELEMENT =   {
    "amount": "0",
    "base_currency": "BTC",
    "close_price": "0.0",
    "closed_at": "Mon Mar 08 2020 06:07:33 GMT+0000 (Coordinated Universal Time)",
    "decay": "0",
    "leverage": "1",
    "liquidation_price": "0.0",
    "margin": "0.0",
    "opened_at": "Mon Mar 08 2020 01:16:34 GMT+0000 (Coordinated Universal Time)",
    "pnl": "0.0",
    "price": "0.0",
    "product": "N/A",
    "side": "N/A",
    "type": "N/A",
    "label": 0,
    "point": DEPOSIT + BONUS
}

with open('reports/trade8.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    trade8 = []
    chartjs = [FIRST_ELEMENT]
    i = 1
    balance = DEPOSIT + BONUS
    for row in reader:
        trade8.append(row)
        balance += float(row['pnl'])
        row.update(dict(label=i, point=balance))
        chartjs.append(row)
        i += 1
    trade8 = sorted(trade8, key = lambda i: i['opened_at']) 
    with open('reports/trade8.json', 'w') as jsonfile:
        json.dump(trade8, jsonfile, sort_keys=True, indent=2)
    with open('charting/src/json_reports/chart.json', 'w') as jsonfile:
        json.dump(chartjs, jsonfile, sort_keys=True, indent=2)

    print(len(chartjs))
        