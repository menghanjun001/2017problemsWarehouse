def shuixianhua(num):
    sum=0
    for i in str(num):
        sum+=int(i)**3
    if sum==num:
        return True

while True:
    try:
        m,n=map(int,input().split())
        number = []
        for i in range(m, n + 1):
            if shuixianhua(i):
                number.append(str(i)) #不转成str之后无法用join方法
        if len(number)==0:
            print('no')
        else:
            print(' '.join(number))
    except:
        break