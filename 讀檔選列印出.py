s1 = 'stores_old.csv'
f1 = open(s1, 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip().split(',')

printdata = (0, 3, 5, 6)
for i in range(len(txtLst)):

    for j in range(len(txtLst[i])):
        if j in printdata:
            print(txtLst[i][j] + ',', end = '')
    print()