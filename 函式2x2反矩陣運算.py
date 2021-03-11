def round_up(value):
 # 替換內建round函式,實現保留2位小數的精確四捨五入
    return round(value * 100) / 100.0

def Matrix_Inverse(MatrixA):
    det = MatrixA[0][0] * MatrixA[1][1] - MatrixA[0][1] * MatrixA[1][0]
    if det != 0:
        a1 = MatrixA[1][1] / det + 0.001
        a2 = -MatrixA[0][1] / det + 0.001
        a3 = -MatrixA[1][0] / det + 0.001
        a4 = MatrixA[0][0] / det + 0.001
        #print(MatrixA[1][1], MatrixA[0][1], MatrixA[1][0], MatrixA[0][0])
        #print('det=', det)
       
        print(round(a1, 1), end = ' ')
        print(round(a2, 1))
        print(round(a3, 1), end = ' ')
        print(round(a4, 1))
    else:
        print('none')

M = []
for i in range(2):
    s = input()
    lst = s.split(' ')
    lst = [int(i) for i in lst]
    M.append(lst)
 
#print(M)

Matrix_Inverse(M)