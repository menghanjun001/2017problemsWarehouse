n,m=map(int,input().split())
a=input().split()
b=input().split()
bingji=set(a)|set(b)   #set
print(' '.join(sorted(bingji,key=int)))  #sorted中的key可以为int