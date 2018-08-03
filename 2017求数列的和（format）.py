while True:
    try:
        m, n = map(int, input().split())
        sum = 0
        for i in range(n):  # 写的for i in n报错,低级错误
            sum += m
            m = m ** 0.5
        print('{:.2f}'.format(sum))
    except:
        break