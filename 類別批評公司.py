class Data:
    def __init__(self, ai, bi, ci):
        self.ai = int(ai)
        self.bi = int(bi)
        self.ci = int(ci)
        self.d = 0
    def show(self):
        print(self.ai, self.bi, self.ci, self.d)
    def fight(self, tar):
        if self.ai > tar.ai and self.bi > tar.ci:
            tar.d = 1
lst = []
lst2 = []
num = int(input())
for i in range(num):
    s = input().split()
    x = Data(s[0], s[1], s[2])
    lst.append(x)

first = int(input())
firstd = lst[first - 1]
firstd.d = 1

for i in lst:
    firstd.fight(i)
    if i.d == 1:
        for j in lst:
            i.fight(j)

count = 0
for i in lst:
    if i.d == 1:
        count += 1
print(count)