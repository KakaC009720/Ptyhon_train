n = int(input())
sum = 0

for i in range(1, n+1):
    a = n%i
    if a == 0:
        sum = sum + i
    else:
        pass

if sum == n + 1:
    print(n, "is prime")
else:
    print(n, "is not prime")