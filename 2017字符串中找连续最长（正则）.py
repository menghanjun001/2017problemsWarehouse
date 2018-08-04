import re
s=input()
pattern=re.compile(r'[0-9]+')
ans=pattern.findall(s)
#sorted方法的key和lambda的巧妙应用
print(sorted(ans,key=lambda x:len(x))[-1])