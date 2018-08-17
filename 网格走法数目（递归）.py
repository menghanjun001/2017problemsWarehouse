def net(x,y):
    if x==0 or y==0:
        return 1
    else:
        return net(x-1,y)+net(x,y-1)
x,y=map(int,input().split())
print(net(x,y))