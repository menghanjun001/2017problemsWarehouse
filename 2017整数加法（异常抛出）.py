cin=input().split()
sum=0
try:
    for i in cin:
        sum+=int(i)
    print(sum)
except ValueError:
    print('error')