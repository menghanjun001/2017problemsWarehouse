a=input()
b=input()
for i in b:
    if i in a:
        # 是错误的
        # a.replace(i,'')
        a=a.replace(i,'')
print(a)