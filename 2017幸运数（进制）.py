def f(x):  #x为int
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum #返回为int

def g(x):  #x为int
    # sum=0
    # for i in str(bin(x)[2:]):
    #     sum+=int(i)
    # return sum #返回为int

    # 优化一下，不需要循环
    return str(bin(x)).count('1')  #count(1)报错,并且bin(123)里有0b

def xingyun(x): #a,b is int
    if f(x)==g(x):
        return True

n=int(input())
count=0
for i in range(1,n+1):
    if xingyun(i):
        count+=1
print(count)