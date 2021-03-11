dict = {'P':'Pikachu', 'M':'Mickey Mouse', 'H':'Hello kitty'}
while True:
    n = input()
    if n == '-1':
        break
    if n in dict:
        print(dict[n])
    else:
        ndata = input(n + ' does not exist. Enter a new one:\n')
        dict[n] = ndata