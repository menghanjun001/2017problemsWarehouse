while True:
    try:
        ss = input()
        l = len(ss)
        s=[]
        for i in ss:
            if i!=' ': #低级错误打成isalpha
                s.extend(i)  #打成append
        s=''.join(s)    #转成字符串没赋值给SS
        if l <= 6:
            print(s)
        elif l > 6 and l <= 14:
            print(s[:6], s[6:])
        else:
            print(s[:6], s[6:14], s[14:])
    except:
        break