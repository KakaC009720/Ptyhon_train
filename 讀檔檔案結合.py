a = input()
b = input()
s1="../app/"+a
s2="../app/"+b
f1 = open(s1, 'r')
content1 = f1.read()
gg1 = content1.split(' ')
f1.close()
lst = []
for i in range(len(gg1)-1):
    lst.append(int(gg1[i]))

f2 = open(s2, 'r')
content2 = f2.read()
gg2 = content2.split(' ')
f2.close()
for i in range(len(gg2)-1):
    lst.append(int(gg2[i]))

lst.sort()
for i in range(len(lst)):
    print(lst[i], end = ' ')