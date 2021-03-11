while True:
    n = input()
    if n == '-1':
        break
    else:
        for i in range(len(n)):
            #if n[i] != ' ':
            if n[i] != ',' and n[i] != '.' and n[i] != "'" and n[i] != ' ':
                two = bin(ord(n[i]))
                two = two[2:]
                print(two, end = ',')
            else:
                two = bin(ord(n[i]))
                two = two[2:]
                print('0'+ two, end = ',')
        print()