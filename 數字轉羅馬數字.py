def romanToInt(num):
    dict = {}
    dict['0'] = ''
    dict['00'] = ''
    dict['000'] = ''
    dict['1'] = 'I'
    dict['2'] = 'II'
    dict['3'] = 'III'
    dict['4'] = 'IV'
    dict['5'] = 'V'
    dict['6'] = 'VI'
    dict['7'] = 'VII'
    dict['8'] = 'VIII'
    dict['9'] = 'IX'
    dict['10'] = 'X'
    dict['20'] = 'XX'
    dict['30'] = 'XXX'
    dict['40'] = 'XL'
    dict['50'] = 'L'
    dict['60'] = 'LX'
    dict['70'] = 'LXX'
    dict['80'] = 'LXXX'
    dict['90'] = 'XC'
    dict['100'] = 'C'
    dict['200'] = 'CC'
    dict['300'] = 'CCC'
    dict['400'] = 'CD'
    dict['500'] = 'D'
    dict['600'] = 'DC'
    dict['700'] = 'DCC'
    dict['800'] = 'DCCC'
    dict['900'] = 'CM'
    dict['1000'] = 'M'
    dict['2000'] = 'MM'
    dict['3000'] = 'MMM'
    ans = ''
    lengh = len(str(num))
    if lengh == 1:
        ans = dict[str(num)]
    elif lengh == 2:
        ten = str(num)[0] + '0'
        digit = str(num)[1]
        ans = dict[ten] + dict[digit]
    elif lengh == 3:
        hun = str(num)[0] + '00'
        ten = str(num)[1] + '0'
        digit = str(num)[2]
        ans = dict[hun] + dict[ten] + dict[digit]
    elif lengh == 4:
        thu = str(num)[0] + '000'
        hun = str(num)[1] + '00'
        ten = str(num)[2] + '0'
        digit = str(num)[3]
        ans = dict[thu] + dict[hun] + dict[ten] + dict[digit]
    return ans

num = 1000
print(romanToInt(num))