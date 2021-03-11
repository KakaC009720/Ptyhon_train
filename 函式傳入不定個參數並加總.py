def add(*nums):
    ans = 0
    for n in nums:
        ans += n
    return ans


n1 = int(input())
n2 = int(input())
n3 = int(input())
qq = add(n1, n2, n3)
print(qq)

n4 = int(input())
n5 = int(input())
qq = add(n4, n5)
print(qq)