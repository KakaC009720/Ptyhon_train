s = input()
f1 = open(s, 'r')
txtLst = f1.readlines()
f1.close()
re = 0
ele = 0
for i in range(1, len(txtLst)):
    txtLst[i] = txtLst[i].strip().split(',')
    if txtLst[i][1] == 'R' and txtLst[i][3] != 'F':
        re += int(txtLst[i][2])
    if txtLst[i][1] == 'E' and txtLst[i][3] != 'F':
        ele += int(txtLst[i][2])
#print(re, ele)
ans = 72 - re
ans1 = 28 - ele
if re == 72 and ele >= 28:
    print('Required:', re)
    print('Elective:', ele)
    print('Y')
elif re < 72 and ele >= 28:
    print('Required:', re)
    print('Elective:', ele)
    print('N')
    print('Student still needs to complete', ans, 'required credits for graduation.')
elif re == 72 and ele < 28:
    print('Required:', re)
    print('Elective:', ele)
    print('N')
    print('Student still needs to complete', ans1, 'elective credits for graduation.')
elif re < 72 and ele < 28:
    print('Required:', re)
    print('Elective:', ele)
    print('N')
    print('Student still needs to complete', ans, 'required credits &', ans1, 'elective credits for graduation.')