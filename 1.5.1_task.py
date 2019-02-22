class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.in_box = 0

    def can_add(self, v):
        if self.capacity >= self.in_box + v:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v) is True:
            self.in_box += v
        else:
            return False


a = MoneyBox(10)

print(a.add(11))

