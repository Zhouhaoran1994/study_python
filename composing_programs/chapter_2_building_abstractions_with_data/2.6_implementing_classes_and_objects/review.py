def make_instance(cls):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_value(instance, value)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_value(instance, value):
    if callable(value):
        def method(*args):
            return value(instance, *args)

        return method
    else:
        return value


def make_class(attributes, base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = base_class['get'](name)
            return value

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    cls = {'get': get_value, 'set': set_value, 'new': new}
    return cls


def init_instance(cls, *args):
    init = cls['get']('__init__')
    if init:
        init(cls, *args)
    instance = make_instance(cls)
    return instance


def make_account_class():
    interest = 0.02

    def __init__(self, holder_name):
        self['set']('balance', 0)
        self['set']('holder_name', holder_name)

    def deposit(self, amount):
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return new_balance

    return make_class(locals())


def get_account_holder(account):
    return account['get']('holder_name')


def deposit(account, amount):
    return account['get']('deposit')(amount)


def check_balance(account):
    return account['get']('balance')


Account = make_account_class()
bill_account = Account['new']('Bill')
print(get_account_holder(bill_account))
print(check_balance(bill_account))
print(deposit(bill_account, 150))


def make_checking_account_class():
    interest = 0.01
    deposit_fee = 1

    def deposit(self, amount):
        deposit_fee = self['get']('deposit_fee')
        return Account['get']('deposit')(self, amount - deposit_fee)

    return make_class(locals(), Account)


CheckingAccount = make_checking_account_class()
jack_account = CheckingAccount['new']('Spock')
print(deposit(jack_account, 50))
