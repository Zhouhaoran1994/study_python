'''
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
        nonlocal balance  # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount  # Re-bind the existing balance name
        return balance

    return withdraw


wd1 = make_withdraw(100)
# wd2 = make_withdraw(5)
wd2 = wd1
print(wd2(1))
print(wd1(5))

q = 1
e = 1
print(id(q), id(e))
print(q is e)


def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': initial_balance
    }

    return dispatch


a = account(100)
print(a['deposit'](50))
print(a['deposit'](50))
b = account(200)
print(b['withdraw'](100))
print(b['withdraw'](100))

'''

from operator import add, sub, mul, truediv


def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)


def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""

    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)

    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint


def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)

    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector


def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()


if __name__ == '__main__':
    celsius = connector('Celsius')
    fahrenheit = connector('Fahrenheit')
    converter(celsius, fahrenheit)
    celsius['set_val']('user', 25)

