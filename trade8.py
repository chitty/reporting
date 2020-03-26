import json
import sys
from constants import BONUS, DEPOSIT, FIRST_ELEMENT, SATOSHIS_TO_BTC
from export import get_report


def report_to_json(data):
    balance = DEPOSIT + BONUS
    trade8 = []
    chartjs = [FIRST_ELEMENT]
    i = 1
    volume = 0
    for row in data:
        trade8.append(row)
        balance += (float(row['pnl']) * SATOSHIS_TO_BTC)
        volume += int(row['amount'])
        row.update(dict(label=volume, label_num=i, point=balance))
        chartjs.append(row)
        i += 1
    with open('reports/trade8.json', 'w') as jsonfile:
        json.dump(trade8, jsonfile, sort_keys=True, indent=2)
    with open('charting/src/json/report.json', 'w') as jsonfile:
        json.dump(chartjs, jsonfile, sort_keys=True, indent=2)

    print(len(chartjs))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        report_data = get_report(sys.argv[1])
        report_to_json(report_data)
    else:
        print("Pass the csv report file!")