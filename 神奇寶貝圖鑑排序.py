class Pokemon:
    def __init__(self, name, lv, hp):
        self.Name = name
        self.Lv = lv
        self.Hp = hp
    def __gt__(self, tar):
        if self.Name > tar.Name:
            return True
        else:
            return False
    def show(self):
        print('Name:', self.Name)
        print('Lv:', self.Lv)
        print('HP:', self.Hp)

def topName(pkms):
    maxP = pkms[0]
    minP = pkms[0]
    midP = pkms[0]
    pkms.sort()
    for i in pkms:
        i.show()
        print()

def topLv(pkms):
    maxP = pkms[0]
    minP = pkms[0]
    midP = pkms[0]
    for i in pkms:
        if i.Lv > maxP.Lv:
            maxP = i

    for i in pkms:
        if i.Lv < minP.Lv:
            minP = i
    
    for i in pkms:
        if i.Lv != maxP.Lv and i.Lv != minP.Lv:
            midP = i
    minP.show()
    print()
    midP.show()
    print()
    maxP.show()
    print()

def topHP(pkms):
    maxP = pkms[0]
    minP = pkms[0]
    midP = pkms[0]
    for i in pkms:
        if i.Hp > maxP.Hp:
            maxP = i

    for i in pkms:
        if i.Hp < minP.Hp:
            minP = i
    
    for i in pkms:
        if i.Hp != maxP.Hp and i.Hp != minP.Hp:
            midP = i
    minP.show()
    print()
    midP.show()
    print()
    maxP.show()
    print()

def order(pkms):
    for i in pkms:
        i.show()
        print()

    
num = int(input())
pst = []
for i in range(num):
    name = input()
    lv = int(input())
    hp = int(input())
    p = Pokemon(name, lv, hp)
    pst.append(p)

num2 = int(input())
if num2 == 0:
    order(pst)
elif num2 == 1:
    topName(pst)
elif num2 == 2:
    topLv(pst)
elif num2 == 3:
    topHP(pst)