from datetime import date, datetime


def date_to_str(date1: date) -> str:
    return date1.strftime('%d/%m/%Y')


def str_to_date(date1: str) -> date:
    return datetime.strptime(date1, '%d/%m/%Y')


def float_to_str_coin(value: float) -> str:
    return f'R$ {value:,.2f}'
