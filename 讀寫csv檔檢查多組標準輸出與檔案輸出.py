n = input()
s1 = 'stores_old' + n +'.csv'
s2 = 'stores_new' + n +'.csv'

f1 = open(s1, 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip().split(',')
    #print(txtLst[i])

printdata = (0, 3, 5, 6)
f2 = open(s2, 'w', encoding = 'utf-8')
for i in range(len(txtLst)):
    for j in range(len(txtLst[i])):
        if j in printdata:
            f2.write(txtLst[i][j]+',')
    f2.write('\n')
f2.close()

f3 = open(s2, 'r')
txtLst2 = f3.readlines()
f3.close()

for i in range(len(txtLst2)):
    txtLst2[i] = txtLst2[i].strip().split(',')
    for j in range(len(txtLst2[i])):
        print(txtLst2[i][j], end = '')
        if j < len(txtLst2[i])-1:
            print(',', end = '')
    print()