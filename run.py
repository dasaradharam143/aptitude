from subprocess import call
from average import

def option():
    condition = input('1)average.py 2)average_reciprocal.py '
                  '\n3)avg_of_sum_of_squares.py 4)find_correct_average.py '
                  '\n5)finding_x.py 6)mean_average.py '
                      '\nPRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = 'average.py'
    elif condition == '2':
        value = 'average_reciprocal.py'
    elif condition == '3':
        value = 'avg_of_sum_of_squares.py'
    elif condition == '4':
        value = 'find_correct_average.py'
    elif condition == '5':
        value = 'finding_x.py'
    elif condition == '6':
        value = 'mean_average.py'
    else:
        exit()
    return value


def openpyfile():
    call(['python',option()])
    print(' ')
    print('/////////////////////////////////////////////////////////')
    print(' ')
    openpyfile()

openpyfile()