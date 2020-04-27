class MoneyBox:
    def __init__(self, capacity, coin_value=0):
        self.capacity = capacity
        self.coin_value = coin_value

    def can_add(self, v):
        if self.capacity - self.coin_value >= v:
            return True
        else:
            return False

    def add(self, coin):
        self.coin_value += coin

