final = []


aa = int(input())

for i in range(aa):
    s = input()
    s1 = []
    count = []
    ans = 0
    num = 0
    for i in range(len(s)):
        if s[i] == '(' or s[i] == ')' or s[i] == '[' or s[i] == ']' or s[i] == '{' or s[i] == '}' or s[i] == '<' or s[i] == '>':
            s1.append(s[i])
    #print(s1)
    if len(s1) % 2 != 0:
        final.append('N')
    else:
        for i in range(len(s1)):
            
            if s1[i] == '(' or s1[i] == '[' or s1[i] == '{' or s1[i] == '<':
                count.append(s1[i])
                num += 1
                ans += 1
            elif s1[i] == ')':
                num -= 1
                if num < 0:
                    #print('N')
                    break
                else:
                    if count.pop() != '(':
                        #print('N')
                        break
                    else:
                        ans -= 1

            elif s1[i] == ']':
                num -= 1
                if num < 0:
                    #print('N')
                    break
                else:
                    if count.pop() != '[':
                        #print('N')
                        break
                    else:
                        ans -= 1

            elif s1[i] == '}':
                num -= 1
                if num < 0:
                    #print('N')
                    break
                else:
                    if count.pop() != '{':
                        #print('N')
                        break
                    else:
                        ans -= 1

            elif s1[i] == '>':
                num -= 1
                if num < 0:
                    #print('N')
                    break
                else:
                    if count.pop() != '<':
                        #print('N')
                        break
                    else:
                        ans -= 1
        
        #print(num, ans)
        if num == 0 and ans ==0:
            final.append('Y')
        else:
            final.append('N')
    
for i in range(len(final)):
    print(final[i])