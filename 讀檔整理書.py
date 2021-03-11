s1 = input()
f1 = open(s1, 'r')
txtLst = f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip().lower().split(',')

dict = {}
lst = []
for i in range(len(txtLst)):
    if txtLst[i][0] in dict:
        dict[txtLst[i][0]] = int(dict[txtLst[i][0]]) + int(txtLst[i][1])
    else:
        dict[txtLst[i][0]] = txtLst[i][1]
        lst.append(txtLst[i][0])

lst.sort()

for i in range(len(lst)):
    if lst[i] in dict:
        print(lst[i], end = ',')
        print(dict[lst[i]])