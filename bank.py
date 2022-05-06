from typing import List, Optional
from time import sleep

from models.client import Client
from models.account import Account

accounts: List[Account] = []


def menu() -> None:
    print('',
          50*'=',
          '  ATM  '.center(50, '='),
          '  Gratieri\'s Bank  '.center(50, '='),
          50*'=',
          sep='\n')

    print('Select an option from the menu below:',
          '1 - Create account',
          '2 - Make withdrawal',
          '3 - Make deposit',
          '4 - Make transfer',
          '5 - Show accounts',
          '6 - Exit to system', sep='\n')

    try:
        option = int(input())
    except ValueError:
        print('Invalid option! Try again.')
        sleep(1)
        menu()

    match option:
        case 1:
            create_an_account()
        case 2:
            make_withdrawal()
        case 3:
            make_deposit()
        case 4:
            make_transfer()
        case 5:
            show_accounts()
        case 6:
            print('Check back often!')
            sleep(2)
            exit(0)
        case _:
            print('Invalid option. Try again.')
            sleep(1)
            menu()


def create_an_account() -> None:
    print('Enter customer data:')

    name: str = input('Name: ')
    email: str = input('Email: ')
    cpf: str = input('CPF: ')
    birth_date: str = input('Birth date: ')

    client: Client = Client(name, email, cpf, birth_date)
    account: Account = Account(client)

    accounts.append(account)

    print('Account created successfully.')
    print('  Account data  '.center(50, '-'), 50*'=', sep='\n')
    print(account)
    sleep(2)
    menu()


def make_withdrawal() -> None:
    if len(accounts) > 0:
        try:
            number: int = int(input('Enter a number account: '))
        except ValueError:
            print('Number invalid. Enter only numbers.')
            sleep(1)
            menu()

        account: Account = search_account_by_number(number)

        if account:
            try:
                value: float = float(input('Enter the amount you want to withdraw: '))
            except ValueError:
                print('Number invalid. Enter only numbers.')
                sleep(1)
                menu()

            account.withdraw(value)
        else:
            print(f'Account number {number} was not found.')
    else:
        print('There are no registered accounts yet.')
    sleep(1)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        try:
            number: int = int(input('Enter a number account: '))
        except ValueError:
            print('Number invalid. Enter only numbers.')
            sleep(1)
            menu()

        account: Account = search_account_by_number(number)

        if account:
            try:
                value: float = float(input('Enter the amount you want to deposit: '))
            except ValueError:
                print('Number invalid. Enter only numbers.')
                sleep(1)
                menu()
            account.deposit(value)
        else:
            print(f'Account number {number} was not found.')
    else:
        print('There are no registered accounts yet.')
    sleep(1)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        try:
            o_number: int = int(input('Enter your account number: '))       # origin account number
        except ValueError:
            print('Number invalid. Enter only numbers.')
            sleep(1)
            menu()

        o_account: Account = search_account_by_number(o_number)     # origin account

        if o_account:
            try:
                d_number: int = int(input('Enter destination account number: '))    # destiny account number
            except ValueError:
                print('Number invalid. Enter only numbers.')
                sleep(1)
                menu()

            d_account: Account = search_account_by_number(d_number)     # destiny account

            if d_account:
                try:
                    value: float = float(input('Enter the amount you want to deposit: '))
                except ValueError:
                    print('Number invalid. Enter only numbers.')
                    sleep(1)
                    menu()
                o_account.transfer(d_account, value)
            else:
                print(f'Account number {d_number} was not found.')
        else:
            print(f'Account number {o_number} was not found.')
    else:
        print('There are no registered accounts yet.')
    sleep(1)
    menu()


def show_accounts() -> None:
    if accounts:
        print('  All accounts  '.center(50, '='))

        for account in accounts:
            print(account, 50*'-', sep='\n')

    else:
        print('There are no registered accounts yet.')
    sleep(1)
    menu()


def search_account_by_number(number: int) -> Account:
    c: Optional[Account] = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                c = account
    return c


def main() -> None:
    menu()


if __name__ == '__main__':
    main()
