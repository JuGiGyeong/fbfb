for i in range(1, 45 + 1):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
    else:
        print('fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0))

