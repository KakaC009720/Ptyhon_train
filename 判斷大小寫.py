n = eval(input())
a = 0
b = 0
c = 0
for i in range(n):
    n1 = input()
    if n1.isupper():
        a = a + 1
    elif n1.islower():
        b = b + 1
    else:
        c = c + 1

print(b, a, c)