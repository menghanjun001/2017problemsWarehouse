# def f(x):
#     if x<=1:
#         return x
#     else:
#         return f(x-1)+f(x-2)
num=int(input())
f=[]
f.extend('0')
f.extend('1')
for i in range(2,31):
    f.append(str(int(f[i-1])+int(f[i-2])))
    if num<int(f[i]):     #不必存储斐波那契数列然后再查找
        if num-int(f[i-1]) > int(f[i])-num:
            print(int(f[i])-num)
            break
        else:
            print(num-int(f[i-1]))
            break

