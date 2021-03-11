def matrixMultiPly(a, b) :
    c=[[],[],[]]
    for i in range(3):
        for j in range(3):
            cans=0
            for k in range(3):
                cans+=a[i][k]*b[k][j]
            c[i].append(cans)           
 
    return c
 
a=[]
b=[]
 
a1=input().strip().split()
a2=input().strip().split()
a3=input().strip().split()
b1=input().strip().split()
b2=input().strip().split()
b3=input().strip().split()
 
for i in range(len(a1)):
    a1[i]=eval(a1[i])
a.append(a1)  
for i in range(len(a2)):
    a2[i]=eval(a2[i])
a.append(a2)
for i in range(len(a3)):
    a3[i]=eval(a3[i])
a.append(a3)
 
for i in range(len(b1)):
    b1[i]=eval(b1[i])
b.append(b1)
for i in range(len(b2)):
    b2[i]=eval(b2[i])
b.append(b2)
for i in range(len(b3)):
    b3[i]=eval(b3[i])
b.append(b3)
 
matrixMultiPly(a,b)
print(matrixMultiPly(a,b)[0])
print(matrixMultiPly(a,b)[1])
print(matrixMultiPly(a,b)[2])