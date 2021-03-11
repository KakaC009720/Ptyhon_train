import time

s = eval(input())

ans = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(s))
ans1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(s))
print(ans)
print(ans1)