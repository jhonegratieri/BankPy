from models.client import Client
from models.account import Account

gabi: Client = Client('Gabi', 'gabi123@123.com', '123.456.678-90', '01/04/1998')
jhone: Client = Client('Jhone', 'jhone321@321.com', '098.876.543-21', '01/04/1999')

# print(jhone, gabi)

account1: Account = Account(gabi)
account2: Account = Account(jhone)

# print(account1, account2, sep=2*'\n')
