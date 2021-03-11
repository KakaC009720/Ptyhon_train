def transform(lst):
    coco = 0
    ans = ''
    ex = ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']
    #print(lst)
    for i in range(len(lst)):
        
        for j in range(len(ex)):
            if lst[i] == ex[j]:
                ans = ans + str(j)
                #print(lst[i], ex[j])
                break
            elif lst[i] not in ex:
                coco += 1
                #ans = 'error'
                break
        if coco > 0:
            ans = 'error'
            break
    
    return ans


test = []
final = []
while True:
    s = input()
    lst = []
    if s == '-1':
        break
    else:
        test = s.split(' ')

    for i in range(len(test)):
        count = 0
        #for j in range(len(test[i])):
            #if test[i][j] != '.' and test[i][j] != '-':
            #    count += 1
        #if count == 0:
        if test[i] != '':
            lst.append(test[i])

    final.append(transform(lst))
    

for i in range(len(final)):
    print(final[i])