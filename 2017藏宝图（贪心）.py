s=input()
t=input()
flag=-1
count=0
for i in t:
    if s.find(i,count)==-1:
        print('No')
        flag=-1
        break
    else:
        count=s.find(i,count)+1      #如果找到则find的位置往后推
        flag=1
if flag==1:
    print('Yes')