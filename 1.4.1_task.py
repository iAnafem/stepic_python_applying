class NameSpace(list):
    names = {"global": ["None"], "None": []}

    def create(self, space, parent):
        self.names[parent].append(space)
        self.names[space] = [parent]
        print(self.names)

    def add(self, space, var):
        self.names[space].append(var)
        print(self.names)

    def get(self, space, var):
        if space == "None":
            print(self.names)
            return
        if var in self.names[space]:
            print(space)
            print(self.names)
            return
        elif self.names[space][0] != "None":
            self.get(self.names[space][0], var)
            print(self.names)
            return
        else:
            print(self.names)
            print("None")
        return


a = NameSpace()
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == "add":
        a.add(s[1], s[2])
    elif s[0] == "create":
        a.create(s[1], s[2])
    else:
        a.get(s[1], s[2])
