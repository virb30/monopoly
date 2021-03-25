import random


class OutOfMoney(Exception):
    pass


class NotEnoughMoney(Exception):
    pass


class AbortInvestment(Exception):
    pass


class Impulsive:
    def __call__(self, *args, **kwargs):
        return True


class Demanding:
    def __call__(self, balance, price, rent):
        return rent > 50


class Cautious:
    def __call__(self, balance, price, rent):
        return balance - price >= 80


class Gambler:
    def __call__(self, balance, price, rent):
        return random.choice((True, False))


class Player:
    def __init__(self, initial_balance, strategy=Impulsive()):
        self.balance = initial_balance
        self.strategy = strategy

    def pay(self, amount):
        if amount > self.balance:
            raise OutOfMoney(repr(self))

        self.balance -= amount
        return amount

    def receive(self, amount):
        self.balance += amount

    def invest(self, price, rent):
        if price > self.balance:
            raise NotEnoughMoney(f'{self!r} can not aford {price}')

        if not self.strategy(self.balance, price, rent):
            raise AbortInvestment(f'{self!r} aborted')

        return self.pay(price)

