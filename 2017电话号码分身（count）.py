t=int(input())
for i in range(t):
    s=input()
    n0,n2,n4,n6,n8=s.count('G'),s.count('Z'),s.count('W'),s.count('U'),s.count('X')
    n3=s.count('O')-n2-n4-n6
    n5=s.count('H')-n0
    n7=s.count('F')-n6
    n9=s.count('S')-n8
    n1=s.count('I')-n0-n7-n8
    print('0'*n0+'1'*n1+'2'*n2+'3'*n3+'4'*n4+'5'*n5+'6'*n6+'7'*n7+'8'*n8+'9'*n9)