def romanToInt(str):
    ans = 0
    for i in range(len(str)):
        ans = ans + change(str[i])
        if str[i] == 'I':
            if (i+1) < len(str):
                if str[i+1] == 'V' or str[i+1] == 'X':
                    ans = ans - 2
        if str[i] == 'X':
            if (i+1) < len(str):
                if str[i+1] == 'L' or str[i+1] == 'C':
                    ans = ans - 20
        if str[i] == 'C':
            if (i+1) < len(str):
                if str[i+1] == 'D' or str[i+1] == 'M':
                    ans = ans - 200
    return ans
def change(s):
    if s == 'I':
        return 1
    elif s == 'V':
        return 5
    elif s == 'X':
        return 10
    elif s == 'L':
        return 50
    elif s == 'C':
        return 100
    elif s == 'D':
        return 500
    elif s == 'M':
        return 1000


str = 'III'
print(romanToInt(str)) 