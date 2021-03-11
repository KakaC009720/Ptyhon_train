class Pokemon:
    def __init__(self, name, lv, hp):
        self.Name = name
        self.Lv = lv
        self.Hp = hp
    def __gt__(self, tar):
        if self.Lv > tar.Lv:
            return True
        else:
            return False
    def show(self):
        print('Name:', self.Name)
        print('Lv:', self.Lv)
        print('HP:', self.Hp)
'''
def topLvPokemon(pkms):
    maxP = pkms[0]
    for p in pkms:
        if p > maxP:
            maxP = p
    return maxP
'''
pst = []
for i in range(3):
    name = input()
    lv = int(input())
    hp = int(input())
    p = Pokemon(name, lv, hp)
    pst.append(p)

topPkm = max(pst)
topPkm.show()