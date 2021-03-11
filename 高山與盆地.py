big = 0
bignum = 0
small = 0
smallnum = 0

n = eval(input())
n1 = input().split()

for i in range(len(n1)):
    
    if i == 0:
        small = eval(n1[i])
        big = eval(n1[i])
        smallnum = i
        bignum = i
    #print(type(big))
    #print(type(small))
    if eval(n1[i]) > big:
        #print('yes')
        big = n1[i]
        big = eval(big)
        bignum = i
 
    elif eval(n1[i]) < small:
        small = n1[i]
        small = eval(small)
        smallnum = i
        
bignum += 1
smallnum += 1
print(bignum, big)
print(smallnum, small)