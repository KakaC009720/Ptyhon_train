def fauc(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum
def P(n,m):
    if n < m:
        return 0
    else:
        return fauc(n) // fauc(n-m)
def C(n,m):
    if n < m:
        return 0
    else:
        return fauc(n) // fauc(m) // fauc(n-m)

a = int(input())
b = int(input())

print(P(a, b))
print(C(a, b))