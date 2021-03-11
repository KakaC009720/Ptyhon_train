s = input()
lst1 = []
lst2 = []
pos = []
A = 0
B = 0


for i in range(len(s)//2):    ###前n個是正確答案
    lst1.append(s[i])
for i in range(len(s)//2 + 1, len(s)):  ###後n個是猜的
    lst2.append(s[i])

for i in range(len(lst1)):  ###先判斷一樣的(A)
    if lst1[i] == lst2[i]:
        A += 1
        pos.append(i)

#print('pos: ', pos)  ###一樣的位置
for i in range(len(pos)):    ###一樣的用'_'取代，將lst改掉避免再判斷B時重複的數會出錯
    for j in range(len(lst1)):
        if j == pos[i]:
            lst1[j] = '_'
            lst2[j] = '-'
#print(lst1)
#print(lst2)

for i in range(len(lst2)):   ###判斷(B)
    if lst1[i] in lst2:
        B += 1
        for j in range(len(lst2)):  ###屬於B後，將該數以@替代
            if lst2[j] == lst1[i]:
                lst2[j] = '@'
                break ###若有重複的數，防止刪到兩次，替代一個後就停止
#print(lst1)
#print(lst2)

print(str(A) + 'A' + str(B) + 'B')