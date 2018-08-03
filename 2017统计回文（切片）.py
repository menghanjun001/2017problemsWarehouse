a=input()
b=input()
def JudgeHuiwen(a,b):
    count=0
    for i in range(len(a)+1):  #len(a)+1,还有一次在末尾
        s=a[0:i]+b+a[i:len(a)]
        if ''.join(s)==''.join(s)[::-1]:
            count+=1
    return count
print(JudgeHuiwen(a,b))