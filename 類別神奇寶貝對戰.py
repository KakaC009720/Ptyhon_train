class Pokemon:
    def __init__(self, name, lv, hp):
        self.Name = name
        self.Lv = lv
        self.HpMax = hp
        self.HpCurrent = hp
    def Attack(self, tar):
        if self.setData(self.Name, self.Lv, self.HpCurrent):
            print(self.Name, 'Attack', tar.Name, self.Lv, 'Points.')
            if tar.Defence(self.Lv):
                return True
            else:
                print(self.Name, 'Win,', tar.Name, 'Lose.')
                return True
        else:
            print(self.Name, 'is unable to attack.')
            return False
    def Defence(self, dmg):
        self.HpCurrent -= dmg
        if self.setData(self.Name, self.Lv, self.HpCurrent):
            return True
        else:
            print(self.Name, 'Seriously Injured.')
    def Cure(self):
        self.HpCurrent = self.HpMax
    def setData(self, name, lv, hp):
        if self.HpCurrent <= 0:
            self.HpCurrent = 0            
            return False
        else:
            return True
    def ShowInfo(self):
        print('Name:', self.Name)
        print('Lv:', self.Lv)
        print('HP:', str(self.HpCurrent) + '/' + str(self.HpMax))


pst = []
num = 1
count = int(input())
for i in range(count):
    name = input()
    lv = int(input())
    hp = int(input())
    p = Pokemon(name, lv, hp)
    pst.append(p)

enemy = Pokemon('Mewtwo', 30, 300)
#pst.append(enemy)
for i in pst:
    print('#' + str(num))
    num += 1
    enemy.Cure()
    while True:
        if i.Attack(enemy) == False:
            break
        if enemy.Attack(i) == False:
            break
    enemy.ShowInfo()
    i.ShowInfo()
    print()