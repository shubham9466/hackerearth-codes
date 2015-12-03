import math
test=int(input())
while test>0:
    print()
    #a,b=map(int ,input().split())
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    sieve=[True]*(b+1)
    for p in range(2,b+1):
        if(sieve[p]==True):
            if(p>=a):
                print(p)
        if(p*p)<=b:
            for i in range(p,b+1,p):
                sieve[i]=False
    test=test-1
