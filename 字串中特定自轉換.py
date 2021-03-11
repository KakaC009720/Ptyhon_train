text = ''
sen = ''
intab = 'defghijklmnopqrstuvwxyzabc'
outtab = 'abcdefghijklmnopqrstuvwxyz'
trantab = str.maketrans(intab, outtab)
while True:
    n1 = input()
    if n1 == '-1':
        break
    n = n1.lower()
    text = n.translate(trantab)
    sen = sen + ' ' + text

print(sen.lstrip())