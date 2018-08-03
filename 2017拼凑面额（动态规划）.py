while True:
    try:
        n=int(input())    #没加int后边都输出不出来
        dp=[0 for i in range(10001)]
        dp[0]=1
        coins=[1,5,10,20,50,100]
        for i in coins:
            for j in range(i,n+1): #j块钱，从i-n
                dp[j]=dp[j]+dp[j-i]
        print(dp[n])
    except:
        break
