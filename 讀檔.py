a = input()
s1="../app/"+a
f1 = open(s1, 'r')
content1 = f1.read()

gg1 = content1.split('\n')
lst = []
for i in range(len(gg1)):
    lst.append(gg1[i])
num = len(gg1) // 2
count = 0
total = 0
for i in range(num):
    print('chef', lst[count], lst[count + 1] )
    pay = int(lst[count + 1])
    count = count + 2
    total += pay
avg = total/num
print('Total:', total)
print('Avg:', '%.2f' %avg)