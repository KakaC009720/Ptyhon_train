n = int(input())
ans = n
change = n // 4
left = n % 4
ans = ans + change

while True:
    if (change + left) >= 4:
        change2 = (change + left) // 4
        left2 = (change + left) % 4
        ans = ans + change2
        change = change2
        left = left2
    elif (change + left) == 3:
        ans = ans +1
        print(ans)
        break
    else:
        print(ans)
        break