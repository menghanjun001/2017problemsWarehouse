s=input().split()
s.sort()
for i in range(len(s)//2+1):
    # 是错误的
    # if s[i:i+4]==s[i:i+4:-1]:
    if s[i:i+len(s)//2]==s[i:i+len(s)//2][::-1]:
        print(s[i])
        break