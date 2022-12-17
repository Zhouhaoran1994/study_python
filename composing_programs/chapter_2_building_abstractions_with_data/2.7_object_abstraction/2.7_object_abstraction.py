from operator import add


class Account:

    def __init__(self, holder_name, balance=[]):
        self.holder_name = holder_name
        self.balance = balance

    def __repr__(self):
        return 'aaa'

    def __bool__(self):
        return self.balance != 0

    def __add__(self, other):
        # return [self.balance[i] + other.balance[i] for i in range(len(self.balance))]
        return list(map(add, self.balance, other.balance))

# a = Account()
# print(a.__repr__())
# print(repr(Account))
# print(a)
if not Account('Jack'):
    print('Jack has nothing')

# rich = Account('rich', 1000)
# poor = Account('poor',20)
# print(rich + poor)

rich = Account('rich', [1000, 2000, 3000])
poor = Account('poor',[10, 20, 30])
print(rich + poor)