dict = {'T':'Top', 'H':'Hoodie', 'B':'Backpack'}
while True:

    
    lst = list(dict.keys())
    lst.sort()
    
    lst1 = list(dict.values())
    lst2 = sorted(lst1, key = str.lower) ###########
    
    n = input()
    if n == '-1':
        break
    elif n == '-2':
        
        print('keys: ', end = '')
        print(lst)
        
        
        print('values: ', end = '')
        print("[", end = "")
        for i in range(len(lst)):
            print("'", end = '')
            print(dict[lst[i]], end = "'")
            if i < len(lst)-1:
                print(",", end = ' ')
        print(']')
    elif n == '-3':
        n2 = input()
        if n2 in dict:
            del dict[n2]
        else:
            print('key ' + n2 + ' does not exist, cannot delete.')
    elif n in dict:
        print(dict[n])
    else:
        ndata = input(n + ' does not exist. Enter a new product category:\n')
        dict[n] = ndata