import math
"""
def prime(n):
    x=int(math.sqrt(n))
    for i in range(4,x+1):
        if n%i==0:
            break
        else:
            print(n)
"""
test=int(input())
while test>0:
    a,b=map(int,input().split())
    if (a%2)!=0:
        for num in range(a,b+1,2):
            if num > 1:
                x=int(math.sqrt(num))
                for i in range(2,x+1):
                    if (num % i)==0:
                        break
                else:
                    print(num)
    else:
        for num in range(a,b+1):
            if num > 1:
                x=int(math.sqrt(num))
                for i in range(2,x+1):
                    if (num % i)==0:
                        break
                else:
                    print(num)

    test=test-1                    
        
