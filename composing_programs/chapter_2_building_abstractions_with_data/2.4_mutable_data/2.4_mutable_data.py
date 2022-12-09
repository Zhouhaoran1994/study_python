a = 1
b = a
b += 1
print(a, b) # 1, 2

a = [1, 2]
b = a
b += [3]
print(a, b) #[1, 2, 3] [1, 2, 3]

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
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance

    return withdraw

wd = make_withdraw(100)
wd(5)