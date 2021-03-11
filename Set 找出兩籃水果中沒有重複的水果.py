itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}

n = input()
itemsA.add(n)
n1 = input()
itemsA.add(n1)
itemsA.remove('蘋果')
n2 = input()
itemsB.add(n2)
n3 = input()
itemsB.add(n3)
itemsB.remove('蓮霧')

lsta = list(itemsA)
lsta.sort()
print('iA: ', end = '')
print(lsta)
lstb = list(itemsB)
lstb.sort()
print('iB: ', end = '')
print(lstb)

u = itemsA.union(itemsB)
i = itemsA.intersection(itemsB)
da = itemsA.difference(itemsB)
db = itemsB.difference(itemsA)
xor = u - i
lst = list(u)
lst.sort()
print('union: ', end = '')
print(lst)
lst1 = list(i)
lst1.sort()
print('intersection: ', end = '')
print(lst1)
lst2 = list(da)
lst2.sort()
print('A diff B: ', end = '')
print(lst2)
lst3 = list(db)
lst3.sort()
print('B diff A: ', end = '')
print(lst3)
lst4 = list(xor)
lst4.sort()
print('A xor B: ', end = '')
print(lst4)