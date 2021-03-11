def Matrix_T(MatrixA):
    row = len(MatrixA)
    col = len(MatrixA[0])
    for i in range(col):
        for j in range(row):
            print(MatrixA[j][i], end = '')
            if j < row-1:
                print(' ', end = '')
        print()

M = []
while True:
    s = input()
    if s == 'q':
        break
    else:
        
        lst = s.split(' ')
        lst = [int(i) for i in lst]
        M.append(lst)

#print(M)
Matrix_T(M)