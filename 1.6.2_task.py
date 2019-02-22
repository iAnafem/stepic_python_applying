class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            self.append(self.pop(-1) + self.pop(-1))

    def sub(self):
        if len(self) >= 2:
            self.append(self.pop(-1) - self.pop(-1))

    def mul(self):
        if len(self) >= 2:
            self.append(self.pop(-1) * self.pop(-1))

    def div(self):
        if len(self) >= 2:
            self.append(self.pop(-1) // self.pop(-1))


