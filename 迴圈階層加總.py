a = 0
while True:
    n = input()
    if n.isdigit():
        #print(type(n))
            n = int(n)
            if n > 0:
                sum = 1
                tem = 0
                for i in range(1, n+1):
                    sum = sum * i
                    tem = tem + sum

                print(tem)
                break