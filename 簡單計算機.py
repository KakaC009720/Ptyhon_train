n = input()
n2 = input()
operator = input()
n = float(n)
n2 = float(n2)

ans = None
if operator == "+":
    ans = n + n2
elif operator == "-":
    ans = n - n2
elif operator == "*":
    ans = n * n2
elif operator == "/":
    ans = n / n2

print("%.2f" %n, operator, "%.2f" %n2, "=", end=' ')
print("%.2f" %ans)