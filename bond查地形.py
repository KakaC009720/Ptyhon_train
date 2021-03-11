n = int(input())
s = input()
lst = s.strip().split(' ')
#print(lst)
top = 0
bot = 0

for i in range(1, len(lst)-1):
    if int(lst[i-1]) < int(lst[i]) and int(lst[i]) > int(lst[i+1]):
        top += 1
        #print('top:', i)
    elif int(lst[i-1]) > int(lst[i]) and int(lst[i]) < int(lst[i+1]):
        bot += 1
        #print('bot:', i)

print(top)
print(bot)