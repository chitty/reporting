import sys
from colorama import init, Fore, Style
from constants import BONUS, DEPOSIT, SATOSHIS_TO_BTC, WITHDRAWAL
from export import get_report

init(autoreset=True)

def print_trade(trade: dict, best: bool):
    product = trade['product']
    pnl = float(trade['pnl'])
    if best:
        print(Fore.GREEN + 'Best  trade: {0} P/L:   {1} sats'.format(
            product,
            int(pnl*SATOSHIS_TO_BTC)
        ))
    else:
        print(Fore.RED + 'Worst trade: {0} P/L: {1} sats'.format(
            product,
            int(pnl*SATOSHIS_TO_BTC)
        ))

def report(rows: list):
    '''
    Given the passed data produces a dict with a report
    '''
    result = dict(
        total_amount = 0,
        total_pnl = 0,
        total_decay = 0,
        winners = 0,
        losers = 0,
        best = dict(),
        worst = dict(),
        total_trades = 0
    )
    for data in rows:
        result['total_amount'] += int(data['amount'])
        result['total_pnl'] += float(data['pnl']) # P/L includes decay
        result['total_decay'] += int(data['decay'])
        # Get best and worst trades
        if not result['best'] or float(result['best']['pnl']) < float(data['pnl']):
            result['best'] = data
        if not result['worst'] or float(result['worst']['pnl']) > float(data['pnl']):
            result['worst'] = data
        if float(data['pnl']) > 0:
            result['winners'] += 1
        else:
            result['losers'] += 1
        result['total_trades'] += 1

    return result

def verbose_report(trade_data: list):
    '''
    Given a list of trade data it prints a report in verbose form
    '''
    result = report(trade_data)
    pnl_in_satoshis = int(result['total_pnl'] * SATOSHIS_TO_BTC)
    x = WITHDRAWAL // result['total_amount']
    print('\nTotal volume traded: {0} = {1} BTC ~{2}x to withdrawal'.format(
        result['total_amount'],
        result['total_amount']*0.001,
        x
    ))
    print('Total P/L: {0} sats / {1} BTC'.format(
        pnl_in_satoshis,
        result['total_pnl']
    ))
    print('Total decay: {0} sats / {1} BTC'. format(
        result['total_decay'],
        result['total_decay']/SATOSHIS_TO_BTC
    ))
    print('Total P/L without decay: {0} sats'.format(
        int(pnl_in_satoshis - result['total_decay'])
    ))
    print('{0} trades, {1} winners VS {2} losers'.format(
        result['total_trades'],
        result['winners'],
        result['losers']
    ))

    print_trade(result['best'], True)
    print_trade(result['worst'], False)

    balance = DEPOSIT + BONUS + pnl_in_satoshis
    print(f'INITIAL deposit: {DEPOSIT} sats')
    print(f'Bonus: {BONUS} sats\n')
    print(f'Current balance: {balance} sats ({balance/SATOSHIS_TO_BTC} BTCs)')

def simple_report(trade_data: dict):
    '''
    Given a list of trade data it prints a report in simple form
    '''
    result = report(trade_data)
    pnl_in_satoshis = int(result['total_pnl'] * SATOSHIS_TO_BTC)
    print('Total P/L: {0} sats / {1} BTC'.format(
        pnl_in_satoshis,
        result['total_pnl']
    ))
    print('{0} trades, {1} winners VS {2} losers'.format(
        result['total_trades'],
        result['winners'],
        result['losers']
    ))

    print_trade(result['best'], True)
    print_trade(result['worst'], False)

def grouped_report(trade_data: list, criteria: str):
    '''
    Reports in trade data grouped by the passed criteria
    '''
    print(f'\n** Reports by {criteria} **')
    columns = list(set([trade[criteria] for trade in trade_data]))
    columns.sort()

    for column in columns:
        print(f'\n----- {column} -----')
        grouped_trade_data = list(filter(lambda x: x[criteria] == column, trade_data))
        simple_report(grouped_trade_data)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        trade_data = get_report(sys.argv[1])
        #grouped_report(trade_data, 'type')
        grouped_report(trade_data, 'amount')
        #grouped_report(trade_data, 'side')
        grouped_report(trade_data, 'product')
        #grouped_report(trade_data, 'leverage')
        #grouped_report(trade_data, 'margin')
        verbose_report(trade_data)
    else:
        print("Pass the csv report file!")

