def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(1,len(list)):
            if list[j]+list[j-1]>list[j-1]+list[j]:
                list[j],list[j-1]=list[j-1],list[j]
    return list
n=int(input())
list=input().split()
bubbleSort(list)
print(''.join(list))