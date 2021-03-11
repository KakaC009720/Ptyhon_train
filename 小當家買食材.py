lst = []
dict = {}
l1 = []
l2 = []
big = 0
n = eval(input())
for i in range(n):
    n1 = input().split()
    lst.append(n1)

    #若key已存在，value相加；key若不存在，則新增
    if n1[0] in dict:
        a = dict[n1[0]]
        b = eval(a) + eval(n1[1])
        
        dict[n1[0]] = str(b)

    else:
        dict[n1[0]] = n1[1]
    
#print(dict)

for key, value in dict.items():
    l1.append(key)
    l2.append(value)


#print(l1)
#print(l2)
l3 = l2.copy()
for i in range(len(l3)):
    num = eval(l3.pop())
    if num > big:
        big = num

for i in range(len(l2)):
    #print(type(l2[i]))
    #print(type(big))
    if l2[i] == str(big):
        print(l1[i], l2[i])