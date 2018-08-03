ans=''.join(map(str,sorted(set(i for i in range(1,10001))-set(map(int,input().split())))))
print(int(ans)%7)