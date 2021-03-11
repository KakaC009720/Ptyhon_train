s1 = input()
f1 = open(s1, 'r')
txtLst = f1.readlines()
f1.close()
PISTOL = 0
SMG = 0
SHOTGUN = 0
AR = 0
SNIPER = 0
for i in range(len(txtLst)):
    txtLst[i] = txtLst[i].strip()

for i in range(len(txtLst)):
    if 'PISTOL' in txtLst[i]:
        PISTOL += 1
    elif 'SMG' in txtLst[i]:
        SMG += 1
    elif 'SHOTGUN' in txtLst[i]:
        SHOTGUN += 1
    elif 'AR' in txtLst[i]:
        AR += 1
    elif 'SNIPER' in txtLst[i]:
        SNIPER += 1

print(PISTOL, SMG, SHOTGUN, AR, SNIPER)