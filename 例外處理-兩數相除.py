while True:
    try:
        a = eval(input())
        b = int(input())
        c = a/b

        print('%d/%d = %.2f'%(a, b, c))
        break
    
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except SyntaxError:
        print('SyntaxError')
    except NameError:
        print('NameError')
    except ValueError:
        print('ValueError')