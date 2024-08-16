def jelly(num):
    count = num
    while count != 0:
        for i in range(2*num-1):
            print('J',end = '')
        print('')
        count -= 1
    count = num
    while count != 0:
        for j in range(num):
            if j == num-1:
                print('S',end = '')
            else:
                print('S',end = ' ')
        print('')
        count -= 1
num = int(input())
jelly(num)
