n1 = eval(input())
dick = {}
ll = []
big = 0
bad = []
bigord = 0
for j in range(n1):
    n = input()
    n = n.upper()
    ll.append(n)
    lst = []
    sum = 0
    for i in range(len(n)):
        lst.append(n[i])
    for i in range(len(lst)):
        x = (ord(lst[i])-64)
        sum = x + sum
        if i == 0:
            bad.append(x)
    #print(n)
    dick[n] = sum    
    if sum > big:
        big = sum
        bigord = j
    elif sum == big:
        #print(bad[bigord], bad[j])
        if bad[bigord] > bad[j]:
            bigord = j
        else:
            continue
    else:
        continue

    
#print(dick)
#print(bad)
#bad.sort()
#print(bad)

for i in range(n1):
    #print(n1)
    #print(dick)
    #print(str(dick[ll[i]]))
    print(ll[i] + ' = ' + str(dick[ll[i]]))

print(ll[bigord] + ' is the key.')