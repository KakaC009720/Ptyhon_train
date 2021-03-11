f1 = open('../app/math_list.csv', 'r', encoding = 'big5')
txtLst = f1.readlines()
f1.close()
math_list = []
for i in range(1, len(txtLst)):
    txtLst[i] = txtLst[i].strip().split(',')
    math_list.append(txtLst[i][0])
#print(math_list)

f2 = open('../app/english_list.csv', 'r', encoding = 'big5')
txtLst2 = f2.readlines()
f2.close()
english_list = []
for i in range(1, len(txtLst2)):
    txtLst2[i] = txtLst2[i].strip().split(',')
    english_list.append(txtLst2[i][0])
#print(english_list)
lst1 = []
lst5 = []
for i in range(len(math_list)):     #######兩門課都有修
    if math_list[i] in english_list:
        lst1.append(math_list[i])
        lst5.append(math_list[i])

lst2 = []
lst3 = []
lst4 = []
for i in range(len(math_list)):       ####只修數學
    if math_list[i] not in english_list:
        lst2.append(math_list[i])
        lst3.append(math_list[i])
        lst5.append(math_list[i])
for i in range(len(english_list)):    ####只修英文
    if english_list[i] not in math_list:
        lst2.append(english_list[i])
        lst4.append(english_list[i])
        lst5.append(english_list[i])
lst1.sort()
print(lst1)
lst2.sort()
print(lst2)
lst3.sort()
print(lst3)
lst4.sort()
print(lst4)
lst5.sort()
print(lst5)