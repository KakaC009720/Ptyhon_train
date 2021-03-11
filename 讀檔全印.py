s1 = 'stores_old.csv'
f1 = open(s1, 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip()
    print(txtLst[i])