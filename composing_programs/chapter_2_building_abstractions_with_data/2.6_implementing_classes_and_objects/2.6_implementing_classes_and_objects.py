def make_instance(cls):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}
    instance = {'get': get_value, 'set': set_value}
    return instance


def bind_method(value, instance):
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
            return base_class['get'](name)

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

    def __init__(self, name, age):
        self['set']('holder', name)
        self['set']('balance', 0)
        self['set']('age', age)

    def deposit(self, amount):
        new_balance = self['get']('balance') + amount
        self['set']('balance', new_balance)
        return self['get']('balance')

    # dispatch = {'deposit': deposit}
    return make_class(locals())


Account = make_account_class()
jack_account = Account['new']('Jack', 9)
print(jack_account['get']('balance'))
jack_account['get']('deposit')(50)
print(jack_account['get']('balance'))
print(jack_account['get']('age'))


