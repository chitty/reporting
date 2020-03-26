import csv

# Constants
DEPOSIT = 0.07654199
BONUS = 0.00373599
SATOSHIS_TO_BTC = 100000000
WITHDRAWAL = 30000

with open('reports/trade8.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_amount = 0
    total_pnl = 0
    total_decay = 0
    winners = 0
    losers = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            total_amount += int(row[4])
            total_pnl += float(row[10])
            total_decay += int(row[11])
            if float(row[10]) > 0:
                winners += 1
            else:
                losers += 1
            
    pnl_in_satoshis = total_pnl * SATOSHIS_TO_BTC
    x = WITHDRAWAL // total_amount
    print(f'Processed {line_count} lines.\n')
    print(f'Total volume traded: {total_amount} = {total_amount*0.001} BTC ~{x}x to withdrawal ')
    print(f'Total P/L: {pnl_in_satoshis} satoshis / {total_pnl} BTC')
    print(f'Total decay: {total_decay} satoshis / {total_decay/SATOSHIS_TO_BTC} BTC')
    print(f'Total P/L + decay: {int(pnl_in_satoshis + total_decay)} satoshis')
    print(f'{winners} winning trades VS {losers} losing trades')

    trading_outcome = (pnl_in_satoshis + total_decay)/SATOSHIS_TO_BTC
    balance = DEPOSIT + BONUS + trading_outcome
    print(f'INITIAL deposit: {DEPOSIT} BTC')
    print(f'Bonus: {BONUS} BTC\n')
    print(f'Current balance: {balance} BTC')