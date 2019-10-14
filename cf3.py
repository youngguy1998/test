def multiple():
    '''九九乘法表函数'''
    row = 1
    while row < 10:
        col = 1
        while col <= row:
            result = row * col
            print('{} * {} = {}'.format(row, col, result), end='\t')
            col += 1
        print('')
        row += 1
