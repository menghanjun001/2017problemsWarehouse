n=int(input())
f=[0,1]
while True:
    # f[0,1]=f[f[1],f[0]+f[1]]
    # TypeError: list indices must be integers or slices, not tuple
    f=[f[1],f[0]+f[1]]
    if f[0]<=n<=f[1]:
        break
print(min(n-f[0],f[1]-n))