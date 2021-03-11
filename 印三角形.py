n = int(input())
b = n
c = 0
for i in range(0, n):
    for j in range(b-1, 0, -1):
        print(" ", end = '')
    
    b = b-1
    for k in range(0, c+1):
        print("*", end = '')
    c = c + 1
    
    print()