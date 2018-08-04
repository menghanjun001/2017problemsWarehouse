s=input().split()
n,k=s[:-1],s[-1]
# aa=sorted(n,key=int)[:int(k)]
# bb=' '.join(sorted(n,key=int)[:int(k)])
print(' '.join(sorted(n,key=int)[:int(k)]))