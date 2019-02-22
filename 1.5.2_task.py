class Buffer:
    def __init__(self):
        self.lst = list()
        self.capacity = 5

    def add(self, *a):
        for item in a:
            self.lst.append(item)
        if len(self.lst) < self.capacity:
            return
        else:
            while len(self.lst) >= self.capacity:
                print(sum(self.lst[0:self.capacity]))
                del self.lst[0:self.capacity]

    def get_current_part(self):
        return self.lst
