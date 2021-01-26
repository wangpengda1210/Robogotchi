class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = 0
        self.cents = 0
        self.add_money(dollars, cents)

    def add_money(self, deposit_dollars, deposit_cents):
        self.cents += deposit_cents
        self.dollars += deposit_dollars + self.cents // 100
        self.cents -= self.cents // 100 * 100
