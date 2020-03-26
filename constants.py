import os
# Constants
DEPOSIT = int(os.environ.get('DEPOSIT', 0))
BONUS   = int(os.environ.get('BONUS', 0))
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
