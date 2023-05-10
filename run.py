from subprocess import call


# import average

def option():
    condition = input('1)average.py 2)average_reciprocal.py '
                      '\n3)avg_of_sum_of_squares.py 4)find_correct_average.py '
                      '\n5)finding_x.py 6)mean_average.py '
                      '\nPRESS 0 TO EXIT enter option = ')

    value = ''
    if condition == '1':
        value = 'average\\average.py'
    elif condition == '2':
        value = 'average\\average_reciprocal.py'
    elif condition == '3':
        value = 'average\\avg_of_sum_of_squares.py'
    elif condition == '4':
        value = 'average\\find_correct_average.py'
    elif condition == '5':
        value = 'average\\finding_x.py'
    elif condition == '6':
        value = 'average\\mean_average.py'
    else:
        exit()
    return value


def openpyfile():
    call(['python', option()])
    print(' ')
    print('/////////////////////////////////////////////////////////')
    print(' ')
    openpyfile()


openpyfile()
