class Account:
    interest = 0.01

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder


if __name__ == '__main__':
    spock_account = Account('Spock')
    kirk_account = Account('Kirk')
    kirk_account.interest = 0.05
    Account.interest = 10
    print(spock_account.interest, kirk_account.interest)
    spock_account.interest = 'a'
    print(spock_account.interest, kirk_account.interest)
    Account.interest = 1
    print(spock_account.interest, kirk_account.interest)
