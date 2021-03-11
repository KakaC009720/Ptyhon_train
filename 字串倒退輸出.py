n = input()
a = n.count(';')
n = n[::-1]
s = n.split(sep = ';')

for i in range(a+1):
    if i != 0:
        print(' ', end = '')
    print(s[i], end = '')