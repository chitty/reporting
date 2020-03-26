import csv
from datetime import datetime

def trim_trash(str_date: str):
    '''
    Get rid of the annoying '(Coordinated Universal Time)' at the end
    '''
    tal = str_date.split(' (')
    return tal[0]

def get_report(file: str):
    '''
    Reads the CVS report file passed and returns a dict with the data
    sorted by `opened_at` date
    '''
    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        result = sorted(
            reader, key = lambda d: datetime.strptime(
                # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                trim_trash(d['closed_at']), '%a %b %d %Y %H:%M:%S %Z%z')
            )
        return result
