a = 1
b = a
b = b + 10
print(a, b)

q = [1, 2]
o = q
o.append('hhh')
print(q, o)

nest = [1, 2]
suits = ['heart', 'diamond', 'spade', 'club']
nest[0] = suits
print(suits is nest[0])
print(suits is ['heart', 'diamond', 'spade', 'club'])
print(suits == ['heart', 'diamond', 'spade', 'club'])

dic_coms = {x:y for x in 'abcd' for y in 'ABCD'}
print(dic_coms)


def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""

    def withdraw(amount):
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance

    return withdraw

wd = make_withdraw(100)
wd(5)