from subprocess import call

def option():
    condition = input('1)average.py 2)average reciprocal.py '
                  '\n3)avg of sum of squares.py 4)find correct average.py '
                  '\n5)finding x.py 6)mean average.py '
                      '\nPRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = 'average.py'
    elif condition == '2':
        value = 'average reciprocal.py'
    elif condition == '3':
        value = 'avg of sum of squares.py'
    elif condition == '4':
        value = 'find correct average.py'
    elif condition == '5':
        value = 'finding x.py'
    elif condition == '6':
        value = 'mean average.py'
    else:
        exit()
    return value


def openpyfile():
    call(['python',option()])
    print()
    print('/////////////////////////////////////////////////////////')
    openpyfile()

openpyfile()