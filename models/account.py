from models.client import Client
from utils.helper import float_to_str_coin


class Account:
    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.code += 1

    def __str__(self: object) -> str:
        return f'Account number: {self.number}' \
               f'\nClient: {self.client.name}' \
               f'\nTotal balance: {float_to_str_coin(self.total_balance)}'

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance += value
            self.total_balance = self._calculate_total_balance
            print('Successful deposit.')
        else:
            print('Error: Deposit a value greater than zero. Try again.')

    def withdraw(self: object, value: float) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining     # remaining is negative number
                self.balance = 0
                self.total_balance = self._calculate_total_balance
                print('Successful withdraw.')
        else:
            print('Withdrawal not carried out. Try again.')

    def transfer(self: object, destination_account: object, value: float) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance -= value
                self.total_balance = self._calculate_total_balance
                destination_account.balance += value
                destination_account.total_balance = destination_account._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.total_balance = self._calculate_total_balance
                destination_account.balance += value
                destination_account.total_balance = destination_account._calculate_total_balance
                self.limit = self.limit + remaining  # remaining is negative number
                print('Successful transfer.')
        else:
            print('The transfer did not take place.. Try again.')
