s=input()
dict={}
for i in s:
    if i.isalpha():
        # 很巧妙这里，get(i,0)方法使i第一次出现在dict中无值则返回默认值0
        dict[i]=dict.get(i,0)+1
        if dict[i]==3:
            break
print(i)