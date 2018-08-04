r2=int(input())   #n is int
count=0
for x in range(1,int(r2**0.5)+1):
    if (r2-x**2)**0.5 %1 == 0:
        count+=1
print(count*4)