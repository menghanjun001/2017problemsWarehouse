def rev(x):   #x is str
    return int(x[::-1])
x,y=input().split()
# 太绕导致嵌套函数出错
print(rev(str(rev(x)+rev(y))))
